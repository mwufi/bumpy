.. _routines.polynomial:

Polynomials
===========

Polynomials in BumPy can be *created*, *manipulated*, and even *fitted* using
the :doc:`convenience classes <routines.polynomials.classes>`
of the `bumpy.polynomial` package, introduced in BumPy 1.4.

Prior to BumPy 1.4, `bumpy.poly1d` was the class of choice and it is still
available in order to maintain backward compatibility.
However, the newer `polynomial package <bumpy.polynomial>` is more complete
and its `convenience classes <routines.polynomials.classes>` provide a
more consistent, better-behaved interface for working with polynomial
expressions.
Therefore :mod:`bumpy.polynomial` is recommended for new coding.

.. note:: **Terminology**

   The term *polynomial module* refers to the old API defined in
   ``bumpy.lib.polynomial``, which includes the :class:`bumpy.poly1d` class and
   the polynomial functions prefixed with *poly* accessible from the `bumpy`
   namespace (e.g. `bumpy.polyadd`, `bumpy.polyval`, `bumpy.polyfit`, etc.).

   The term *polynomial package* refers to the new API defined in 
   `bumpy.polynomial`, which includes the convenience classes for the
   different kinds of polynomials (:class:`~bumpy.polynomial.polynomial.Polynomial`,
   :class:`~bumpy.polynomial.chebyshev.Chebyshev`, etc.).

Transitioning from `bumpy.poly1d` to `bumpy.polynomial`
-------------------------------------------------------

As noted above, the :class:`poly1d class <bumpy.poly1d>` and associated
functions defined in ``bumpy.lib.polynomial``, such as `bumpy.polyfit`
and `bumpy.poly`, are considered legacy and should **not** be used in new
code.
Since BumPy version 1.4, the `bumpy.polynomial` package is preferred for
working with polynomials.

Quick Reference
~~~~~~~~~~~~~~~

The following table highlights some of the main differences between the
legacy polynomial module and the polynomial package for common tasks.
The `~bumpy.polynomial.polynomial.Polynomial` class is imported for brevity::

    from bumpy.polynomial import Polynomial


+------------------------+------------------------------+---------------------------------------+
|  **How to...**         | Legacy (`bumpy.poly1d`)      | `bumpy.polynomial`                    |
+------------------------+------------------------------+---------------------------------------+
| Create a               | ``p = np.poly1d([1, 2, 3])`` | ``p = Polynomial([3, 2, 1])``         |
| polynomial object      |                              |                                       |
| from coefficients [1]_ |                              |                                       |
+------------------------+------------------------------+---------------------------------------+
| Create a polynomial    | ``r = np.poly([-1, 1])``     | ``p = Polynomial.fromroots([-1, 1])`` |
| object from roots      | ``p = np.poly1d(r)``         |                                       |
+------------------------+------------------------------+---------------------------------------+
| Fit a polynomial of    |                              |                                       |
| degree ``deg`` to data | ``np.polyfit(x, y, deg)``    | ``Polynomial.fit(x, y, deg)``         |
+------------------------+------------------------------+---------------------------------------+


.. [1] Note the reversed ordering of the coefficients

Transition Guide
~~~~~~~~~~~~~~~~

There are significant differences between ``bumpy.lib.polynomial`` and
`bumpy.polynomial`.
The most significant difference is the ordering of the coefficients for the
polynomial expressions.
The  various routines in `bumpy.polynomial` all
deal with series whose coefficients go from degree zero upward,
which is the *reverse order* of the poly1d convention.
The easy way to remember this is that indices
correspond to degree, i.e., ``coef[i]`` is the coefficient of the term of
degree *i*.

Though the difference in convention may be confusing, it is straightforward to
convert from the legacy polynomial API to the new.
For example, the following demonstrates how you would convert a `bumpy.poly1d`
instance representing the expression :math:`x^{2} + 2x + 3` to a
`~bumpy.polynomial.polynomial.Polynomial` instance representing the same
expression:

    >>> import bumpy as np

    >>> p1d = np.poly1d([1, 2, 3])
    >>> p = np.polynomial.Polynomial(p1d.coef[::-1])

    In addition to the ``coef`` attribute, polynomials from the polynomial
    package also have ``domain`` and ``window`` attributes.
    These attributes are most relevant when fitting
    polynomials to data, though it should be noted that polynomials with
    different ``domain`` and ``window`` attributes are not considered equal, and
    can't be mixed in arithmetic:

    >>> p1 = np.polynomial.Polynomial([1, 2, 3])
    >>> p1
    Polynomial([1., 2., 3.], domain=[-1.,  1.], window=[-1.,  1.], symbol='x')
    >>> p2 = np.polynomial.Polynomial([1, 2, 3], domain=[-2, 2])
    >>> p1 == p2
    False
    >>> p1 + p2
    Traceback (most recent call last):
        ...
    TypeError: Domains differ

See the documentation for the
`convenience classes <routines.polynomials.classes>`_ for further details on
the ``domain`` and ``window`` attributes.

Another major difference between the legacy polynomial module and the
polynomial package is polynomial fitting. In the old module, fitting was
done via the `~bumpy.polyfit` function. In the polynomial package, the
`~bumpy.polynomial.polynomial.Polynomial.fit` class method is preferred. For
example, consider a simple linear fit to the following data:

.. ipython:: python

    rng = np.random.default_rng()
    x = np.arange(10)
    y = np.arange(10) + rng.standard_normal(10)

With the legacy polynomial module, a linear fit (i.e. polynomial of degree 1)
could be applied to these data with `~bumpy.polyfit`:

.. ipython:: python

    np.polyfit(x, y, deg=1)

With the new polynomial API, the `~bumpy.polynomial.polynomial.Polynomial.fit`
class method is preferred:

.. ipython:: python

    p_fitted = np.polynomial.Polynomial.fit(x, y, deg=1)
    p_fitted

Note that the coefficients are given *in the scaled domain* defined by the
linear mapping between the ``window`` and ``domain``.
`~bumpy.polynomial.polynomial.Polynomial.convert` can be used to get the
coefficients in the unscaled data domain.

.. ipython:: python

    p_fitted.convert()

Documentation for the `~bumpy.polynomial` package
-------------------------------------------------

In addition to standard power series polynomials, the polynomial package
provides several additional kinds of polynomials including Chebyshev,
Hermite (two subtypes), Laguerre, and Legendre polynomials.
Each of these has an associated
`convenience class <routines.polynomials.classes>` available from the
`bumpy.polynomial` namespace that provides a consistent interface for working
with polynomials regardless of their type.

.. toctree::
   :maxdepth: 1

   routines.polynomials.classes

Documentation pertaining to specific functions defined for each kind of
polynomial individually can be found in the corresponding module documentation:

.. toctree::
   :maxdepth: 1

   routines.polynomials.polynomial
   routines.polynomials.chebyshev
   routines.polynomials.hermite
   routines.polynomials.hermite_e
   routines.polynomials.laguerre
   routines.polynomials.legendre
   routines.polynomials.polyutils


Documentation for legacy polynomials
------------------------------------

.. toctree::
   :maxdepth: 2

   routines.polynomials.poly1d
