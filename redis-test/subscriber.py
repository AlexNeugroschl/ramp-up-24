import redis

redis_client = redis.Redis(host='localhost', port=6379, db=0)

pubsub = redis_client.pubsub()
pubsub.subscribe('my_channel')

print("Subscribed to the 'my_channel' channel...")

for message in pubsub.listen():
    if message['type'] == 'message':
        # Decode the byte string to a regular string
        print(f"Received message: {message['data'].decode('utf-8')}")
    else:
        print(f"Received non-message data: {message}")