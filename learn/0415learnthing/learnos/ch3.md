ubuntu 安装这个sudo apt install libusb-dev



-std=c++11

课程怎么看，看课程，然后总结。



有个东西叫tldr Linux终端小工具之tldr:https://cloud.tencent.com/developer/article/1839955



Xv6

https://alfredthiel.gitbook.io/pintosbook/

操作系统自学：

6.s081

https://github.com/panks/Xv6

riscv64没啥历史包袱

理解jyy课的代码，

创建两个线程交替出现a和b

![image-20220523082553956](/Users/lixiang/Documents/typora/learn/0415learnthing/learnos/ch3.assets/image-20220523082553956.png)

200%的cpu load

4个线程为啥还是200%，说明只有2个cpu！



1如何证明线程确实共享内存

定义一个全局变量

2如何证明线程具有独立堆栈：



栈是从高地址向低地址增长

每个线程8192kb，写小程序，知道计算机系统发生了什么，一页是什么 

（栈帧）

strance看系统调用



原子性：

1alipay因为付钱时候，多个线程都在减钱，钱为0了还被减，unsign会出现费城大的数

2多线程求和，不是正确的，因为sum++ 不是原子操作。 原子操作还不行，还需要带lock，！



那为啥printf没有奇怪的字符，写乱之类的，因为有缓冲区！thread safety 

所以lock unlock可以阻止并发

99%---队列

顺序：

O1 

o2优化--单线程顺序优化代码，



可见性：

x=1操作原子化--》先取x到寄存器，修改寄存器，寄存器存入x的内存！

为啥会出现00，因为今天的处理器也是编译器！

cpu乱序执行，指令重排

tomasulo算法，

