



有line有segement，等等



【Baidu Apollo】6.2 Lattice Planner规划算法

https://blog.csdn.net/yuxuan20062007/article/details/82330165



规划详解：https://blog.csdn.net/nn243823163/article/details/124029553

Lattice Planner从学习到放弃（二）：二次规划的应用与调试、https://zhuanlan.zhihu.com/p/266901715



百度无人驾驶系统Apollo 2.0小解析https://zhuanlan.zhihu.com/p/32511462

Apollo 2.0 框架及源码分析(一) | 软硬件框架 

<img src="/Users/lixiang/Documents/typora/learn/0415learnthing/apollo业务.assets/image-20220417144852239.png" alt="image-20220417144852239" style="zoom:50%;" />

![image-20220417144917535](/Users/lixiang/Documents/typora/learn/0415learnthing/apollo业务.assets/image-20220417144917535.png)



![image-20220417145319141](/Users/lixiang/Documents/typora/learn/0415learnthing/apollo业务.assets/image-20220417145319141.png)

perception--感知障碍物，标志，

perdiction--感知别人是怎么走de

routing模块就可以根据终点位置计算出具体的导航信息

根据车辆定位模块**localizationg**提供的车辆位置由planning模块得到车辆应该走的具体车道

得到车道后车辆**control**模块结合车辆的当前状态计算加速、刹车和方向的操作信号，此信号进入CAN卡后输出到车内，如此实现了车辆的自动驾驶



Apollo 2.0 框架及源码分析(三) | 感知模块 | Radar & Fusionhttps://zhuanlan.zhihu.com/p/33852112



Apollo 2.0 框架及源码分析(二) | 感知模块 | Lidar：https://zhuanlan.zhihu.com/p/33416142

太牛了，流程框图直接都看明白了：Apollo Planning模块源代码分析https://blog.csdn.net/davidhopper/article/details/79176505

但估计还是看不懂！



二次规划是规划什么的

