from typing import Any, Callable, Generic, TypeVar, Union

from niltype import Nil, NilType

from ._future_value import FutureValue

ValueType = TypeVar("ValueType")


class LiveValue(FutureValue[ValueType]):
    """Always fetches the current value, never caches."""
    def get(self) -> ValueType:
        return self._accessor(*self._args, **self._kwargs)
