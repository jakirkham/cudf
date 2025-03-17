# Copyright (c) 2024, NVIDIA CORPORATION.
from collections.abc import Mapping
from typing import TypeAlias

from typing_extensions import Self

from rmm.pylibrmm.stream import Stream

from pylibcudf.column import Column
from pylibcudf.io.types import (
    CompressionType,
    JSONRecoveryMode,
    SinkInfo,
    SourceInfo,
    TableWithMetadata,
)
from pylibcudf.table import Table
from pylibcudf.types import DataType

ChildNameToTypeMap: TypeAlias = Mapping[str, ChildNameToTypeMap]

NameAndType: TypeAlias = tuple[str, DataType, list[NameAndType]]

class JsonReaderOptions:
    def set_dtypes(
        self, types: list[DataType] | list[NameAndType]
    ) -> None: ...
    def enable_keep_quotes(self, keep_quotes: bool) -> None: ...
    def enable_mixed_types_as_string(
        self, mixed_types_as_string: bool
    ) -> None: ...
    def enable_prune_columns(self, prune_columns: bool) -> None: ...
    def set_byte_range_offset(self, offset: int) -> None: ...
    def set_byte_range_size(self, size: int) -> None: ...
    def enable_lines(self, val: bool) -> None: ...
    def set_delimiter(self, val: str) -> None: ...
    def enable_dayfirst(self, val: bool) -> None: ...
    def enable_experimental(self, val: bool) -> None: ...
    def enable_normalize_single_quotes(self, val: bool) -> None: ...
    def enable_normalize_whitespace(self, val: bool) -> None: ...
    def set_strict_validation(self, val: bool) -> None: ...
    def allow_unquoted_control_chars(self, val: bool) -> None: ...
    def allow_numeric_leading_zeros(self, val: bool) -> None: ...
    def allow_nonnumeric_numbers(self, val: bool) -> None: ...
    def set_na_values(self, vals: list[str]) -> None: ...
    @staticmethod
    def builder(source: SourceInfo) -> JsonReaderOptionsBuilder: ...

class JsonReaderOptionsBuilder:
    def byte_range_offset(self, byte_range_offset: int) -> Self: ...
    def byte_range_size(self, byte_range_size: int) -> Self: ...
    def compression(self, compression_type: CompressionType) -> Self: ...
    def dayfirst(self, val: bool) -> Self: ...
    def delimiter(self, delimiter: str) -> Self: ...
    def dtypes(self, types: list) -> Self: ...
    def experimental(self, val: bool) -> Self: ...
    def keep_quotes(self, val: bool) -> Self: ...
    def lines(self, val: bool) -> Self: ...
    def mixed_types_as_string(self, val: bool) -> Self: ...
    def na_values(self, vals: list) -> Self: ...
    def nonnumeric_numbers(self, val: bool) -> Self: ...
    def normalize_single_quotes(self, val: bool) -> Self: ...
    def normalize_whitespace(self, val: bool) -> Self: ...
    def numeric_leading_zeros(self, val: bool) -> Self: ...
    def prune_columns(self, val: bool) -> Self: ...
    def recovery_mode(self, recovery_mode: JSONRecoveryMode) -> Self: ...
    def strict_validation(self, val: bool) -> Self: ...
    def unquoted_control_chars(self, val: bool) -> Self: ...
    def build(self) -> JsonReaderOptions: ...

def read_json(
    options: JsonReaderOptions, stream: Stream = None
) -> TableWithMetadata: ...

class JsonWriterOptions:
    @staticmethod
    def builder(sink: SinkInfo, table: Table) -> JsonWriterOptionsBuilder: ...
    def set_rows_per_chunk(self, val: int) -> None: ...
    def set_true_value(self, val: str) -> None: ...
    def set_false_value(self, val: str) -> None: ...
    def set_compression(self, comptype: CompressionType) -> None: ...

class JsonWriterOptionsBuilder:
    def metadata(self, tbl_w_meta: TableWithMetadata) -> Self: ...
    def na_rep(self, val: str) -> Self: ...
    def include_nulls(self, val: bool) -> Self: ...
    def lines(self, val: bool) -> Self: ...
    def compression(self, comptype: CompressionType) -> Self: ...
    def build(self) -> JsonWriterOptions: ...

def write_json(options: JsonWriterOptions, stream: Stream = None) -> None: ...
def chunked_read_json(
    options: JsonReaderOptions,
    chunk_size: int = 100_000_000,
    stream: Stream = None,
) -> tuple[list[Column], list[str], ChildNameToTypeMap]: ...
