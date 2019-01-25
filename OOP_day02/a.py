# -*- coding: utf-8 -*-


class A:
    def __init__(self, name):
        self.name = name
        # self.age = age

    def print(self):
        print('A类的print方法被调用！')

    # def __str__(self):
    #     return 'name=%s' % self.name


class B(A):
    def __init__(self, name, id):
        super().__init__(name)         # 调用父类构造方法
        self.id = id                   # id属性被创建

    def print(self):
        print('B类print方法别调用！')

    def __repr__(self):                # 重写__repr__方法
        # 返回例如“B('Jerry','0001')”
        return "B('%s','%s')" % (self.name, self.id)

    # def __str__(self):                 # 重写__str__方法
    #     return 'name=%s,id=%s' % (self.name, self.id)


b = B('Jerry', '0001')
print(b)
# str_obj = repr(b)
# print(str_obj)
# new_obj = eval(str_obj)
# print(new_obj)


# str_b = str(b)
# print(str_b)

# print(b.id)
# print(b.name)
# super(B, b).print()                # 根据对象b找到父类，并调用父类的print方法
# print(issubclass(B, A))            # True
# print(issubclass(B, (B,object)))   # True
# print(issubclass(A, B))            # False
# print(issubclass(A, object))       # True
# print(issubclass(B,B))             # True
