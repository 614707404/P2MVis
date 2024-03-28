import asyncio
import tensorflow as tf
import numpy as np
import pprint
import pickle
import os
from tensorflow.python.autograph.core.converter import Feature
from tensorflow.python.keras.backend import dropout
from p2m.config import *
from utils.dataloader import *
import utils.tools as tools
import p2m.GCN as GCN
from p2m.losses import *
from utils.visualize import plot_scatter


def get_loss(output1, output2, output3, output1_2, output2_2, features, trainable_variables, labels, edges,
             faces_triangle, lape_idx):
    '''损失函数'''
    # # Weight decay loss
    loss = tf.zeros([])
    # Cross entropy error
    # Pixel2mesh loss
    loss += mesh_loss(pred=output1, labels=labels, edges=edges, faces_triangle=faces_triangle, block_id=1)
    loss += mesh_loss(pred=output2, labels=labels, edges=edges, faces_triangle=faces_triangle, block_id=2)
    loss += mesh_loss(pred=output3, labels=labels, edges=edges, faces_triangle=faces_triangle, block_id=3)
    loss += laplace_loss(pred1=features, pred2=output1, lape_idx=lape_idx, block_id=1)
    loss += laplace_loss(pred1=output1_2, pred2=output2, lape_idx=lape_idx, block_id=2)
    loss += laplace_loss(pred1=output2_2, pred2=output3, lape_idx=lape_idx, block_id=3)
    # Weight decay loss
    # conv_layers = list(range(1, 15)) + list(range(17, 31)) + list(range(33, 48))
    # for layer_id in conv_layers:
    for var1 in trainable_variables:
        for var in var1:
            loss += 5e-6 * tf.nn.l2_loss(var)
    return loss

def get_loss_aux(output1, output2, output3, output1_2, output2_2, features, trainable_variables, labels, edges,
             faces_triangle, lape_idx):
    '''损失函数'''
    # # Weight decay loss
    loss = tf.zeros([])
    # Cross entropy error
    # Pixel2mesh loss
    p_loss_1, e_loss_1, n_loss_1 = mesh_loss_aux(pred=output1, labels=labels, edges=edges, faces_triangle=faces_triangle, block_id=1)
    p_loss_2, e_loss_2, n_loss_2 = mesh_loss_aux(pred=output2, labels=labels, edges=edges, faces_triangle=faces_triangle, block_id=2)
    p_loss_3, e_loss_3, n_loss_3 = mesh_loss_aux(pred=output3, labels=labels, edges=edges, faces_triangle=faces_triangle, block_id=3)
    l_loss_1, m_loss_1 = laplace_loss_aux(pred1=features, pred2=output1, lape_idx=lape_idx, block_id=1)
    l_loss_2, m_loss_2 =  laplace_loss_aux(pred1=output1_2, pred2=output2, lape_idx=lape_idx, block_id=2)
    l_loss_3, m_loss_3 =  laplace_loss_aux(pred1=output2_2, pred2=output3, lape_idx=lape_idx, block_id=3)
    # Weight decay loss
    # conv_layers = list(range(1, 15)) + list(range(17, 31)) + list(range(33, 48))
    # for layer_id in conv_layers:
    p_loss = (p_loss_1 + p_loss_2 + p_loss_3)
    e_loss = (e_loss_1 + e_loss_2 + e_loss_3)
    n_loss = (n_loss_1 + n_loss_2 + n_loss_3)
    l_loss = (l_loss_1 + l_loss_2 + l_loss_3)
    m_loss = (m_loss_1 + m_loss_2 + m_loss_3)
    loss = (p_loss + e_loss + n_loss + l_loss + m_loss)
    for var1 in trainable_variables:
        for var in var1:
            loss += 5e-6 * tf.nn.l2_loss(var)
    return loss, p_loss, e_loss, n_loss, l_loss, m_loss


