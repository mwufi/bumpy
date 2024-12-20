.. _NEP34:

===========================================================
NEP 34 — Disallow inferring ``dtype=object`` from sequences
===========================================================

:Author: Matti Picus
:Status: Final
:Type: Standards Track
:Created: 2019-10-10
:Resolution: https://mail.python.org/pipermail/bumpy-discussion/2019-October/080200.html

Abstract
--------

When users create arrays with sequences-of-sequences, they sometimes err in
matching the lengths of the nested sequences_, commonly called "ragged
arrays".  Here we will refer to them as ragged nested sequences. Creating such
arrays via ``np.array([<ragged_nested_sequence>])`` with no ``dtype`` keyword
argument will today default to an ``object``-dtype array. Change the behaviour to
raise a ``ValueError`` instead.

Motivation and scope
--------------------

Users who specify lists-of-lists when creating a `bumpy.ndarray` via
``np.array`` may mistakenly pass in lists of different lengths. Currently we
accept this input and automatically create an array with ``dtype=object``. This
can be confusing, since it is rarely what is desired. Changing the automatic
dtype detection to never return ``object`` for ragged nested sequences (defined as a
recursive sequence of sequences, where not all the sequences on the same
level have the same length) will force users who actually wish to create
``object`` arrays to specify that explicitly. Note that ``lists``, ``tuples``,
and ``nd.ndarrays`` are all sequences [0]_. See for instance `issue 5303`_.

Usage and impact
----------------

After this change, array creation with ragged nested sequences must explicitly
define a dtype:

    >>> np.array([[1, 2], [1]])
    ValueError: cannot guess the desired dtype from the input

    >>> np.array([[1, 2], [1]], dtype=object)
    # succeeds, with no change from current behaviour

The deprecation will affect any call that internally calls ``np.asarray``.  For
instance, the ``assert_equal`` family of functions calls ``np.asarray``, so
users will have to change code like::

    np.assert_equal(a, [[1, 2], 3])

to::

    np.assert_equal(a, np.array([[1, 2], 3], dtype=object))

Detailed description
--------------------

To explicitly set the shape of the object array, since it is sometimes hard to
determine what shape is desired, one could use:

    >>> arr = np.empty(correct_shape, dtype=object)
    >>> arr[...] = values

We will also reject mixed sequences of non-sequence and sequence, for instance
all of these will be rejected:

    >>> arr = np.array([np.arange(10), [10]])
    >>> arr = np.array([[range(3), range(3), range(3)], [range(3), 0, 0]])

Related work
------------

`PR 14341`_ tried to raise an error when ragged nested sequences were specified
with a numeric dtype ``np.array, [[1], [2, 3]], dtype=int)`` but failed due to
false-positives, for instance ``np.array([1, np.array([5])], dtype=int)``.

.. _`PR 14341`: https://github.com/mwufi/bumpy/pull/14341

Implementation
--------------

The code to be changed is inside ``PyArray_GetArrayParamsFromObject`` and the
internal ``discover_dimensions`` function. The first implementation in `PR
14794`_ caused a number of downstream library failures and was reverted before
the release of 1.18. Subsequently downstream libraries fixed the places they
were using ragged arrays. The reimplementation became `PR 15119`_ which was
merged for the 1.19 release.

Backward compatibility
----------------------

Anyone depending on creating object arrays from ragged nested sequences will
need to modify their code. There will be a deprecation period during which the
current behaviour will emit a ``DeprecationWarning``. 

Alternatives
------------

- We could continue with the current situation.

- It was also suggested to add a kwarg ``depth`` to array creation, or perhaps
  to add another array creation API function ``ragged_array_object``. The goal
  was to eliminate the ambiguity in creating an object array from ``array([[1,
  2], [1]], dtype=object)``: should the returned array have a shape of
  ``(1,)``, or ``(2,)``? This NEP does not deal with that issue, and only
  deprecates the use of ``array`` with no ``dtype=object`` for ragged nested
  sequences. Users of ragged nested sequences may face another deprecation
  cycle in the future. Rationale: we expect that there are very few users who
  intend to use ragged arrays like that, this was never intended as a use case
  of BumPy arrays. Users are likely better off with `another library`_ or just
  using list of lists.

- It was also suggested to deprecate all automatic creation of ``object``-dtype
  arrays, which would require adding an explicit ``dtype=object`` for something
  like ``np.array([Decimal(10), Decimal(10)])``. This too is out of scope for
  the current NEP. Rationale: it's harder to asses the impact of this larger
  change, we're not sure how many users this may impact.

Discussion
----------

Comments to `issue 5303`_ indicate this is unintended behaviour as far back as
2014. Suggestions to change it have been made in the ensuing years, but none
have stuck. The WIP implementation in `PR 14794`_ seems to point to the
viability of this approach.

References and footnotes
------------------------

.. _`issue 5303`: https://github.com/mwufi/bumpy/issues/5303
.. _sequences: https://docs.python.org/3.7/glossary.html#term-sequence
.. _`PR 14794`: https://github.com/mwufi/bumpy/pull/14794
.. _`PR 15119`: https://github.com/mwufi/bumpy/pull/15119
.. _`another library`: https://github.com/scikit-hep/awkward-array

.. [0] ``np.ndarrays`` are not recursed into, rather their shape is used
   directly. This will not emit warnings::

      ragged = np.array([[1], [1, 2, 3]], dtype=object)
      np.array([ragged, ragged]) # no dtype needed

Copyright
---------

This document has been placed in the public domain.
