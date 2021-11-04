除了上一个说的内容理解的pr指标外，

说下推荐的相关指标：



#### auc：

正样本预测结果，大于负样本的预测结果的概率

###### 推荐系统之AUC评价指标https://zhuanlan.zhihu.com/p/73335362



#### Ap:

```python
def AP(ranked_list, ground_truth):
    """Compute the average precision (AP) of a list of ranked items
    ground_truth 表示是否正确的标识
    hits 表示 score （预测结果分值）倒排，从第0个到当前个的累计预测正确样本数
    sum_precs 表示每个 ground_truth = 1 的位置的 precision 的累加
    """
    hits = 0
    sum_precs = 0
    for n in range(len(ranked_list)):
        if ranked_list[n] in ground_truth:
            hits += 1
            sum_precs += hits / (n + 1.0)
    if hits > 0:
        return sum_precs / len(ground_truth)
    else:
        return 0

```



召回结果的平均准确率：

![image-20210920121851183](/Users/lixiang/Documents/typora/learn/0920learn/tuijian.assets/image-20210920121851183.png)

###### 推荐系统中的 MAP 评估指标https://blog.csdn.net/xiedelong/article/details/112500657

### 3map：

多个用户的平均ap

### 4mrr

###### MRR-推荐算法评价指标https://blog.csdn.net/devil_son1234/article/details/108727990

正确检索结果值在检索结果中的排名（多个序相加，除以用户数）



5ndgc：

gain：收益，在推荐中，为1

cg：k个item的gain累加

discounted cumulative gain： gain/rank排位(log)

Ndcg:推荐的dcg，除以理想情况--推荐都为1的时候的idcg

###### NDCG及实现https://zhuanlan.zhihu.com/p/84206752



我的实现：

只实现了dcg，不是很全！！

http://localhost:8888/notebooks/arena/algorithm/mywork/recom_kup20/src/process.ipynb











auc说明：

离线评价指标一定要跟线上业务指标一致，可以拿历史数据做回放，来模拟用户行为，再计算业务指标。当然这部分回放数据不能出现在训练集里面

推荐的指标：

