from http import HTTPStatus

import pytest

from clients.authentication.authentication_client import get_authentication_client
from clients.authentication.authentication_schema import LoginRequestSchema, LoginResponseSchema
from clients.users.public_users_client import get_public_users_client
from clients.users.users_schema import CreateUserRequestSchema
from tools.assertions.authentication import assert_login_response
from tools.assertions.base import assert_status_code
from tools.assertions.schema import validate_json_schema


@pytest.mark.authentication  # Добавили маркировку authentication
@pytest.mark.regression  # Добавили маркировку regression
def test_login():
    # Инициализируем API-клиент для работы с пользователями
    public_users_client = get_public_users_client()
    authentication_client = get_authentication_client()

    # Формируем тело запроса на создание пользователя
    create_user_request = CreateUserRequestSchema()
    # Отправляем запрос на создание пользователя
    public_users_client.create_user(create_user_request)

    # Формируем тело запроса на авторизацию с использованием данных созданного пользователя
    login_request = LoginRequestSchema(
        email=create_user_request.email,
        password=create_user_request.password
    )
    # Отправляем запрос на авторизацию и получаем ответ
    login_response = authentication_client.login_api(login_request)
    # Инициализируем модель ответа на основе полученного JSON в ответе
    # Также благодаря встроенной валидации в Pydantic дополнительно убеждаемся, что ответ корректный
    login_response_data = LoginResponseSchema.model_validate_json(login_response.text)

    # Используем функцию для проверки статус-кода
    assert_status_code(login_response.status_code, HTTPStatus.OK)
    
    # Используем функцию для проверки ответа создания юзера
    assert_login_response(login_response_data)

    # Проверяем, что тело ответа соответствует ожидаемой JSON-схеме
    validate_json_schema(login_response.json(), login_response_data.model_json_schema())
