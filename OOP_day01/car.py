# car.py
# 家用小汽车类,继承示例


from AutoMobile import *


class Car(AutoMobile):
    pass


if __name__=="__main__":
    mycar = Car('小汽车','蓝色',1.40)
    mycar.startup()  # 启动
    mycar.run()
    mycar.stop()
    mycar.info()