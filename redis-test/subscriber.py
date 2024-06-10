# import redis

# redis_client = redis.Redis(host='redis', port=6379, db=0)

# pubsub = redis_client.pubsub()
# pubsub.subscribe('my_channel')

# print("Subscribed to the 'my_channel' channel...")

# for message in pubsub.listen():
#     if message['type'] == 'message':
#         # No need to decode if decode_responses=True is set
#         print(f"Received message: {message['data']}")
#     else:
#         print(f"Received non-message data: {message}")
import os
import redis

redis_host = os.getenv('REDIS_HOST', 'redis')
redis_port = int(os.getenv('REDIS_PORT', 6379))

redis_client = redis.Redis(host=redis_host, port=redis_port, db=0)

pubsub = redis_client.pubsub()
pubsub.subscribe('my_channel')

print("Subscribed to the 'my_channel' channel...")

for message in pubsub.listen():
    if message['type'] == 'message':
        # Decode the byte string to a regular string
        print(f"Received message: {message['data'].decode('utf-8')}")
    else:
        print(f"Received non-message data: {message}")
