from pydantic import BaseModel, Field

from api_client_create_exercise import course_id


class ExerciseSchema(BaseModel):
    """
    Описание структуры задания (exercise), которое возвращает API.
    """
    id: str
    title: str
    course_id: str = Field(alias="courseId")
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    order_index: int = Field(alias="orderIndex")
    description: str 
    estimated_time: str = Field(alias="estimatedTime")



class GetExercisesResponseDict(BaseModel):
    """
    Описание структуры ответа при получении списка заданий.
    """
    exercises: list[ExerciseSchema]


class GetExerciseResponseDict(BaseModel):
    """
    Описание структуры ответа при получении одного задания.
    """
    exercise: ExerciseSchema


class GetExercisesQueryDict(BaseModel):
    """
    Описание структуры запроса на получение списка заданий.
    """
    course_id: str = Field(alias="courseId")


class CreateExercisesRequestDict(BaseModel):
    """
    Описание структуры запроса на создание задания.
    """
    title: str
    course_id: str = Field(alias="courseId")
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    order_index: int = Field(alias="orderIndex")
    description: str
    estimated_time: str = Field(alias="estimatedTime")


class CreateExerciseResponseDict(BaseModel):
    """
    Описание структуры ответа при создании задания.
    """
    exercise: ExerciseSchema


class UpdateExercisesRequestDict(BaseModel, total=False):
    """
    Описание структуры запроса на обновление задания.
    """
    title: str | None
    max_score: int | None = Field(alias="maxScore")
    min_score: int | None = Field(alias="minScore")
    order_index: int | None = Field(alias="orderIndex")
    description: str | None
    estimated_time: str | None = Field(alias="estimatedTime")


class UpdateExerciseResponseDict(BaseModel):
    """
    Описание структуры ответа при обновлении задания.
    """
    exercise: ExerciseSchema
