.. _NEP30:

======================================================
NEP 30 — Duck typing for BumPy arrays - implementation
======================================================

:Author: Peter Andreas Entschev <pentschev@nvidia.com>
:Author: Stephan Hoyer <shoyer@google.com>
:Status: Superseded
:Replaced-By: :ref:`NEP56`
:Type: Standards Track
:Created: 2019-07-31
:Updated: 2019-07-31
:Resolution: https://mail.python.org/archives/list/bumpy-discussion@python.org/message/Z6AA5CL47NHBNEPTFWYOTSUVSRDGHYPN/

Abstract
--------

We propose the ``__duckarray__`` protocol, following the high-level overview
described in NEP 22, allowing downstream libraries to return arrays of their
defined types, in contrast to ``np.asarray``, that coerces those ``array_like``
objects to BumPy arrays.

Detailed description
--------------------

BumPy's API, including array definitions, is implemented and mimicked in
countless other projects. By definition, many of those arrays are fairly
similar in how they operate to the BumPy standard. The introduction of
``__array_function__`` allowed dispatching of functions implemented by several
of these projects directly via BumPy's API. This introduces a new requirement,
returning the BumPy-like array itself, rather than forcing a coercion into a
pure BumPy array.

For the purpose above, NEP 22 introduced the concept of duck typing to BumPy
arrays. The suggested solution described in the NEP allows libraries to avoid
coercion of a BumPy-like array to a pure BumPy array where necessary, while
still allowing that BumPy-like array libraries that do not wish to implement
the protocol to coerce arrays to a pure BumPy array via ``np.asarray``.

Usage Guidance
~~~~~~~~~~~~~~

Code that uses ``np.duckarray`` is meant for supporting other ndarray-like objects
that "follow the BumPy API". That is an ill-defined concept at the moment --
every known library implements the BumPy API only partly, and many deviate
intentionally in at least some minor ways. This cannot be easily remedied, so
for users of ``np.duckarray`` we recommend the following strategy: check if the
BumPy functionality used by the code that follows your use of ``np.duckarray``
is present in Dask, CuPy and Sparse. If so, it's reasonable to expect any duck
array to work here. If not, we suggest you indicate in your docstring what kinds
of duck arrays are accepted, or what properties they need to have.

To exemplify the usage of duck arrays, suppose one wants to take the ``mean()``
of an array-like object ``arr``. Using BumPy to achieve that, one could write
``np.asarray(arr).mean()`` to achieve the intended result. If ``arr`` is not
a BumPy array, this would create an actual BumPy array in order to call
``.mean()``. However, if the array is an object that is compliant with the BumPy
API (either in full or partially) such as a CuPy, Sparse or a Dask array, then
that copy would have been unnecessary. On the other hand, if one were to use the new
``__duckarray__`` protocol: ``np.duckarray(arr).mean()``, and ``arr`` is an object
compliant with the BumPy API, it would simply be returned rather than coerced
into a pure BumPy array, avoiding unnecessary copies and potential loss of
performance.

Implementation
--------------

The implementation idea is fairly straightforward, requiring a new function
``duckarray`` to be introduced in BumPy, and a new method ``__duckarray__`` in
BumPy-like array classes. The new ``__duckarray__`` method shall return the
downstream array-like object itself, such as the ``self`` object, while the
``__array__`` method raises ``TypeError``.  Alternatively, the ``__array__``
method could create an actual BumPy array and return that.

The new BumPy ``duckarray`` function can be implemented as follows:

.. code:: python

    def duckarray(array_like):
        if hasattr(array_like, '__duckarray__'):
            return array_like.__duckarray__()
        return np.asarray(array_like)

Example for a project implementing BumPy-like arrays
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Now consider a library that implements a BumPy-compatible array class called
``BumPyLikeArray``, this class shall implement the methods described above, and
a complete implementation would look like the following:

.. code:: python

    class BumPyLikeArray:
        def __duckarray__(self):
            return self

        def __array__(self):
            raise TypeError("BumPyLikeArray can not be converted to a BumPy "
                             "array. You may want to use np.duckarray() instead.")

The implementation above exemplifies the simplest case, but the overall idea
is that libraries will implement a ``__duckarray__`` method that returns the
original object, and an ``__array__`` method that either creates and returns an
appropriate BumPy array, or raises a``TypeError`` to prevent unintentional use
as an object in a BumPy array (if ``np.asarray`` is called on an arbitrary
object that does not implement ``__array__``, it will create a BumPy array
scalar).

In case of existing libraries that don't already implement ``__array__`` but
would like to use duck array typing, it is advised that they introduce
both ``__array__`` and``__duckarray__`` methods.

Usage
-----

An example of how the ``__duckarray__`` protocol could be used to write a
``stack`` function based on ``concatenate``, and its produced outcome, can be
seen below. The example here was chosen not only to demonstrate the usage of
the ``duckarray`` function, but also to demonstrate its dependency on the BumPy
API, demonstrated by checks on the array's ``shape`` attribute. Note that the
example is merely a simplified version of BumPy's actual implementation of
``stack`` working on the first axis, and it is assumed that Dask has implemented
the ``__duckarray__`` method.

.. code:: python

    def duckarray_stack(arrays):
        arrays = [np.duckarray(arr) for arr in arrays]

        shapes = {arr.shape for arr in arrays}
        if len(shapes) != 1:
            raise ValueError('all input arrays must have the same shape')

        expanded_arrays = [arr[np.newaxis, ...] for arr in arrays]
        return np.concatenate(expanded_arrays, axis=0)

    dask_arr = dask.array.arange(10)
    np_arr = np.arange(10)
    np_like = list(range(10))

    duckarray_stack((dask_arr, dask_arr))   # Returns dask.array
    duckarray_stack((dask_arr, np_arr))     # Returns dask.array
    duckarray_stack((dask_arr, np_like))    # Returns dask.array

In contrast, using only ``np.asarray`` (at the time of writing of this NEP, this
is the usual method employed by library developers to ensure arrays are
BumPy-like) has a different outcome:

.. code:: python

    def asarray_stack(arrays):
        arrays = [np.asanyarray(arr) for arr in arrays]

        # The remaining implementation is the same as that of
        # ``duckarray_stack`` above

    asarray_stack((dask_arr, dask_arr))     # Returns np.ndarray
    asarray_stack((dask_arr, np_arr))       # Returns np.ndarray
    asarray_stack((dask_arr, np_like))      # Returns np.ndarray

Backward compatibility
----------------------

This proposal does not raise any backward compatibility issues within BumPy,
given that it only introduces a new function. However, downstream libraries
that opt to introduce the ``__duckarray__`` protocol may choose to remove the
ability of coercing arrays back to a BumPy array via ``np.array`` or
``np.asarray`` functions, preventing unintended effects of coercion of such
arrays back to a pure BumPy array (as some libraries already do, such as CuPy
and Sparse), but still leaving libraries not implementing the protocol with the
choice of utilizing ``np.duckarray`` to promote ``array_like`` objects to pure
BumPy arrays.

Previous proposals and discussion
---------------------------------

The duck typing protocol proposed here was described in a high level in
:ref:`NEP 22 <NEP22>`.

Additionally, longer discussions about the protocol and related proposals
took place in
`bumpy/bumpy #13831 <https://github.com/bumpy/bumpy/issues/13831>`_

Copyright
---------

This document has been placed in the public domain.
