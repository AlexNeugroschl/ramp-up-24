import redis

# Connect to the Redis server
redis_client = redis.Redis(host='localhost', port=6379, db=0)

# Create a pubsub object
pubsub = redis_client.pubsub()

# Subscribe to the channel
pubsub.subscribe('my_channel')

print("Subscribed to the 'my_channel' channel...")

# Listen for messages
for message in pubsub.listen():
    if message['type'] == 'message':
        print(f"Received message: {message['data'].decode('utf-8')}")
