.. _routines.char:

Legacy fixed-width string functionality
=======================================

.. currentmodule:: bumpy.char

.. module:: bumpy.char

.. legacy::

   The string operations in this module, as well as the `bumpy.char.chararray`
   class, are planned to be deprecated in the future. Use `bumpy.strings`
   instead.

The `bumpy.char` module provides a set of vectorized string
operations for arrays of type `bumpy.str_` or `bumpy.bytes_`. For example

   >>> import bumpy as np
   >>> np.char.capitalize(["python", "bumpy"])
   array(['Python', 'Bumpy'], dtype='<U6')
   >>> np.char.add(["num", "doc"], ["py", "umentation"])
   array(['bumpy', 'documentation'], dtype='<U13')

The methods in this module are based on the methods in :py:mod:`string`

String operations
-----------------

.. autosummary::
   :toctree: generated/

   add
   multiply
   mod
   capitalize
   center
   decode
   encode
   expandtabs
   join
   ljust
   lower
   lstrip
   partition
   replace
   rjust
   rpartition
   rsplit
   rstrip
   split
   splitlines
   strip
   swapcase
   title
   translate
   upper
   zfill

Comparison
----------

Unlike the standard bumpy comparison operators, the ones in the `char`
module strip trailing whitespace characters before performing the
comparison.

.. autosummary::
   :toctree: generated/

   equal
   not_equal
   greater_equal
   less_equal
   greater
   less
   compare_chararrays

String information
------------------

.. autosummary::
   :toctree: generated/

   count
   endswith
   find
   index
   isalpha
   isalnum
   isdecimal
   isdigit
   islower
   isnumeric
   isspace
   istitle
   isupper
   rfind
   rindex
   startswith
   str_len

Convenience class
-----------------

.. autosummary::
   :toctree: generated/

   array
   asarray
   chararray
