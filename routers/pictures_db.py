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

