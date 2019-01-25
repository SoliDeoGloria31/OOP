import pygame
from pygame.locals import *

# awp.py
# 狙击枪类


class AWP:
    def __init__(self, img_path, x, y, window):  # 构造方法
        self.name = "AWP"  # 名称
        self.max_bullets = 10  # 弹夹容量
        self.bullet_left = 0  # 剩余子弹
        self.destructRatio = 1.0  # 杀伤系数
        self.img = pygame.image.load(img_path) # 枪的图片
        self.x = x # 枪的起始ｘ坐标
        self.y = y # 枪的起始ｙ坐标
        self.window = window # 贴在窗口中
        self.fire_sound = pygame.mixer.Sound("awp.ogg")  # 枪的开火音效

    # 枪的贴图方法
    def display(self):
        self.window.blit(self.img, (self.x, self.y))

    def reload(self):  # 填弹
        # 填弹后，剩余子弹数等于弹夹容量
        self.bullet_left = self.max_bullets

    def fire(self):
        if self.bullet_left <= 0:
            print("请填弹")
            return
        # 计算剩余子弹
        self.bullet_left -= 1  # 打出1发子弹
        # 计算杀伤力
        damage = int(self.destructRatio * 100)
        # 播放声音
        self.fire_sound.play()
        print("杀伤力%d, 剩余子弹%d" %
              (damage, self.bullet_left))
