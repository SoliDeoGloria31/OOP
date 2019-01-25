# test.py
# 测试程序

import ak47
import awp
import time
# name, max_bullets, bullets_left,dest_ratio, firing_bullets

ak = ak47.AK47('AK47', 30, 0, 0.4, 3)   # 实例化AK47对象
ak.reload()        # 填弹
for i in range(40):
    if ak.bullets_left > 0:
        ak.fire()          # 开火
        time.sleep(0.3)
    else:
        _ = input('请按回车键填弹!')
        ak.reload()
        print()

print('\n---------------------------\n')

_ = input('\n请按回车键切换到AWP!\n')

awp = awp.AWP('AWP', 10, 0, 1, 1)    # 实例化AWP对象
awp.openTelescope()
awp.reload()       # 填弹
for i in range(15):
    if awp.bullets_left > 0:
        awp.fire()         # 开火
        time.sleep(0.3)
    else:
        _ = input('请按回车键填弹!')
        awp.reload()
        print()
awp.closeTelescope()

print('\n---------------------------\n')

ak2 = ak47.AK47('AK47', 20, 0, 0.4, 3)   # 实例化AK47对象
