from pydantic import BaseModel
from typing import Optional

# Entidad para definir los perfiles
class Profile(BaseModel):
   userid: str
   username: str
   description: str
   gender: str
   looking_for: str