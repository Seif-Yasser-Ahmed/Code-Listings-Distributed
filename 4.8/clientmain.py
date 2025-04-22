import redis
import rpc1
from constRPC import *
import json

def client(channelID, clientID, serverID):
    redis_client = redis.StrictRedis(host='192.168.100.4', port=6379, db=0)
    s1 = rpc1.DBList([1, 2])
    message = {'operation': 'append', 'data': 'c', 'list': s1.value}


    redis_client.publish('append_channel', json.dumps(message))

    print("Value s1:", s1.value)


channelID = 1
clientID = 20
serverID = 10
client(channelID, clientID, serverID)
