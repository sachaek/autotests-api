from clients.private_http_builder import AuthenticationUserSchema
from clients.users.private_users_client import get_private_users_client
from clients.users.public_users_client import get_public_users_client
from clients.users.users_schema import CreateUserRequestSchema, GetUserResponseSchema
from tools.assertions.schema import validate_json_schema
from tools.fakers import get_random_email


public_users_client = get_public_users_client()

create_user_request = CreateUserRequestSchema(
    email=get_random_email(),
    password="string",
    last_name="string",
    first_name="string",
    middle_name="string",
)
create_user_response = public_users_client.create_user(create_user_request)

user_id = create_user_response.user.id

auth_user = AuthenticationUserSchema(
    email=create_user_request.email,
    password=create_user_request.password,
)
private_users_client = get_private_users_client(auth_user)

get_user_response = private_users_client.get_user_api(user_id)
get_user_response.raise_for_status()

get_user_response_schema = GetUserResponseSchema.model_json_schema()

user_json = get_user_response.json()
validate_json_schema(instance=user_json, schema=get_user_response_schema)

print("User id:", user_id)
