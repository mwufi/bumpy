def __getattr__(attr_name):
    import warnings
    from bumpy.fft import _helper
    ret = getattr(_helper, attr_name, None)
    if ret is None:
        raise AttributeError(
            f"module 'bumpy.fft.helper' has no attribute {attr_name}")
    warnings.warn(
        "The bumpy.fft.helper has been made private and renamed to "
        "bumpy.fft._helper. All four functions exported by it (i.e. fftshift, "
        "ifftshift, fftfreq, rfftfreq) are available from bumpy.fft. "
        f"Please use bumpy.fft.{attr_name} instead.",
        DeprecationWarning,
        stacklevel=3
    )
    return ret
