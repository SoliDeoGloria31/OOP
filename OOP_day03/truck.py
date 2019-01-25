# -*- coding: utf-8 -*-

# truck.py
# 卡车类，演示运算符重载

class Truck:
    def __init__(self,load):
        self.load = load     # 载重

    def __add__(self,value):
        print('__add__()被调用')
        return Truck(self.load + value)

    def __mul__(self,value):
        return Truck(self.load*value)

    def __str__(self):
        return 'load: %d' % self.load


if __name__=='__main__':
    t = Truck(20)
    t2 = t + 1
    print(t2)
    t3 = t *4
    print(t3)