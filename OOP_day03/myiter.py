# -*- coding: utf-8 -*-

# myiter.py
# 通过函数重写，实现自定义迭代器


class MyIter:
    def __init__(self, lst):
        self.data = lst       # lst是列表
        self.cur_index = 0    # 计数器

    def __iter__(self):       # 返回可迭代对象
        return MyIter(self.data)

    def __next__(self):
        if self.cur_index >= len(self.data):
            raise StopIteration   # 抛出异常
        else:
            i = self.cur_index    # 记录计数器
            self.cur_index +=1
            return self.data[i]


if __name__ == '__mian__':
    myiter = iter(MyIter(range(1, 10)))
    for x in myiter:
        print(x, end=' ')
    print()
