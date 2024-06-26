import logging
from settings import settings
logging.basicConfig(filename=settings.log_filename, level=settings.logging_level, format='%(asctime)s - %(levelname)s - %(message)s')

from fastapi import FastAPI
from routers import profile,profile_db,pictures_db
from data.apikey import enableApiKey
from middlewares.ingoingSecurityCheck import IngoingSecurityCheck
from middlewares.outgoingSecurityCheck import OutgoingSecurityCheck
import asyncio

summary="Microservicio que se encarga de todo lo relativo a datos adicionales del usuario (como por ejemplo descripciones e imágenes)"

app=FastAPI(
    title="perfil",
    version="0.0.7",
    summary=summary,
    docs_url='/api-docs'
)

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

if settings.isRunningTests == False:
   asyncio.create_task(enableApiKey())
