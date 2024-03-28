
# Dependencies

Requirements：

- Python 3.6+
- Tensorflow(version 2.0+) 
- numpy
- ...

# Dataset

采用[ShapeNet](https://shapenet.org/)数据集，视角的Rendered方法来自[3D-R2N2](https://github.com/chrischoy/3D-R2N2)
训练和测试的数据集可以在***data/train_list.txt***和***data/test_list.txt***中找到。具体数据集的下载可以从[Pixel2Mesh++](https://github.com/walsvid/Pixel2MeshPlusPlus)里下载。


## 

首先在`cfgs/mvp2m.yaml`中将对应路径设置成自己数据集所在的位置
- `train_file_path`: the path of your own train split file which contains training data name for each instance
- `train_image_path`: input image path
- `train_data_path`: ground-truth model path
- `coarse_result_*`: the configuration items related to the coarse intermediate mesh should be same as the training data

## License

Apache License version 2.0

## References

本项目引用了以下GitHub仓库：

- [Pixel2Mesh-Tensorflow2](https://github.com/yannqi/Pixel2Mesh-Tensorflow2) - 提供基于TF2实现的Pixel2Mesh源代码