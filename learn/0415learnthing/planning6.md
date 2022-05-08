apollo怎么做的！

百度apollo的东西，

上节课，规划的核心，dp qp，

---reward问题优化

然后学了怎么和环境交互的问题，aabb，在优化问题里面，

objective function是什么，通过平滑性，各方面指标定义。是一个合集

优化问题，前面还介绍了build block constant obj func怎么设置。

剩下，包括solver，solver怎么样去qp dp怎么去solve 

实际中无人车，怎么样抽象，constraint

![image-20220504201458509](/Users/lixiang/Documents/typora/learn/0415learnthing/planning6.assets/image-20220504201458509.png)



动态障碍物，逆向车----最难得

人为的decision，决策问题， 选择的过程，优化，dp发挥很多重要，

人为的决策，不能很好地搞。

不能overtake ，直接follow  交通规则，不能商量，

把decision 更加平滑，三维空间优化问题，local op

smoothing spline 抽象问题，qp是slover

soft -》decision！

换道的决策，可以改，parella 

本车道生成一个策略trajectory

下一个车道生成一个策略。trajectory

再比较哪个好！

![image-20220504202547950](/Users/lixiang/Documents/typora/learn/0415learnthing/planning6.assets/image-20220504202547950.png)



三维空间的难点，抽象

二维，能画，三维，拓扑意义上，很复杂，slt，一个车，不是简单的一条线段，

离散化方式，--生成三维空间的trajectory。

trajectory optimization in frenet frame

路径函数空间+无穷维度，降为到paraed 维度，像poly

能不能handle复杂case。 

高维空间优化：

1 离散化cf 生成三维轨迹，---》trajectory optimization in frenet frame  第一节课，第二节课的文章

2 sample 颗粒度，dp，discretize都有颗粒度，轨迹，不是很局限，也可以很乱，轨迹函数 正无穷维度，用参数化的，比如多项式，可以降成常数项维度的。

曲线的自由度也有限制。



-----全局化，后话！千万不要局限某种方法，所有问题，都有他的问题，这些都是你的参考， 最重要的是你自己。

path speed iterative algorithm

em可以证明到local 最优化。考虑不了那么多事情，翔安一件事，先在一个维度进行优化，另一个维度优化，先考虑一个问题。再另一个方向的最优解。

实际生活中，期末考试，先复习数学，然后交换。

无人车上，先生成optim path，在这个path基础上，把所有障碍物进行投影，given方向盘这样去动，怎么样生成一个，最优速度方案。然后 =-》速度在下一个周期会送到路径优化中。 

不断迭代得到最优间，em的缺点：迭代算法，贪心算法，只能收敛local optim，你说够不够用

取决于什么样的问题！   能不能满足交通规则，local也是可以的，超高的话，会完全不一样。

二维，三维聚云分布在立方体。超高为，重量分布，是在表面，非常有意思。



em寻找最优解的过程， ---》出现在40m的位置。40m最优nudge ，需要减速，---然后新的速度给轨迹--规划处新的路径，根据现在·的现象得到一个最优的，能够converge到local的性质很重要。

![image-20220504205745805](/Users/lixiang/Documents/typora/learn/0415learnthing/planning6.assets/image-20220504205745805.png)

最大的刹车粒度是多少，然后提前减速。dynamic constraint也很重要

先通过dp，有花的方式给出来，更平滑的解， 在决策规划问题里面，path里面·，![image-20220504210243260](/Users/lixiang/Documents/typora/learn/0415learnthing/planning6.assets/image-20220504210243260.png)

动态规划也是优化问题，优化问题，有objective function

找离散的线，通用考虑够不够平滑，大概够不够避开障碍物，不要求是凸的



![image-20220504210430913](/Users/lixiang/Documents/typora/learn/0415learnthing/planning6.assets/image-20220504210430913.png)

怎么抽象成qp问题，用smooth spline表示连续的函数，三阶导数连续

而且能满足约束条件和自由解！

是二次型，



动态怎么做：

st图：

![image-20220504210832179](/Users/lixiang/Documents/typora/learn/0415learnthing/planning6.assets/image-20220504210832179.png)

![image-20220504211008250](/Users/lixiang/Documents/typora/learn/0415learnthing/planning6.assets/image-20220504211008250.png)

能不能摒弃dp ---因为上面nudge 下面接受了（很难知道是不是overtake 然后yield  不够smooth

镇与镇连续性，不  决策有连续性，进一步，规划也要连续性，因为控制的同学最不喜欢这样

（假象副驾驶频繁的叫你换，这样好吗）

100ms后又规划了一条线，因为taylor 站考，smooth line 这两天最优解的距离差的很小。被error控制的！

因为高阶收敛

control为什么眼睛mpc。把qp和控制结合，利用稳定接，苏孔，知道设呢么时候该打方向盘。如果pid做控制，	是一直跟error来谎。error用到mpc很多！

![image-20220504211730653](/Users/lixiang/Documents/typora/learn/0415learnthing/planning6.assets/image-20220504211730653.png)

![image-20220504211802874](/Users/lixiang/Documents/typora/learn/0415learnthing/planning6.assets/image-20220504211802874.png)

hotstart 最优的差不多，从上一个点出发（qp可以，保证decision连续）



难得地方，是什么，工程化的问题！

决策可执行性，看到车让不一定cover case ，遇到了你怎么办

换到怎么搞，并行化

决策规划的平滑性，中心线，生成轨迹的平滑性。通过smooth

时效性，c++ 

硬件级别的优化！

![image-20220504212036042](/Users/lixiang/Documents/typora/learn/0415learnthing/planning6.assets/image-20220504212036042.png)



![image-20220504212131315](/Users/lixiang/Documents/typora/learn/0415learnthing/planning6.assets/image-20220504212131315.png)









