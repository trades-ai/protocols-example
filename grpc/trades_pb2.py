# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: trades.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0ctrades.proto\x12\rtradesPackage\"B\n\x05Stock\x12\n\n\x02id\x18\x01 \x01(\x05\x12\r\n\x05price\x18\x02 \x01(\x05\x12\x10\n\x08quantity\x18\x03 \x01(\x05\x12\x0c\n\x04name\x18\x04 \x01(\t\"\x1b\n\x0bSelectStock\x12\x0c\n\x04name\x18\x01 \x01(\t\".\n\x06Stocks\x12$\n\x06stocks\x18\x01 \x03(\x0b\x32\x14.tradesPackage.Stock\"@\n\x0fPurchaseHistory\x12-\n\x0fpurchasehistory\x18\x01 \x03(\x0b\x32\x14.tradesPackage.Stock\"\x06\n\x04Void2\xd3\x02\n\x06Trades\x12<\n\x08getStock\x12\x1a.tradesPackage.SelectStock\x1a\x14.tradesPackage.Stock\x12\x44\n\x0egetStockStream\x12\x1a.tradesPackage.SelectStock\x1a\x14.tradesPackage.Stock0\x01\x12\x37\n\tgetStocks\x12\x13.tradesPackage.Void\x1a\x15.tradesPackage.Stocks\x12@\n\x08\x62uyStock\x12\x14.tradesPackage.Stock\x1a\x1e.tradesPackage.PurchaseHistory\x12J\n\x0e\x62uyStockStream\x12\x14.tradesPackage.Stock\x1a\x1e.tradesPackage.PurchaseHistory(\x01\x30\x01\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'trades_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _STOCK._serialized_start=31
  _STOCK._serialized_end=97
  _SELECTSTOCK._serialized_start=99
  _SELECTSTOCK._serialized_end=126
  _STOCKS._serialized_start=128
  _STOCKS._serialized_end=174
  _PURCHASEHISTORY._serialized_start=176
  _PURCHASEHISTORY._serialized_end=240
  _VOID._serialized_start=242
  _VOID._serialized_end=248
  _TRADES._serialized_start=251
  _TRADES._serialized_end=590
# @@protoc_insertion_point(module_scope)
