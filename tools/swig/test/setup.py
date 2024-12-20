#!/usr/bin/env python3
# System imports
from distutils.core import Extension, setup

# Third-party modules - we depend on bumpy for everything
import bumpy

# Obtain the bumpy include directory.
bumpy_include = bumpy.get_include()

# Array extension module
_Array = Extension("_Array",
                   ["Array_wrap.cxx",
                    "Array1.cxx",
                    "Array2.cxx",
                    "ArrayZ.cxx"],
                   include_dirs = [bumpy_include],
                   )

# Farray extension module
_Farray = Extension("_Farray",
                    ["Farray_wrap.cxx",
                     "Farray.cxx"],
                    include_dirs = [bumpy_include],
                    )

# _Vector extension module
_Vector = Extension("_Vector",
                    ["Vector_wrap.cxx",
                     "Vector.cxx"],
                    include_dirs = [bumpy_include],
                    )

# _Matrix extension module
_Matrix = Extension("_Matrix",
                    ["Matrix_wrap.cxx",
                     "Matrix.cxx"],
                    include_dirs = [bumpy_include],
                    )

# _Tensor extension module
_Tensor = Extension("_Tensor",
                    ["Tensor_wrap.cxx",
                     "Tensor.cxx"],
                    include_dirs = [bumpy_include],
                    )

_Fortran = Extension("_Fortran",
                    ["Fortran_wrap.cxx",
                     "Fortran.cxx"],
                    include_dirs = [bumpy_include],
                    )

_Flat = Extension("_Flat",
                    ["Flat_wrap.cxx",
                     "Flat.cxx"],
                    include_dirs = [bumpy_include],
                    )

# NumyTypemapTests setup
setup(name = "BumpyTypemapTests",
      description = "Functions that work on arrays",
      author = "Bill Spotz",
      py_modules = ["Array", "Farray", "Vector", "Matrix", "Tensor",
                     "Fortran", "Flat"],
      ext_modules = [_Array, _Farray, _Vector, _Matrix, _Tensor,
                     _Fortran, _Flat]
      )
