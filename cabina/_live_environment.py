import os
from functools import partial
from typing import Any, Callable, Dict, Mapping, Tuple, Union, cast

from niltype import Nil, NilType

from . import LazyEnvironment
from . import LiveValue
from ._future_value import FutureValue, ValueType
from .errors import EnvKeyError
from .parsers import (
    parse_as_is,
    parse_bool,
    parse_float,
    parse_int,
    parse_none,
    parse_str,
    parse_tuple,
)

class LiveEnvironment(LazyEnvironment):
    """LazyEnvironment variant that returns live reads, not cached ones."""
    def raw(
        self,
        name: str,
        default: Union[NilType, ValueType] = Nil,
        parser: Callable[[str], ValueType] = parse_as_is,
    ) -> ValueType:
        return LiveValue(self.get, name, default=default, parser=parser)
