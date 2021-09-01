from fastapi import FastAPI
from routers import router
from utils import delete_config

app = FastAPI()
delete_config()

app.include_router(router)


@app.get('/')
def root():
    return {'message': 'This application can scrap full user information from Instagram'}
