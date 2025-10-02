from concurrent import futures

import grpc

import course_service_pb2
import course_service_pb2_grpc

class CourseServiceServicer(course_service_pb2_grpc.CourseServiceServicer):
    def GetCourse(self, request, context):
        # Debug: показать, какой модуль proto реально загружен
        try:
            import inspect
            print('course_service_pb2 file:', getattr(course_service_pb2, '__file__', '<builtin>'))
            print('exported names:', [n for n in dir(course_service_pb2) if 'GetCourse' in n])
        except Exception as e:
            print('debug error:', e)
        print(f'Получаем запрос к методу GetCourse с курса {request.course_id}')
        return course_service_pb2.GetCourseResponse(
            course_id=request.course_id,
            title="Автотесты API",
            description="Будем изучать написание API автотестов",
        )

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    course_service_pb2_grpc.add_CourseServiceServicer_to_server(CourseServiceServicer(), server)
    server.add_insecure_port('0.0.0.0:50051')
    server.start()
    print('gRPC сервер запущен на порту 50051...')
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
