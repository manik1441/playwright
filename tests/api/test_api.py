from api.base_client import BaseClient


def test_verify_db():
    #API Interaction (Example)
    api = BaseClient("https://reqres.in/api")
    response = api.get("/users/2")
    assert response.status_code == 200