class Trainer:
    def __init__(self, cfg):
        self.cfg = cfg
        self.root_dir = ''
        self.model_dir = ''
        self.log_dir = ''
        self.plt_dir = ''
        self.train_loss = None
        self.pkl = None
        self.edges = None
        self.faces = None
        self.features = None
        self.support1 = None
        self.support2 = None
        self.support3 = None
        self.pool_idx = None
        self.lape_idx = None
        self.faces_triangle = None
        self.sample_adj = None
        self.sample_coord = None
        self.num_features_nonzero = None
        self.dropout = 0
        self.pre_train = False
        self.pre_weight = True
        self.model = None
        self.model_weights_save_path = None
        self.optimizer = None
        self.step = 0
        self.train_number = 0
        self.is_paused = True
        self.data = None
        self.img_feat = None
        self.output1 = None
        self.output2 = None
        self.output3 = None
        self.loss = 0
        self.mean_loss = 0
        self.p_loss = 0
        self.e_loss = 0
        self.n_loss = 0
        self.l_loss = 0
        self.m_loss = 0
        self.grads = None
        self.img_all_view = None

    @tf.function(experimental_relax_shapes=True)
    def train_step(self, img_with_cameras, labels):
        with tf.GradientTape() as tape:
            output1, output2, output3, output1_2, output2_2, trainable_variables, img_feat = self.model(
                img_with_cameras)
            loss, p_loss, e_loss, n_loss, l_loss, m_loss  = get_loss_aux(output1, output2, output3, output1_2, output2_2, self.features, trainable_variables, labels,
                            self.edges, self.faces_triangle, self.lape_idx)
        grads = tape.gradient(loss, self.model.trainable_variables)  # 梯度
        self.optimizer.apply_gradients(zip(grads, self.model.trainable_variables))
        return loss, p_loss, e_loss, n_loss, l_loss, m_loss, output1, output2, output3, img_feat, grads

    def init_environment(self):
        os.environ['CUDA_VISIBLE_DEVICES'] = "0"
        physical_devices = tf.config.list_physical_devices('GPU')
        try:
            tf.config.experimental.set_memory_growth(physical_devices[0], True)
        except:
            pass
        seed = 614
        np.random.seed(seed)
        self.root_dir = os.path.join(self.cfg.save_path, self.cfg.name)
        print('输出路径：{}'.format(self.cfg.save_path))
        self.model_dir = os.path.join(self.cfg.save_path, self.cfg.name, 'models')
        self.log_dir = os.path.join(self.cfg.save_path, self.cfg.name, 'logs')
        self.plt_dir = os.path.join(self.cfg.save_path, self.cfg.name, 'plt')
        if not os.path.exists(self.root_dir):
            os.makedirs(self.root_dir)
            print('==> make root dir {}'.format(self.root_dir))
        if not os.path.exists(self.model_dir):
            os.makedirs(self.model_dir)
            print('==> make model dir {}'.format(self.model_dir))
        if not os.path.exists(self.log_dir):
            os.makedirs(self.log_dir)
            print('==> make log dir {}'.format(self.log_dir))
        if not os.path.exists(self.plt_dir):
            os.makedirs(self.plt_dir)
            print('==> make plt dir {}'.format(self.plt_dir))
        self.train_loss = open('{}/train_loss_record.txt'.format(self.log_dir), 'a')
        self.train_loss.write('Net {} | Start training | lr =  {}\n'.format(self.cfg.name, self.cfg.lr))
        # 读取数据的逻辑需要调整
        self.data = DataFetcher(file_list=self.cfg.train_file_path, data_root=self.cfg.train_data_path,
                                image_root=self.cfg.train_image_path,
                                is_val=False)
        self.data.setDaemon(True)
        self.data.start()
        
        self.pkl = pickle.load(open('data/iccv_p2mpp.dat', 'rb'))
        self.edges, self.faces, self.features, self.support1, self.support2, self.support3, self.pool_idx, self.lape_idx, self.faces_triangle, self.sample_adj, self.sample_coord = tools.construct_feed_dict(
            self.pkl)
        self.features = tf.constant(self.features, dtype=tf.float32)
        if self.pre_train:
            self.model = tf.keras.models.load_model(
                '/workspace/3D/tf2_gcn-main/results/coarse_mvp2m/models/20200222model')
        else:
            self.model = GCN.GCN_model(placeholders_features=self.features,
                                       num_features_nonzero=self.num_features_nonzero,
                                       placeholder_dropout=dropout,
                                       pool_idx=self.pool_idx, args=self.cfg, support1=self.support1,
                                       support2=self.support2, support3=self.support3,
                                       lape_idx=self.lape_idx, edges=self.edges, faces_triangle=self.faces_triangle)
        if self.pre_weight:
            self.model.load_weights(
                '/home/giga/Desktop/davistao/p2m_tf2/Pixel2Mesh-Tensorflow2/results/coarse_mvp2m/models/20200223model_weights/epoch10')
        # 权重保存位置
        self.model_weights_save_path = '/home/giga/Desktop/davistao/p2m_tf2/Pixel2Mesh-Tensorflow2/results/coarse_mvp2m/models' \
                                       '/20230316model_weights/epoch'

        self.optimizer = tf.keras.optimizers.Adam(learning_rate=self.cfg.lr)

    async def train(self):
        self.train_number = self.data.number
        for epoch in range(self.cfg.epochs):
            current_epoch = epoch + 1 + self.cfg.init_epoch
            epoch_plt_dir = os.path.join(self.plt_dir, str(current_epoch))
            if not os.path.exists(epoch_plt_dir):
                os.mkdir(epoch_plt_dir)
            mean_loss = 0
            all_loss = np.zeros(self.train_number, dtype='float32')
            for iters in range(self.train_number):

                # print(f"Training epoch {self.step}")
                # self.step += 1
                # await asyncio.sleep(1) 
                self.step += 1
                # 
                self.img_all_view, labels, cameras, data_id, mesh = self.data.fetch()
                img_with_cameras = {}
                img_with_cameras.update({'img_all_view': self.img_all_view})
                img_with_cameras.update({'cameras': cameras})
                # cameras : [3,5]
                await self.check_pause()
                loss, self.p_loss, self.e_loss, self.n_loss, self.l_loss, self.m_loss, self.output1, self.output2, self.output3, self.img_feat, self.grads = self.train_step(img_with_cameras, labels)

                all_loss[iters] = loss
                mean_loss = np.mean(all_loss[np.where(all_loss)])
                print('Epoch {}, Iteration {}, Mean loss = {}, iter loss = {}, {}, data id {}'.format(current_epoch,
                                                                                                      iters + 1,
                                                                                                      mean_loss, loss,
                                                                                                      self.data.queue.qsize(),
                                                                                                      data_id))
                if iters + 1 % 1000 == 0:
                    self.train_loss.write(
                        'Epoch {}, Iteration {}, Mean loss = {}, iter loss = {}, {}, data id {}\n'.format(current_epoch,
                                                                                                          iters + 1,
                                                                                                          mean_loss,
                                                                                                          loss,
                                                                                                          self.data.queue.qsize(),
                                                                                                          data_id))
                    plot_scatter(pt=self.output3, data_name=data_id, plt_path=epoch_plt_dir)
                await asyncio.sleep(0)
                self.train_loss.flush()
                self.loss = loss;
                self.mean_loss = mean_loss;
                
            self.model.save_weights(self.model_weights_save_path + str(current_epoch))

    async def check_pause(self):
        print("Checking pause...")
        while self.is_paused:
            await asyncio.sleep(0.1)  # 增加等待时间

    def play(self):
        self.is_paused = False

    def pause(self):
        self.is_paused = True


# 模拟数据和配置对象


# 测试程序
async def main():
    yaml_path = '/home/giga/Desktop/davistao/p2m_tf2/Pixel2Mesh-Tensorflow2/cfgs/mvp2m.yaml'
    args = execute(yaml_path)
    trainer = Trainer(args)
    trainer.init_environment()

    trainer.play()
    train_task = asyncio.create_task(trainer.train())

    await asyncio.sleep(10)
    print("Pausing training...")
    trainer.pause()

    await asyncio.sleep(50)
    print("Resuming training...")
    trainer.play()

    await train_task
    trainer.data.shutdown()
    print("Training completed.")


if __name__ == "__main__":
    asyncio.run(main())
