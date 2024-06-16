from pydantic import BaseModel
from typing import List

# Entidad para definir las fotos
class Picture(BaseModel):
#   userid: str
   name: str
   url: str
   order: int 
   type: str    
   
class Pictures(BaseModel):
   userid: str
   pictures:List[Picture]