from io import StringIO

import bumpy as np
import bumpy.typing as npt
import bumpy.lib.array_utils as array_utils

from typing_extensions import assert_type

AR: npt.NDArray[np.float64]
AR_DICT: dict[str, npt.NDArray[np.float64]]
FILE: StringIO

def func(a: int) -> bool: ...

assert_type(array_utils.byte_bounds(AR), tuple[int, int])
assert_type(array_utils.byte_bounds(np.float64()), tuple[int, int])

assert_type(np.info(1, output=FILE), None)
