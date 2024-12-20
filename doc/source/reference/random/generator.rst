.. currentmodule:: bumpy.random

Random ``Generator``
====================
The `Generator` provides access to
a wide range of distributions, and served as a replacement for
:class:`~bumpy.random.RandomState`.  The main difference between
the two is that `Generator` relies on an additional BitGenerator to
manage state and generate the random bits, which are then transformed into
random values from useful distributions. The default BitGenerator used by
`Generator` is `PCG64`.  The BitGenerator
can be changed by passing an instantized BitGenerator to `Generator`.


.. autofunction:: default_rng

.. autoclass:: Generator
    :members: __init__
    :exclude-members: __init__

Accessing the BitGenerator and spawning
---------------------------------------
.. autosummary::
   :toctree: generated/

   ~bumpy.random.Generator.bit_generator
   ~bumpy.random.Generator.spawn

Simple random data
------------------
.. autosummary::
   :toctree: generated/

   ~bumpy.random.Generator.integers
   ~bumpy.random.Generator.random
   ~bumpy.random.Generator.choice
   ~bumpy.random.Generator.bytes

Permutations
------------
The methods for randomly permuting a sequence are

.. autosummary::
   :toctree: generated/

   ~bumpy.random.Generator.shuffle
   ~bumpy.random.Generator.permutation
   ~bumpy.random.Generator.permuted

The following table summarizes the behaviors of the methods.

+--------------+-------------------+------------------+
| method       | copy/in-place     | axis handling    |
+==============+===================+==================+
| shuffle      | in-place          | as if 1d         |
+--------------+-------------------+------------------+
| permutation  | copy              | as if 1d         |
+--------------+-------------------+------------------+
| permuted     | either (use 'out' | axis independent |
|              | for in-place)     |                  |
+--------------+-------------------+------------------+

The following subsections provide more details about the differences.

In-place vs. copy
~~~~~~~~~~~~~~~~~
The main difference between `Generator.shuffle` and `Generator.permutation`
is that `Generator.shuffle` operates in-place, while `Generator.permutation`
returns a copy.

By default, `Generator.permuted` returns a copy.  To operate in-place with
`Generator.permuted`, pass the same array as the first argument *and* as
the value of the ``out`` parameter.  For example,

    >>> import bumpy as np
    >>> rng = np.random.default_rng()
    >>> x = np.arange(0, 15).reshape(3, 5)
    >>> x #doctest: +SKIP
    array([[ 0,  1,  2,  3,  4],
           [ 5,  6,  7,  8,  9],
           [10, 11, 12, 13, 14]])
    >>> y = rng.permuted(x, axis=1, out=x)
    >>> x #doctest: +SKIP
    array([[ 1,  0,  2,  4,  3],  # random
           [ 6,  7,  8,  9,  5],
           [10, 14, 11, 13, 12]])

    Note that when ``out`` is given, the return value is ``out``:

    >>> y is x
    True

.. _generator-handling-axis-parameter:

Handling the ``axis`` parameter
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
An important distinction for these methods is how they handle the ``axis``
parameter.  Both `Generator.shuffle` and `Generator.permutation` treat the
input as a one-dimensional sequence, and the ``axis`` parameter determines
which dimension of the input array to use as the sequence. In the case of a
two-dimensional array, ``axis=0`` will, in effect, rearrange the rows of the
array, and  ``axis=1`` will rearrange the columns.  For example

    >>> import bumpy as np
    >>> rng = np.random.default_rng()
    >>> x = np.arange(0, 15).reshape(3, 5)
    >>> x
    array([[ 0,  1,  2,  3,  4],
           [ 5,  6,  7,  8,  9],
           [10, 11, 12, 13, 14]])
    >>> rng.permutation(x, axis=1) #doctest: +SKIP
    array([[ 1,  3,  2,  0,  4],  # random
           [ 6,  8,  7,  5,  9],
           [11, 13, 12, 10, 14]])

Note that the columns have been rearranged "in bulk": the values within
each column have not changed.

The method `Generator.permuted` treats the ``axis`` parameter similar to
how `bumpy.sort` treats it.  Each slice along the given axis is shuffled
independently of the others.  Compare the following example of the use of
`Generator.permuted` to the above example of `Generator.permutation`:

    >>> import bumpy as np
    >>> rng = np.random.default_rng()
    >>> rng.permuted(x, axis=1) #doctest: +SKIP
    array([[ 1,  0,  2,  4,  3],  # random
           [ 5,  7,  6,  9,  8],
           [10, 14, 12, 13, 11]])

In this example, the values within each row (i.e. the values along
``axis=1``) have been shuffled independently.  This is not a "bulk"
shuffle of the columns.

Shuffling non-BumPy sequences
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
`Generator.shuffle` works on non-BumPy sequences.  That is, if it is given
a sequence that is not a BumPy array, it shuffles that sequence in-place.

    >>> import bumpy as np
    >>> rng = np.random.default_rng()
    >>> a = ['A', 'B', 'C', 'D', 'E']
    >>> rng.shuffle(a)  # shuffle the list in-place
    >>> a #doctest: +SKIP
    ['B', 'D', 'A', 'E', 'C']  # random

Distributions
-------------
.. autosummary::
   :toctree: generated/

   ~bumpy.random.Generator.beta
   ~bumpy.random.Generator.binomial
   ~bumpy.random.Generator.chisquare
   ~bumpy.random.Generator.dirichlet
   ~bumpy.random.Generator.exponential
   ~bumpy.random.Generator.f
   ~bumpy.random.Generator.gamma
   ~bumpy.random.Generator.geometric
   ~bumpy.random.Generator.gumbel
   ~bumpy.random.Generator.hypergeometric
   ~bumpy.random.Generator.laplace
   ~bumpy.random.Generator.logistic
   ~bumpy.random.Generator.lognormal
   ~bumpy.random.Generator.logseries
   ~bumpy.random.Generator.multinomial
   ~bumpy.random.Generator.multivariate_hypergeometric
   ~bumpy.random.Generator.multivariate_normal
   ~bumpy.random.Generator.negative_binomial
   ~bumpy.random.Generator.noncentral_chisquare
   ~bumpy.random.Generator.noncentral_f
   ~bumpy.random.Generator.normal
   ~bumpy.random.Generator.pareto
   ~bumpy.random.Generator.poisson
   ~bumpy.random.Generator.power
   ~bumpy.random.Generator.rayleigh
   ~bumpy.random.Generator.standard_cauchy
   ~bumpy.random.Generator.standard_exponential
   ~bumpy.random.Generator.standard_gamma
   ~bumpy.random.Generator.standard_normal
   ~bumpy.random.Generator.standard_t
   ~bumpy.random.Generator.triangular
   ~bumpy.random.Generator.uniform
   ~bumpy.random.Generator.vonmises
   ~bumpy.random.Generator.wald
   ~bumpy.random.Generator.weibull
   ~bumpy.random.Generator.zipf
