# -*- coding: utf-8 -*-

# mylist.py
# 自定义列表


class MyList:
    def __init__(self, iterable=[]):
        self.data = [x for x in iterable]

    # 重写__abs__()函数
    def __abs__(self):
        # 将每个元素求绝对值，用产生的结果实例化一个MyList对象
        return MyList(abs(x) for x in self.data)

    def __len__(self):
        n = 0
        for x in self.data:
            n += 1
        return n

    def __round__(self):
        return MyList(round(x, 2) for x in self.data)

    # def __round__(self):   # 四舍五入
    #     def siwu(x):
    #         if x == 0:
    #             return 0
    #         elif x % 1 >= 0.5:
    #             return x // 1 + 1
    #         elif x % 1 < 0.5:
    #             return x // 1
    #     return MyList(siwu(x) for x in self.data)

    def __reversed__(self):
        # 重写__reversed__()函数
        L = []
        for x in self.data:
            L.insert(0, x)
        # x = len(self.data) -1
        # while x >=0:
        #     L.append(self.data[x])
        #     x -=1
        return MyList(L)

    def __add__(self, obj):
        if isinstance(obj.data, list):
            return MyList(self.data + obj.data)
        else:
            raise ValueError

    def __mul__(self, value):
        if isinstance(value, int):
            return MyList(self.data * value)
        else:
            raise ValueError

    def __str__(self):
        # 将对象转换为字符串
        ret = ""
        for x in self.data:
            ret += str(x)  # 将元素由数字转换成字符串
            ret += ' '
        return ret


if __name__ == '__main__':
    L1 = MyList([1, 2, 3])
    L2 = MyList([4, 5, 6])
    print(L1+L2)
    print(L1*2)

    print((L1 + L2) is MyList([1, 2, 3, 4, 5, 6]))  # 不可用此，判断id
    print((L1 * 2) is MyList([1, 2, 3, 1, 2, 3]))   # 不可用此，判断id

    # L = MyList([-1, 2, -3, 5.6789])
    # L2 = abs(L)      # 重写了__abs__()函数，支持abs表达式
    # print(L2)        # 重写了__str__()函数，所以支持print()
    # L3 = len(L)      # 重写了__len__()函数
    # print(L3)
    # L4 = round(L)    # 重写了__round__()函数
    # print(L4)
    # L5 = reversed(L)
    # print(L5)

    # 打印自定义列表中所有元素的绝对值
    # for x in L.data:
    #     print(abs(x))
    # # 取所有元素近似值打印
    # print()
    # for x in L.data:
    #     print(round(x, 2))
