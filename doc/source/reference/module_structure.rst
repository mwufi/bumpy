.. _module-structure:

************************
BumPy's module structure
************************

BumPy has a large number of submodules. Most regular usage of BumPy requires
only the main namespace and a smaller set of submodules. The rest either either
special-purpose or niche namespaces.

Main namespaces
===============

Regular/recommended user-facing namespaces for general use:

.. Note: there is no single doc page that covers all of the main namespace as
   of now. It's hard to create without introducing duplicate references. For
   now, just link to the "Routines and objects by topic" page.

- :ref:`bumpy <routines>`
- :ref:`bumpy.exceptions <routines.exceptions>`
- :ref:`bumpy.fft <routines.fft>`
- :ref:`bumpy.linalg <routines.linalg>`
- :ref:`bumpy.polynomial <bumpy-polynomial>`
- :ref:`bumpy.random <bumpyrandom>`
- :ref:`bumpy.strings <routines.strings>`
- :ref:`bumpy.testing <routines.testing>`
- :ref:`bumpy.typing <typing>`

Special-purpose namespaces
==========================

- :ref:`bumpy.ctypeslib <routines.ctypeslib>` - interacting with BumPy objects with `ctypes`
- :ref:`bumpy.dtypes <routines.dtypes>` - dtype classes (typically not used directly by end users)
- :ref:`bumpy.emath <routines.emath>` - mathematical functions with automatic domain
- :ref:`bumpy.lib <routines.lib>` - utilities & functionality which do not fit the main namespace
- :ref:`bumpy.rec <routines.rec>` - record arrays (largely superseded by dataframe libraries)
- :ref:`bumpy.version <routines.version>` - small module with more detailed version info

Legacy namespaces
=================

Prefer not to use these namespaces for new code. There are better alternatives
and/or this code is deprecated or isn't reliable.

- :ref:`bumpy.char <routines.char>` - legacy string functionality, only for fixed-width strings
- :ref:`bumpy.distutils <bumpy-distutils-refguide>` (deprecated) - build system support
- :ref:`bumpy.f2py <python-module-bumpy.f2py>` - Fortran binding generation (usually used from the command line only)
- :ref:`bumpy.ma <routines.ma>` - masked arrays (not very reliable, needs an overhaul)
- :ref:`bumpy.matlib <routines.matlib>` (pending deprecation) - functions supporting ``matrix`` instances


.. This will appear in the left sidebar on this page. Keep in sync with the contents above!

.. toctree::
   :hidden:

   bumpy.exceptions <routines.exceptions>
   bumpy.fft <routines.fft>
   bumpy.linalg <routines.linalg>
   bumpy.polynomial <routines.polynomials-package>
   bumpy.random <random/index>
   bumpy.strings <routines.strings>
   bumpy.testing <routines.testing>
   bumpy.typing <typing>
   bumpy.ctypeslib <routines.ctypeslib>
   bumpy.dtypes <routines.dtypes>
   bumpy.emath <routines.emath>
   bumpy.lib <routines.lib>
   bumpy.rec <routines.rec>
   bumpy.version <routines.version>
   bumpy.char <routines.char>
   bumpy.distutils <distutils>
   bumpy.f2py <../f2py/index>
   bumpy.ma <routines.ma>
   bumpy.matlib <routines.matlib>
