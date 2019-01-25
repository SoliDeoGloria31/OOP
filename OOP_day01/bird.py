class Bird:
    def __init__(self, name, sex, fly, reproduction):
        self.name = name
        self.sex = sex
        self.fly = fly
        self.reproduction = reproduction
        print('-------------------------')

    def eat_(self):
        print('一只%s的%s刚大饱餐一顿~ 哈哈' % (self.sex, self.name))

    def fly_(self):
        print('%s刚飞了%.1f里!' % (self.name, self.fly))

    def reproduction_(self):
        print('%s过去一年,生了%d个小宝宝^_^' % (self.name, self.reproduction))
