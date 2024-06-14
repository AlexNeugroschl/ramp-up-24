from fastapi import FastAPI, Request
import redis

app = FastAPI()

redis_client = redis.Redis(host='redis', port=6379, db=0)

@app.post("/publish{message}")
async def publish_message(request:Request, message:str):
    redis_client.publish("my_channel", message)
    return {"message":"Message published successfully", "message":message}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("publisher:app", host="0.0.0.0", port=8000, reload=True)

