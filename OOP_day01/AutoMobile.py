# s2 = ['HelloTarena',' haha','xixi']
# f = open('tarena.txt','r+')
# f.writelines(s2)
# print(f.tell())
# print(f.seek(0, 0))
# print(f.read(10))
# print(f.tell())
# f.close()

#####


# class Ellipse:
#     def __init__(self, a, b):
#         self.a = a  # 属性:短半径
#         self.b = b  # 属性:长半径
#
#     def calc_len(self):  # 计算周长
#         return 2 * 3.14 * self.a + 4 * (self.b - self.a)
#
#     def calc_area(self):  # 计算面积
#         return 3.14 * self.a * self.b
#
# print(Ellipse(3,5))
# print(Ellipse(3,5).calc_len(),Ellipse(3,5).calc_area())

#####

import random  # import 要在class外部或者def 下面
n = int(input('请输入百公里油耗(L): '))  # 外部输入百公里油耗; 外部可以传参,但不可以调用私有属性


class AutoMobile:

    # a = 'a'
    # global b
    # b = 'b'
    def __init__(self, name, color, output_volumn):
        self.name = name
        self.color = color
        self.output_volumn = output_volumn
        self.__distance = 0.00  # 行驶里程
        self.__bglyh = n     # 没百公理油耗

    def __calc__distance(self):  # 计算行驶里程
        # import random
        self.__distance += random.randint(1, 400)  # 改变行驶里程,[1,400]随机

    def get_distance(self):   # 在类的外部调用,显示私有的里程属性
        return self.__distance   # 返回里程数据

    def get_yh(self):
        return self.__distance * self.__bglyh

    def startup(self):
        print('汽车启动!')

    def run(self):
        self.__calc__distance()  # 调用行驶里程计算方法
        print('汽车行驶!')

    def stop(self):
        print('汽车停止!')

    def info(self):
        print('\n名称:%s\n颜色:%s\n排量:%.1fL' %
              (self.name, self.color, self.output_volumn))


if __name__ == '__main__':
    auto_mobile = AutoMobile('家用轿车', '红色', 2)

    auto_mobile.startup()
    auto_mobile.run()
    auto_mobile.stop()
    auto_mobile.info()
    # print('行驶了%.1d'% auto_mobile.distance)
    # print('行驶了%.1d'% auto_mobile.__distance)
    # print(a)
    # print(b)
    print('共行驶了 %.1f公里' % auto_mobile.get_distance())
    print('共耗油 %.1fL' % auto_mobile.get_yh())
