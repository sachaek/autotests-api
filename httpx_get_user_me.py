from typing import Tuple, Any

import httpx

hostname = "http://localhost:8000"
endpoint_login = "/api/v1/authentication/login"
endpoint_get_user_me = "/api/v1/users/me"


def get_token_login() -> str:
    payload_login = {
        "email": "user1@example.com",
        "password": "string"
    }
    response = httpx.post(f"{hostname}{endpoint_login}", json=payload_login)
    data_response = response.json()
    access_token = data_response["token"]["accessToken"]
    return access_token


def get_user_me_data_status(access_token: str) -> tuple[Any, int]:
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    response = httpx.get(f"{hostname}{endpoint_get_user_me}", headers=headers)
    response_data = response.json()
    response_status = response.status_code
    return response_data, response_status


def main():
    response_data, response_status = get_user_me_data_status(get_token_login())
    print(response_data)
    print(response_status)


if __name__ == "__main__":
    main()
