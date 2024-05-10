from fastapi import FastAPI
from routers import profile,profile_db,pictures_db
from settings import Settings

#from pydantic_settings import BaseSettings,SettingsConfigDict

#class Settings(BaseSettings):
#    disable_db:bool=False
#
#    model_config = SettingsConfigDict(env_file=".env")	
#	
settings=Settings()	

summary="Microservicio que se encarga de todo lo relativo a datos adicionales del usuario (como por ejemplo descripciones e imágenes)"

app=FastAPI(title="perfil",version="0.0.2",summary=summary)

# Para iniciar el server hacer: uvicorn main:app --reload

# Url local: http://127.0.0.1:8000
# Documentación con swagger: http://127.0.0.1:8000/docs 
# Documentación con Redocly: http://127.0.0.1:8000/redoc 
# Url: http://127.0.0.1:8000/user/{id}/profile 

# Routers (subconjuntos dentro de la API principal)
if settings.disable_db==True:
   print("no usa bd")
   app.include_router(profile.router)
else:
   print("usa bd")
   app.include_router(profile_db.router)
   app.include_router(pictures_db.router)

# HTTP response
# 100 información
# 200 las cosas han ido bien
# 201 se ha creado algo
# 204 no hay contenido
# 300 hay una redireccion
# 304 no hay modificaciones 
# 400 error
# 404 no encontrado
# 500 error interno

