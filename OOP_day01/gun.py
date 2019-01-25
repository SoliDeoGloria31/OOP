# gun.py
# 枪械类


class Gun:
    def __init__(self,
                 name, max_bullets, bullets_left,
                 dest_ratio, firing_bullets):
        self.name = name                        # 名称
        self.max_bullets = max_bullets          # 弹夹容量
        self.bullets_left = bullets_left
        self.dest_ratio = dest_ratio            # 杀伤系数
        self.firing_bullets = firing_bullets    # 每次开火击发子弹数量

    def reload(self):
        self.bullets_left = self.max_bullets
        print('填弹完成,剩余子弹%2d发' % self.bullets_left)

    def fire(self):
        if self.bullets_left <= 0:
            print('请按回车键填弹! ')
            return
        elif self.bullets_left > self.firing_bullets:
            self.bullets_left -= self.firing_bullets
        else:
            self.bullets_left = 0

        damage = int(self.dest_ratio * 100)
        print('%s开火,杀伤力%d,剩余子弹%d' % (self.name, damage, self.bullets_left))
