from fastapi import APIRouter,HTTPException
from data.profile import Profile

# Sustituto provisorio de base de datos con los perfiles
profiles_list = [Profile(userid="1",username="LuisHuergo",description="Argentino. Ingeniero civil",gender="Hombre",looking_for="Mujer"),
                 Profile(userid="2",username="ElisaBachofen",description="Argentina. Ingeniera civil",gender="Mujer",looking_for="Hombre") ]

router=APIRouter(tags=["profile"])

# Para iniciar el server hacer: uvicorn profile:app --reload

# Url local: http://127.0.0.1:8000
# Documentación con swagger: http://127.0.0.1:8000/docs 
# Documentación con Redocly: http://127.0.0.1:8000/redoc 
# Url: http://127.0.0.1:8000/user/profile/{id} 

# Operaciones de la API

@router.get("/user/profile/{id}",response_model=Profile)
async def view_profile(id: str): 
   profiles = filter(lambda profiles_list: profiles_list.userid==id,profiles_list)
   try:
       return list(profiles)[0]
   except:
       raise HTTPException(status_code=404,detail="No se ha encontrado el usuario") 

def validar(profile: Profile):	   
   if profile.userid=="":
      raise HTTPException(status_code=400,detail="Falta indicar el id de usuario")
   if profile.username=="":
      raise HTTPException(status_code=400,detail="Falta indicar el nombre de usuario")	  
   if profile.gender=="":
      raise HTTPException(status_code=400,detail="Falta indicar el genero")	 
	   
@router.post("/user/profile/")
async def create_profile(new_profile: Profile):
#   if id!=new_profile.userid:
#      raise HTTPException(status_code=400,detail="El id de la ruta no coincide con el id del perfil")    

#   if new_profile.userid=="":
#      raise HTTPException(status_code=400,detail="Falta indicar el id de usuario")
#   if new_profile.username=="":
#      raise HTTPException(status_code=400,detail="Falta indicar el nombre de usuario")	  
#   if new_profile.gender=="":
#      raise HTTPException(status_code=400,detail="Falta indicar el genero")	 

   validar(new_profile)

   for profile in profiles_list:
#       if profile.userid == id:
        if profile.userid == new_profile.userid:
          raise HTTPException(status_code=400,detail="El usuario ya existe")      
   profiles_list.append(new_profile)   
	  
@router.put("/user/profile/{id}")
async def update_profile(id: str,updated_profile:Profile):     
   if id!=updated_profile.userid:
      raise HTTPException(status_code=400,detail="El id de la ruta no coincide con el id del perfil")

   validar(updated_profile)	  
	  
   found = False
   for index,profile in enumerate(profiles_list):
      if profile.userid == id:
         profiles_list[index]=updated_profile   
         found = True

   if not found:
      raise HTTPException(status_code=404,detail="No existe el usuario")  

@router.delete("/user/profile/{id}")
async def delete_profile(id: str): 
   found = False
   for index,profile in enumerate(profiles_list):
      if profile.userid == id:
         del profiles_list[index]
         found = True
   
   if not found:
      raise HTTPException(status_code=404,detail="No existe el usuario")
