from fastapi import APIRouter,HTTPException
from pydantic import BaseModel
from data.client import client_db
from bson import ObjectId

# Entidad para definir los perfiles
class Profile(BaseModel):
   id: str
   username: str
   description: str

def profile_schema(profile)-> dict:
    return {"id":str(profile["_id"]),"username":profile["username"],"description":profile["description"]}
	
router=APIRouter(tags=["profile_db"])

# Para iniciar el server hacer: uvicorn profile_db:app --reload

# Url local: http://127.0.0.1:8000
# Documentación con swagger: http://127.0.0.1:8000/docs 
# Documentación con Redocly: http://127.0.0.1:8000/redoc 
# Url: http://127.0.0.1:8000/user/{id}/profile 

# Operaciones de la API

@router.get("/user/{id}/profile",response_model=Profile)
async def view_profile(id: str): 
   try:
      profile = client_db.local.profiles.find_one({"_id":ObjectId(id)})
      return Profile(**profile_schema(profile)) 	  
   except:
      raise HTTPException(status_code=400,detail="No se ha encontrado el usuario")

@router.put("/user/{id}/profile")
async def update_profile(id: str,updated_profile:Profile):     
   if id!=updated_profile.id:
      raise HTTPException(status_code=400,detail="El id de la ruta no coincide con el id del perfil") 
   updated_profile_dict=dict(updated_profile)
   del updated_profile_dict["id"]
   try:
      client_db.local.profiles.find_one_and_replace({"_id":ObjectId(id)},updated_profile_dict)
   except:
      raise HTTPException(status_code=400,detail="No existe el usuario")

#   if id!=updated_profile.id:
#      raise HTTPException(status_code=400,detail="El id de la ruta no coincide con el id del perfil")      
#	  #return {"error": "El id de la ruta no coincide con el id del perfil"}
#   found = False
#   for index,profile in enumerate(profiles_list):
#      if profile.id == id:
#         profiles_list[index]=updated_profile   
#         found = True
#
#   if not found:
#      raise HTTPException(status_code=400,detail="No existe el usuario")
#	  #return {"error": "No existe el usuario"}  

@router.delete("/user/{id}/profile")
async def delete_profile(id: str): 
   found = client_db.local.profiles.find_one_and_delete({"_id":ObjectId(id)})
   
   if not found:
      raise HTTPException(status_code=400,detail="No existe el usuario")
	  #return {"error": "No existe el usuario"}	  