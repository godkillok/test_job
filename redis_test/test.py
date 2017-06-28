# -*- coding:utf-8 -*-
import redis

def run():
    t = redis
    r =t.Redis(host='localhost', port=6379)
    r.set('bing', 'baz')
    r.rpush('rlist',1,2,3)
    print(r.get('bing'))
    print(r.get('rlist'))




if __name__ == "__main__":
    run()