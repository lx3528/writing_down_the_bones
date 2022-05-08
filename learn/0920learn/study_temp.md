query被切割分词成多个term后，term之间的距离与顺序跟文本相关性有关





推荐系统&计算广告

https://www.zhihu.com/collection/148983717?page=3

#### 小白必看：一文读懂推荐系统负采样

https://zhuanlan.zhihu.com/p/387378387



###### 《推荐系统》系列之三：一文读懂冷启动推荐https://zhuanlan.zhihu.com/p/376798647



###### 想学习推荐系统，如何从小白成为高手?

在理解基本的推荐知识之后，你大概会了解到推荐具体是做什么的，那么其问题又可以分成几个方面。如召回、CTR预估、Learning to Rank等等。这个时候我建议的话就是开始阅读经典论文了。下面整理一些我看过的比较经典的论文吧，可能有遗漏，也欢迎大家补充。FM：《Factorization Machines》
FFM：《Field-aware Factorization Machines for CTR Prediction》
DeepFM：《DeepFM: A Factorization-Machine based Neural Network for CTR 
链接：https://www.zhihu.com/question/23194692/answer/805896718







###### 点估计、区间估计、中心极限定理之间的联系https://www.zhihu.com/question/21871331

###### 中心极限定理是推断统计（包含参数估计和假设检验）的理论基础，从而也是参数估计（包含点估计和区间估计）的基础



学习负采样：

1借鉴skip-gram的negative sample

###### 基于Skip-gram的负采样https://zhuanlan.zhihu.com/p/153502072

###### 理解 Word2Vec 之 Skip-Gram 模型https://zhuanlan.zhihu.com/p/27234078

一元模型分布（unigram distribution）”来选择“negative words

高频词，低频词，每个词分配长度：

![image-20210920125409180](/Users/lixiang/Documents/typora/learn/0920learn/study_temp.assets/image-20210920125409180.png)

能够提升腰部被采集到的概率。



2real negative subsampling的方法：

高曝光负样本，丢弃

3sample refinement with pu learning

可能负样本--过一个分类器，学习可靠的负样本，对负样本进行泛化！

4**Fuzzy Positive Sample Augmentation**

扩充正样本-- 去cpm高的，去精排高的，label要小于1

5sampling with noise contrastive estimation

###### 推荐系统遇上深度学习(一零二)-[百度]展示广告中的样本优化https://blog.csdn.net/abcdefg90876/article/details/109712698

###### 召回]_百度Sample Optimization For Display Advertisinghttps://zhuanlan.zhihu.com/p/306262182



###### Noise Contrastive Estimation 学习https://zhuanlan.zhihu.com/p/58369131





我就是cv转过来的，建议先从基本流程着手：数据产出-特征工程-召回-模型训练-排序调优-线上serving等，整体流程要有个概念，自己负责的模块则需要精通

![image-20220227224334446](/Users/lixiang/Documents/typora/learn/0920learn/study_temp.assets/image-20220227224334446.png)



