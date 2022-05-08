https://www.bilibili.com/video/BV1nL411W7az?spm_id_from=333.999.0.0



接3

拐角的线，mapping很复杂，  半换接支线，不够。



道路中心线平滑，才能沿着这个走！

function是不是连续的

中心线，curature连续的，

不连续，生成的曲线也不是连续的

![image-20220504165438417](/Users/lixiang/Documents/typora/learn/0415learnthing/planning4.assets/image-20220504165438417.png)

无限连续，无限阶光滑，因为高阶导数为0

但能说平滑吗，所以说平滑的道路中心线很重要。

curative进行后期的平滑，可以吗》

![image-20220504165714453](/Users/lixiang/Documents/typora/learn/0415learnthing/planning4.assets/image-20220504165714453.png)



![image-20220504165752674](/Users/lixiang/Documents/typora/learn/0415learnthing/planning4.assets/image-20220504165752674.png)

因为xt yt决定了kappa值，  拿smooth线糊弄，在control看非常危险

增加了误差

必须知道动力学模型，然后在做平滑！

![image-20220504165947032](/Users/lixiang/Documents/typora/learn/0415learnthing/planning4.assets/image-20220504165947032.png)

龙格现象，高阶不能平滑！

然后用b样条

![image-20220504170105066](/Users/lixiang/Documents/typora/learn/0415learnthing/planning4.assets/image-20220504170105066.png)



![image-20220504170138147](/Users/lixiang/Documents/typora/learn/0415learnthing/planning4.assets/image-20220504170138147.png)



![image-20220504170210141](/Users/lixiang/Documents/typora/learn/0415learnthing/planning4.assets/image-20220504170210141.png)

找控制点，但不是插值那样的，插值是必须经过这些点，但不是必须的

但是不要离点太远。--从而生成光滑曲线！

![image-20220504170412679](/Users/lixiang/Documents/typora/learn/0415learnthing/planning4.assets/image-20220504170412679.png)

![image-20220504170451727](/Users/lixiang/Documents/typora/learn/0415learnthing/planning4.assets/image-20220504170451727.png)

![image-20220504170530233](/Users/lixiang/Documents/typora/learn/0415learnthing/planning4.assets/image-20220504170530233.png)



miniaze length的话，还可以编一个形式

smooth line的发展史，就是说你能不能minimize length。二阶导数的变化率，用评方，是因为平放好酸，还能minize 三阶导平滑性指标

性质：

1帮助类条件，从a到b，

前提，只有boundary 给定边界条件下，polynoimal 是可以得到一个最优解

中间有障碍物怎么按，cost很大， piecewise polynomial去搞

![image-20220504171859384](/Users/lixiang/Documents/typora/learn/0415learnthing/planning4.assets/image-20220504171859384.png)

那曲线更加平滑，增加约束项。去模拟真实解！

![image-20220504171945967](/Users/lixiang/Documents/typora/learn/0415learnthing/planning4.assets/image-20220504171945967.png)



![image-20220504172108902](/Users/lixiang/Documents/typora/learn/0415learnthing/planning4.assets/image-20220504172108902.png)



![image-20220504172121177](/Users/lixiang/Documents/typora/learn/0415learnthing/planning4.assets/image-20220504172121177.png)



后面会讲，怎么抽象constraint



spline 2D

生成点，再去平滑够不够，有可能并不满足约束！hit 到bund

用piecewise spline表示曲线，让曲线足够光滑，怎么度量--之前说的，长度短，闭折线

用到导数上，平滑性指标！

 ![image-20220504172813683](/Users/lixiang/Documents/typora/learn/0415learnthing/planning4.assets/image-20220504172813683.png)



min积分，但是发生了，我们希望旋转不变形

curative本身具有旋转不变性，



旋转变换后---我们旋转变化后还是多项式形式！ 



生成的曲线不能随着坐标系的变化而变化，

本身是一个qp的过程·

![image-20220504173753671](/Users/lixiang/Documents/typora/learn/0415learnthing/planning4.assets/image-20220504173753671.png)

用平方的积分是因为，平方好计算！---均值方差好求，但中位数难求

用一节一节的线段表示光滑的曲线，内部二维polynical表示

本身可导，n阶可到。接的点怎么保证平滑。

这个就是约束条件，叫断电的约束条件，保重之间的导数，要相接的

三阶导相等，就能保证三阶导连续，很好地性质。![image-20220504174144420](/Users/lixiang/Documents/typora/learn/0415learnthing/planning4.assets/image-20220504174144420.png)



平滑参考系，是为了后面，相对这个参考系建立path足够的平滑！



螺旋曲线，spiral path

是用极坐标形式，建立，curavature建立。（kappa curature）

![image-20220504174449203](/Users/lixiang/Documents/typora/learn/0415learnthing/planning4.assets/image-20220504174449203.png)



论文中说，如果起点终点满足path，怎么生成螺旋曲线

为什么重要，如果让曲线满足起点终点的条件，

![image-20220504174625234](/Users/lixiang/Documents/typora/learn/0415learnthing/planning4.assets/image-20220504174625234.png)

计算这条线的cost function 有可能和其他线服用

，不用算其他的，叫动态规划 

想生成xy点的曲线，不想用2d spline生成的话，想用spiral生成的话，

就要考虑满足起点终点约束是什么情况

bound hit problem  曲线足够米， 用piecewise polynomial

出发点不一样piecewis 图控件，hen快

spiral是从 configureation space出发  比如开车，转方向盘是否平滑，

转向过程足够平滑，---理论上是比piece和曲率变化大的情况



![image-20220504175026729](/Users/lixiang/Documents/typora/learn/0415learnthing/planning4.assets/image-20220504175026729.png)

![image-20220504175039439](/Users/lixiang/Documents/typora/learn/0415learnthing/planning4.assets/image-20220504175039439.png)

![image-20220504175052249](/Users/lixiang/Documents/typora/learn/0415learnthing/planning4.assets/image-20220504175052249.png)

![image-20220504175106483](/Users/lixiang/Documents/typora/learn/0415learnthing/planning4.assets/image-20220504175106483.png)







