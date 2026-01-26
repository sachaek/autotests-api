from httpx import Response

from clients.api_client import APIClient
from clients.private_http_builder import get_private_http_client, AuthenticationUserSchema
from clients.exercises.exercises_schema import GetExercisesQuerySchema, GetExercisesResponseSchema, GetExerciseResponseSchema, CreateExercisesRequestSchema, CreateExerciseResponseSchema, UpdateExercisesRequestSchema, UpdateExerciseResponseSchema

class ExercisesClient(APIClient):
    """
    Клиент для работы с /api/v1/exercises
    """
    def get_exercises_api(self, query: GetExercisesQuerySchema) -> Response:
        """
        Метод получения заданий по id курса
        :param query: Словарь с courseId
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get("/api/v1/exercises", params=query.model_dump(by_alias=True))

    def get_exercises(self, query: GetExercisesQuerySchema) -> GetExercisesResponseSchema:
        """
        Метод получения списка заданий по id курса.

        :param query: Словарь с courseId.
        :return: JSON-ответ от API, приведённый к GetExercisesResponseSchema.
        """
        response = self.get_exercises_api(query)
        return GetExercisesResponseSchema.model_validate_json(response.text)


    def get_exercise_api(self, exercise_id: str) -> GetExerciseResponseSchema:
        """
        Метод получения задания по id задания
        :param exercise_id: str : id задания    
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f"/api/v1/exercises/{exercise_id}")

    def get_exercise(self, exercise_id: str) -> GetExerciseResponseSchema:
        """
        Метод получения задания по id задания.

        :param exercise_id: str : id задания.
        :return: JSON-ответ от API, приведённый к GetExerciseResponseSchema.
        """
        response = self.get_exercise_api(exercise_id)
        # return response.json()
        return GetExerciseResponseSchema.model_validate_json(response.text)

    def create_exercise_api(self, request: CreateExercisesRequestSchema) -> Response:
        """
        Метод создания задания
        :param request: Словарь с title, courseId,
         maxScore, minScore, orderIndex, description, estimatedTime
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post("/api/v1/exercises", json=request.model_dump(by_alias=True))

    def create_exercise(self, request: CreateExercisesRequestSchema) -> CreateExerciseResponseSchema:
        """
        Метод создания задания.

        :param request: Словарь с title, courseId, maxScore, minScore,
         orderIndex, description, estimatedTime.
        :return: JSON-ответ от API, приведённый к CreateExerciseResponseDict.
        """
        response = self.create_exercise_api(request)
        # return response.json()
        return CreateExerciseResponseSchema.model_validate_json(response.text)

    def update_exercise_api(self,
                            exercise_id: str,
                            request: UpdateExercisesRequestSchema) -> Response:
        """
        Метод обновления задания.

        :param exercise_id: Идентификатор задания.
        :param request: Словарь с title, maxScore, minScore,
         orderIndex, description, estimatedTime.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.patch(f"/api/v1/exercises/{exercise_id}",
                          json=request.model_dump(by_alias=True))

    def update_exercise(self,
                        exercise_id: str,
                        request: UpdateExercisesRequestSchema) -> UpdateExerciseResponseSchema:
        """
        Метод обновления задания.

        :param exercise_id: Идентификатор задания.
        :param request: Словарь с title, maxScore, minScore,
         orderIndex, description, estimatedTime.
        :return: JSON-ответ от API, приведённый к UpdateExerciseResponseSchema.
        """
        response = self.update_exercise_api(exercise_id=exercise_id, request=request)
        return UpdateExerciseResponseSchema.model_validate_json(response.text)

    def delete_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод удаления задания.

        :param exercise_id: Идентификатор задания.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(f"/api/v1/exercises/{exercise_id}")


def get_exercises_client(user: AuthenticationUserSchema) -> ExercisesClient:
    """
    Фабрика клиента `ExercisesClient` с приватной (авторизованной) сессией.

    :param user: Данные пользователя для авторизации (email/password).
    :return: Экземпляр ExercisesClient.
    """
    return ExercisesClient(client=get_private_http_client(user))