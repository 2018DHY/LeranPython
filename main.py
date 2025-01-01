from itertools import chain
from math import frexp
from os import remove


def mypt(log=""):
    print("\n"+log+"\n")

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

print("-----------sector4-------------")
magicians =['alice','david','carolina']
#for循环下连续的行,有缩进的行,每一次循环都会执行一次
for item in magicians:#不要忘了冒号
    print("welcom !!!"+item)
    print(item.title()+", that was a great trick!!!")

print("\nThank you ,everyone.That was a great magic show!")

print(len(magicians))
# for num in len(magicians):
#     print(num)

#4.4使用列表的一部分
print("-----------4.4-------------")
players=['charles','mrtina','michael','florence','eli']
print(players[0:3])#此处打印players的子集,从0开始三个元素(0,1,2)
print(players[:4])#没有指定开始的话,自动从零开始
print(players[-3:])#负数索引代表离列表末尾相应距离的元素,末尾不指定代表到末尾

#复制列表
print("-----------4.4.3-------------")
my_foods=['pizza','falafel','cake']
friends_foods=my_foods[:]#代表复制
my_foods.append('rice')
friends_foods.append('noodle')
print(my_foods)
print(friends_foods)

friends_foods=my_foods#friends_foods与my_foods指向同一个空间
my_foods.append("apple")
friends_foods.append("orange")
print(my_foods)
print(friends_foods)

#元组 用圆括号标识
print("-----------4.5-------------")


#sector5 if语句
print("-----------sector5-if语句-------------")
cars=['bmw','audi','toyota','subaru']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

answer=17
if answer !=42:
    print("\nthat is not the correct answer")

age0=22
age1=18
if age0>=21 and age1>=22:
    print("\nboth are pass!\n")
else:
    print("\nboth are not pass!\n")

print(age0>=21 or age1>=21)
#if else
age=17
if age>=18:
    print("you are old enough to vote");
    print("have you registered to vote yet?")
else:
    print("sorry,you are too young to vote")
    print("please register to vote as soon as you turn 18")

#if elif else (else可以省略)
print("\n#if elif else\n")
age=12

if age <4:
    print("you admission cost is $0")
elif age<18:
    print("your admission cost is $5")
else:
    print("your admission cost is $10")

#5.4 使用if判断列表是不是空的
mypt("5.4 使用if判断列表是不是空的")
requested_toppings=[]
if requested_toppings:
    for requested_topping in requested_toppings:
        print("Adding"+ requested_topping + ".")
    mypt("Finished making your pizza")
else:
    print("Are you sure you want a plain pizza")

#sector6 字典 描述为键值对
mypt("sector6 字典")

alien_0={}#空字典
alien_0['color']='green'
alien_0['points']=5
print(alien_0)

#6.2.4修改字典中的值
alien_0['color']='yellow'
print(alien_0)


#sector8函数
def get_name(name='dhy'):
    print(name)
