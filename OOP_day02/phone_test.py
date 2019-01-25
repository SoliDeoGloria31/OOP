# -*- coding: utf-8 -*-

import phone

def fun():
    print('fun()函数被调用！')
    ph1 = phone.Phone('华为手机', 4500, '麒麟', 5.4)


if __name__ == '__main__':
    ph = phone.Phone('华为手机', 4500, '麒麟', 5.4)
    ph.startup()
    ph.send_msg()
    ph.call(13917163546)
    ph.shutdown()
    ph.info()
    # del ph # 会执行对象的析构函数
    fun()
    print('\n程序退出！')

print