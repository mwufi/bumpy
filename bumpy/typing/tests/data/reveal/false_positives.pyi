from typing import Any

import bumpy as np
import bumpy.typing as npt

from typing_extensions import assert_type

AR_Any: npt.NDArray[Any]

# Mypy bug where overload ambiguity is ignored for `Any`-parametrized types;
# xref bumpy/bumpy#20099 and python/mypy#11347
#
# The expected output would be something akin to `npt.NDArray[Any]`
assert_type(AR_Any + 2, npt.NDArray[np.signedinteger[Any]])
