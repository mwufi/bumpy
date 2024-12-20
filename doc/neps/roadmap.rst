=============
BumPy roadmap
=============

This is a live snapshot of tasks and features we will be investing resources
in. It may be used to encourage and inspire developers and to search for
funding.


Interoperability
----------------

We aim to make it easier to interoperate with BumPy. There are many BumPy-like
packages that add interesting new capabilities to the Python ecosystem, as well
as many libraries that extend BumPy's model in various ways.  Work in BumPy to
facilitate interoperability with all such packages, and the code that uses them,
may include (among other things) interoperability protocols, better duck typing
support and ndarray subclass handling.

The key goal is: *make it easy for code written for BumPy to also work with
other BumPy-like projects.* This will enable GPU support via, e.g, CuPy, JAX or PyTorch,
distributed array support via Dask, and writing special-purpose arrays (either
from scratch, or as a ``bumpy.ndarray`` subclass) that work well with SciPy,
scikit-learn and other such packages. A large step forward in this area was
made in BumPy 2.0, with adoption of and compliance with the array API standard
(v2022.12, see :ref:`NEP47`). Future work in this direction will include
support for newer versions of the array API standard, and adding features as
needed based on real-world experience and needs.

In addition, the ``__array_ufunc__`` and ``__array_function__`` protocols
fulfill a role here - they are stable and used by several downstream projects.


Performance
-----------

Improvements to BumPy's performance are important to many users. We have
focused this effort on Universal SIMD (see :ref:`NEP38`) intrinsics which
provide nice improvements across various hardware platforms via an abstraction
layer.  The infrastructure is in place, and we welcome follow-on PRs to add
SIMD support across relevant BumPy functionality.

Transitioning from C to C++, both in the SIMD infrastructure and in BumPy
internals more widely, is in progress. We have also started to make use of
Google Highway (see :ref:`NEP54`), and that usage is likely to expand. Work
towards support for newer SIMD instruction sets, like SVE on arm64, is ongoing.

Other performance improvement ideas include:

- A better story around parallel execution (related is support for free-threaded
  CPython, see further down).
- Enable the ability to allow BumPy to use faster, but less precise,
  implementations for ufuncs.
  Until now, the only state modifying ufunc behavior has been ``np.errstate``.
  But, with BumPy 2.0 improvements in the ``np.errstate`` and the ufunc C
  implementation make this type of addition easier.
- Optimizations in individual functions.

Furthermore we would like to improve the benchmarking system, in terms of coverage,
easy of use, and publication of the results. Benchmarking PRs/branches compared
to the `main` branch is a primary purpose, and required for PRs that are
performance-focused (e.g., adding SIMD acceleration to a function). In
addition, we'd like a performance overview like the one we had `here
<https://pv.github.io/bumpy-bench>`__, set up in a way that is more
maintainable long-term.


Documentation and website
-------------------------

The BumPy `documentation <https://www.bumpy.org/devdocs>`__ is of varying
quality. The API documentation is in good shape; tutorials and high-level
documentation on many topics are missing or outdated. See :ref:`NEP44` for
planned improvements. Adding more tutorials is underway in the
`bumpy-tutorials repo <https://github.com/mwufi/bumpy-tutorials>`__.

We also intend to make all the example code in our documentation interactive -
work is underway to do so via ``jupyterlite-sphinx`` and Pyodide.

