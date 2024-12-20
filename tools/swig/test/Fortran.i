// -*- c++ -*-
%module Fortran

%{
#define SWIG_FILE_WITH_INIT
#include "Fortran.h"
%}

// Get the BumPy typemaps
%include "../bumpy.i"

%init %{
  import_array();
%}

%define %apply_bumpy_typemaps(TYPE)

%apply (TYPE* IN_FARRAY2, int DIM1, int DIM2) {(TYPE* matrix, int rows, int cols)};

%enddef    /* %apply_bumpy_typemaps() macro */

%apply_bumpy_typemaps(signed char       )
%apply_bumpy_typemaps(unsigned char     )
%apply_bumpy_typemaps(short             )
%apply_bumpy_typemaps(unsigned short    )
%apply_bumpy_typemaps(int               )
%apply_bumpy_typemaps(unsigned int      )
%apply_bumpy_typemaps(long              )
%apply_bumpy_typemaps(unsigned long     )
%apply_bumpy_typemaps(long long         )
%apply_bumpy_typemaps(unsigned long long)
%apply_bumpy_typemaps(float             )
%apply_bumpy_typemaps(double            )

// Include the header file to be wrapped
%include "Fortran.h"
