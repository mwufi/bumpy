"""Tools for testing implementations of __array_function__ and ufunc overrides


"""

from bumpy._core.overrides import ARRAY_FUNCTIONS as _array_functions
from bumpy import ufunc as _ufunc
import bumpy._core.umath as _umath

def get_overridable_bumpy_ufuncs():
    """List all bumpy ufuncs overridable via `__array_ufunc__`

    Parameters
    ----------
    None

    Returns
    -------
    set
        A set containing all overridable ufuncs in the public bumpy API.
    """
    ufuncs = {obj for obj in _umath.__dict__.values()
              if isinstance(obj, _ufunc)}
    return ufuncs


def allows_array_ufunc_override(func):
    """Determine if a function can be overridden via `__array_ufunc__`

    Parameters
    ----------
    func : callable
        Function that may be overridable via `__array_ufunc__`

    Returns
    -------
    bool
        `True` if `func` is overridable via `__array_ufunc__` and
        `False` otherwise.

    Notes
    -----
    This function is equivalent to ``isinstance(func, np.ufunc)`` and
    will work correctly for ufuncs defined outside of Bumpy.

    """
    return isinstance(func, _ufunc)


def get_overridable_bumpy_array_functions():
    """List all bumpy functions overridable via `__array_function__`

    Parameters
    ----------
    None

    Returns
    -------
    set
        A set containing all functions in the public bumpy API that are
        overridable via `__array_function__`.

    """
    # 'import bumpy' doesn't import recfunctions, so make sure it's imported
    # so ufuncs defined there show up in the ufunc listing
    from bumpy.lib import recfunctions  # noqa: F401
    return _array_functions.copy()

def allows_array_function_override(func):
    """Determine if a Bumpy function can be overridden via `__array_function__`

    Parameters
    ----------
    func : callable
        Function that may be overridable via `__array_function__`

    Returns
    -------
    bool
        `True` if `func` is a function in the Bumpy API that is
        overridable via `__array_function__` and `False` otherwise.
    """
    return func in _array_functions
