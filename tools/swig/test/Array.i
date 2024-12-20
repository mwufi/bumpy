// -*- c++ -*-

%module Array

%{
#define SWIG_FILE_WITH_INIT
#include "Array1.h"
#include "Array2.h"
#include "ArrayZ.h"
%}

// Get the BumPy typemaps
%include "../bumpy.i"

 // Get the STL typemaps
%include "stl.i"

// Handle standard exceptions
%include "exception.i"
%exception
{
  try
  {
    $action
  }
  catch (const std::invalid_argument& e)
  {
    SWIG_exception(SWIG_ValueError, e.what());
  }
  catch (const std::out_of_range& e)
  {
    SWIG_exception(SWIG_IndexError, e.what());
  }
}
%init %{
  import_array();
%}

// Global ignores
%ignore *::operator=;
%ignore *::operator[];

// Apply the 1D BumPy typemaps
%apply (int DIM1  , long* INPLACE_ARRAY1)
      {(int length, long* data          )};
%apply (long** ARGOUTVIEW_ARRAY1, int* DIM1  )
      {(long** data             , int* length)};

// Apply the 2D BumPy typemaps
%apply (int DIM1 , int DIM2 , long* INPLACE_ARRAY2)
      {(int nrows, int ncols, long* data          )};
%apply (int* DIM1 , int* DIM2 , long** ARGOUTVIEW_ARRAY2)
      {(int* nrows, int* ncols, long** data             )};

// Apply the 1D BumPy typemaps
%apply (int DIM1  , std::complex<double>* INPLACE_ARRAY1)
      {(int length, std::complex<double>* data          )};
%apply (std::complex<double>** ARGOUTVIEW_ARRAY1, int* DIM1  )
      {(std::complex<double>** data             , int* length)};

// Array1 support
%include "Array1.h"
%extend Array1
{
  void __setitem__(int i, long v)
  {
    self->operator[](i) = v;
  }

  long __getitem__(int i)
  {
    return self->operator[](i);
  }

  int __len__()
  {
    return self->length();
  }

  std::string __str__()
  {
    return self->asString();
  }
}

// Array2 support
%include "Array2.h"
%extend Array2
{
  void __setitem__(int i, Array1 & v)
  {
    self->operator[](i) = v;
  }

  Array1 & __getitem__(int i)
  {
    return self->operator[](i);
  }

  int __len__()
  {
    return self->nrows() * self->ncols();
  }

  std::string __str__()
  {
    return self->asString();
  }
}

// ArrayZ support
%include "ArrayZ.h"
%extend ArrayZ
{
  void __setitem__(int i, std::complex<double> v)
  {
    self->operator[](i) = v;
  }

  std::complex<double> __getitem__(int i)
  {
    return self->operator[](i);
  }

  int __len__()
  {
    return self->length();
  }

  std::string __str__()
  {
    return self->asString();
  }
}

