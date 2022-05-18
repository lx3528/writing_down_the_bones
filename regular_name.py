#coding=utf-8
'''
Python会默认使用ASCII码保存文件，这时如果你的代码中有中文就会出错了，即使你的中文是包含在注释里面的，将文件存成了UTF-8也没用。。
遍历所有的文件

然后修改文件名字 让其符合windows的格式要求
'''
import os

escapechar=["?","、","\\","/",":","*","<",">","|"]
print("len:",len(escapechar))
for i in escapechar:
    print("now_char:",i)

path1="./"

all_arr=[]
def parse_dir(path1):
    if ".git" in path1:
        return
    global all_arr
    l1_name=os.listdir(path1)

    for name in l1_name:
        new_path=os.path.join(path1,name)

        if not os.path.exists(new_path):
            print("not has")

        if os.path.isdir(new_path):
            parse_dir(new_path)
        else:
            all_arr.append(new_path)

    #add_dir_patg
    all_arr.append(path1)

parse_dir(path1)


print("all_arr",all_arr)
for i in all_arr:
    for esc in escapechar:
        if esc in i:
            print("now_in",i)

