# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: CurrencyConverterService.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1e\x43urrencyConverterService.proto\x12\x18\x43urrencyConverterService\"\x16\n\x14\x43urrencyCodesRequest\".\n\x15\x43urrencyCodesResponse\x12\x15\n\rcurrencyCodes\x18\x01 \x03(\t\"k\n\x13\x43onvertValueRequest\x12\x15\n\rcurrent_value\x18\x01 \x01(\x02\x12\x1d\n\x15\x63urrent_currency_code\x18\x02 \x01(\t\x12\x1e\n\x16\x65xpected_currency_code\x18\x03 \x01(\t\"$\n\x14\x43onvertValueResponse\x12\x0c\n\x04rate\x18\x01 \x01(\x02\x32\x87\x02\n\x18\x43urrencyConverterService\x12u\n\x10getCurrencyCodes\x12..CurrencyConverterService.CurrencyCodesRequest\x1a/.CurrencyConverterService.CurrencyCodesResponse\"\x00\x12t\n\x11getConvertedValue\x12-.CurrencyConverterService.ConvertValueRequest\x1a..CurrencyConverterService.ConvertValueResponse\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'CurrencyConverterService_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _CURRENCYCODESREQUEST._serialized_start=60
  _CURRENCYCODESREQUEST._serialized_end=82
  _CURRENCYCODESRESPONSE._serialized_start=84
  _CURRENCYCODESRESPONSE._serialized_end=130
  _CONVERTVALUEREQUEST._serialized_start=132
  _CONVERTVALUEREQUEST._serialized_end=239
  _CONVERTVALUERESPONSE._serialized_start=241
  _CONVERTVALUERESPONSE._serialized_end=277
  _CURRENCYCONVERTERSERVICE._serialized_start=280
  _CURRENCYCONVERTERSERVICE._serialized_end=543
# @@protoc_insertion_point(module_scope)
