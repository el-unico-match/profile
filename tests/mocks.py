from fastapi import HTTPException
#pendiente de subir al repositorio

class Profiles_mock:

    def __init__(self):
        pass    
 
    def find(self):
        return [{ "userid" : "1",
   "username" : "Luis Huergo",
   "email" : "lhuergo@fi.uba.ar",
   "description" : "Estudié en la UBA",
   "gender" : "Hombre",
   "looking_for" : "Mujer",
   "age" : 33,
   "education" : "Ingeniero civil",
   "ethnicity" : "Europeo"
   }
   ]
	
    def find_one(self,dictionary):
#        print(dictionary["userid"])	
        if dictionary["userid"]!="1":
#           print("no encontrado")
           raise HTTPException(status_code=404,detail="No se ha encontrado el usuario")
        else:
#           print("no encontrado")
           return { "userid" : "1",
   "username" : "Luis Huergo",
   "email" : "lhuergo@fi.uba.ar",
   "description" : "Estudié en la UBA",
   "gender" : "Hombre",
   "looking_for" : "Mujer",
   "age" : 33,
   "education" : "Ingeniero civil",
   "ethnicity" : "Europeo"
   }



class Mocks:

    profiles=Profiles_mock()

    def __init__(self):
        pass  