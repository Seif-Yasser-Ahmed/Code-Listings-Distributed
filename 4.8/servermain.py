import redis
import rpc1
import json
from constRPC import *

def server(channelID, serverID):
    print("Server is running...")
    redis_client = redis.StrictRedis(host='192.168.100.78', port=6379, db=0)
    pubsub = redis_client.pubsub()
    pubsub.subscribe('append_channel')

    for message in pubsub.listen():
        if message['type'] == 'message':
            try:

                message_data = json.loads(message['data'].decode('utf-8')) 
                operation = message_data.get('operation')

                if operation == 'append':

                    db_list = rpc1.DBList(message_data['list'])
                    result = db_list.append(message_data['data'])
                    print(f"Server received append request. Updated list: {result.value}")
            except Exception as e:
                print(f"Error processing message: {e}")


channelID = 1
serverID = 10
server(channelID, serverID)
