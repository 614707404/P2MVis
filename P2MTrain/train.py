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

class Train(object):

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
        self.pre_weight = False
        self.model = None
        self.model_weights_save_path = None
        self.optimizer = None
        self.step = 0
        self.train_number = 0
        self.pause_event = threading.Event()
        self.pause_event.set()  # 设置为非暂停状态
        self.training_thread = threading.Thread(target=self.train)


    # 训练函数
    @tf.function(experimental_relax_shapes=True)
    def train_step(self, img_with_cameras, labels):
        with tf.GradientTape() as tape:
            output1, output2, output3, output1_2, output2_2, trainable_variables = self.model(img_with_cameras)
            loss = get_loss(output1, output2, output3, output1_2, output2_2, self.features, trainable_variables, labels,
                            self.edges, self.faces_triangle, self.lape_idx)
        grads = tape.gradient(loss, self.model.trainable_variables) # 梯度
        self.optimizer.apply_gradients(zip(grads, self.model.trainable_variables))
        return loss, output3
    
    def init_environment(self):
        os.environ['CUDA_VISIBLE_DEVICES'] = "0"
        physical_devices = tf.config.list_physical_devices('GPU')
        try:
            tf.config.experimental.set_memory_growth(physical_devices[0], True)
        except:
            pass
        seed = 614
        np.random.seed(seed)
        self.root_dir = os.path.join(cfg.save_path, cfg.name)
        print('输出路径：{}'.format(cfg.save_path))
        self.model_dir = os.path.join(cfg.save_path, cfg.name, 'models')
        self.log_dir = os.path.join(cfg.save_path, cfg.name, 'logs')
        self.plt_dir = os.path.join(cfg.save_path, cfg.name, 'plt')
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
        self.train_loss.write('Net {} | Start training | lr =  {}\n'.format(cfg.name, cfg.lr))
        self.pkl = pickle.load(open('data/iccv_p2mpp.dat', 'rb'))
        self.edges, self.faces, self.features, self.support1, self.support2, self.support3, self.pool_idx, self.lape_idx, self.faces_triangle, self.sample_adj, self.sample_coord = tools.construct_feed_dict(self.pkl)
        self.features = tf.constant(self.features, dtype=tf.float32)
        if self.pre_train:
            self.model = tf.keras.models.load_model('/workspace/3D/tf2_gcn-main/results/coarse_mvp2m/models/20200222model')
        else:
            self.model = GCN.GCN_model(placeholders_features=self.features, num_features_nonzero=self.num_features_nonzero,
                                placeholder_dropout=dropout,
                                pool_idx=self.pool_idx, args=cfg, support1=self.support1, support2=self.support2, support3=self.support3,
                                lape_idx=self.lape_idx, edges=self.edges, faces_triangle=self.faces_triangle)
        if self.pre_weight:
            self.model.load_weights('/workspace/3D/tf2_gcn-main/results/coarse_mvp2m/models/20200223model_weights/epoch1')
        # 权重保存位置
        self.model_weights_save_path = '/home/giga/Desktop/davistao/p2m_tf2/Pixel2Mesh-Tensorflow2/results/coarse_mvp2m/models' \
                                '/20230316model_weights/epoch'

        self.optimizer = tf.keras.optimizers.Adam(learning_rate=cfg.lr)

    
    def train(self):
        self.train_number = self.data.number
        self.step = 0
        for epoch in range(cfg.epochs):
            self.pause_event.wait()
            print("train")

    def play(self):
        self.pause_event.set()  # 设置事件对象，使训练继续
        if not self.training_thread.is_alive():
            self.training_thread.start()  # 如果训练线程未启动，则启动训练线程

    def pause(self):
        self.pause_event.clear()  # 清除事件对象，使训练暂停
