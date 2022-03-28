import threading


class MyThread(threading.Thread):
    def __init__(self, thread_name, begin_num, nums):
        threading.Thread.__init__(self)
        self.thread_name = thread_name
        self.begin_num = begin_num
        self.nums = nums

    def run(self):
        print("开启线程： " + self.thread_name)
        for i in range(self.begin_num, self.begin_num + 1000):
            # 获取锁，用于线程同步
            threadLock.acquire()
            self.squ(i)
            # 释放锁，开启下一个线程
            threadLock.release()

    def squ(self, x):
        print(f'{self.thread_name}正在处理{x}...')
        self.nums[x] = x ** 2


if __name__ == '__main__':
    threadLock = threading.Lock()
    threads = []
    nums = list(range(10000))
    print(nums)

    # 创建10个线程
    for i in range(10):
        threads.append(MyThread(f'Thread-{i}', i * 1000, nums))

    # 启动所有线程
    for thread in threads:
        thread.start()

    # 等待所有线程完成
    for thread in threads:
        thread.join()

    print(nums)
    print("退出主线程")
