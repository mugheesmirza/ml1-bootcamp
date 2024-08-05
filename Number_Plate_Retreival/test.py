from fastapi import FastAPI

app = FastAPI()

@app.post("/")
async def func():
    return {"message": "Hello World"}
