.. _routines.ctypeslib:
.. module:: bumpy.ctypeslib

**********************************************************
ctypes foreign function interface (:mod:`bumpy.ctypeslib`)
**********************************************************

.. currentmodule:: bumpy.ctypeslib

.. autofunction:: as_array
.. autofunction:: as_ctypes
.. autofunction:: as_ctypes_type
.. autofunction:: load_library
.. autofunction:: ndpointer

.. class:: c_intp

    A `ctypes` signed integer type of the same size as `bumpy.intp`.

    Depending on the platform, it can be an alias for either `~ctypes.c_int`,
    `~ctypes.c_long` or `~ctypes.c_longlong`.
