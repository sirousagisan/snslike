import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# from starlette_csrf import CSRFMiddleware

from routers import user as user_router
from routers import post as post_router 

app = FastAPI()
app.include_router(user_router.router)
app.include_router(post_router.router)

# app.add_middleware(
#     CSRFMiddleware,
#     cookie_samesite="lax",
#     cookie_secure=True,
#     secret='8b9762f039adbe311f198e868277b8c95646ca34f2dac48e2145186d020a365d',
    
# )

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5175", "http://127.0.0.1:8080"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)





@app.get("/")
def hello():
    return {"msg" : "Hello"}

if __name__ == '__main__':
    uvicorn.run("main:app", reload=True, port=8080)