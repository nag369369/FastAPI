from fastapi import APIRouter, FastAPI, Depends, HTTPException, Security
from fastapi.security import HTTPBearer
from jose import jwt
import requests

router = APIRouter(prefix="/auth2", tags=["Authentication2"])

security = HTTPBearer()

AUTH0_DOMAIN = "dev-d3rkt7vg3hq0lgzm.us.auth0.com"
API_AUDIENCE = "https://dev-d3rkt7vg3hq0lgzm.us.auth0.com/api/v2/"
ALGORITHMS = ["RS256"]



def verify_token(credentials=Depends(security)):
    token = credentials.credentials

    jwks = requests.get(
        f"https://{AUTH0_DOMAIN}/.well-known/jwks.json"
    ).json()

    unverified_header = jwt.get_unverified_header(token)

    rsa_key = {}

    for key in jwks["keys"]:
        if key["kid"] == unverified_header["kid"]:
            rsa_key = {
                "kty": key["kty"],
                "kid": key["kid"],
                "use": key["use"],
                "n": key["n"],
                "e": key["e"]
            }

    if rsa_key:
        try:
            payload = jwt.decode(
                token,
                rsa_key,
                algorithms=ALGORITHMS,
                audience=API_AUDIENCE,
                issuer=f"https://{AUTH0_DOMAIN}/"
            )
            return payload

        except Exception:
            raise HTTPException(status_code=401, detail="Invalid token")

    raise HTTPException(status_code=401, detail="Invalid token")


def get_token():
    AUTH0_DOMAIN = "dev-d3rkt7vg3hq0lgzm.us.auth0.com"
    CLIENT_ID = "Rk2zljNlPSVJdfGZQZUDm5pPB2GAMWI9"
    CLIENT_SECRET = "QXKNdQQZxonyqFcX9LY6LAMwFVx9JdTTs0UEZ1HOxoLRn7ROqvh0t2eGnnOky0sO"
    AUDIENCE = "https://dev-d3rkt7vg3hq0lgzm.us.auth0.com/api/v2/"

    url = f"https://{AUTH0_DOMAIN}/oauth/token"

    payload = {
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "audience": AUDIENCE,
        "grant_type": "client_credentials"
    }

    response = requests.post(url, json=payload)
    print(response.status_code)
    print(response.text)
    token = response.json()["access_token"]
    print(token)
    return token

@router.get("/token")
def get_token(token=Depends(get_token)):
    return {"message": token}


@router.get("/validatetoken")
def protected(user=Depends(verify_token)):
    return {
        "message": "Token valid",
        "user": user
    }