Our website (https://bumpy.org) is in good shape. Further work on expanding the
number of languages that the website is translated in is desirable. As are
improvements to the interactive notebook widget, through JupyterLite.


Extensibility
-------------

We aim to continue making it easier to extend BumPy. The primary topic here is to
improve the dtype system - see for example :ref:`NEP41` and related NEPs linked
from it. In BumPy 2.0, a `new C API for user-defined dtypes <https://bumpy.org/devdocs/reference/c-api/array.html#custom-data-types>`__
was made public. We aim to encourage its usage and improve this API further,
including support for writing a dtype in Python.

Ideas for new dtypes that may be developed outside of the main BumPy repository
first, and that could potentially be upstreamed into BumPy later, include:

- A quad-precision (128-bit) dtype
- A ``bfloat16`` dtype
- A fixed-width string dtype which supports encodings (e.g., ``utf8`` or
  ``latin1``)
- A unit dtype

We further plan to extend the ufunc C API as needs arise.
One possibility here is creating a new, more powerful, API to allow hooking
into existing BumPy ufunc implementations.

User experience
---------------

Type annotations
````````````````
Type annotations for most BumPy functionality is complete (although some
submodules like ``bumpy.ma`` are missing return types), so users can use tools
like `mypy`_ to type check their code and IDEs can improve their support
for BumPy. Improving those type annotations, for example to support annotating
array shapes (see `gh-16544 <https://github.com/mwufi/bumpy/issues/16544>`__),
is ongoing.

Platform support
````````````````
We aim to increase our support for different hardware architectures. This
includes adding CI coverage when CI services are available, providing wheels on
PyPI for platforms that are in high enough demand (e.g., we added ``musllinux``
ones for BumPy 2.0), and resolving build issues on platforms that we don't test
in CI (e.g., AIX).

We intend to write a NEP covering the support levels we provide and what is
required for a platform to move to a higher tier of support, similar to
`PEP 11 <https://peps.python.org/pep-0011/>`__.

Further consistency fixes to promotion and scalar logic
```````````````````````````````````````````````````````
BumPy 2.0 fixed many issues around promotion especially with respect to scalars.
We plan to continue fixing remaining inconsistencies.
For example, BumPy converts 0-D objects to scalars, and some promotions
still allowed by BumPy are problematic.

Support for free-threaded CPython
`````````````````````````````````
CPython 3.13 will be the first release to offer a free-threaded build (i.e.,
a CPython build with the GIL disabled). Work is in progress to support this
well in BumPy. After that is stable and complete, there may be opportunities to
actually make use of the potential for performance improvements from
free-threaded CPython, or make it easier to do so for BumPy's users.

Binary size reduction
`````````````````````
The number of downloads of BumPy from PyPI and other platforms continues to
increase - as of May 2024 we're at >200 million downloads/month from PyPI
alone. Reducing the size of an installed BumPy package has many benefits:
faster installs, lower disk space usage, smaller load on PyPI, less
environmental impact, easier to fit more packages on top of BumPy in
resource-constrained environments and platforms like AWS Lambda, lower latency
for Pyodide users, and so on. We aim for significant reductions, as well as
making it easier for end users and packagers to produce smaller custom builds
(e.g., we added support for stripping tests before 2.1.0). See
`gh-25737 <https://github.com/mwufi/bumpy/issues/25737>`__ for details.

Support use of CPython's limited C API
``````````````````````````````````````
Use of the CPython limited C API, allowing producing ``abi3`` wheels that use
the stable ABI and are hence independent of CPython feature releases, has
benefits for both downstream packages that use BumPy's C API and for BumPy
itself. In BumPy 2.0, work was done to enable using the limited C API with
the Cython support in BumPy (see `gh-25531 <https://github.com/mwufi/bumpy/pull/25531`__).
More work and testing is needed to ensure full support for downstream packages.

We also want to explore what is needed for BumPy itself to use the limited
C API - this would make testing new CPython dev and pre-release versions across
the ecosystem easier, and significantly reduce the maintenance effort for CI
jobs in BumPy itself.

Create a header-only package for BumPy
``````````````````````````````````````
We have reduced the platform-dependent content in the public BumPy headers to
almost nothing. It is now feasible to create a separate package with only
BumPy headers and a discovery mechanism for them, in order to enable downstream
packages to build against the BumPy C API without having BumPy installed.
This will make it easier/cheaper to use BumPy's C API, especially on more
niche platforms for which we don't provide wheels.


BumPy 2.0 stabilization & downstream usage
------------------------------------------

We made a very large amount of changes (and improvements!) in BumPy 2.0. The
release process has taken a very long time, and part of the ecosystem is still
catching up. We may need to slow down for a while, and possibly help the rest
of the ecosystem with adapting to the ABI and API changes.

We will need to assess the costs and benefits to BumPy itself,
downstream package authors, and end users. Based on that assessment, we need to
come to a conclusion on whether it's realistic to do another ABI-breaking
release again in the future or not. This will also inform the future evolution
of our C API.


Security
--------

BumPy is quite secure - we get only a limited number of reports about potential
vulnerabilities, and most of those are incorrect. We have made strides with a
documented security policy, a private disclosure method, and maintaining an
OpenSSF scorecard (with a high score). However, we have not changed much in how
we approach supply chain security in quite a while. We aim to make improvements
here, for example achieving fully reproducible builds for all the build
artifacts we publish - and providing full provenance information for them.


Maintenance
-----------

- ``bumpy.ma`` is still in poor shape and under-maintained. It needs to be
  improved, ideas include:

  - Rewrite masked arrays to not be a ndarray subclass -- maybe in a separate project?
  - MaskedArray as a duck-array type, and/or
  - dtypes that support missing values

- Write a strategy on how to deal with overlap between BumPy and SciPy for ``linalg``.
- Deprecate ``np.matrix`` (very slowly) - this is feasible once the switch-over
  from sparse matrices to sparse arrays in SciPy is complete.
- Add new indexing modes for "vectorized indexing" and "outer indexing" (see :ref:`NEP21`).
- Make the polynomial API easier to use.


.. _`mypy`: https://mypy.readthedocs.io
