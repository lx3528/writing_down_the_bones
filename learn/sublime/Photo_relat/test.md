

相反数

~a+1

~这个符号表示按位取反

1. !是逻辑运算符(与||，&&是一类符号)，表示逻辑取反，可以把非0值变成0，把0值变为1
2. ~是位运算符（与|，&是一类符号），表示按位取反，在数值的二进制表示上，将0变为1，将1变为0

  **&** （位  “与”）  and
   **^** （位  “异或”）
   **|**  （位   “或”）  or
   **~** （位  “取反”）
2 移位运算符：
   **<<**（左移）

   **>>**（右移）

void Binarycout(int n) 
{ 
 for (int i=31;i>=0;i--) 
 { 
 cout<<((n>>i)&1); 
 } 
 cout<<endl; 
} 

```
for(vector<int>::iterator iter=ivec.begin();iter!=ivec.end();++iter)
        *iter=0;
```

if (testMap.find(key) == testMap.end())    cout << "no this key" << endl;