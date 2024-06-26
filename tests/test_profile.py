from fastapi.testclient import TestClient
#from tests.profiles_mock import profiles
##from routers.profile_db import router
import data.client as client
from main import app
from tests.mocks import Mocks

def override_get_db():
   mocks=Mocks()
   return mocks
#    return profiles

app.dependency_overrides[client.get_db] = override_get_db

client = TestClient(app)

def test_status():
    response = client.get("/status")
    assert response.status_code == 200
    assert response.json()['status'] == "ok"

def test_view_user_1_profile():
    response = client.get("/user/profile/1")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["userid"] == "1"
    assert data["username"] == "Luis Huergo"
    assert data["email"] == "lhuergo@fi.uba.ar"
    assert data["description"] == "Estudié en la UBA"
    assert data["gender"] == "Hombre"
    assert data["looking_for"] == "Mujer"
    assert data["age"] == 33
    assert data["education"] == "Ingeniero civil"
    assert data["ethnicity"] == "Europeo"

def test_view_inexistent_user_profile():
    response = client.get("/user/profile/1234")
    assert response.status_code == 404, response.text
	
def test_view_profiles():
    response = client.get("/users/profiles/")
    assert response.status_code == 200, response.text
    data = response.json()[0]
    assert data["userid"] == "1"
    assert data["username"] == "Luis Huergo"
    assert data["email"] == "lhuergo@fi.uba.ar"
    assert data["description"] == "Estudié en la UBA"
    assert data["gender"] == "Hombre"
    assert data["looking_for"] == "Mujer"
    assert data["age"] == 33
    assert data["education"] == "Ingeniero civil"
    assert data["ethnicity"] == "Europeo"	

def test_1_create_invalid_user_profile():
    response = client.post("/user/profile/",
    json={ "userid" : "",
   "username" : "Luis Huergo",
   "email" : "lhuergo@fi.uba.ar",
   "description" : "Estudié en la UBA",
   "gender" : "Hombre",
   "looking_for" : "Mujer",
   "age" : 33,
   "education" : "Ingeniero civil",
   "ethnicity" : ""
})
    assert response.status_code == 400, response.text
    response = response.text
    print(response)
    assert response == '{"detail":"Falta indicar el id de usuario"}'

def test_2_create_invalid_user_profile():
    response = client.post("/user/profile/",
    json={ "userid" : "2",
   "username" : "",
   "email" : "lhuergo@fi.uba.ar",
   "description" : "Estudié en la UBA",
   "gender" : "Hombre",
   "looking_for" : "Mujer",
   "age" : 33,
   "education" : "Ingeniero civil",
   "ethnicity" : ""
})
    assert response.status_code == 400, response.text
    response = response.text
    print(response)
    assert response == '{"detail":"Falta indicar el nombre de usuario"}'

def test_3_create_invalid_user_profile():
    response = client.post("/user/profile/",
    json={ "userid" : "2",
   "username" : "Luis",
   "email" : "lhuergo@fi.uba.ar",
   "description" : "Estudié en la UBA",
   "gender" : "",
   "looking_for" : "Mujer",
   "age" : 33,
   "education" : "Ingeniero civil",
   "ethnicity" : ""
})
    assert response.status_code == 400, response.text
    response = response.text
    print(response)
    assert response == '{"detail":"Falta indicar el genero"}'

def test_create_existent_user_profile():
    response = client.post("/user/profile",
    json={ "userid": "1",
  "username": "Luis Huergo",
  "email": "lhuergo@fi.uba.ar",
  "description": "Estudié en la UBA",
  "gender": "Hombre",
  "looking_for": "Mujer",
  "age": 33,
  "education": "Ingeniero civil",
  "ethnicity": "Europeo"
})

    assert response.status_code == 400, response.text
    response = response.text
    print(response)
    assert response == '{"detail":"El usuario ya existe"}'

def test_2_update_invalid_user_profile():
    response = client.put("/user/profile/1",
    json={ "userid" : "1",
   "username" : "",
   "email" : "lhuergo@fi.uba.ar",
   "description" : "Estudié en la UBA",
   "gender" : "Hombre",
   "looking_for" : "Mujer",
   "age" : 33,
   "education" : "Ingeniero civil",
   "ethnicity" : ""
})
    assert response.status_code == 400, response.text
    response = response.text
    print(response)
    assert response == '{"detail":"Falta indicar el nombre de usuario"}'

def test_3_update_invalid_user_profile():
    response = client.put("/user/profile/1",
    json={ "userid" : "1",
   "username" : "Luis",
   "email" : "lhuergo@fi.uba.ar",
   "description" : "Estudié en la UBA",
   "gender" : "",
   "looking_for" : "Mujer",
   "age" : 33,
   "education" : "Ingeniero civil",
   "ethnicity" : ""
})
    assert response.status_code == 400, response.text
    response = response.text
    print(response)
    assert response == '{"detail":"Falta indicar el genero"}'

def test_update_inexistent_user_profile():
    response = client.put("/user/profile/1234",
    json={ "userid" : "1234",
   "username" : "Luis",
   "email" : "lhuergo@fi.uba.ar",
   "description" : "Estudié en la UBA",
   "gender" : "Hombre",
   "looking_for" : "Mujer",
   "age" : 33,
   "education" : "Ingeniero civil",
   "ethnicity" : ""
})
    assert response.status_code == 404, response.text
    response = response.text
    assert response == '{"detail":"No existe el usuario"}'
	
def test_view_user_1_pictures():
    response = client.get("/user/profile/pictures/1")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["userid"] == "1"
    pictures=data["pictures"][0]
    assert pictures["name"] == "foto1.jpg"
    assert pictures["url"] == "myurl/foto1.jpg"
    assert pictures["order"] == 0
    assert pictures["type"] == "profile"
	
def test_view_inexistent_user_pictures():
    response = client.get("/user/profile/pictures/1234")
    assert response.status_code == 404, response.text	
	
def test_create_existent_user_pictures():
    response = client.post("/user/profile/pictures",
    json={
        "userid": "1",
        "pictures": [
        {
           "name": "foto1.jpg",
           "url": "myurl/foto1.jpg",
           "order": 0,
		   "type": "profile"
        }
        ]
        })

    assert response.status_code == 400, response.text
    response = response.text
    print(response)
    assert response == '{"detail":"El usuario ya existe"}'	
	
def test_update_inexistent_user_pictures():
    response = client.put("/user/profile/pictures/1234",
    json={
        "userid": "1234",
        "pictures": [
        {
           "name": "foto1.jpg",
           "url": "myurl/foto1.jpg",
           "order": 0,
		   "type": "profile"
        }
        ]
        })
    assert response.status_code == 404, response.text
    response = response.text
    print(response)
    assert response == '{"detail":"No existe el usuario"}'
	
def test_delete_inexistent_user_profile():
    response = client.delete("/user/profile/1234")
    assert response.status_code == 404, response.text
    response = response.text
    assert response == '{"detail":"No existe el usuario"}'	