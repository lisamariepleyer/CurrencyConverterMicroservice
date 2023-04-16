#!/usr/bin/env python3

from concurrent import futures
import grpc
import CurrencyConverterService_pb2
import CurrencyConverterService_pb2_grpc


class CurrencyConverterServiceServicer(CurrencyConverterService_pb2_grpc.CurrencyConverterServiceServicer):
    def getCurrencyCodes(self, request, context):
        message = 'Hi!'
        return CurrencyConverterService_pb2.CurrencyCodesResponse(message=message)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    CurrencyConverterService_pb2_grpc.add_CurrencyConverterServiceServicer_to_server(CurrencyConverterServiceServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()