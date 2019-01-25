from bird import *


class Eagle(Bird):
    def eat_(self):
        print('我是%s，我喜欢吃肉！~' % self.name)

    def fly_(self):
        print('我是%s,我飞的又高又快！~' % self.name)
