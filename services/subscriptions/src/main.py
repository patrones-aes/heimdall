import os
import sys

from threading import Thread
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

sys.path.append(os.path.join(os.getcwd(), './src'))
from controller import SubscriptionController
from event_handler import start_events_listening

load_dotenv(override=True)

app = FastAPI(
    title='Subscrptions Service',
    version='0.0.1',
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# Routes
app.include_router(SubscriptionController.router())

@app.on_event('startup')
async def listen_events() -> None:
    event_listener_thread = Thread(target=start_events_listening)
    event_listener_thread.daemon = True
    event_listener_thread.start()
