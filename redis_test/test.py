# -*- coding:utf-8 -*-
import redis

def run():
    t = redis
    r =t.Redis(host='localhost', port=6379)
    print(r.set('bing', 'baz'))
    print(r.sadd('b2ing', 'baz'))
    r.rpush('rlist',1,2,3)
    print(r.lrange('rlist', 0, -1) )
    print(r.get('bing'))
    r.sadd('set-key', 'a', 'b', 'c')

    print(r.smembers('set-key'))

    a=r.hmset('user:013', {
        'title': 'title',
        'link': 'link',
        'poster': 'user',
        'time': 'now',
        'votes': 1,
    })
    dic=r.hgetall('user:013')
    for (k,v) in dic.items():
        print(k,v)

    print (r.hgetall('user:012'))
    # print(r.get('rlis22t'))




if __name__ == "__main__":
    run()