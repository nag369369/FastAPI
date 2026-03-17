from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import app
from app.exceptions.user_exceptions import UserNotFoundError, InvalidTokenError


@app.exception_handler(UserNotFoundError)
async def user_not_found_handler(request: Request, exc: UserNotFoundError):
    return JSONResponse(
        status_code=404,
        content={"error": exc.message}
    )

@app.exception_handler(InvalidTokenError)
async def invalid_token_handler(request: Request, exc: InvalidTokenError):
    return JSONResponse(
        status_code=401,
        content={"error": exc.message}
    )