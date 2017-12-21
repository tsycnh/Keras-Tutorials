# Keras 入门课0 -- 目录

  网络上Keras入门的课程或教程都有很多，基本上都是一些最简单的例子，而自己真正去使用的时候，发现需要学习的内容还有很多，看官方文档的时候，效率也是比较低下的。所以才有了这个系列的课程。通过一些例子，逐渐深入的去学习Keras，每节课一个例子，遇到的新的知识点都会拿出来进行分析。这样就会形成一个知识点目录，之后想使用某个知识点的时候，可以很方便的根据知识点进行回看，查询对应的example，这样对于一些方法的使用和拓展都有很大的好处。

本系列主要针对一些Keras官方的一些examples来学习Keras的使用。课程使用的例子都来自这里 https://github.com/keras-team/keras/tree/master/examples

官方给的examples有一些地方和最新的Keras版本不符合，我都相应做了修改。同时有一些累赘的地方也加了一些修改，删除。尽可能在每一课中做到代码清晰易懂，不重复。

**课程系列目前还在更新中。。。**

## 文章目录
1.	[Keras入门课1 -- 用MLP识别mnist手写字符][class_1]
2. [Keras入门课2 -- 使用CNN识别mnist手写数字][class_2]
3. [Keras入门课3 -- 使用CNN识别cifar10数据集][class_3]
4. [Keras入门课4 -- 使用ResNet识别cifar10数据集][class_4]
5. [Keras入门课5 -- 网络可视化及训练监控][class_5]
## 知识点目录

点击对应知识点可以直接跳转到指定文章，方便速查

### 数据处理相关
1.	[载入Keras中预置的数据库及数据库数据的基本变换][class_1]
1.  [根据不同的模型数据要求，给原始数据图像增加维度][class_2]
1. [使用Keras内置的ImageDataGenerator来做数据增强][class_3]

### 模型相关（Model）
1.	[Sequential模型的定义，以及如何添加层][class_1]
1. [另一种使用Sequential()构建模型的方法，更加的简单快捷][class_3]
1. [使用函数式模型（Functional）更加自由的构建模型][class_4]
1. [将通过Functional方式定义的层初始化为一个模型（Model）][class_4]
1.	[使用compile对网络进行配置][class_1]
1.	[使用fit方法来对小数据库进行训练，这里的小数据库指的是所有数据可以一次性载入到内存][class_1]
1. [使用fit_generator来进行针对增强数据的训练][class_3]
1.	[使用evaluate方法来对模型进行效果评估][class_1]
1. [保存模型][class_3]

### 网络层相关（Layers）
1.	[如何对Dense层及Dropout层进行基本的配置][class_1]
1. [Conv2D卷积层和MaxPooling2D池化层的使用][class_2]
1. [使用keras.layers.add方法，将两个一模一样的张量进行相加][class_4]

### 经典网络
1. [搭建一个精简版的ResNet网络][class_4]

### 训练技巧
1. [在训练中调用回调函数][class_4]
1. [使用LearningRateScheduler在训练过程中动态的调节学习率][class_4]
1. [使用ModelCheckpoint保存checkpoint][class_4]
1. [使用ReduceLROnPlateau在训练进入平台期的时候动态调节学习率][class_4]

### 其他
1. [何用TensorBoard监控训练过程][class_5]
2. [如何保存网络结构图][class_5]





[class_1]:http://blog.csdn.net/tsyccnh/article/details/78834171
[class_2]:http://blog.csdn.net/tsyccnh/article/details/78835384
[class_3]:http://blog.csdn.net/tsyccnh/article/details/78838005
[class_4]:http://blog.csdn.net/tsyccnh/article/details/78865167
[class_5]:http://blog.csdn.net/tsyccnh/article/details/78867562