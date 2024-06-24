from fastapi import APIRouter,Path,Depends,Response,HTTPException
#from data.client import client_db
from data.profile import Profile
from typing import List
from bson import ObjectId
import data.client as client
from settings import settings
import logging

logging.basicConfig(format='%(asctime)s [%(filename)s] %(levelname)s %(message)s',filename=settings.log_filename,level=settings.logging_level)
logger=logging.getLogger(__name__)


def profile_schema(profile)-> dict:
    return {"userid":profile["userid"],
         	"username":profile["username"],
	        "email":profile["email"],
			"description":profile["description"],
			"gender":profile["gender"],
			"looking_for":profile["looking_for"],
			"age":profile["age"],
			"education":profile["education"],
	        "ethnicity":profile["ethnicity"]
			}

def profiles_schema(profiles)-> list:
   list=[]
   for profile in profiles:
       list.append(Profile(**profile_schema(profile)))
   return list
	    
			
router=APIRouter(tags=["profile"])

# Para iniciar el server hacer: uvicorn profile_db:app --reload

# Url local: http://127.0.0.1:8000
# Documentación con swagger: http://127.0.0.1:8000/docs 
# Documentación con Redocly: http://127.0.0.1:8000/redoc 
# Url: http://127.0.0.1:8000/user/profile/{id} 

# Operaciones de la API

@router.get("/status",summary="Retorna el estado del servicio")
async def view_status(): 
    logger.info("retornando status")
    return {"status":"ok"}

@router.get("/users/profiles",response_model=List[Profile],summary="Retorna una lista con todos los perfiles")
async def view_profiles(client_db = Depends(client.get_db)):
    logger.info("buscando todos los perfiles")
    profiles = client_db.profiles.find()
    return profiles_schema(profiles)

@router.get("/user/profile/{id}",response_model=Profile,summary="Retorna el perfil solicitado")
async def view_profile(client_db = Depends(client.get_db),id: str = Path(..., description="El id del usuario")): 
   logger.info("buscando el perfil asociado al id de usuario:"+id) 
   try:
      profile = client_db.profiles.find_one({"userid":id})
      return Profile(**profile_schema(profile)) 	  
   except Exception as e:
      logger.error(str(e))
      raise HTTPException(status_code=404,detail="No se ha encontrado el usuario")

def validate(profile: Profile):	
   logger.info("validando campos del perfil")   
   if profile.userid=="":
      logger.error("Falta indicar el id de usuario")     
      raise HTTPException(status_code=400,detail="Falta indicar el id de usuario")
   if profile.username=="":
      logger.error("Falta indicar el nombre de usuario")  
      raise HTTPException(status_code=400,detail="Falta indicar el nombre de usuario")	  
   if profile.gender=="":
      logger.error("Falta indicar el genero")     
      raise HTTPException(status_code=400,detail="Falta indicar el genero")	 
	   	  

@router.post("/user/profile",response_model=Profile,summary="Crea un nuevo perfil")
async def create_profile(new_profile:Profile,client_db = Depends(client.get_db)): 
   logger.info("creando el perfil") 
   
   validate(new_profile)

   logger.info("chequeando si ya existe el perfil")   
   found=client_db.profiles.find_one({"userid":new_profile.userid})
   
   if found:
      logger.error("el usuario ya existe")   
      raise HTTPException(status_code=400,detail="El usuario ya existe")        
   
   profile_dict=dict(new_profile)
   logger.info("creando el perfil en base de datos")     
   client_db.profiles.insert_one(profile_dict)  

   profile = client_db.profiles.find_one({"userid":new_profile.userid})
   return Profile(**profile_schema(profile)) 	 
   
@router.put("/user/profile/{id}",response_model=Profile,summary="Actualiza el perfil solicitado")
async def update_profile(updated_profile:Profile,client_db = Depends(client.get_db),id: str = Path(..., description="El id del usuario")):     
   logger.info("actualizando el perfil")
   
   if id!=updated_profile.userid:
      logger.error("El id de la ruta no coincide con el id del perfil")         
      raise HTTPException(status_code=400,detail="El id de la ruta no coincide con el id del perfil") 

   validate(updated_profile)	  

   updated_profile_dict=dict(updated_profile)
#   print(updated_profile_dict)
   logger.info("actualizando el perfil en base de datos")
   found=client_db.profiles.find_one_and_replace({"userid":id},updated_profile_dict)

   if not found:
      logger.error("el usuario no existe")      
      raise HTTPException(status_code=404,detail="No existe el usuario")

   profile = client_db.profiles.find_one({"userid":updated_profile.userid})
   return Profile(**profile_schema(profile)) 	  

@router.delete("/user/profile/{id}",summary="Elimina el perfil solicitado", response_class=Response)
async def delete_profile(client_db = Depends(client.get_db),id: str = Path(..., description="El id del usuario"))-> None: 

   logger.info("eliminando el perfil asociado al id de usuario:"+id)   
   found = client_db.profiles.find_one_and_delete({"userid":id})

   if not found:
      logger.error("el usuario no existe")    
      raise HTTPException(status_code=404,detail="No existe el usuario")
