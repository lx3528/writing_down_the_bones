听公开课

https://www.bilibili.com/video/BV1gb4y1k7xA?spm_id_from=333.999.0.0

第一讲

![image-20220425081738221](/Users/lixiang/Documents/typora/learn/0415learnthing/planning.assets/image-20220425081738221.png)

怎么样规划的好，通过一个函数定义，fx，决策规划是找到一个最优解



机器学习--定义寻找mapping 到一个状态

大数据motion planning 建立状态到action的映射

imitation learing



搜索是 根据一个状态，优化一个运动的过程

![image-20220425082119320](/Users/lixiang/Documents/typora/learn/0415learnthing/planning.assets/image-20220425082119320.png)

先从一个简单问题来思考--不考虑速度，

扫地机器人path 规划

path finding problem

swarch

bfs--dfs 计算效率更高

<img src="/Users/lixiang/Documents/typora/learn/0415learnthing/planning.assets/image-20220425082345120.png" alt="image-20220425082345120" style="zoom:50%;" />

![image-20220425082401287](/Users/lixiang/Documents/typora/learn/0415learnthing/planning.assets/image-20220425082401287.png)

加入目标信息---强化学习的同学知道！

增加约束了

![image-20220425082523025](/Users/lixiang/Documents/typora/learn/0415learnthing/planning.assets/image-20220425082523025.png)

能看到3步，5步   incremental search

![image-20220425082841744](/Users/lixiang/Documents/typora/learn/0415learnthing/planning.assets/image-20220425082841744.png)

有没有可能全局最优--不能也没必要--北京到上海，人不是一定找到最好，

Dstar论文

折线，并不是一个很好地方式！

怎么加动力学模型

![image-20220425085641244](/Users/lixiang/Documents/typora/learn/0415learnthing/planning.assets/image-20220425085641244.png)



informative，目前有的！

但不平滑object function

![image-20220425090432691](/Users/lixiang/Documents/typora/learn/0415learnthing/planning.assets/image-20220425090432691.png)

20 20 100 m 一角急啥， 动的障碍物

没加上交通规则！

运转周期100ms！

醉酒反应时间下降！

有限时间，找到比较好的解！

![image-20220425090546620](/Users/lixiang/Documents/typora/learn/0415learnthing/planning.assets/image-20220425090546620.png)

静态动态信息输入来进行规划

![image-20220425090647416](/Users/lixiang/Documents/typora/learn/0415learnthing/planning.assets/image-20220425090647416.png)



![image-20220425090734408](/Users/lixiang/Documents/typora/learn/0415learnthing/planning.assets/image-20220425090734408.png)

![image-20220425090818713](/Users/lixiang/Documents/typora/learn/0415learnthing/planning.assets/image-20220425090818713.png)



1 介绍传统robotics入手---

2 怎么处理周围环境，怎么把高静赌徒用手（静态）

3 怎么找到local最优解（动态+全部）

4 一节课介绍em planning---怎么用到无人车上

5 现在流行的方向，data driven 很火。

为什么要做data driven 

最关键的是要知道什么样的问题，才用这个方法，什么能解决，什么不能解决所以用这个！

这节课总结：

1informative 和non- 全职网络  global routing

大致知道怎么走，

2是不是沿着中心线走，是不是换到，动态障碍物静止？交通规则

3 跟control相关，mpec和这个的关系。

![image-20220425091353076](/Users/lixiang/Documents/typora/learn/0415learnthing/planning.assets/image-20220425091353076.png)

