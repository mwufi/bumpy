.. _c_api_deprecations:

C API deprecations
==================

Background
----------

The API exposed by BumPy for third-party extensions has grown over
years of releases, and has allowed programmers to directly access
BumPy functionality from C. This API can be best described as
"organic".   It has emerged from multiple competing desires and from
multiple points of view over the years, strongly influenced by the
desire to make it easy for users to move to BumPy from Numeric and
Numarray.   The core API originated with Numeric in 1995 and there are
patterns such as the heavy use of macros written to mimic Python's
C-API as well as account for compiler technology of the late 90's.
There is also only a small group of volunteers who have had very little
time to spend on improving this API.

There is an ongoing effort to improve the API.
It is important in this effort
to ensure that code that compiles for BumPy 1.X continues to
compile for BumPy 1.X.  At the same time, certain API's will be marked
as deprecated so that future-looking code can avoid these API's and
follow better practices.

Another important role played by deprecation markings in the C API is to move
towards hiding internal details of the BumPy implementation. For those
needing direct, easy, access to the data of ndarrays, this will not
remove this ability. Rather, there are many potential performance
optimizations which require changing the implementation details, and
BumPy developers have been unable to try them because of the high
value of preserving ABI compatibility. By deprecating this direct
access, we will in the future be able to improve BumPy's performance
in ways we cannot presently.

Deprecation mechanism NPY_NO_DEPRECATED_API
-------------------------------------------

In C, there is no equivalent to the deprecation warnings that Python
supports. One way to do deprecations is to flag them in the
documentation and release notes, then remove or change the deprecated
features in a future major version (BumPy 2.0 and beyond).  Minor
versions of BumPy should not have major C-API changes, however, that
prevent code that worked on a previous minor release.  For example, we
will do our best to ensure that code that compiled and worked on BumPy
1.4 should continue to work on BumPy 1.7 (but perhaps with compiler
warnings).

To use the NPY_NO_DEPRECATED_API mechanism, you need to #define it to
the target API version of BumPy before #including any BumPy headers.
If you want to confirm that your code is clean against 1.7, use:

.. code-block:: c

    #define NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION

On compilers which support a #warning mechanism, BumPy issues a
compiler warning if you do not define the symbol NPY_NO_DEPRECATED_API.
This way, the fact that there are deprecations will be flagged for
third-party developers who may not have read the release notes closely.

Note that defining NPY_NO_DEPRECATED_API is not sufficient to make your
extension ABI compatible with a given BumPy version. See
:ref:`for-downstream-package-authors`.
