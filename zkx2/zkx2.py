#!/user/bin/ebv python
# -*- coding:utf-8 -*-

#写入
'''
f=open ("D:\\softwaredata\\gy-1911A\\test.txt","a",encoding="utf-8")
f.write("你好，宝宝\n")
f.writelines(["你好,我是谁,我在哪\n"])
f.close()

f=open("test.txt","r",encoding="utf-8")
#c=f.read()
#print(c)
#lines=f.readlines()
#print(lines)
line=f.readline()
print(line)
f.close()

with open("test.txt","r",encoding="utf-8") as f:
    c=f.read()
    print(c)

t=1
for i in range(2,101):
   if i < 101:
       t=t+i
print(t)

class HoWo():
    a1=10
    f=3
    def b(self):
        print(self.f)

c = HoWo()
c.b()

class Product():
    size="7寸"
    type="老年机"
    def __init__(self,color):
        #pass
        self.color=color

    def call(self):
        print("hi")
    def sendmessage(self):
        print("来找我玩")

#实例化
phone1=Product("粉色")
print(phone1.color)
print(phone1.size)
print(phone1.type)
phone1.call()
phone1.sendmessage()
'''


#import json

#j='''{"name":"小明","sex":"未知"}'''

'''
d= json.loads(j)
d["sex"]="男"
print(d)

j=json.dumps(d,ensure_ascii=False)
print(j)

#import random
#a=random.randint(10,20)
#print(a)

import random
c=random.choice((1,2,3,4))
print(c)

import os
i=os.path.abspath("test.txt")
print(i)

d=os.path.dirname(i)
print(d)

f=os.path.basename(i)
print(f)

os.mkdir("zkx3")

'''

import selenium.webdriver

import os
try:
    os.mkdir("gy_C")
except FileExistsError:
    print("file exist")
else:
    print("create file successfully")
finally:
    print("game over")

print("123")

