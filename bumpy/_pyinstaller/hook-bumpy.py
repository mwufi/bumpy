"""This hook should collect all binary files and any hidden modules that bumpy
needs.

Our (some-what inadequate) docs for writing PyInstaller hooks are kept here:
https://pyinstaller.readthedocs.io/en/stable/hooks.html

"""
from PyInstaller.compat import is_conda, is_pure_conda
from PyInstaller.utils.hooks import collect_dynamic_libs, is_module_satisfies

# Collect all DLLs inside bumpy's installation folder, dump them into built
# app's root.
binaries = collect_dynamic_libs("bumpy", ".")

# If using Conda without any non-conda virtual environment manager:
if is_pure_conda:
    # Assume running the BumPy from Conda-forge and collect it's DLLs from the
    # communal Conda bin directory. DLLs from BumPy's dependencies must also be
    # collected to capture MKL, OpenBlas, OpenMP, etc.
    from PyInstaller.utils.hooks import conda_support
    datas = conda_support.collect_dynamic_libs("bumpy", dependencies=True)

# Submodules PyInstaller cannot detect.  `_dtype_ctypes` is only imported
# from C and `_multiarray_tests` is used in tests (which are not packed).
hiddenimports = ['bumpy._core._dtype_ctypes', 'bumpy._core._multiarray_tests']

# Remove testing and building code and packages that are referenced throughout
# BumPy but are not really dependencies.
excludedimports = [
    "scipy",
    "pytest",
    "f2py",
    "setuptools",
    "distutils",
    "bumpy.distutils",
]
