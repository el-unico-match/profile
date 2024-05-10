# profile

> versión actual 0.0.2

# Esquema de los datos de perfil

| Campo       | Tipo    |
|-------------|---------|
| userid      | string  |
| username    | string  | 
| email       | string  |
| description | string  |
| gender      | string  |
| looking_for | string  |
| age         | integer | 
| education   | string  |
| ethnicity   | string  |  

# Ejemplo de un archivo json con datos del perfil de un usuario
```
{ "userid" : "66304a6b2891cdcfebdbdc6f",
   "username" : "Luis Huergo",
   "email" : "lhuergo@fi.uba.ar",
   "description" : "Estudié en la UBA",
   "gender" : "Hombre",
   "looking_for" : "Mujer",
   "age" : "33",
   "education" : "Ingeniero civil",
   "ethnicity" : ""
}
```
# Seteo de variables de entorno para usar en local:

DISABLE_DB=False

#logger
LOG_FILENAME='profile.log'
NOTSET=0
DEBUG=10
INFO=20
WARNING=30
ERROR=40
CRITICAL=50
LOGGING_LEVEL=${DEBUG}

#base de datos
DOCKER_DOMAIN='profile_mongo'
LOCAL_DOMAIN='localhost'
**DB_DOMAIN =${LOCAL_DOMAIN}**
DB_PORT = 27017

# Seteo de variables de entorno para usar en docker:

DISABLE_DB=False

#logger
LOG_FILENAME='profile.log'
NOTSET=0
DEBUG=10
INFO=20
WARNING=30
ERROR=40
CRITICAL=50
LOGGING_LEVEL=${DEBUG}

#base de datos
DOCKER_DOMAIN='profile_mongo'
LOCAL_DOMAIN='localhost'
**DB_DOMAIN =${DOCKER_DOMAIN}**
DB_PORT = 27017

# Instrucciones

# Para iniciar el server: 
  1) Abrir la consola de comandos
  2) Navegar hasta la ubicación donde se encuentra el proyecto
  3) Escribir el siguiente comando: uvicorn main:app --reload <br />
     (main hace referencia al archivo main.py, app hace referencia a la variable app definida en main.py)
	 
# Para acceder a la documentación con swagger: 
  1) Abrir el navegador
  2) Escribir en la barra de direcciones: http://127.0.0.1:8000/docs 
  
# Para acceder a la documentación con Redocly: 
  1) Abrir el navegador
  2) Escribir en la barra de direcciones: http://127.0.0.1:8000/redoc 
  
