#!/usr/bin/env python3

from concurrent import futures
import grpc
import CurrencyConverterService_pb2
import CurrencyConverterService_pb2_grpc

from BaseCurrencies import BaseCurrencies
from Converter import Converter


class CurrencyConverterServiceServicer(CurrencyConverterService_pb2_grpc.CurrencyConverterServiceServicer):
    def getCurrencyCodes(self, request, context):
        base_currencies = BaseCurrencies()
        currency_codes = base_currencies.getCurrencyRateDictionary().keys()
        return CurrencyConverterService_pb2.CurrencyCodesResponse(currencyCodes=currency_codes)

    def getConvertedValue(self, request, context):
        converter = Converter()

        if not request.current_value:
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            raise ValueError("Parameter current_value has incorrect type or is missing!")
        if not request.current_currency_code or not request.expected_currency_code:
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            raise ValueError("Currency code parameter is missing!")

        try:
            rate = converter.getConvertedValue(
                current_value=request.current_value,
                current_currency_code=request.current_currency_code,
                expected_currency_code=request.expected_currency_code
            )
            return CurrencyConverterService_pb2.ConvertValueResponse(rate=rate)
        except ValueError as value_error:
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            context.set_details(value_error.args[0])


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
