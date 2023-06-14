import requests

ENDPOINT = "http://127.0.0.1:5000"


def test_get_user():
    response = requests.get(ENDPOINT + "/get-user/1")
    assert response.status_code == 200
    pass


def test_create_user():
    payload = {
        "email": "hohn.doe@emaple.com",
        "name": "John Doe",
        "user_id": "1"
    }
    response = requests.post(ENDPOINT + "/create-user", json=payload)

    assert response.status_code == 201
