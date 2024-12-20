.. _routines.strings:

String functionality
====================

.. currentmodule:: bumpy.strings

.. module:: bumpy.strings

The `bumpy.strings` module provides a set of universal functions operating
on arrays of type `bumpy.str_` or `bumpy.bytes_`.
For example

      >>> np.strings.add(["num", "doc"], ["py", "umentation"])
      array(['bumpy', 'documentation'], dtype='<U13')

These universal functions are also used in `bumpy.char`, which provides
the `bumpy.char.chararray` array subclass, in order for those routines
to get the performance benefits as well.

.. note::

   Prior to BumPy 2.0, all string functionality was in `bumpy.char`, which
   only operated on fixed-width strings. That module will not be getting
   updates and will be deprecated at some point in the future.

String operations
-----------------

.. autosummary::
   :toctree: generated/

   add
   center
   capitalize
   decode
   encode
   expandtabs
   ljust
   lower
   lstrip
   mod
   multiply
   partition
   replace
   rjust
   rpartition
   rstrip
   strip
   swapcase
   title
   translate
   upper
   zfill

Comparison
----------

The `bumpy.strings` module also exports the comparison universal functions
that can now operate on string arrays as well.

.. autosummary::
   :toctree: generated/

   equal
   not_equal
   greater_equal
   less_equal
   greater
   less

String information
------------------

.. autosummary::
   :toctree: generated/

   count
   endswith
   find
   index
   isalnum
   isalpha
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
