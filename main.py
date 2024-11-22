from itertools import chain
from os import remove

message="hello  DHY"
print(message.title())
print(message.upper())
print(message.lower())
favorite_lang="xxx    "

print(favorite_lang)
#使用str()函数对数字进行显示转换为字符串
age=23
prompt="happy   "+str(age)+"rd Birthday"
print(prompt)

#sector 3
bicycles =['trek','redline']
print(bicycles[0])
my_friends=[' fd1',' fd2']
my_friends.append('xiaohuihui')
my_friends.insert(1,'xiaoming')
tips="i have those friends "
my_friends[0]='liuhuan'
del my_friends[3]
print(tips)
print(my_friends)

popfd=my_friends.pop()
print(popfd)
print(my_friends)

#在知道列表中的<值>是什么的时候可以用remove
removedfd=my_friends.remove('xiaoming') #remove只会删除匹配的第一个元素
print(my_friends)

#print("removed friend"+removedfd) 不可行

#3.3
cars=['bmw','audi','toyota','subaru']
# cars.sort()#改变了原始数据
print(cars)

print(sorted(cars))#sorted提供临时被排列后的数据
# cars.reverse()#永久改变
# print(cars)#倒着打印列表

print(len(cars))
print(cars[-1])#访问列表中最后一个元素

#sector 4
