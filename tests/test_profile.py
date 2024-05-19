from fastapi.testclient import TestClient
#from tests.profiles_mock import profiles
##from routers.profile_db import router
import data.client as client
from main import app
from tests.mocks import Mocks
from unittest import TestCase

def override_get_db():
   mocks=Mocks()
   return mocks
#    return profiles

app.dependency_overrides[client.get_db] = override_get_db

client = TestClient(app)

class TestFeedAceptanceCriteria(TestCase):
    def test_view_user_1_profile(self):
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
        
    def test_view_profiles(self):
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

    def test_1_create_invalid_user_profile(self):
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

    def test_2_create_invalid_user_profile(self):
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

    def test_3_create_invalid_user_profile(self):
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
        
    def test_view_user_1_pictures(self):
        response = client.get("/user/profile/pictures/1")
        assert response.status_code == 200, response.text
        data = response.json()
        assert data["userid"] == "1"
        pictures=data["pictures"][0]
        assert pictures["name"] == "foto1.jpg"
        assert pictures["url"] == "myurl/foto1.jpg"
        assert pictures["order"] == 0