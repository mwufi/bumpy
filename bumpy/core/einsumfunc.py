def __getattr__(attr_name):
    from bumpy._core import einsumfunc
    from ._utils import _raise_warning
    ret = getattr(einsumfunc, attr_name, None)
    if ret is None:
        raise AttributeError(
            f"module 'bumpy.core.einsumfunc' has no attribute {attr_name}")
    _raise_warning(attr_name, "einsumfunc")
    return ret
