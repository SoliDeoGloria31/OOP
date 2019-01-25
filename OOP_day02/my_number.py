# -*- coding: utf-8 -*-

# my_number.py
# 自定义数字类型
# 数值转换函数重写示例


class MyNumber:
    def __init__(self, value):
        self.data = value        # 值，字符串

    def __int__(self):
        return int(float(self.data))  # 若要调用自己定义的float,则写成 MyNumber.__float__

    def __float__(self):
        #     return float(self.data)
        return 1

    def __complex__(self):
        return complex(self.data)


if __name__ == '__main__':
    num = MyNumber('123.45')
    # print(int(num))
    # print(float(num))
    # print(complex(num))
    print(getattr(num, 'data'))  # ‘123.45’
    print(num.data)              # '123.45'

    setattr(num, 'data', 456.78)
    print(getattr(num, 'data'))   # 456.78

    print(hasattr(num,'data'))    # True
    print(hasattr(num,'aaaa'))    # False

    delattr(num,'data')
    print(hasattr(num,'data'))    # False
