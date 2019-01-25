# ak47.py
# AK47类

from gun import *


class AK47(Gun):
    pass
    # def __init__(self):
    #     self.name = 'AK47'
    #     self.max_bulles = 30       # 弹夹容量
    #     self.bullet_left = 0       # 剩余子弹
    #     self.destructRatio = 0.4   # 杀伤系数
    #
    # def reload(self):              # 填弹
    #     self.bullet_left = self.max_bulles   # 填弹后,剩余子弹就等于弹夹容量
    #
    # def fire(self):                # 开火,每发3颗子弹
    #     if self.bullet_left <= 0:
    #         print('请填弹!')
    #         return
    #     elif self.bullet_left > 3:
    #         self.bullet_left -= 3
    #     else:
    #         self.bullet_left = 0   # 全部打出去
    #
    #     damage = int(self.destructRatio * 100)  # 计算杀伤力
    #     print('哒哒哒  杀伤力%2d, 剩余子弹 %2d' % (damage, self.bullet_left))
