from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator
app = FastAPI()

Instrumentator().instrument(app).expose(app)

@app.get('/')
async def root() -> dict[str, str]:
    return {"message": "Hi, Shura"}