from fastapi import HTTPException
from pydantic import BaseModel


# Entidad para definir los perfiles
class Profile(BaseModel):
   id: int
   username: str
   description: str
   
# Sustituto provisorio de base de datos con los perfiles
profiles_list = [Profile(id=1,username="LuisHuergo",description="Argentino. Ingeniero civil"),Profile(id=2,username="ElisaBachofen",description="Argentina. Ingeniera civil") ]

def view(id:int):
   profiles = filter(lambda profiles_list: profiles_list.id==id,profiles_list)
   try:
      return list(profiles)[0]
   except:
      raise HTTPException(status_code=400,detail="No se ha encontrado el usuario")
      #return {"error":"No se ha encontrado el usuario"}     

def update(id:int,updated_profile:Profile):
   if id!=updated_profile.id:
      raise HTTPException(status_code=400,detail="El id de la ruta no coincide con el id del perfil")      
	  #return {"error": "El id de la ruta no coincide con el id del perfil"}
   found = False
   for index,profile in enumerate(profiles_list):
      if profile.id == id:
         profiles_list[index]=updated_profile   
         found = True

   if not found:
      raise HTTPException(status_code=400,detail="No existe el usuario")
	  #return {"error": "No existe el usuario"}  	   

def delete(id:int):
   found = False
   for index,profile in enumerate(profiles_list):
      if profile.id == id:
         del profiles_list[index]
         found = True
   
   if not found:
      raise HTTPException(status_code=400,detail="No existe el usuario")
	  #return {"error": "No existe el usuario"}
	  