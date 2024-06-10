# from fastapi import FastAPI, Request
# import redis

# app = FastAPI()

# redis_client = redis.Redis(host='redis', port=6379, db=0)

# @app.post("/publish{message}")
# async def publish_message(request:Request, message:str):
#     redis_client.publish("my_channel", message)
#     return {"message":"Message published successfully", "message":message}

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run("publisher:app", host="0.0.0.0", port=8000, reload=True)
import os
import redis
from fastapi import FastAPI
import uvicorn

app = FastAPI()

redis_host = os.getenv('REDIS_HOST', 'redis')
redis_port = int(os.getenv('REDIS_PORT', 6379))

try:
    redis_client = redis.Redis(host=redis_host, port=redis_port, db=0)
    redis_client.ping()
    print("Connected to Redis successfully!")
except redis.ConnectionError:
    print("Failed to connect to Redis.")

@app.post("/publishmessage")
def publish_message(message: str):
    try:
        redis_client.publish("my_channel", message)
        return {"status": "Message published"}
    except Exception as e:
        return {"status": "Failed to publish message", "error": str(e)}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
