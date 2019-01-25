from bird import *


class Ostrich(Bird):
    def __init__(self, name, sex, fly, reproductin, run):
        super().__init__(name, sex, fly, reproductin)
        self.run = run

    def run_(self):
        print('%s刚跑了%.2f里~' % (self.name, self.run))

    def fly_(self):  # 重写fly方法
        print('我是%s,太重了不能飞！~' % self.name)
