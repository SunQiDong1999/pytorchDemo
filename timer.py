import time


# 装饰器函数timer,其中function为你想要装饰的函数
def timer(function):
    def wrapper():
        time_start = time.time()
        function()
        time_end = time.time()
        cost_time = time_end - time_start
        print("花费时间：{}秒".format(cost_time))

    return wrapper


# 对Time函数进行装饰器的添加，@timer引用timer装饰器函数
@timer
def Time():
    time.sleep(1)


if __name__ == '__main__':
    Time()
