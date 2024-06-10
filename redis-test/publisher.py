from fastapi import FastAPI, Request
import redis

app = FastAPI()

redis_client = redis.Redis(host='localhost', port=6379, db=0)

@app.post("/publish")
async def publish_message(request: Request):
    data = await request.json()
    msg = data.get("msg")
    if not msg:
        return {"error": "Message text is required"}
    redis_client.publish("my_channel", msg)
    return {"message": "Message published successfully"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("publisher:app", host="0.0.0.0", port=8000, reload=True)
