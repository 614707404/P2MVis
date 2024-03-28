from io import StringIO
import pprint
import threading
import time
from concurrent import futures
from queue import Queue

import grpc
import streaming_pb2
import streaming_pb2_grpc
from train_ctl import *
from p2m.config import *

import json
import numpy
from dataset_zip_creator import ZipCreator
from PIL import Image
# 张量通道轴做归一化
def channel_normalize(x):
    # Sum along the channel axis
    x_sum = tf.reduce_sum(x, axis=-1)

    # Normalize the values to the range [0, 1]
    x_min, x_max = tf.reduce_min(x_sum), tf.reduce_max(x_sum)
    x_normalized = (x_sum - x_min) / (x_max - x_min)

    return x_normalized


def tensor_to_list(tensor):
    return tensor.numpy().tolist()


class StreamingServicer(streaming_pb2_grpc.StreamingServiceServicer):
    def __init__(self, trainer):
        self.trainer = trainer
        self.pre_send_json = 0

    def BidirectionalStream(self, request_iterator, context):
        count = 0
        counting = False
        message_queue = Queue()

        def message_handler():
            nonlocal counting
            for request in request_iterator:
                message_queue.put(request.message)

        threading.Thread(target=message_handler, daemon=True).start()

        while True:
            if not message_queue.empty():
                message = message_queue.get()
                if message == "play":
                    print("Starting count")
                    counting = True
                    self.trainer.play()
                elif message == "pause":
                    print("Stopping count")
                    counting = False
                    self.trainer.pause()

            if counting:
                time.sleep(0.1)
                if (self.trainer.img_feat is None):
                    continue
                    
                
                                
                # 向客户端发送消息
                if self.pre_send_json != self.trainer.step:
                    # print(self.trainer.output1.shape)
                    # print(self.trainer.output2.shape)
                    # print(self.trainer.output3.shape)
                    # print(self.trainer.img_feat[0].shape)
                    # print(self.trainer.img_feat[1].shape)
                    # print(self.trainer.img_feat[2].shape)
                    # print(self.trainer.img_feat[3].shape)
                    # 查看 grads 的长度
                    # length_of_grads = len(self.trainer.grads)

                    # # 获取每个张量的尺寸
                    # shapes_of_tensors = [tensor.shape for tensor in self.trainer.grads]

                    # print("Length of grads:", length_of_grads)
                    print("Type of imgs:", type(self.trainer.img_all_view))
                    print("Shape of imgs:", self.trainer.img_all_view.shape)
                    

                    self.pre_send_json = self.trainer.step
                    update = False
                    if self.trainer.step % 100 == 0 and update == True:
                        print("features save")
                        # 生成obj文件
                        vert = self.trainer.output1
                        vert = np.hstack((np.full([vert.shape[0],1], 'v'), vert))
                        face = np.loadtxt('data/face1.obj', dtype='|S32')
                        mesh = np.vstack((vert, face))
                        pred_path = '/home/giga/Desktop/davistao/the_lab/the_lab/public/predict1.obj'
                        np.savetxt(pred_path, mesh, fmt='%s', delimiter=' ')

                        vert = self.trainer.output2
                        vert = np.hstack((np.full([vert.shape[0],1], 'v'), vert))
                        face = np.loadtxt('data/face2.obj', dtype='|S32')
                        mesh = np.vstack((vert, face))
                        pred_path = '/home/giga/Desktop/davistao/the_lab/the_lab/public/predict2.obj'
                        np.savetxt(pred_path, mesh, fmt='%s', delimiter=' ')

                        vert = self.trainer.output3
                        vert = np.hstack((np.full([vert.shape[0],1], 'v'), vert))
                        face = np.loadtxt('data/face3.obj', dtype='|S32')
                        mesh = np.vstack((vert, face))
                        pred_path = '/home/giga/Desktop/davistao/the_lab/the_lab/public/predict3.obj'
                        np.savetxt(pred_path, mesh, fmt='%s', delimiter=' ')
                        

                        img_data = (self.trainer.img_all_view[0] * 255).astype(np.uint8)
                        img = Image.fromarray(img_data)
                        img.save("/home/giga/Desktop/davistao/the_lab/the_lab/public/input.png")

                        img_data = (self.trainer.img_all_view[1] * 255).astype(np.uint8)
                        img = Image.fromarray(img_data)
                        img.save("/home/giga/Desktop/davistao/the_lab/the_lab/public/input_1.png")

                        img_data = (self.trainer.img_all_view[2] * 255).astype(np.uint8)
                        img = Image.fromarray(img_data)
                        img.save("/home/giga/Desktop/davistao/the_lab/the_lab/public/input_2.png")

                        for i, f in enumerate(self.trainer.img_feat):
                            # file_path = os.path.join('features', 'C{}'.format(i + 1))
                            # try:
                            #     np.savez(file_path, f)
                            # except OSError as e:
                            #     print(f"Error saving file {file_path}: {e}")
                            if (i == 0 or i == 1 or i == 4):
                                numpy_array = f.numpy()
                                creator = ZipCreator(name='C{}'.format(i + 1), precision=8)
                                creator.create(numpy_array)
                        img_feats = [channel_normalize(x) for x in self.trainer.img_feat]
                        img_feat_list = [tensor_to_list(x) for x in img_feats]
                        img_feat_json = json.dumps({"x1": img_feat_list[4], "x2": img_feat_list[0], "x3": img_feat_list[1]})
                        with open("/home/giga/Desktop/davistao/the_lab/the_lab/public/img_feat_json.json", 'w', encoding='utf-8') as file:
                            json.dump(img_feat_json, file, ensure_ascii=False, indent=4)                   
                    #     print("send json")
                        yield streaming_pb2.ServerMessage(message=f"{self.trainer.step}", img_feat_json="T", number1 = numpy.round(self.trainer.loss).astype(int));
                    
                    yield streaming_pb2.ServerMessage(message=f"{self.trainer.step}",
                                                            number1 = numpy.round(self.trainer.loss).astype(int), 
                                                            number2 = numpy.round(self.trainer.mean_loss).astype(int),
                                                            p_loss = numpy.round(self.trainer.p_loss).astype(int),
                                                            e_loss = numpy.round(self.trainer.e_loss).astype(int),
                                                            n_loss = numpy.round(self.trainer.n_loss).astype(int),
                                                            l_loss = numpy.round(self.trainer.l_loss).astype(int),
                                                            m_loss = numpy.round(self.trainer.m_loss).astype(int))


def serve(trainer):
    options = [
        ('grpc.max_send_message_length', 50 * 1024 * 1024),  # 50MB
        ('grpc.max_receive_message_length', 50 * 1024 * 1024)  # 50MB
    ]
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10), options=options)
    streaming_pb2_grpc.add_StreamingServiceServicer_to_server(StreamingServicer(trainer), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    print("Server started on port 50051")
    server.wait_for_termination()


def threaded_serve(trainer):
    server_thread = threading.Thread(target=serve, args=(trainer,), daemon=True)
    server_thread.start()


async def main():
    yaml_path = '/home/giga/Desktop/davistao/p2m_tf2/Pixel2Mesh-Tensorflow2/cfgs/mvp2m.yaml'
    args = execute(yaml_path)
    trainer = Trainer(args)
    trainer.init_environment()
    # trainer.play()
    train_task = asyncio.create_task(trainer.train())
    threaded_serve(trainer)
    await train_task


if __name__ == "__main__":
    asyncio.run(main())
