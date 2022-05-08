第二讲：

https://www.bilibili.com/video/BV1mM4y1M7cK?spm_id_from=333.999.0.0



![image-20220425130849368](/Users/lixiang/Documents/typora/learn/0415learnthing/planning2.assets/image-20220425130849368.png)

![image-20220425130933241](/Users/lixiang/Documents/typora/learn/0415learnthing/planning2.assets/image-20220425130933241.png)



从离散化场景出发：

质点模型：

 机器人系统的构形空间（即C空间）是系统所有可能构形的空间。因此，构形只是这个抽象构形空间中的一个点https://blog.csdn.net/penge666/article/details/78841812

![image-20220425131022483](/Users/lixiang/Documents/typora/learn/0415learnthing/planning2.assets/image-20220425131022483.png)



质点模型，有些东西处理不了，碰撞。

增加了optimation的难度

用自行车模型不太够

![image-20220425131217653](/Users/lixiang/Documents/typora/learn/0415learnthing/planning2.assets/image-20220425131217653.png)

minimal length但不平滑

![image-20220425131251985](/Users/lixiang/Documents/typora/learn/0415learnthing/planning2.assets/image-20220425131251985.png)



曲率不连续

所以需要combination smooth

![image-20220425131334067](/Users/lixiang/Documents/typora/learn/0415learnthing/planning2.assets/image-20220425131334067.png)



![image-20220425131342679](/Users/lixiang/Documents/typora/learn/0415learnthing/planning2.assets/image-20220425131342679.png)



![image-20220425131400065](/Users/lixiang/Documents/typora/learn/0415learnthing/planning2.assets/image-20220425131400065.png)



离散化，优化在边界，但别介不好，碰怎么办，后话

![image-20220425131455518](/Users/lixiang/Documents/typora/learn/0415learnthing/planning2.assets/image-20220425131455518.png)

3



![image-20220425131519235](/Users/lixiang/Documents/typora/learn/0415learnthing/planning2.assets/image-20220425131519235.png)



![image-20220425131536419](/Users/lixiang/Documents/typora/learn/0415learnthing/planning2.assets/image-20220425131536419.png)



![image-20220425131552813](/Users/lixiang/Documents/typora/learn/0415learnthing/planning2.assets/image-20220425131552813.png)



局部撒点

![image-20220425131609625](/Users/lixiang/Documents/typora/learn/0415learnthing/planning2.assets/image-20220425131609625.png)

![image-20220425131623358](/Users/lixiang/Documents/typora/learn/0415learnthing/planning2.assets/image-20220425131623358.png)

![image-20220425131630529](/Users/lixiang/Documents/typora/learn/0415learnthing/planning2.assets/image-20220425131630529.png)



![image-20220425131654588](/Users/lixiang/Documents/typora/learn/0415learnthing/planning2.assets/image-20220425131654588.png)

真的平滑了吗--高速，这么打方向吗--规则道路不用这么撒点

![image-20220425131809368](/Users/lixiang/Documents/typora/learn/0415learnthing/planning2.assets/image-20220425131809368.png)

打死，还是不够平滑--但解决了问题方格。打死，然后打死---一会左，一会右！

但可以解决了，有多个处理方法！但每一步指数级别！

先撒点，然后平滑线连接，都是在fix点上，简化计算，



动态规划本质，动力学有些重复计算，记录下来

![image-20220425132326473](/Users/lixiang/Documents/typora/learn/0415learnthing/planning2.assets/image-20220425132326473.png)

怎么撒 sl坐标系上，frenet frame 



还缺时间， 时间维度上sample。然后用dp--为什么要时间，因为动态障碍物的存在，碰撞，所以需要加上这个障碍物进行规划！

复杂度很高

![image-20220425140106993](/Users/lixiang/Documents/typora/learn/0415learnthing/planning2.assets/image-20220425140106993.png)



横向和纵向，path 和speed的规划，三维很难，人可以绕过去，从拓扑意义上，更难，

在抽象支线点后，怎么用平滑线去做

有人用螺旋线来做！

![image-20220425140256647](/Users/lixiang/Documents/typora/learn/0415learnthing/planning2.assets/image-20220425140256647.png)



分成path和speed两个模块去优化

有一招就是低位先解决，然后转换为高位

三维先拆借为一个是xy，一个是st，两个超平面上解决，然后---path speed iterative的方式，解决！

搜索问题，扎到---global太男，所以local的方式，三维增加维度上升了N

local的发发不一定最优，迭代怎么能克服drawbach



所有模型是错的，但是有有用的，有信息的，

rrt不能搞，path不幸。

![image-20220425140745705](/Users/lixiang/Documents/typora/learn/0415learnthing/planning2.assets/image-20220425140745705.png)



用到的是什么，图控件，凸优化，有唯一最优解。要么在边界，要么在中心点，非常快速度！

牛顿法---需优化，二次迭代收敛double exp

所以为什么用qp，要求目标函数tu

tu的性质

但无人车本质不是tu的。---，非常快

![image-20220425231710133](/Users/lixiang/Documents/typora/learn/0415learnthing/planning2.assets/image-20220425231710133.png)

先优化再平滑，先找折线，b样条，也是piecewise polynomial的。cubic bspline

但curation是这样

![image-20220425232010496](/Users/lixiang/Documents/typora/learn/0415learnthing/planning2.assets/image-20220425232010496.png)



方向盘抖，更告诫 quadratic cubic》

![image-20220425232137138](/Users/lixiang/Documents/typora/learn/0415learnthing/planning2.assets/image-20220425232137138.png)

![image-20220425232205741](/Users/lixiang/Documents/typora/learn/0415learnthing/planning2.assets/image-20220425232205741.png)



无穷解平滑

有没有其它问题，1撞到障碍物！

2uturn





平滑性基础上安全性

interpolation，差值穿过这些点，高阶---但有龙格现象。

![image-20220425232331622](/Users/lixiang/Documents/typora/learn/0415learnthing/planning2.assets/image-20220425232331622.png)



motionplanning有的时候



降为，然后不断迭，先生成path，然后生成speed

![image-20220425232759273](/Users/lixiang/Documents/typora/learn/0415learnthing/planning2.assets/image-20220425232759273.png)



b样条，先生成离散点，然后平滑！



先介绍了在有限制环境下怎么做，rrt，lattice，之后介绍了现在的做法，dp和qp。但怎么着点









