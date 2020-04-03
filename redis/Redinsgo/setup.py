import redis

user = "user:"
score = "score:"
cartela = "cartela:"

redis_con = redis.Redis(host='nosql_redis', port=6380, db=0, password="Jasinski")
redis_con.flushall()
redis_con.sadd("stones", *range(1, 100))

#setup
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

#game start
print("Iniciando Bingo!")
turn = 0
while stone := redis_con.spop("stones", 1):

    turn = turn + 1
    bingo = False;
    intStone = int(stone[0])
    print("turno: " + str(turn) + ", pedra tirada: " + str(intStone))

    for i in range(50):
        if redis_con.sismember(cartela + str(i), intStone):
            pipe.incr(score + str(i))
    pipe.execute()

    for i in range(50):
        if int(redis_con.get(score + str(i))) == 15:
            print("Bingo! Vencedor: " + user + str(i))
            bingo = True

    if bingo:
        break;

if not bingo:
    "Acabaram as pedras!"

pipe.close()
