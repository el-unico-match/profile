from pydantic import BaseModel

# Entidad para definir los perfiles
class Profile(BaseModel):
   id: str
   username: str
   description: str