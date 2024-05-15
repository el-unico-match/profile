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

def test_view_profile_1():
    response = client.get("/user/profile/1")
#    print(response)
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