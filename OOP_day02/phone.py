# -*- coding: utf-8 -*-
import time


class Phone:
    def __init__(self, name, price, cpu, screen_size):
        self.name = name
        self.price = price
        self.cpu = cpu
        self.screen_size = screen_size

    def startup(self):
        time.sleep(2)
        print('%s已开机！~' % self.name)

    def shutdown(self):
        time.sleep(3)
        print('%s已关机！~' % self.name)

    def call(self, num):
        time.sleep(2)
        print('%s正在拨号！~ 号码为：%d' % (self.name, num))
        time.sleep(2)
        print('%s正在通话！~' % self.name)
        time.sleep(5)
        print('%s通话结束！' % self.name)

    def send_msg(self):
        time.sleep(1)
        print('%s正在编辑短信！~' % self.name)
        time.sleep(3)
        print('%s给您发来一条节日问候!~' % self.name)

    def info(self):
        print('\n名为：%s\n价格：%dRMB\nCPU: %s\n屏幕尺寸：%.1f寸' %
              (self.name, self.price, self.cpu, self.screen_size))

    def __del__(self):   # 析构方法
        print('__del__方法被调用')


if __name__ == '__main__':
    ph = Phone('华为手机', 4500, '麒麟', 5.4)
    # ph.startup()
    # ph.send_msg()
    # ph.call(13917163546)
    # ph.shutdown()
    ph.info()
    # del ph  # 会执行对象的析构函
    # ph.info()
    print('\n程序退出！')
