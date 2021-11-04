from torch import nn

import torch

 eb=nn.Embedding(4,6)

 ab=nn.Embedding(8,6)

eb.weight

type(eb.weight)

torch.FloatTensor([1,2,3])

torch.FloatTensor(eb.weight)

torch.nn.Parameter(torch.FloatTensor(eb.weight))

torch.nn.Parameter(torch.FloatTensor(eb.weight-110))

eb.weight=torch.nn.Parameter(torch.FloatTensor(eb.weight-110))

eb.weight

eb

ab=nn.Embedding(8,6)

tmp=torch.cat((torch.FloatTensor(eb.weight-110),torch.FloatTensor(eb.weight-110)),axis=1)

tmp

tmp.shape

tmp=torch.cat((torch.FloatTensor(eb.weight-110),torch.FloatTensor(eb.weight-110)),axis=0)

tmp.shape

ab.weight=torch.nn.Parameter(tmp)

ab

ab.weight

ab.weight=eb.weight

ab

eb

ab.weight.shape

ab(torch.FloatTensor([1,2])

)

ab.weight=torch.nn.Parameter(tmp)

ab(torch.FloatTensor([1,2])

)

ab(torch.LongTensor([1,2])

)

ab.weight

ab.weight=eb.weight

ab(torch.LongTensor([1,2])

)

ab(torch.LongTensor([1,7])

)

ab.weight=torch.nn.Parameter(tmp)

ab(torch.LongTensor([1,7])

)

history

![image-20210407084736063](/Users/lixiang/Documents/typora/技术相关/torch/Untitled.assets/image-20210407084736063.png)

![image-20210407084741040](/Users/lixiang/Documents/typora/技术相关/torch/Untitled.assets/image-20210407084741040.png)

```python
.data.normal_(0, 1)

和torch randn
https://www.cnblogs.com/jfdwd/p/11269601.html
  
```