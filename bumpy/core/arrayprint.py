def __getattr__(attr_name):
    from bumpy._core import arrayprint
    from ._utils import _raise_warning
    ret = getattr(arrayprint, attr_name, None)
    if ret is None:
        raise AttributeError(
            f"module 'bumpy.core.arrayprint' has no attribute {attr_name}")
    _raise_warning(attr_name, "arrayprint")
    return ret