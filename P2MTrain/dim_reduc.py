
import numpy as np
from sklearn.manifold import TSNE
from sklearn.decomposition import PCA
import umap 
import pandas as pd
from sklearn.manifold import LocallyLinearEmbedding
from sklearn.manifold import Isomap
import json

# pca降维方法
def pca_function(img_f):
    f_1 = np.array(img_f[4][0])
    f_2 = np.array(img_f[1][0])
    f_3 = np.array(img_f[2][0])
           
    feature_1 = f_1.reshape(-1, 32)
    feature_2 = f_2.reshape(-1, 128)
    feature_3 = f_3.reshape(-1, 256)

    pca = PCA(n_components=1)

    feature_1_2d = pca.fit_transform(feature_1)
    feature_2_2d = pca.fit_transform(feature_2)
    feature_3_2d = pca.fit_transform(feature_3)

    feature_1_3d = feature_1_2d.reshape(112, 112, 1)
    feature_2_3d = feature_2_2d.reshape(28, 28, 1)
    feature_3_3d = feature_3_2d.reshape(14, 14, 1)
    # 将NumPy数组转换为Python列表
    feature_1_list = feature_1_3d.tolist()
    feature_2_list = feature_2_3d.tolist()
    feature_3_list = feature_3_3d.tolist()

    # 创建一个包含三个特征向量的字典
    features_dict = {
                    "x1": feature_1_list,
                    "x2": feature_2_list,
                    "x3": feature_3_list,
                }

    # 将字典转换为JSON字符串
    img_feat_json = json.dumps(features_dict)
    return img_feat_json

def tsne_function(img_f):
    f_1 = np.array(img_f[4][0])
    f_2 = np.array(img_f[1][0])
    f_3 = np.array(img_f[2][0])
           
    feature_1 = f_1.reshape(-1, 32)
    feature_2 = f_2.reshape(-1, 128)
    feature_3 = f_3.reshape(-1, 256)

    tsne = TSNE(n_components=1)

    feature_1_2d = tsne.fit_transform(feature_1)
    feature_2_2d = tsne.fit_transform(feature_2)
    feature_3_2d = tsne.fit_transform(feature_3)

    feature_1_3d = feature_1_2d.reshape(112, 112, 1)
    feature_2_3d = feature_2_2d.reshape(28, 28, 1)
    feature_3_3d = feature_3_2d.reshape(14, 14, 1)
    # 将NumPy数组转换为Python列表
    feature_1_list = feature_1_3d.tolist()
    feature_2_list = feature_2_3d.tolist()
    feature_3_list = feature_3_3d.tolist()

    # 创建一个包含三个特征向量的字典
    features_dict = {
                    "x1": feature_1_list,
                    "x2": feature_2_list,
                    "x3": feature_3_list,
                }

    # 将字典转换为JSON字符串
    img_feat_json = json.dumps(features_dict)
    return img_feat_json

def umap_function(img_f):
    f_1 = np.array(img_f[4][0])
    f_2 = np.array(img_f[1][0])
    f_3 = np.array(img_f[2][0])
           
    feature_1 = f_1.reshape(-1, 32)
    feature_2 = f_2.reshape(-1, 128)
    feature_3 = f_3.reshape(-1, 256)

    reducer = umap.UMAP(n_components=1)

    feature_1_2d = reducer.fit_transform(feature_1)
    feature_2_2d = reducer.fit_transform(feature_2)
    feature_3_2d = reducer.fit_transform(feature_3)

    feature_1_3d = feature_1_2d.reshape(112, 112, 1)
    feature_2_3d = feature_2_2d.reshape(28, 28, 1)
    feature_3_3d = feature_3_2d.reshape(14, 14, 1)
    # 将NumPy数组转换为Python列表
    feature_1_list = feature_1_3d.tolist()
    feature_2_list = feature_2_3d.tolist()
    feature_3_list = feature_3_3d.tolist()

    # 创建一个包含三个特征向量的字典
    features_dict = {
                    "x1": feature_1_list,
                    "x2": feature_2_list,
                    "x3": feature_3_list,
                }

    # 将字典转换为JSON字符串
    img_feat_json = json.dumps(features_dict)
    return img_feat_json

def lle_function(img_f):
    f_1 = np.array(img_f[4][0])
    f_2 = np.array(img_f[1][0])
    f_3 = np.array(img_f[2][0])
           
    feature_1 = f_1.reshape(-1, 32)
    feature_2 = f_2.reshape(-1, 128)
    feature_3 = f_3.reshape(-1, 256)

    lle = LocallyLinearEmbedding(n_components=1)

    feature_1_2d = lle.fit_transform(feature_1)
    feature_2_2d = lle.fit_transform(feature_2)
    feature_3_2d = lle.fit_transform(feature_3)

    feature_1_3d = feature_1_2d.reshape(112, 112, 1)
    feature_2_3d = feature_2_2d.reshape(28, 28, 1)
    feature_3_3d = feature_3_2d.reshape(14, 14, 1)
    # 将NumPy数组转换为Python列表
    feature_1_list = feature_1_3d.tolist()
    feature_2_list = feature_2_3d.tolist()
    feature_3_list = feature_3_3d.tolist()

    # 创建一个包含三个特征向量的字典
    features_dict = {
                    "x1": feature_1_list,
                    "x2": feature_2_list,
                    "x3": feature_3_list,
                }

    # 将字典转换为JSON字符串
    img_feat_json = json.dumps(features_dict)
    return img_feat_json

def lso_function(img_f):
    f_1 = np.array(img_f[4][0])
    f_2 = np.array(img_f[1][0])
    f_3 = np.array(img_f[2][0])
           
    feature_1 = f_1.reshape(-1, 32)
    feature_2 = f_2.reshape(-1, 128)
    feature_3 = f_3.reshape(-1, 256)

    iso = Isomap(n_components=1,n_neighbors=10)

    feature_1_2d = iso.fit_transform(feature_1)
    feature_2_2d = iso.fit_transform(feature_2)
    feature_3_2d = iso.fit_transform(feature_3)

    feature_1_3d = feature_1_2d.reshape(112, 112, 1)
    feature_2_3d = feature_2_2d.reshape(28, 28, 1)
    feature_3_3d = feature_3_2d.reshape(14, 14, 1)
    # 将NumPy数组转换为Python列表
    feature_1_list = feature_1_3d.tolist()
    feature_2_list = feature_2_3d.tolist()
    feature_3_list = feature_3_3d.tolist()

    # 创建一个包含三个特征向量的字典
    features_dict = {
                    "x1": feature_1_list,
                    "x2": feature_2_list,
                    "x3": feature_3_list,
                }

    # 将字典转换为JSON字符串
    img_feat_json = json.dumps(features_dict)
    return img_feat_json