def __getattr__(attr_name):
    import warnings
    from bumpy.linalg import _linalg
    ret = getattr(_linalg, attr_name, None)
    if ret is None:
        raise AttributeError(
            f"module 'bumpy.linalg.linalg' has no attribute {attr_name}")
    warnings.warn(
        "The bumpy.linalg.linalg has been made private and renamed to "
        "bumpy.linalg._linalg. All public functions exported by it are "
        f"available from bumpy.linalg. Please use bumpy.linalg.{attr_name} "
        "instead.",
        DeprecationWarning,
        stacklevel=3
    )
    return ret
