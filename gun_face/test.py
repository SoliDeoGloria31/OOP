
import pygame  # 导入动态模块(.dll .pyd .so) 不需要在包名后边跟模块名
from pygame.locals import *
import sys
import time
import awp

WINDOW_HEIGHT = 908
WINDOW_WIDTH = 1792


def main():
    """主函数  一般将程序的入口"""
    pygame.init()
    # 创建窗口  set_mode((窗口尺寸))
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    # 将图片加载到内存中  load(图片资源路径)
    bg_img = pygame.image.load("1.jpg")
    awp1 = awp.AWP("awp.png", 100, 100, window)

    while True:
        # 贴图 把图片贴到窗口中  blit(图片对象, 相对原点的坐标)
        window.blit(bg_img, (0, 0))
        # 贴枪图
        awp1.display()
        # 刷新界面  不刷新不会更新显示的内容
        pygame.display.update()
        # 获取事件，比如按键等  先显示界面,再根据获取的事件,修改界面效果
        for event in pygame.event.get():
            # 判断是否是点击了退出按钮
            if event.type == QUIT:
                sys.exit()  # 让程序终止
                pygame.quit()
            # 监测鼠标事件
            # 按下事件
            # 按下的区域判断
            g = pygame.mouse.get_pressed()
            (x, y) = pygame.mouse.get_pos()
            if g ==(1,0,0) and awp1.x <= x <= awp1.x + 510 and awp1.y <= y <= awp1.y + 113:
                awp1.fire()
                print("1")
            elif g ==(0,0,1) and awp1.x <= x <= awp1.x + 510 and awp1.y <= y <= awp1.y + 113:
                awp1.reload()
                print("2")

        time.sleep(0.1)


if __name__ == '__main__':  # 判断是否主动执行该文件
    main()
