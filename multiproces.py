# coding: utf-8
import multiprocessing
import os, time, random
import 

def Lee(txt):
    print("\nRun task Lee-%s" % (os.getpid()))  # os.getpid()获取当前的进程的ID
    start = time.time()
    time.sleep(2)  # random.random()随机生成0-1之间的小数
    end = time.time()
    print('Task Lee, runs %0.2f seconds.%s' % (end - start,txt))
    return 2


def Lee2(txt):
    print("\nRun task Lee-%s" % (os.getpid()))  # os.getpid()获取当前的进程的ID
    start = time.time()
    time.sleep(4)  # random.random()随机生成0-1之间的小数
    end = time.time()

    print('Task fffff, runs %0.2f seconds.%s' % (end - start,txt))
    return 4


if __name__ == '__main__':
    t1=time.time()
    # msg = 'str'
    # a=Lee(msg)
    # b=Lee2(msg)
    # c=a+b
    t2=time.time()
    function_list = [Lee, Lee2]
    print ("parent process %s" % (os.getpid()))

    pool = multiprocessing.Pool(4)
    result=[]
    for i,func in enumerate(function_list,0):
        msg='str'+str(i)
        result.append(pool.apply_async(func, (msg, )))  # Pool执行函数，apply执行函数,当有一个进程执行完毕后，会添加一个新的进程到pool中

    print('Waiting for all subprocesses done...')
    pool.close()
    pool.join()
    t3 = time.time()
    # 调用join之前，一定要先调用close() 函数，否则会出错, close()执行后不会有新的进程加入到pool,join函数等待素有子进程结束
    for res in result:
        print( ":::", res.get())
    print('All subprocesses done.{},{}'.format(t2-t1,t3-t2))