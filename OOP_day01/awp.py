# awp.py
# 狙击枪类


from gun import *


class AWP(Gun):
    # def __init__(self):
    #     self.telescope_type = telescope_type

    def openTelescope(self):
        print('瞄准镜已打开!')

    def closeTelescope(self):
        print('瞄准镜已关闭!')

    # def __init__(self):
    #     self.name = 'AWP'
    #     self.max_bulles = 10       # 弹夹容量
    #     self.bullet_left = 0       # 剩余子弹
    #     self.destructRatio = 1.0   # 杀伤系数
    #
    # def reload(self):              # 填弹
    #     self.bullet_left = self.max_bulles   # 填弹后,剩余子弹就等于弹夹容量
    #
    # def fire(self):                # 开火,每发3颗子弹
    #     if self.bullet_left <= 0:
    #         print('请填弹!')
    #         return
    #     self.bullet_left -= 1
    #
    #     damage = int(self.destructRatio * 100)  # 计算杀伤力
    #     print('bong!!!  杀伤力%2d, 剩余子弹 %2d' % (damage, self.bullet_left))
