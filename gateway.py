from fastapi import FastAPI, Request, HTTPException

import requests

app = FastAPI()

SERVICE_URL = "http://localhost:9000"

# Basic authentication check
def validate_token(token: str):
    if token != "my-secret-token":
        raise HTTPException(status_code=401, detail="Unauthorized")

# Gateway route
@app.get("/gateway/users")
def get_users(request: Request):

    token = request.headers.get("Authorization")
    validate_token(token)

    response = requests.get(f"{SERVICE_URL}/users")

    return response.json()


@app.post("/gateway/orders")
def create_order(request: Request, body: dict):

    token = request.headers.get("Authorization")
    validate_token(token)

    response = requests.post(
        f"{SERVICE_URL}/orders",
        json=body
    )

    return response.json()