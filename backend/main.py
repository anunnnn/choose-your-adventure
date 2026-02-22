from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from core.config import settings
 
# from routers import router

app = FastAPI(
    title="Chose Your Own Adeventure Game API",
    description="API for a Chose Your Own Adeventure Game",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
    