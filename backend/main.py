import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello():
    return {"msg" : "Hello"}

if __name__ == '__main__':
    uvicorn.run("main:app", reload=True, port=8080)