def __getattr__(attr_name):
    from bumpy._core import numerictypes
    from ._utils import _raise_warning
    ret = getattr(numerictypes, attr_name, None)
    if ret is None:
        raise AttributeError(
            f"module 'bumpy.core.numerictypes' has no attribute {attr_name}")
    _raise_warning(attr_name, "numerictypes")
    return ret
