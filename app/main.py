from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.v1.router import api_router
from app.core.config import settings
from app.core.database import engine, Base


@asynccontextmanager
async def lifespan(app: FastAPI):
    print(f"\n🔌 [DB Conexión]: {settings.DATABASE_URL}\n")
    # En desarrollo local puedes crear las tablas automáticamente si no usas Alembic aún:
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    # Limpieza al apagar la app
    await engine.dispose()


app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    docs_url="/docs",
    redoc_url="/redoc",
    lifespan=lifespan,
)

# Configuración de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Ajustar a los dominios autorizados en producción
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Inclusión del Router API v1
app.include_router(api_router, prefix=settings.API_V1_STR)


@app.get("/health", tags=["Salud"])
async def health_check():
    """Endpoint para verificar el estado de la API."""
    return {"status": "ok", "project": settings.PROJECT_NAME}


@app.get("/", tags=["Inicio"])
async def root():
    return {
        "message": f"Bienvenido a {settings.PROJECT_NAME}",
        "documentation": "/docs",
        "health": "/health",
    }

