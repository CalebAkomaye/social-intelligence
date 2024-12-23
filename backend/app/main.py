from fastapi import FastAPI
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware
from config.config import HOST, PORT
from api.routers import auth
import uvicorn
import os

load_dotenv()

app = FastAPI(debug=True)

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(auth.router)


if __name__ == "__main__":
    uvicorn.run(app, host=HOST, port=PORT)
