# -*- coding: utf-8 -*-

# mul_inh.py
# 多重继承实例
# 超人类继承自战士、飞行者、喷火者
# 三个类


class Fighter:           # 默认继承自object
    def fight(self):
        print('我能战斗')

    def roar(self):
        print('战士吼叫！！！嗷嗷嗷！！！')


class Firer:
    def fire(self):
        print('我能喷火')


class Flyer:
    def fly(self):
        print('我能飞翔')

    def roar(self):
        print('飞行者吼叫！！！呼呼呼！！！')


class SuperMan(Flyer, Fighter, Firer):   # 多继承,若方法名称相同，则按此顺序调用第一个父类里的
    pass


if __name__ == '__main__':
    super_man = SuperMan()
    super_man.fight()
    super_man.fly()
    super_man.fire()
    super_man.roar()  # 超人吼叫，先调用自身方法，若没有，则按父类列表顺序，找到第一个出现此方法的类的方法
    # Method Resolution Order
    # 决定调用哪一个父类方法
    # print(SuperMan.__mro__)
    print(SuperMan.__bases__)
    print(Fighter.__bases__)
    print(Flyer.__bases__)
    print(Fighter.__bases__)
