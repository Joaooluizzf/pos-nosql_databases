import redis

user = "user:"
score = "score:"
cartela = "cartela:"

redis_con = redis.Redis(host='localhost', port=6380, db=0, password="Jasinski")
redis_con.flushall()
redis_con.sadd("stones", *range(1, 100))

pipe = redis_con.pipeline()
for i in range(50):
    useri = user+str(i)
    cartelai = cartela + str(i)
    scorei = score + str(i)
    pipe.hset(useri, "name", useri)
    pipe.hset(useri, "bcartela", cartelai)
    pipe.hset(useri, "bscore", scorei)
    pipe.sadd(cartelai, *redis_con.srandmember("stones", 15))
    pipe.set(scorei, 0)
pipe.execute()



#client.sadd(user.cartelaKey, user.cartela);
#client.set(user.scoreKey, 0);

