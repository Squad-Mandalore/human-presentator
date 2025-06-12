from fastapi import FastAPI

from src.controller import memo_controller

app = FastAPI()

app.include_router(memo_controller.router)
