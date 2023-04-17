#!/usr/bin/env python3

from concurrent import futures
import grpc
import CurrencyConverterService_pb2
import CurrencyConverterService_pb2_grpc

from BaseCurrencies import BaseCurrencies


class CurrencyConverterServiceServicer(CurrencyConverterService_pb2_grpc.CurrencyConverterServiceServicer):
    def getCurrencyCodes(self, request, context):
        base_currencies = BaseCurrencies()
        currency_codes = base_currencies.getCurrencyRateDictionary().keys()
        return CurrencyConverterService_pb2.CurrencyCodesResponse(currencyCodes=currency_codes)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    CurrencyConverterService_pb2_grpc.add_CurrencyConverterServiceServicer_to_server(
        CurrencyConverterServiceServicer(),
        server
    )
    server.add_insecure_port('[::]:8501')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
