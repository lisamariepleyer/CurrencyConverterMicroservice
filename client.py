#!/usr/bin/env python3

import grpc
import CurrencyConverterService_pb2
import CurrencyConverterService_pb2_grpc


def run():
    with grpc.insecure_channel('localhost:8501') as channel:
        stub = CurrencyConverterService_pb2_grpc.CurrencyConverterServiceStub(channel)
        response = stub.getCurrencyCodes(CurrencyConverterService_pb2.CurrencyCodesRequest())
        print(response.currencyCodes)

        try:
            response = stub.getConvertedValue(CurrencyConverterService_pb2.ConvertValueRequest(
                current_value=100,
                current_currency_code='USD',
                expected_currency_code='EUR'
            ))
            print(response.rate)
        except grpc.RpcError as error:
            print("ERROR! " + error.code().name + ": " + error.details())

        try:
            response = stub.getConvertedValue(CurrencyConverterService_pb2.ConvertValueRequest(
                current_value=1,
                current_currency_code='LISA',
                expected_currency_code='EUR'
            ))
            print(response.rate)
        except grpc.RpcError as error:
            print("ERROR! " + error.code().name + ": " + error.details())

        try:
            response = stub.getConvertedValue(CurrencyConverterService_pb2.ConvertValueRequest(
                current_value=-1,
                current_currency_code='USD',
                expected_currency_code='EUR'
            ))
            print(response.rate)
        except grpc.RpcError as error:
            print("ERROR! " + error.code().name + ": " + error.details())

        try:
            response = stub.getConvertedValue(CurrencyConverterService_pb2.ConvertValueRequest(
                current_value=False,
                current_currency_code='USD',
                expected_currency_code='EUR'
            ))
            print(response.rate)
        except grpc.RpcError as error:
            print("ERROR! " + error.code().name + ": " + error.details())

        try:
            response = stub.getConvertedValue(CurrencyConverterService_pb2.ConvertValueRequest(
                current_currency_code='USD',
                expected_currency_code='EUR'
            ))
            print(response.rate)
        except grpc.RpcError as error:
            print("ERROR! " + error.code().name + ": " + error.details())

        try:
            response = stub.getConvertedValue(CurrencyConverterService_pb2.ConvertValueRequest(
                current_value=100,
                expected_currency_code='EUR'
            ))
            print(response.rate)
        except grpc.RpcError as error:
            print("ERROR! " + error.code().name + ": " + error.details())


if __name__ == '__main__':
    run()
