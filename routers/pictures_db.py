from fastapi import APIRouter,HTTPException
from data.client import client_db
from data.pictures import Picture,Pictures
from bson import ObjectId

def picture_schema(picture)-> dict:
    return {"name":picture["name"],
         	"url":picture["url"],
	        "order":picture["order"]
			}

def pictures_schema(pictures)-> dict:
#   print("pictures"+str(pictures))
   list=[]
   for picture in pictures["pictures"]:
#       print("itera")
#       list.append(Picture(**picture_schema(picture)))
       list.append(picture_schema(picture))
   return {"userid":pictures["userid"],"pictures":list}

router=APIRouter(tags=["pictures"])

# Operaciones de la API

@router.post("/user/profile/pictures")
async def create_pictures(new_pictures:Pictures):	 
   found=client_db.pictures_albums.find_one({"userid":new_pictures.userid})
   
   if found:
      raise HTTPException(status_code=400,detail="El usuario ya existe")        
   
   pictures_dict=pictures_schema(new_pictures)
#   print("pictures_dict:"+str(pictures_dict))
   client_db.pictures_albums.insert_one(pictures_dict)

@router.get("/user/profile/pictures/{id}")
async def view_pictures(id: str): 
#   logger.info("buscando el perfil asociado al id de usuario:"+id) 
   try:
      pictures_album = client_db.pictures_albums.find_one({"userid":id})
#      print(   pictures_album["pictures"])
#      pictures=pictures_album["pictures"]
#      print(pictures_album)
#      print(type({"pictures":pictures}))
      return pictures_schema(pictures_album)
	  #return Pictures(**pictures_schema({"pictures":pictures})) 	  
   except Exception as e:
#      logger.error(str(e))
#      print(e)
      raise HTTPException(status_code=404,detail="No se ha encontrado el usuario")   
   
@router.put("/user/profile/pictures/{id}")
async def update_pictures(id: str,new_pictures:Pictures):     
#   logger.info("actualizando el perfil")
   
   if id!=new_pictures.userid:
#      logger.error("El id de la ruta no coincide con el id del perfil")         
      raise HTTPException(status_code=400,detail="El id de la ruta no coincide con el id del perfil") 

   new_pictures_dict=pictures_schema(new_pictures)
   print(new_pictures_dict)
#   logger.info("actualizando el perfil en base de datos")
   found=client_db.pictures_albums.find_one_and_replace({"userid":id},new_pictures_dict)

   if not found:
#      logger.error("el usuario no existe")      
      raise HTTPException(status_code=404,detail="No existe el usuario")   
   
"""   
@router.post("/user/profile/pictures/{id}/{name}")
async def add_picture(id: str,name:str,new_picture:Picture):     
   pictures_album = client_db.pictures_albums.find_one({"userid":id})
   
   if not pictures_album:
      raise HTTPException(status_code=404,detail="No se ha encontrado el usuario")

   new_picture_dict=dict(new_picture)	  
   pictures_album["pictures"].append(new_picture_dict)   
#   del pictures_album["_id"]
   found=client_db.pictures_albums.find_one_and_replace({"userid":id},pictures_album)  
	
   if not found:
#      logger.error("el usuario no existe")      
      raise HTTPException(status_code=404,detail="No existe el usuario")
   
#	pictures_album.append(new_picture)   

@router.put("/user/profile/pictures/{id}/{name}")
async def replace_picture(id: str,name:str,new_picture:Picture):     
   pictures_album = client_db.pictures_albums.find_one({"userid":id})
   
   if not pictures_album:
      raise HTTPException(status_code=404,detail="No se ha encontrado el usuario")

   new_picture_dict=dict(new_picture)	  
   
   pictures=pictures_album["pictures"]
   
   index=find_index(pictures,name)   
   
   if not index:
      raise HTTPException(status_code=404,detail="No existe la foto")    

#   print("intenta reemplazar en la lista de fotos")	  
   pictures[index]=new_picture_dict   
#   del pictures_album["_id"]
#   print("intenta reemplazar en la base de datos")
   found=client_db.pictures_albums.find_one_and_replace({"userid":id},pictures_album)  
#   print("reemplazo en la base de datos")
   
   if not found:
#      logger.error("el usuario no existe")      
      raise HTTPException(status_code=404,detail="No existe el usuario")


def find_index(pictures,name):
   index=None 
   for index,picture in enumerate(pictures):
      if picture["name"] == name:
         return index      	
   return None
"""   