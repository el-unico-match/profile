from fastapi import FastAPI
from routers import profile

app=FastAPI()

# Para iniciar el server hacer: uvicorn main:app --reload

# Url local: http://127.0.0.1:8000
# Documentación con swagger: http://127.0.0.1:8000/docs 
# Documentación con Redocly: http://127.0.0.1:8000/redoc 
# Url: http://127.0.0.1:8000/user/{id}/profile 

# Routers (subconjuntos dentro de la API principal)
app.include_router(profile.router)

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

