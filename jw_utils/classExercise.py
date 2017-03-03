# -*- coding: utf-8 -*-
# ====================######
# File: ClassExercise.py
# Author: cuijun
# Date: 2016-11-11
# ====================######

# eclipse pydev, python2.7
class GirlFriend:
    population = 0

    def __init__(self, name):
        self.name = name
        print('(Initialize {0})'.format(self.name))
        GirlFriend.population += 1

    def __del__(self):  # 析构器
        print('{0} is being destroyed!'.format(self.name))
        GirlFriend.population -= 1

        if GirlFriend.population == 0:
            print('{0} was the last one.'.format(self.name))
        else:
            # {0:d} 表示使用10进制输出
            print('There are still {0:d} girl friends.'.format(GirlFriend.population))

    def sayLove(self):
        print('Greetings, my boy friend loves me, {0}.'.format(self.name))

    # @staticmethod
    def howMany():
        print('We have {0:d} girl friends.'.format(GirlFriend.population))

    howMany = staticmethod(howMany)


gf1 = GirlFriend('Caroline')
gf1.sayLove()
GirlFriend.howMany()

gf2 = GirlFriend('Wendy')
gf2.sayLove()
GirlFriend.howMany()

del gf1  # 手动调用 程序结束会自动调用析构函数
del gf2

GirlFriend.howMany()