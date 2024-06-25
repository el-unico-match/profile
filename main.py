from fastapi import FastAPI
from routers import profile,profile_db,pictures_db
from settings import settings
from data.apikey import enableApiKey
from middlewares.ingoingSecurityCheck import IngoingSecurityCheck
from middlewares.outgoingSecurityCheck import OutgoingSecurityCheck

summary="Microservicio que se encarga de todo lo relativo a datos adicionales del usuario (como por ejemplo descripciones e imágenes)"

app=FastAPI(
    title="perfil",
    version="0.0.7",
    summary=summary,
    docs_url='/api-docs'
)

enableApiKey()

app.add_middleware(IngoingSecurityCheck)
app.add_middleware(OutgoingSecurityCheck)

# Routers (subconjuntos dentro de la API principal)
if settings.disable_db==True:
   print("no usa bd")
   app.include_router(profile.router)

else:
   print("usa bd")
   app.include_router(profile_db.router)
   app.include_router(pictures_db.router)

