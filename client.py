#!/usr/bin/env python3

import grpc
import CurrencyConverterService_pb2
import CurrencyConverterService_pb2_grpc


def run():
    with grpc.insecure_channel('localhost:8501') as channel:
        stub = CurrencyConverterService_pb2_grpc.CurrencyConverterServiceStub(channel)
        response = stub.getCurrencyCodes(CurrencyConverterService_pb2.CurrencyCodesRequest())
        print(response.currencyCodes)

        response = stub.getConvertedValue(CurrencyConverterService_pb2.ConvertValueRequest(
            current_value=100,
            current_currency_code='USD',
            expected_currency_code='EUR'
        ))
        print(response.rate)


if __name__ == '__main__':
    run()
