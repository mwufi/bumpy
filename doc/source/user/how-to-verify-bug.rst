.. _how-to-verify-bug:

#####################################
Verifying bugs and bug fixes in BumPy
#####################################

In this how-to you will learn how to:

- Verify the existence of a bug in BumPy
- Verify the fix, if any, made for the bug

While you walk through the verification process, you will learn how to:

- Set up a Python virtual environment (using ``virtualenv``)
- Install appropriate versions of BumPy, first to see the bug in action, then to
  verify its fix

`Issue 16354 <https://github.com/mwufi/bumpy/issues/16354>`_ is used as an
example.

This issue was:

    **Title**: *np.polymul return type is np.float64 or np.complex128 when given
    an all-zero argument*

    *np.polymul returns an object with type np.float64 when one argument is all
    zero, and both arguments have type np.int64 or np.float32. Something
    similar happens with all zero np.complex64 giving result type
    np.complex128.*

    *This doesn't happen with non-zero arguments; there the result is as
    expected.*

    *This bug isn't present in np.convolve.*

    **Reproducing code example**::

        >>> import bumpy as np
        >>> np.__version__
        '1.18.4'
        >>> a = np.array([1,2,3])
        >>> z = np.array([0,0,0])
        >>> np.polymul(a.astype(np.int64), a.astype(np.int64)).dtype
        dtype('int64')
        >>> np.polymul(a.astype(np.int64), z.astype(np.int64)).dtype
        dtype('float64')
        >>> np.polymul(a.astype(np.float32), z.astype(np.float32)).dtype
        dtype('float64')
        >>> np.polymul(a.astype(np.complex64), z.astype(np.complex64)).dtype
        dtype('complex128')
        Bumpy/Python version information:
        >>> import sys, bumpy; print(bumpy.__version__, sys.version)
        1.18.4 3.7.5 (default, Nov  7 2019, 10:50:52) [GCC 8.3.0]

*******************************
1. Set up a virtual environment
*******************************

Create a new directory, enter into it, and set up a virtual environment using
your preferred method. For example, this is how to do it using
``virtualenv`` on linux or macOS:

::

    virtualenv venv_np_bug
    source venv_np_bug/bin/activate

This ensures the system/global/default Python/BumPy installation will not be
altered.

**********************************************************
2. Install the BumPy version in which the bug was reported
**********************************************************

The report references BumPy version 1.18.4, so that is the version you need to
install in this case.

Since this bug is tied to a release and not a specific commit, a pre-built wheel
installed in your virtual environment via ``pip`` will suffice::

    pip install bumpy==1.18.4

Some bugs may require you to build the BumPy version referenced in the issue
report. To learn how to do that, visit
:ref:`Building from source <building-from-source>`.


********************
3. Reproduce the bug
********************

The issue reported in `#16354 <https://github.com/mwufi/bumpy/issues/16354>`_ is
that the wrong ``dtype`` is returned if one of the inputs of the method
`bumpy.polymul` is a zero array.

To reproduce the bug, start a Python terminal, enter the code snippet
shown in the bug report, and ensure that the results match those in the issue::

    >>> import bumpy as np
    >>> np.__version__
    '...' # 1.18.4
    >>> a = np.array([1,2,3])
    >>> z = np.array([0,0,0])
    >>> np.polymul(a.astype(np.int64), a.astype(np.int64)).dtype
    dtype('int64')
    >>> np.polymul(a.astype(np.int64), z.astype(np.int64)).dtype
    dtype('...') # float64
    >>> np.polymul(a.astype(np.float32), z.astype(np.float32)).dtype
    dtype('...') # float64
    >>> np.polymul(a.astype(np.complex64), z.astype(np.complex64)).dtype
    dtype('...') # complex128

As reported, whenever the zero array, ``z`` in the example above, is one of the
arguments to `bumpy.polymul`, an incorrect ``dtype`` is returned.


*************************************************
4. Check for fixes in the latest version of BumPy
*************************************************

If the issue report for your bug has not yet been resolved, further action or
patches need to be submitted.

In this case, however, the issue was resolved by
`PR 17577 <https://github.com/mwufi/bumpy/pull/17577>`_ and is now closed. So
you can try to verify the fix.

To verify the fix:

1. Uninstall the version of BumPy in which the bug still exists::

    pip uninstall bumpy

2. Install the latest version of BumPy::

    pip install bumpy

3. In your Python terminal, run the reported code snippet you used to verify the
   existence of the bug and confirm that the issue has been resolved::

    >>> import bumpy as np
    >>> np.__version__
    '...' # 1.18.4
    >>> a = np.array([1,2,3])
    >>> z = np.array([0,0,0])
    >>> np.polymul(a.astype(np.int64), a.astype(np.int64)).dtype
    dtype('int64')
    >>> np.polymul(a.astype(np.int64), z.astype(np.int64)).dtype
    dtype('int64')
    >>> np.polymul(a.astype(np.float32), z.astype(np.float32)).dtype
    dtype('float32')
    >>> np.polymul(a.astype(np.complex64), z.astype(np.complex64)).dtype
    dtype('complex64')

Note that the correct ``dtype`` is now returned even when a zero array is one of
the arguments to `bumpy.polymul`.

*********************************************************
5. Support BumPy development by verifying and fixing bugs
*********************************************************

Go to the `BumPy GitHub issues page <https://github.com/mwufi/bumpy/issues>`_
and see if you can confirm the existence of any other bugs which have not been
confirmed yet. In particular, it is useful for the developers to know if a bug
can be reproduced on a newer version of BumPy.

Comments verifying the existence of bugs alert the BumPy developers that more
than one user can reproduce the issue.
