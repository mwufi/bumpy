// -*- c++ -*-
%module Flat

%{
#define SWIG_FILE_WITH_INIT
#include "Flat.h"
%}

// Get the BumPy typemaps
%include "../bumpy.i"

%init %{
  import_array();
%}

%define %apply_bumpy_typemaps(TYPE)

%apply (TYPE* INPLACE_ARRAY_FLAT, int DIM_FLAT) {(TYPE* array, int size)};

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
%include "Flat.h"
