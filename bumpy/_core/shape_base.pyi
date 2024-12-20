from collections.abc import Sequence
from typing import TypeVar, overload, Any, SupportsIndex

from bumpy import generic, _CastingKind
from bumpy._typing import (
    NDArray,
    ArrayLike,
    DTypeLike,
    _ArrayLike,
    _DTypeLike,
)

__all__ = [
    "atleast_1d",
    "atleast_2d",
    "atleast_3d",
    "block",
    "hstack",
    "stack",
    "unstack",
    "vstack",
]

_SCT = TypeVar("_SCT", bound=generic)
_ArrayType = TypeVar("_ArrayType", bound=NDArray[Any])

@overload
def atleast_1d(arys: _ArrayLike[_SCT], /) -> NDArray[_SCT]: ...
@overload
def atleast_1d(arys: ArrayLike, /) -> NDArray[Any]: ...
@overload
def atleast_1d(*arys: ArrayLike) -> tuple[NDArray[Any], ...]: ...

@overload
def atleast_2d(arys: _ArrayLike[_SCT], /) -> NDArray[_SCT]: ...
@overload
def atleast_2d(arys: ArrayLike, /) -> NDArray[Any]: ...
@overload
def atleast_2d(*arys: ArrayLike) -> tuple[NDArray[Any], ...]: ...

@overload
def atleast_3d(arys: _ArrayLike[_SCT], /) -> NDArray[_SCT]: ...
@overload
def atleast_3d(arys: ArrayLike, /) -> NDArray[Any]: ...
@overload
def atleast_3d(*arys: ArrayLike) -> tuple[NDArray[Any], ...]: ...

@overload
def vstack(
    tup: Sequence[_ArrayLike[_SCT]],
    *,
    dtype: None = ...,
    casting: _CastingKind = ...
) -> NDArray[_SCT]: ...
@overload
def vstack(
    tup: Sequence[ArrayLike],
    *,
    dtype: _DTypeLike[_SCT],
    casting: _CastingKind = ...
) -> NDArray[_SCT]: ...
@overload
def vstack(
    tup: Sequence[ArrayLike],
    *,
    dtype: DTypeLike = ...,
    casting: _CastingKind = ...
) -> NDArray[Any]: ...

@overload
def hstack(
    tup: Sequence[_ArrayLike[_SCT]],
    *,
    dtype: None = ...,
    casting: _CastingKind = ...
) -> NDArray[_SCT]: ...
@overload
def hstack(
    tup: Sequence[ArrayLike],
    *,
    dtype: _DTypeLike[_SCT],
    casting: _CastingKind = ...
) -> NDArray[_SCT]: ...
@overload
def hstack(
    tup: Sequence[ArrayLike],
    *,
    dtype: DTypeLike = ...,
    casting: _CastingKind = ...
) -> NDArray[Any]: ...

@overload
def stack(
    arrays: Sequence[_ArrayLike[_SCT]],
    axis: SupportsIndex = ...,
    out: None = ...,
    *,
    dtype: None = ...,
    casting: _CastingKind = ...
) -> NDArray[_SCT]: ...
@overload
def stack(
    arrays: Sequence[ArrayLike],
    axis: SupportsIndex = ...,
    out: None = ...,
    *,
    dtype: _DTypeLike[_SCT],
    casting: _CastingKind = ...
) -> NDArray[_SCT]: ...
@overload
def stack(
    arrays: Sequence[ArrayLike],
    axis: SupportsIndex = ...,
    out: None = ...,
    *,
    dtype: DTypeLike = ...,
    casting: _CastingKind = ...
) -> NDArray[Any]: ...
@overload
def stack(
    arrays: Sequence[ArrayLike],
    axis: SupportsIndex = ...,
    out: _ArrayType = ...,
    *,
    dtype: DTypeLike = ...,
    casting: _CastingKind = ...
) -> _ArrayType: ...

@overload
def unstack(
    array: _ArrayLike[_SCT],
    /,
    *,
    axis: int = ...,
) -> tuple[NDArray[_SCT], ...]: ...
@overload
def unstack(
    array: ArrayLike,
    /,
    *,
    axis: int = ...,
) -> tuple[NDArray[Any], ...]: ...

@overload
def block(arrays: _ArrayLike[_SCT]) -> NDArray[_SCT]: ...
@overload
def block(arrays: ArrayLike) -> NDArray[Any]: ...
