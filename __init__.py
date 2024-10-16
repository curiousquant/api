from fastapi import FastAPI
import uvicorn
from routes import routes
from config import Settings
from contextlib import asynccontextmanager
from config import settings
from db import init_db




# lifespan code

@asynccontextmanager
async def lifespan(app:FastAPI):
    await init_db()
    yield

def create_app():
    app = FastAPI(
        description="This is a simple REST API for a news",
        title="News",
        version=settings.VERSION,
        lifespan=lifespan
    )
    app.include_router(routes)
    return app


app = create_app()

if __name__=='__main__':
    uvicorn.run("__init__:app", reload=True)