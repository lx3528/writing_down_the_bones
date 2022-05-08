https://www.bilibili.com/video/BV1LM4y1M7UW?spm_id_from=333.999.0.0

d无节课

![image-20220504175234358](/Users/lixiang/Documents/typora/learn/0415learnthing/pingning5.assets/image-20220504175234358.png)

抽象离散空间，把重复计算铜过agg方式简化！

光有动态规划，够不够！

piecewise linear 

打成很细的网格，是能达到最优解，但计算是

![image-20220504175353088](/Users/lixiang/Documents/typora/learn/0415learnthing/pingning5.assets/image-20220504175353088.png)

牛顿法，比bs快，看变化趋势，是qp的核心。

指数收敛， 指数的速度，log指数的iteration number

收敛到最优解

没有考虑斜率变化率，牛顿法核心思想，二阶泰勒展开

一阶逼近，是binary search。



二次规划，脱离不开tayir展开，只是涉及到--是一个均衡的过程



牛顿法，--- 

收敛性很难保证，不一定收敛最优解

 二次规划，动态规划，都不太行。分段，diverand concquer



emplann 组合优化的思想，dvide and conquer

启发式搜索

粗浅的认识，

撒点，

![image-20220504190218225](/Users/lixiang/Documents/typora/learn/0415learnthing/pingning5.assets/image-20220504190218225.png)

启发式搜索，+动态+dp emplanning

想得到global 先dp得到粗浅认识，然后再细化！

决策问题，从左边nudge 还是右边，用动态规划，



模拟退火，借鉴---组建搜索加快，不一定收敛到最优解，

只要reward function不是很麻烦基本上接近了



![image-20220504190622157](/Users/lixiang/Documents/typora/learn/0415learnthing/pingning5.assets/image-20220504190622157.png)

二次规划

qp问题，最优解，要么在边界，要么，最终集

唯一

![image-20220504190902963](/Users/lixiang/Documents/typora/learn/0415learnthing/pingning5.assets/image-20220504190902963.png)

没有约束条件，求导数，+边界两个点。

active constraint

二次规划问题，

![image-20220504191056314](/Users/lixiang/Documents/typora/learn/0415learnthing/pingning5.assets/image-20220504191056314.png)



![image-20220504191231824](/Users/lixiang/Documents/typora/learn/0415learnthing/pingning5.assets/image-20220504191231824.png)

数值分析，求解方程组的步骤

![image-20220504191259334](/Users/lixiang/Documents/typora/learn/0415learnthing/pingning5.assets/image-20220504191259334.png)

没有约束，可以很快地求解线性返程组，on3

带约束呢

![image-20220504191358160](/Users/lixiang/Documents/typora/learn/0415learnthing/pingning5.assets/image-20220504191358160.png)



ex=d 是高位空间超平面，

![image-20220504191505528](/Users/lixiang/Documents/typora/learn/0415learnthing/pingning5.assets/image-20220504191505528.png)

好处理

![image-20220504191530185](/Users/lixiang/Documents/typora/learn/0415learnthing/pingning5.assets/image-20220504191530185.png)

最优解是导数为0的店！

![image-20220504191723856](/Users/lixiang/Documents/typora/learn/0415learnthing/pingning5.assets/image-20220504191723856.png)



如果约束太满，满职 那就直接输出！--注意constraint

![image-20220504191829336](/Users/lixiang/Documents/typora/learn/0415learnthing/pingning5.assets/image-20220504191829336.png)

active constraint

![image-20220504191947896](/Users/lixiang/Documents/typora/learn/0415learnthing/pingning5.assets/image-20220504191947896.png)

如果是非active dual parameter lambda 为0

interior method

![image-20220504192210741](/Users/lixiang/Documents/typora/learn/0415learnthing/pingning5.assets/image-20220504192210741.png)



从qp出发，先从一维和牛顿法出发，然后高维qp怎么解，在没有约束情况下，你的最优解应该怎么样去求解，有约束情况下，最优解应该怎么样求解，同事参考kkt，lagrangian 

目标函数不是二次型呢？不是二次型的凸的



![image-20220504192537216](/Users/lixiang/Documents/typora/learn/0415learnthing/pingning5.assets/image-20220504192537216.png)

有局部牛顿法逼近。先求二阶导，只要error能控制主， 构造一个qp问题。估计收敛

![image-20220504192724594](/Users/lixiang/Documents/typora/learn/0415learnthing/pingning5.assets/image-20220504192724594.png)

高维空间hessian难求

---拟牛顿法，lbfgs~

总结：

solve nonlinear optimization 首先，无人车本身是nonlinear optimization 首先它不一定是凸的，

![image-20220504193023253](/Users/lixiang/Documents/typora/learn/0415learnthing/pingning5.assets/image-20220504193023253.png)

用了个启发式搜索的方法，先用动态规划给一个粗略解，右边好，那就右边qp凸空间

![image-20220504193113587](/Users/lixiang/Documents/typora/learn/0415learnthing/pingning5.assets/image-20220504193113587.png)



![image-20220504193131545](/Users/lixiang/Documents/typora/learn/0415learnthing/pingning5.assets/image-20220504193131545.png)



