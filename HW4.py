import math
import time
import random
from functools import wraps


class Cylinder:
    def __init__(self, id, r, h):
        self.id = id
        self.r = r
        self.h = h

    def PrintInfo(self):
        print(f'第{self.id}个圆柱半径为{self.r}，高为{self.h}')

    def GetVolume(self):
        return self.h * self.r ** 2 * math.pi


def timer(function):
    @wraps(function)
    def function_timer(*args, **kwargs):
        t0 = time.time()
        result = function(*args, **kwargs)
        t1 = time.time()
        print(f'[finished {function.__name__} in {t1 - t0:.2f}s]')
        return result

    return function_timer


@timer
def random_delete(ob_list):
    time.sleep(1)
    while len(ob_list) != 0:
        next_del = random.randint(0, 9)
        if 0 <= next_del < len(ob_list):
            del ob_list[next_del]


if __name__ == '__main__':
    ob_list = []
    for i in range(10):
        ob_list.append(Cylinder(i, i, i))
    for cylinder in ob_list:
        cylinder.PrintInfo()

    print('开始删除对象......')
    random_delete(ob_list)
