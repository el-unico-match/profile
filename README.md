# profile

> __versión actual:__\
> 0.0.5
> \
> __Funcionalidades actuales:__\
> \
> Creación de nuevo perfil\
> Actualización de perfil solicitado\
> Consulta de perfil solicitado\
> Consulta de todos los perfiles\
> Eliminación de perfil solicitado\
> Consulta del estado del servicio\
> Creación de imágenes de perfil\
> Actualización de imágenes de perfil solicitado\
> Consulta de imágenes de perfil solicitado

| Operación                                       | Retorna           | HTTP request                                                                             |
|-------------------------------------------------|-------------------|------------------------------------------------------------------------------------------|
| Retornar el estado del servicio                 | Estado            | GET https://profile-uniquegroup-match-fiuba.azurewebsites.net/status                     |
| Retornar una lista con todos los perfiles lista | Lista de perfiles | GET https://profile-uniquegroup-match-fiuba.azurewebsites.net/users/profiles             |
| Retornar el perfil solicitado                   | Perfil            | GET https://profile-uniquegroup-match-fiuba.azurewebsites.net/user/profile/{id}          |
| Actualizar el perfil solicitado                 | Nada              | PUT https://profile-uniquegroup-match-fiuba.azurewebsites.net/user/profile/{id}          |
| Eliminar el perfil solicitado                   | Nada              | DELETE https://profile-uniquegroup-match-fiuba.azurewebsites.net/user/profile/{id}       |
| Crear el perfil solicitado                      | Nada              | POST https://profile-uniquegroup-match-fiuba.azurewebsites.net/user/profile              |
|                                                 |                   |                                                                                          |
| Crear imágenes de perfil                        | Nada              | POST https://profile-uniquegroup-match-fiuba.azurewebsites.net/user/profile/pictures     |
| Retornar las imágenes del perfil solicitado     | Imágenes          | GET https://profile-uniquegroup-match-fiuba.azurewebsites.net/user/profile/pictures/{id} |
| Actualizar las imágenes del perfil solicitado   | Nada              | PUT https://profile-uniquegroup-match-fiuba.azurewebsites.net/user/profile/pictures/{id} |

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
   "age" : 33,
   "education" : "Ingeniero civil",
   "ethnicity" : ""
}
```
# Ejemplo de un archivo json con datos de imágenes de un usuario
```
{
  "userid": "1",
  "pictures": [
    {
      "name": "foto1.jpg",
      "url": "myurl/foto1.jpg",
      "order": 0
    }
  ]
}
```

# Seteo de variables de entorno para usar en local:

  DISABLE_DB=False

  LOG_FILENAME='profile.log'\
  NOTSET=0\
  DEBUG=10\
  INFO=20\
  WARNING=30\
  ERROR=40\
  CRITICAL=50\
  LOGGING_LEVEL=${DEBUG}

  DOCKER_DOMAIN='profile_mongo'\
  LOCAL_DOMAIN='localhost'\
  **DB_DOMAIN =${LOCAL_DOMAIN}**\
  DB_PORT = 27017

# Seteo de variables de entorno para usar en docker:

  DISABLE_DB=False

  LOG_FILENAME='profile.log'\
  NOTSET=0\
  DEBUG=10\
  INFO=20\
  WARNING=30\
  ERROR=40\
  CRITICAL=50\
  LOGGING_LEVEL=${DEBUG}

  DOCKER_DOMAIN='profile_mongo'\
  LOCAL_DOMAIN='localhost'\
  **DB_DOMAIN =${DOCKER_DOMAIN}**\
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
  
