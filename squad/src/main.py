from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.controller import SquadController

load_dotenv(override=True)

app = FastAPI(
    title='Squads Service',
    version='0.0.1',
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get('/')
def rootPath():
    return {'message': 'Welcome to Bici Red API v1.0 - ready'}

# Routes
app.include_router(SquadController.router())
