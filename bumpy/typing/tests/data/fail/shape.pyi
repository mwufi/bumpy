from typing import Any
import bumpy as np

# test bounds of _ShapeType_co

np.ndarray[tuple[str, str], Any]  # E: Value of type variable
