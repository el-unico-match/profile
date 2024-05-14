from fastapi import APIRouter,Path,HTTPException
from data.client import client_db
from data.pictures import Picture,Pictures
from bson import ObjectId

def picture_schema(picture)-> dict:
    return {"name":picture.name,
         	"url":picture.url,
	        "order":picture.order
			}

def pictures_schema(pictures)-> dict:
#   print("pictures"+str(pictures))
   list=[]
   for picture in pictures.pictures:
#       print("itera")
#       list.append(Picture(**picture_schema(picture)))
       list.append(picture_schema(picture))
   return {"userid":pictures.userid,"pictures":list}

router=APIRouter(tags=["pictures"])

# Operaciones de la API

@router.post("/user/profile/pictures")
async def create_pictures(new_pictures:Pictures):	 
   found=client_db.pictures_albums.find_one({"userid":new_pictures.userid})
   
   if found:
      raise HTTPException(status_code=400,detail="El usuario ya existe")        

   print(type(new_pictures)) 
   
   pictures_dict=pictures_schema(new_pictures)
#   print("pictures_dict:"+str(pictures_dict))
   client_db.pictures_albums.insert_one(pictures_dict)

@router.get("/user/profile/pictures/{id}")
async def view_pictures(id: str = Path(..., description="El id del usuario")): 
#   logger.info("buscando el imágenes") 
   try:
      pictures_album = client_db.pictures_albums.find_one({"userid":id})

#      print(type(pictures_album)) 
      return Pictures(**pictures_album)
	  #return Pictures(**pictures_schema({"pictures":pictures})) 	  
   except Exception as e:
#      logger.error(str(e))
      print(e)
      raise HTTPException(status_code=404,detail="No se ha encontrado el usuario")   
   
@router.put("/user/profile/pictures/{id}")
async def update_pictures(new_pictures:Pictures,id: str = Path(..., description="El id del usuario")):     
#   logger.info("actualizando el imágenes")
   
   if id!=new_pictures.userid:
#      logger.error("El id de la ruta no coincide con el id del perfil")         
      raise HTTPException(status_code=400,detail="El id de la ruta no coincide con el id del perfil") 

#   print(type(new_pictures)) 
   new_pictures_dict=pictures_schema(new_pictures)
#   print(new_pictures_dict)
#   logger.info("actualizando las imágenes en base de datos")
   found=client_db.pictures_albums.find_one_and_replace({"userid":id},new_pictures_dict)

   if not found:
#      logger.error("el usuario no existe")      
      raise HTTPException(status_code=404,detail="No existe el usuario")   
