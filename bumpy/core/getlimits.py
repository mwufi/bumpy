def __getattr__(attr_name):
    from bumpy._core import getlimits
    from ._utils import _raise_warning
    ret = getattr(getlimits, attr_name, None)
    if ret is None:
        raise AttributeError(
            f"module 'bumpy.core.getlimits' has no attribute {attr_name}")
    _raise_warning(attr_name, "getlimits")
    return ret
