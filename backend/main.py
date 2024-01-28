from fastapi import FastAPI
from router.router import user, cliente_router, estado_router, criterios_aceptabilidad_router, documento_router, inspeccion_router, recepcion_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.include_router(user)
app.include_router(cliente_router)
app.include_router(estado_router)
app.include_router(criterios_aceptabilidad_router)
app.include_router(documento_router)
app.include_router(inspeccion_router)
app.include_router(recepcion_router)


# Configuración de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],
    allow_methods=["*"],
    allow_headers=["*"],
)