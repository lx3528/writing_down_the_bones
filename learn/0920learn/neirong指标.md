1常用指标学习

# 之前的总结：



1tensorflow冻层！



https://blog.csdn.net/mingo220/article/details/103568970

https://blog.csdn.net/b876144622/article/details/79962759

https://www.jianshu.com/p/16a42b6a036d



Ssh 网络转发：ssh -L hostA:portA:hostB:portB username@hostB







查看：

data/work/nlu_project/data/corpus_video/standard_test_predict/





REDIS 持久化：

https://blog.csdn.net/zhangpower1993/article/details/89034941



## 二分类问题的指标

**术语**

**TP**(True Positive): 真值为positive，预测为positive的样本数

**FN**(False Negative): 真值为positive，预测为negative的样本数

**FP**(False Positive): 真值为negative，预测为positive的样本数

**TN**(True Negative): 真值为negative，预测为negative的样本数

**指标**

**主要关注指标**

**准确率**（precision）= TP/(TP+FP)

**召回率**（recall）= TP/(TP+FN)

F1-score = 2 * **准确率 \* 召回率 / ( 准确率 + 召回率 )**

**其它指标说明**

**漏检率**（miss rate）= 1 - **召回率**

**误检率**（false alarm ） = FP/(FP+TN)

**正确率** （accuracy）= （TP+TN）/(TP+FP+TN+FN)  

**错误率**（error rate) = 1 - **正确率** 

**灵敏度**（sensitive）= **召回率**

**特异度**（specificity）= TN/(TN+FP) = 1 - **误检率**

## 多标签(multi-label)和多分类(multi-class)

**multi-class**是相对于binary二分类来说的，意思是需要分类的样本不止有两个类别，可能是N个类别取一个。

**multi-label**是更加general的一种情况，一个样本的标签可以有多个。比如一个东西可以既是紫的，又是圆的，又是酸的，又是甜的，它是一颗葡萄。

## 多标签问题的指标

假设各标签之间都不是互斥的，多标签问题本质上可以看成是各个标签上的二分类问题。

在实际标注时会出现两种情况：一是人工标注时容易给出样本所有正确的标签的情况（易完全标注），二是人工标注时难以给出样本所有正确的标签的情况（难完全标注）。在我们的业务中，类目标签、地域标签就是易完全标注的，关键词、概念词就是难完全标注的。

## 易完全标注情况

一般选用的指标包括：Recall、Precision、F1-score。

**每个类别上的指标**

对于每一个类别（标签）上的指标，无论是多分类（单标签）还是多标签，都可以当成独立的二分类问题来统计各指标。具体计算方式参考前述二分类指标。

**综合指标**

比较麻烦的是如何评估总体的的Recall、Precision、F1-score。有几种综合方法可以考虑：

1.微平均(micro-average)，看成是每一个可能的(sample,label)元组是否匹配的二分类问题。比如有N个样本，K个标签，则需要判断的(sample,label)元组总共N*K个。每个(sample,label)元组同等看待。

2.样本平均(sample-average)，先对每个样本计算微平均指标，再取所有样本指标的平均。每个样本同等看待。

3.宏平均(macro-average)，将每个类别上的指标直接平均。大类小类同等看待。

4.加权平均(weighted-average)，将每个类别上的指标按样本占比取平均。大类小类根据样本量分别看待。

下图是scikit-learn的相关表述：





我们在业务中计算综合指标时，使用的是微平均。





## 难完全标注情况

难完全标注情况，主要是由于可选择的标签过多，且可选多个标签。这种情况，人工也不太可能标注出一个比较完善测试集。算法给出置信度排序top k的结果，人工也只能判断算法给出的结果的准确性。

一般选用的指标包括：Top-k正确率，Top-k全对率。

1. Top-k 正确率：算法给出top k 标签中，只要有一个标签正确，这条样本就算预测正确。Top-k 正确率为这样的预测正确样本的占比。
2. Top-k 全对率：算法给出top k 标签中，只有全部标签正确，这条样本才算预测正确。Top-k 全对率为这样的预测正确样本的占比。

我们在业务中使用的是Top-k 全对率。

**
 针对每个标签，当作二分类对待**

得到：

standard_count

pred_count

similar_count

向阳标签：

b，c，d

模型预测：

d，e，f

正确，

similar_count[d]+=1.

向阳标签：

b，c

模型预测：

d，e，f

错误：

standard_count[b]+=1.

standard_count[c]+=1.

pred_count[d]+=1.



**
**