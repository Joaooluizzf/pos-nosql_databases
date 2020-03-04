import redis

r = redis.Redis(host='localhost', port=6379, db=0, password="Jasinski")
r.flushall()

#r.set('foo', 'bar')
#r.get('foo')
#r.incr('incr')