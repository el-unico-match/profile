from fastapi import APIRouter,Path,Depends,Response,HTTPException
#from data.client import client_db
from data.pictures import Picture,Pictures
from bson import ObjectId
import data.client as client
from settings import settings
import logging


#logging.basicConfig(format='%(asctime)s [%(filename)s] %(levelname)s %(message)s',filename=settings.log_filename,level=settings.logging_level)
logger=logging.getLogger(__name__)
streamHandler = logging.StreamHandler()
streamHandler.setLevel(settings.logging_level)
formatter = logging.Formatter('%(levelname)s %(asctime)s [%(filename)s] %(message)s')
streamHandler.setFormatter(formatter)
logger.addHandler(streamHandler)

def picture_schema(picture)-> dict:
    return {"name":picture.name,
         	"url":picture.url,
	        "order":picture.order,
			"type":picture.type
			}

def pictures_schema(pictures)-> dict:
#   print("pictures"+str(pictures))
   list=[]
   for picture in pictures.pictures:
#       list.append(Picture(**picture_schema(picture)))
       list.append(picture_schema(picture))
   return {"userid":pictures.userid,"pictures":list}

router=APIRouter(tags=["pictures"])

# Operaciones de la API

@router.post("/user/profile/pictures", response_model=Pictures,summary="Crea nuevas imágenes")
async def create_pictures(new_pictures:Pictures,client_db = Depends(client.get_db)):	 
   logger.info("creando imágenes")
   found=client_db.pictures_albums.find_one({"userid":new_pictures.userid})
   
   if found:
      logger.error("el usuario no existe")    
      raise HTTPException(status_code=400,detail="El usuario ya existe")        

   print(type(new_pictures)) 
   
   pictures_dict=pictures_schema(new_pictures)
#   print("pictures_dict:"+str(pictures_dict))
   client_db.pictures_albums.insert_one(pictures_dict)

   pictures_album = client_db.pictures_albums.find_one({"userid":new_pictures.userid})
   return Pictures(**pictures_album)   
   
@router.get("/user/profile/pictures/{id}", response_model=Pictures,summary="Retorna las imágenes solicitadas")
async def view_pictures(client_db = Depends(client.get_db),id: str = Path(..., description="El id del usuario")): 
   logger.info("buscando imágenes") 
   try:
      pictures_album = client_db.pictures_albums.find_one({"userid":id})

#      print(type(pictures_album)) 
      return Pictures(**pictures_album)
   except Exception as e:
      logger.error(str(e))
      print(e)
      raise HTTPException(status_code=404,detail="No se ha encontrado el usuario")   
   
@router.put("/user/profile/pictures/{id}", response_model=Pictures,summary="Actualiza las imágenes solicitadas")
async def update_pictures(new_pictures:Pictures,client_db = Depends(client.get_db),id: str = Path(..., description="El id del usuario")):     
   logger.info("actualizando imágenes")
   
   if id!=new_pictures.userid:
      logger.error("El id de la ruta no coincide con el id del perfil")         
      raise HTTPException(status_code=400,detail="El id de la ruta no coincide con el id del perfil") 

   new_pictures_dict=pictures_schema(new_pictures)
#   print(new_pictures_dict)
   logger.info("actualizando las imágenes en base de datos")
   found=client_db.pictures_albums.find_one_and_replace({"userid":id},new_pictures_dict)

   if not found:
      logger.error("el usuario no existe")      
      raise HTTPException(status_code=404,detail="No existe el usuario")   

   pictures_album = client_db.pictures_albums.find_one({"userid":new_pictures.userid})
   return Pictures(**pictures_album) 	  