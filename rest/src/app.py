from os.path import join, dirname
from dotenv import load_dotenv

load_dotenv(join(dirname(__file__), ".env"))

from fastapi import FastAPI, APIRouter
from .controllers.routers import routers

api_ver = "v1"
app = FastAPI()
for router in routers:
    app.include_router(router, prefix=f"/{api_ver}", tags=router.tags if router.tags else [])


@app.get("/")
async def root():
    return {"message": "Hello World"}
