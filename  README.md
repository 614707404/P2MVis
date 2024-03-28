# 项目名称

## 简介

本项目包含两个子项目：P2MVis和P2MTrain，旨在实现一个基于Pixel2Mesh的图像到三维模型转换系统。P2MVis作为Web端，提供了用户交互界面和后台服务，以便与本地运行的P2MTrain训练程序进行通信。P2MTrain则负责执行Pixel2Mesh训练过程。

### P2MVis

- **前端界面**：使用Vue.js框架开发。
- **后台服务**：基于Express，负责处理前端请求并与P2MTrain通信。

### P2MTrain

- **训练程序**：在本地运行的Pixel2Mesh训练程序，通过Express与Web端P2MVis进行数据交换。

## 部署

在开始之前，请确保分别阅读P2MVis和P2MTrain子项目中的`README.md`文件，完成必要的准备工作。这将帮助您了解每个子项目的依赖和配置要求。

## 运行

1. Run `cd P2MVis_demo`
2. Run `npm run dev`
3. Open the URL shown in the terminal
4. Run `cd server`
5. Run `npm start`
6. Run `cd ../P2MTrain`
7. Run `python serve.py`

## References

本项目引用了以下GitHub仓库：
- [iFeaLiD](https://github.com/BiodataMiningGroup/IFeaLiD) - 提供实时向量相似度计算能力
- [Pixel2Mesh-Tensorflow2](https://github.com/yannqi/Pixel2Mesh-Tensorflow2) - 提供基于TF2实现的Pixel2Mesh源代码