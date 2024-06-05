from fastapi import FastAPI

app = FastAPI() 

@app.get('/{name}') 
async def say_hi(name:str):
    return {'message' : f"hi, {name}"}