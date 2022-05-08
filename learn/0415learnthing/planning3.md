# Apollo Planning——Motion Planning With Environment-1

https://www.bilibili.com/video/BV16o4y1X7BD?spm_id_from=333.999.0.0

1研究质点，自行车模型

2 还要考虑刚体，但还是不够



3 怎么样生成平滑的线

--先离散化再优化有问题

--直接优化，也有问题

---道路弯曲坐标怎么办

![image-20220504153206501](/Users/lixiang/Documents/typora/learn/0415learnthing/planning3.assets/image-20220504153206501.png)



pointmass model不太够 configuration space里面 

![image-20220504153316632](/Users/lixiang/Documents/typora/learn/0415learnthing/planning3.assets/image-20220504153316632.png)



前后轮转向不一样，怎么描述这种不一样，怎么描述

![image-20220504153424349](/Users/lixiang/Documents/typora/learn/0415learnthing/planning3.assets/image-20220504153424349.png)

除了坐标，多了个转向，前轮转向和车身heading，没有关系，

车轮一直可动，但对车带来什么difference？

自行车，前进的方向和前轮有关。不可能发生策划

从质点，变到自行车坐标系，变到带转向的。

后轮也是    ---  都是沿着同一个转向中心转

![image-20220504160620371](/Users/lixiang/Documents/typora/learn/0415learnthing/planning3.assets/image-20220504160620371.png)



![image-20220504160628944](/Users/lixiang/Documents/typora/learn/0415learnthing/planning3.assets/image-20220504160628944.png)



差速器，后轮走过的和前轮走过的不一样

这就是bicycle，先从最简单的出发

![image-20220504160842915](/Users/lixiang/Documents/typora/learn/0415learnthing/planning3.assets/image-20220504160842915.png)

运动学模型，但可能会撞到障碍物！



横向偏移了，坐标在什么位置

s坐标 l坐标

ls 最多走一个path

![image-20220504161626195](/Users/lixiang/Documents/typora/learn/0415learnthing/planning3.assets/image-20220504161626195.png)

如果是平行的走的话，k满足这个公式

实际情况，line上偏移了障碍物，nudge一下，那curative就变化了，关系就比较复杂！

sl的推导非常复杂，你们研究下，为什么要做这么一个推导转换



xy坐标对sl坐标是不是唯一的！

园的sy坐标系不唯一，但一定条件下唯一，因为转向半径挺大30-40m

但还是要处理，掉头的线，要考虑如果是个人在中间，

![image-20220504162614600](/Users/lixiang/Documents/typora/learn/0415learnthing/planning3.assets/image-20220504162614600.png)

o1不行，



地图表示什么方式！

找到投影：

![image-20220504162953647](/Users/lixiang/Documents/typora/learn/0415learnthing/planning3.assets/image-20220504162953647.png)

xy题sl坐标！

![image-20220504163012332](/Users/lixiang/Documents/typora/learn/0415learnthing/planning3.assets/image-20220504163012332.png)

下一步研究：

障碍物之间的关系

![image-20220504163211287](/Users/lixiang/Documents/typora/learn/0415learnthing/planning3.assets/image-20220504163211287.png)



动态障碍物，



障碍物本身，凸的polygon。为什么凸 ---用bbbox来研究，相交，

但还是很难！---简化，怎么办

![image-20220504163403002](/Users/lixiang/Documents/typora/learn/0415learnthing/planning3.assets/image-20220504163403002.png)



一定有个支线

![image-20220504163436838](/Users/lixiang/Documents/typora/learn/0415learnthing/planning3.assets/image-20220504163436838.png)



另一种方法，一定可以找到这样的边，然后把两个分割开！

必须要要精确计算，aabb和上面这种不能cover啊，还是on2的问题

什么地方可以简化，什么地方不可以，怎么办呢，并行计算！

aabb nlogn

决策规划系统，障碍物之间碰撞

先把小知识学会，





