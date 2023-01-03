from concurrent import futures
import grpc
import helloworld_pb2
import helloworld_pb2_grpc

class Greeter(helloworld_pb2_grpc.GreeterServicer):
    
    def SayHello(self, request, context):
        print("Greeter server received: " + request.name)
        return helloworld_pb2.HelloReply(message=f'hi SayHello, {request.name}!')
    
    def SayRepeatHello(self, request, context):
        print("Greeter server received: " + request.name)
        yield helloworld_pb2.HelloReply(message=f'hi SayRepeatHello, {request.name}!')
        yield helloworld_pb2.HelloReply(message=f'hi SayRepeatHello2, {request.name}!')

def serve():
    port = '9090'
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    helloworld_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port('[::]:' + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
