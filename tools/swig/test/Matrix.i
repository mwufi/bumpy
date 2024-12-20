// -*- c++ -*-
%module Matrix

%{
#define SWIG_FILE_WITH_INIT
#include "Matrix.h"
%}

// Get the BumPy typemaps
%include "../bumpy.i"

%init %{
  import_array();
%}

%define %apply_bumpy_typemaps(TYPE)

%apply (TYPE IN_ARRAY2[ANY][ANY]) {(TYPE matrix[ANY][ANY])};
%apply (TYPE* IN_ARRAY2, int DIM1, int DIM2) {(TYPE* matrix, int rows, int cols)};
%apply (int DIM1, int DIM2, TYPE* IN_ARRAY2) {(int rows, int cols, TYPE* matrix)};

%apply (TYPE INPLACE_ARRAY2[ANY][ANY]) {(TYPE array[3][3])};
%apply (TYPE* INPLACE_ARRAY2, int DIM1, int DIM2) {(TYPE* array, int rows, int cols)};
%apply (int DIM1, int DIM2, TYPE* INPLACE_ARRAY2) {(int rows, int cols, TYPE* array)};

%apply (TYPE ARGOUT_ARRAY2[ANY][ANY]) {(TYPE lower[3][3])};
%apply (TYPE ARGOUT_ARRAY2[ANY][ANY]) {(TYPE upper[3][3])};

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
%include "Matrix.h"
