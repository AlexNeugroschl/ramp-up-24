import redis
import logging

# Configure logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
logger = logging.getLogger()

r = redis.Redis(host='redis', port=6379, decode_responses=True)


pubsub = r.pubsub()
pubsub.subscribe('my_channel')

logger.info("Subscriber is running and waiting for messages...")

# Listen for messages
for message in pubsub.listen():

    logger.info("Received message: " + str(message["data"]))
