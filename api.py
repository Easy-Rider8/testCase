import requests

BASE_URL = "https://jsonplaceholder.typicode.com/users"

def test_list_users():
    response = requests.get(BASE_URL)
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_create_user():
    payload =   {
    "id": 11,
    "name": "Test",
    "username": "Delphine",
    "email": "Chaim_McDermott@dana.io",
    "address": {
      "street": "Dayna Park",
      "suite": "Suite 449",
      "city": "Bartholomebury",
      "zipcode": "76495-3109",
      "geo": {
        "lat": "24.6463",
        "lng": "-168.8889"
      }
    },
    "phone": "(775)976-6794 x41206",
    "website": "conrad.com",
    "company": {
      "name": "Yost and Sons",
      "catchPhrase": "Switchable contextually-based project",
      "bs": "aggregate real-time technologies"
    }
  }
    response = requests.post(BASE_URL, json=payload)
    assert response.status_code == 201
    assert response.json()["name"] == payload["name"]

def test_update_user():
    user_id = 10
    payload = {"name": "Updated User"}
    response = requests.put(f"{BASE_URL}/{user_id}", json=payload)
    assert response.status_code == 200
    assert response.json()["name"] == payload["name"]

def test_delete_user():
    user_id = 11
    response = requests.delete(f"{BASE_URL}/{user_id}")
    assert response.status_code == 200

def test_invalid_user_request():
    response = requests.get(f"{BASE_URL}/99999")
    assert response.status_code in [404, 200]

test_list_users()
test_create_user()
test_update_user()
test_delete_user()
test_invalid_user_request()