from fastapi import APIRouter,HTTPException
from data.client import client_db
from data.pictures import Picture,Pictures
from bson import ObjectId

def picture_schema(picture)-> dict:
    return {"name":picture.name,
         	"url":picture.url,
	        "order":picture.order
			}

def pictures_schema(pictures)-> dict:
   list=[]
   for picture in pictures.pictures:
#       list.append(Picture(**picture_schema(picture)))
       list.append(picture_schema(picture))
   return {"userid":pictures.userid,"pictures":list}

router=APIRouter(tags=["pictures_db"])

# Operaciones de la API

@router.post("/user/profile/pictures")
async def create_pictures(new_pictures:Pictures):	 
   found=client_db.local.pictures_albums.find_one({"userid":new_pictures.userid})
   
   if found:
      raise HTTPException(status_code=400,detail="El usuario ya existe")        
   
   pictures_dict=pictures_schema(new_pictures)
#   print("pictures_dict:"+str(pictures_dict))
   client_db.local.pictures_albums.insert_one(pictures_dict)
   
   
@router.put("/user/profile/pictures/{id}/{name}")
async def add_picture(id: str,name:str,new_picture:Picture):     
   pictures_album = client_db.local.pictures_albums.find_one({"userid":id})
   
   if not pictures_album:
      raise HTTPException(status_code=404,detail="No se ha encontrado el usuario")

   new_picture_dict=dict(new_picture)	  
   pictures_album["pictures"].append(new_picture_dict)   
#   del pictures_album["_id"]
   found=client_db.local.pictures_albums.find_one_and_replace({"userid":id},pictures_album)  
	
   if not found:
#      logger.error("el usuario no existe")      
      raise HTTPException(status_code=404,detail="No existe el usuario")
   
#	pictures_album.append(new_picture)   