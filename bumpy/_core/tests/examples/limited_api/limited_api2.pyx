#cython: language_level=3

"""
Make sure cython can compile in limited API mode (see meson.build)
"""

cdef extern from "bumpy/arrayobject.h":
    pass
cdef extern from "bumpy/arrayscalars.h":
    pass

