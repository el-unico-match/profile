from fastapi import APIRouter,HTTPException
from data.client import client_db
from data.profile import Profile
from bson import ObjectId

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
	    
			
router=APIRouter(tags=["profile_db"])

# Para iniciar el server hacer: uvicorn profile_db:app --reload

# Url local: http://127.0.0.1:8000
# Documentación con swagger: http://127.0.0.1:8000/docs 
# Documentación con Redocly: http://127.0.0.1:8000/redoc 
# Url: http://127.0.0.1:8000/user/profile/{id} 

# Operaciones de la API

@router.get("/user/profile/status",summary="Retorna el estado del servicio")
async def view_status(): 
    return {"status":"ok"}

@router.get("/users/profiles/",summary="Retorna una lista con todos los perfiles")
async def view_profiles():
    profiles = client_db.local.profiles.find()
    return profiles_schema(profiles)

@router.get("/user/profile/{id}",response_model=Profile,summary="Retorna el perfil solicitado")
async def view_profile(id: str): 
   try:
      profile = client_db.local.profiles.find_one({"userid":id})
      return Profile(**profile_schema(profile)) 	  
   except:
      raise HTTPException(status_code=404,detail="No se ha encontrado el usuario")

def validar(profile: Profile):	   
   if profile.userid=="":
      raise HTTPException(status_code=400,detail="Falta indicar el id de usuario")
   if profile.username=="":
      raise HTTPException(status_code=400,detail="Falta indicar el nombre de usuario")	  
   if profile.gender=="":
      raise HTTPException(status_code=400,detail="Falta indicar el genero")	 
	   	  

@router.post("/user/profile/",summary="Crea un nuevo perfil")
async def create_profile(new_profile:Profile):	 
#   if new_profile.userid=="":
#      raise HTTPException(status_code=400,detail="Falta indicar el id de usuario")
#   if new_profile.username=="":
#      raise HTTPException(status_code=400,detail="Falta indicar el nombre de usuario")	  
#   if new_profile.gender=="":
#      raise HTTPException(status_code=400,detail="Falta indicar el genero")	 

   validar(new_profile)
   
   found=client_db.local.profiles.find_one({"userid":new_profile.userid})
   
   if found:
      raise HTTPException(status_code=400,detail="El usuario ya existe")        
   
   profile_dict=dict(new_profile)
   client_db.local.profiles.insert_one(profile_dict)
	  
	  
@router.put("/user/profile/{id}",summary="Actualiza el perfil solicitado")
async def update_profile(id: str,updated_profile:Profile):     
   if id!=updated_profile.userid:
      raise HTTPException(status_code=400,detail="El id de la ruta no coincide con el id del perfil") 

   validar(updated_profile)	  

   updated_profile_dict=dict(updated_profile)
#   print(updated_profile_dict)
   found=client_db.local.profiles.find_one_and_replace({"userid":id},updated_profile_dict)

   if not found:
      raise HTTPException(status_code=404,detail="No existe el usuario")
  

@router.delete("/user/profile/{id}",summary="Elimina el perfil solicitado")
async def delete_profile(id: str): 
   
   found = client_db.local.profiles.find_one_and_delete({"userid":id})

   if not found:
      raise HTTPException(status_code=404,detail="No existe el usuario")
