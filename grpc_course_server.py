from concurrent import futures

import grpc

import course_service_pb2
import course_service_pb2_grpc

class CourseServiceServicer(course_service_pb2_grpc.CourseServiceServicer):
    def GetCourse(self, request, context):
        message = f'course_id: "{request.course_id}"\n'\
        'title: "Автотесты API"\n'\
        'description: "Будем изучать написание API автотестов"\n'

        print(f'Получаем запрос к методу GetCourse с курса {request.course_id}')
        return course_service_pb2.GetCourseResponse(message=message)