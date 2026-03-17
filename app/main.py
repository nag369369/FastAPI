from fastapi import FastAPI
from app.routers import auth2_router, order_router

app = FastAPI(title="Order API", description="API to submit and view orders", version="1.0")

#app = FastAPI()

app.include_router(auth2_router.router)
#app.include_router(auth_router.router)
app.include_router(order_router.router)

# @app.get("/ping")
# def ping():
#     return {"message": "pong"}

