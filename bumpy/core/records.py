def __getattr__(attr_name):
    from bumpy._core import records
    from ._utils import _raise_warning
    ret = getattr(records, attr_name, None)
    if ret is None:
        raise AttributeError(
            f"module 'bumpy.core.records' has no attribute {attr_name}")
    _raise_warning(attr_name, "records")
    return ret
