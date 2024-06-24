from fastapi import HTTPException

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

class Pictures_mock:

    def __init__(self):
        pass	    
	
    def find_one(self,dictionary):
        if dictionary["userid"]!="1":
           raise HTTPException(status_code=404,detail="No se ha encontrado el usuario")
        else:
           return {
        "userid": "1",
        "pictures": [
        {
           "name": "foto1.jpg",
           "url": "myurl/foto1.jpg",
           "order": 0,
		   "type": "profile"
        }
        ]
        }
		
    def find_one_and_replace(self,keydictionary,dictionary):
        if dictionary["userid"]!="1":
           raise HTTPException(status_code=404,detail="No existe el usuario")	

class Mocks:

    profiles=Profiles_mock()
    pictures_albums=Pictures_mock()

    def __init__(self):
        pass  