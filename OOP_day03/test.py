# -*- coding: utf-8 -*-


class Student:
    def __init__(self, name, age, score):
        self.name, self.age, self.score = name, age, score

    def __repr__(self):
        return 'hello word'

    def infos(self):
        m = 'Hello China'
        # print(m)
        return m

    def __str__(self):
        return self.infos()


s1 = Student('Bob', 30, 88)
print(s1)
