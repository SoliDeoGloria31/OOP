import eagle
import ostrich
# import bird

ea = eagle.Eagle('大鹰', '公', 50.0, 5)
os = ostrich.Ostrich('鸵鸟', '母', 0.0, 3, 50.5)


if __name__ == '__main__':
    ea.eat_()
    ea.fly_()
    ea.reproduction_()

    print('\n-------------------\n')

    os.eat_()
    os.fly_()
    os.run_()
    os.reproduction_()
