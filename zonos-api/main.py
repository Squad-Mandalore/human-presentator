from fastapi import FastAPI

from src.controller import zonos_controller

app = FastAPI()

app.include_router(zonos_controller.router)

