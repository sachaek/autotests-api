import httpx
from tools.fakers import get_random_email

create_user_payload = {
    "email": get_random_email(),
    "password": "string",
    "lastName": "string",
    "firstName": "string",
    "middleName": "string"
}

create_user_response = httpx.post("http://localhost:8000/api/v1/users", json=create_user_payload)
create_user_data = create_user_response.json()

print(f"Create usr data: {create_user_data}")

login_payload = {
    "email": create_user_payload["email"],
    "password": create_user_payload["password"]
}
login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)

login_response_data = login_response.json()
print("Login response data: ", login_response_data)
login_response_id = create_user_data["user"]["id"]
auth_token = login_response_data["token"]["accessToken"]
print("User id:", login_response_id)

update_user_payload = {
  "email": get_random_email(),
  "lastName": "string",
  "firstName": "string",
  "middleName": "string"
}
params = {"user_id": login_response_id}

update_user_response = httpx.patch(f"http://localhost:8000/api/v1/users/{login_response_id}",
                                 json=update_user_payload,
                                 headers={"Authorization": f"Bearer {auth_token}"})
response_data = update_user_response.json()
print(f"\nResponse data <Updated user>: {response_data}")

