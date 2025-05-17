from fastapi import FastAPI
from zonos.utils import DEFAULT_DEVICE as device

from src.controller import zonos_controller

app = FastAPI()

app.include_router(zonos_controller.router)

