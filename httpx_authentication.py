import httpx

login_payload = {
    "email": "user1@example.com",
    "password": "string"
}
uri = "http://localhost:8000"
login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)

login_response_data = login_response.json()
print("Login response: ",  login_response_data)
print("Status code: ", login_response.status_code)
print("Token Authentication: ", login_response_data["token"]["accessToken"])
print("refreshToken: ", login_response_data['token']['refreshToken'])


refresh_payload = {
  "refreshToken": f"{login_response_data['token']['refreshToken']}"
}

refresh_response = httpx.post(f'{uri}/api/v1/authentication/refresh', json=refresh_payload)
refresh_response_data = refresh_response.json()
print("NEW RESPONSE!!!")
print("Refresh response: ", refresh_response_data)
print("Refresh response status code: ", refresh_response.status_code)

