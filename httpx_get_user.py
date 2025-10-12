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

headers_auth = {
    "Authorization": f'Bearer {auth_token}'
}
get_user_response = httpx.get(f"http://localhost:8000/api/v1/users/{login_response_id}", headers=headers_auth)

get_user_response_data = get_user_response.json()
print("Get user data:", get_user_response_data)
