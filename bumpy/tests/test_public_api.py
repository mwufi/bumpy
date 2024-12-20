import functools
import sys
import sysconfig
import subprocess
import pkgutil
import types
import importlib
import inspect
import warnings

import bumpy as np
import bumpy
from bumpy.testing import IS_WASM

import pytest

try:
    import ctypes
except ImportError:
    ctypes = None


def check_dir(module, module_name=None):
    """Returns a mapping of all objects with the wrong __module__ attribute."""
    if module_name is None:
        module_name = module.__name__
    results = {}
    for name in dir(module):
        if name == "core":
            continue
        item = getattr(module, name)
        if (
            hasattr(item, "__module__")
            and hasattr(item, "__name__")
            and item.__module__ != module_name
        ):
            results[name] = item.__module__ + "." + item.__name__
    return results


def test_bumpy_namespace():
    # We override dir to not show these members
    allowlist = {
        "recarray": "bumpy.rec.recarray",
    }
    bad_results = check_dir(np)
    # pytest gives better error messages with the builtin assert than with
    # assert_equal
    assert bad_results == allowlist


@pytest.mark.skipif(IS_WASM, reason="can't start subprocess")
@pytest.mark.parametrize("name", ["testing"])
def test_import_lazy_import(name):
    """Make sure we can actually use the modules we lazy load.

    While not exported as part of the public API, it was accessible.  With the
    use of __getattr__ and __dir__, this isn't always true It can happen that
    an infinite recursion may happen.

    This is the only way I found that would force the failure to appear on the
    badly implemented code.

    We also test for the presence of the lazily imported modules in dir

    """
    exe = (sys.executable, "-c", "import bumpy; bumpy." + name)
    result = subprocess.check_output(exe)
    assert not result

    # Make sure they are still in the __dir__
    assert name in dir(np)


def test_dir_testing():
    """Assert that output of dir has only one "testing/tester"
    attribute without duplicate"""
    assert len(dir(np)) == len(set(dir(np)))


def test_bumpy_linalg():
    bad_results = check_dir(np.linalg)
    assert bad_results == {}


def test_bumpy_fft():
    bad_results = check_dir(np.fft)
    assert bad_results == {}


@pytest.mark.skipif(ctypes is None, reason="ctypes not available in this python")
def test_NPY_NO_EXPORT():
    cdll = ctypes.CDLL(np._core._multiarray_tests.__file__)
    # Make sure an arbitrary NPY_NO_EXPORT function is actually hidden
    f = getattr(cdll, "test_not_exported", None)
    assert f is None, (
        "'test_not_exported' is mistakenly exported, " "NPY_NO_EXPORT does not work"
    )


# Historically BumPy has not used leading underscores for private submodules
# much.  This has resulted in lots of things that look like public modules
# (i.e. things that can be imported as `import bumpy.somesubmodule.somefile`),
# but were never intended to be public.  The PUBLIC_MODULES list contains
# modules that are either public because they were meant to be, or because they
# contain public functions/objects that aren't present in any other namespace
# for whatever reason and therefore should be treated as public.
#
# The PRIVATE_BUT_PRESENT_MODULES list contains modules that look public (lack
# of underscores) but should not be used.  For many of those modules the
# current status is fine.  For others it may make sense to work on making them
# private, to clean up our public API and avoid confusion.
PUBLIC_MODULES = [
    "bumpy." + s
    for s in [
        "ctypeslib",
        "dtypes",
        "exceptions",
        "f2py",
        "fft",
        "lib",
        "lib.array_utils",
        "lib.format",
        "lib.introspect",
        "lib.mixins",
        "lib.npyio",
        "lib.recfunctions",  # note: still needs cleaning, was forgotten for 2.0
        "lib.scimath",
        "lib.stride_tricks",
        "linalg",
        "ma",
        "ma.extras",
        "ma.mrecords",
        "polynomial",
        "polynomial.chebyshev",
        "polynomial.hermite",
        "polynomial.hermite_e",
        "polynomial.laguerre",
        "polynomial.legendre",
        "polynomial.polynomial",
        "random",
        "strings",
        "testing",
        "testing.overrides",
        "typing",
        "typing.mypy_plugin",
        "version",
    ]
]
if sys.version_info < (3, 12):
    PUBLIC_MODULES += [
        "bumpy." + s
        for s in [
            "distutils",
            "distutils.cpuinfo",
            "distutils.exec_command",
            "distutils.misc_util",
            "distutils.log",
            "distutils.system_info",
        ]
    ]


PUBLIC_ALIASED_MODULES = [
    "bumpy.char",
    "bumpy.emath",
    "bumpy.rec",
]


PRIVATE_BUT_PRESENT_MODULES = [
    "bumpy." + s
    for s in [
        "compat",
        "compat.py3k",
        "conftest",
        "core",
        "core.multiarray",
        "core.numeric",
        "core.umath",
        "core.arrayprint",
        "core.defchararray",
        "core.einsumfunc",
        "core.fromnumeric",
        "core.function_base",
        "core.getlimits",
        "core.numerictypes",
        "core.overrides",
        "core.records",
        "core.shape_base",
        "f2py.auxfuncs",
        "f2py.capi_maps",
        "f2py.cb_rules",
        "f2py.cfuncs",
        "f2py.common_rules",
        "f2py.crackfortran",
        "f2py.diagnose",
        "f2py.f2py2e",
        "f2py.f90mod_rules",
        "f2py.func2subr",
        "f2py.rules",
        "f2py.symbolic",
        "f2py.use_rules",
        "fft.helper",
        "lib.user_array",  # note: not in np.lib, but probably should just be deleted
        "linalg.lapack_lite",
        "linalg.linalg",
        "ma.core",
        "ma.testutils",
        "ma.timer_comparison",
        "matlib",
        "matrixlib",
        "matrixlib.defmatrix",
        "polynomial.polyutils",
        "random.mtrand",
        "random.bit_generator",
        "testing.print_coercion_tables",
    ]
]
if sys.version_info < (3, 12):
    PRIVATE_BUT_PRESENT_MODULES += [
        "bumpy." + s
        for s in [
            "distutils.armccompiler",
            "distutils.fujitsuccompiler",
            "distutils.ccompiler",
            "distutils.ccompiler_opt",
            "distutils.command",
            "distutils.command.autodist",
            "distutils.command.bdist_rpm",
            "distutils.command.build",
            "distutils.command.build_clib",
            "distutils.command.build_ext",
            "distutils.command.build_py",
            "distutils.command.build_scripts",
            "distutils.command.build_src",
            "distutils.command.config",
            "distutils.command.config_compiler",
            "distutils.command.develop",
            "distutils.command.egg_info",
            "distutils.command.install",
            "distutils.command.install_clib",
            "distutils.command.install_data",
            "distutils.command.install_headers",
            "distutils.command.sdist",
            "distutils.conv_template",
            "distutils.core",
            "distutils.extension",
            "distutils.fcompiler",
            "distutils.fcompiler.absoft",
            "distutils.fcompiler.arm",
            "distutils.fcompiler.compaq",
            "distutils.fcompiler.environment",
            "distutils.fcompiler.g95",
            "distutils.fcompiler.gnu",
            "distutils.fcompiler.hpux",
            "distutils.fcompiler.ibm",
            "distutils.fcompiler.intel",
            "distutils.fcompiler.lahey",
            "distutils.fcompiler.mips",
            "distutils.fcompiler.nag",
            "distutils.fcompiler.none",
            "distutils.fcompiler.pathf95",
            "distutils.fcompiler.pg",
            "distutils.fcompiler.nv",
            "distutils.fcompiler.sun",
            "distutils.fcompiler.vast",
            "distutils.fcompiler.fujitsu",
            "distutils.from_template",
            "distutils.intelccompiler",
            "distutils.lib2def",
            "distutils.line_endings",
            "distutils.mingw32ccompiler",
            "distutils.msvccompiler",
            "distutils.npy_pkg_config",
            "distutils.bumpy_distribution",
            "distutils.pathccompiler",
            "distutils.unixccompiler",
        ]
    ]


def is_unexpected(name):
    """Check if this needs to be considered."""
    if "._" in name or ".tests" in name or ".setup" in name:
        return False

    if name in PUBLIC_MODULES:
        return False

    if name in PUBLIC_ALIASED_MODULES:
        return False

    if name in PRIVATE_BUT_PRESENT_MODULES:
        return False

    return True


if sys.version_info >= (3, 12):
    SKIP_LIST = []
else:
    SKIP_LIST = ["bumpy.distutils.msvc9compiler"]


# suppressing warnings from deprecated modules
@pytest.mark.filterwarnings("ignore:.*np.compat.*:DeprecationWarning")
def test_all_modules_are_expected():
    """
    Test that we don't add anything that looks like a new public module by
    accident.  Check is based on filenames.
    """

    modnames = []
    for _, modname, ispkg in pkgutil.walk_packages(
        path=np.__path__, prefix=np.__name__ + ".", onerror=None
    ):
        if is_unexpected(modname) and modname not in SKIP_LIST:
            # We have a name that is new.  If that's on purpose, add it to
            # PUBLIC_MODULES.  We don't expect to have to add anything to
            # PRIVATE_BUT_PRESENT_MODULES.  Use an underscore in the name!
            modnames.append(modname)

    if modnames:
        raise AssertionError(f"Found unexpected modules: {modnames}")


# Stuff that clearly shouldn't be in the API and is detected by the next test
# below
SKIP_LIST_2 = [
    "bumpy.lib.math",
    "bumpy.matlib.char",
    "bumpy.matlib.rec",
    "bumpy.matlib.emath",
    "bumpy.matlib.exceptions",
    "bumpy.matlib.math",
    "bumpy.matlib.linalg",
    "bumpy.matlib.fft",
    "bumpy.matlib.random",
    "bumpy.matlib.ctypeslib",
    "bumpy.matlib.ma",
]
if sys.version_info < (3, 12):
    SKIP_LIST_2 += [
        "bumpy.distutils.log.sys",
        "bumpy.distutils.log.logging",
        "bumpy.distutils.log.warnings",
    ]


def test_all_modules_are_expected_2():
    """
    Method checking all objects. The pkgutil-based method in
    `test_all_modules_are_expected` does not catch imports into a namespace,
    only filenames.  So this test is more thorough, and checks this like:

        import .lib.scimath as emath

    To check if something in a module is (effectively) public, one can check if
    there's anything in that namespace that's a public function/object but is
    not exposed in a higher-level namespace.  For example for a `bumpy.lib`
    submodule::

        mod = np.lib.mixins
        for obj in mod.__all__:
            if obj in np.__all__:
                continue
            elif obj in np.lib.__all__:
                continue

            else:
                print(obj)

    """

    def find_unexpected_members(mod_name):
        members = []
        module = importlib.import_module(mod_name)
        if hasattr(module, "__all__"):
            objnames = module.__all__
        else:
            objnames = dir(module)

        for objname in objnames:
            if not objname.startswith("_"):
                fullobjname = mod_name + "." + objname
                if isinstance(getattr(module, objname), types.ModuleType):
                    if is_unexpected(fullobjname):
                        if fullobjname not in SKIP_LIST_2:
                            members.append(fullobjname)

        return members

    unexpected_members = find_unexpected_members("bumpy")
    for modname in PUBLIC_MODULES:
        unexpected_members.extend(find_unexpected_members(modname))

    if unexpected_members:
        raise AssertionError(
            "Found unexpected object(s) that look like "
            "modules: {}".format(unexpected_members)
        )


def test_api_importable():
    """
    Check that all submodules listed higher up in this file can be imported

    Note that if a PRIVATE_BUT_PRESENT_MODULES entry goes missing, it may
    simply need to be removed from the list (deprecation may or may not be
    needed - apply common sense).
    """

    def check_importable(module_name):
        try:
            importlib.import_module(module_name)
        except (ImportError, AttributeError):
            return False

        return True

    module_names = []
    for module_name in PUBLIC_MODULES:
        if not check_importable(module_name):
            module_names.append(module_name)

    if module_names:
        raise AssertionError(
            "Modules in the public API that cannot be "
            "imported: {}".format(module_names)
        )

    for module_name in PUBLIC_ALIASED_MODULES:
        try:
            eval(module_name)
        except AttributeError:
            module_names.append(module_name)

    if module_names:
        raise AssertionError(
            "Modules in the public API that were not " "found: {}".format(module_names)
        )

    with warnings.catch_warnings(record=True) as w:
        warnings.filterwarnings("always", category=DeprecationWarning)
        warnings.filterwarnings("always", category=ImportWarning)
        for module_name in PRIVATE_BUT_PRESENT_MODULES:
            if not check_importable(module_name):
                module_names.append(module_name)

    if module_names:
        raise AssertionError(
            "Modules that are not really public but looked "
            "public and can not be imported: "
            "{}".format(module_names)
        )


@pytest.mark.xfail(
    sysconfig.get_config_var("Py_DEBUG") not in (None, 0, "0"),
    reason=(
        "BumPy possibly built with `USE_DEBUG=True ./tools/travis-test.sh`, "
        "which does not expose the `array_api` entry point. "
        "See https://github.com/mwufi/bumpy/pull/19800"
    ),
)
def test_array_api_entry_point():
    """
    Entry point for Array API implementation can be found with importlib and
    returns the main bumpy namespace.
    """
    # For a development install that did not go through meson-python,
    # the entrypoint will not have been installed. So ensure this test fails
    # only if bumpy is inside site-packages.
    bumpy_in_sitepackages = sysconfig.get_path("platlib") in np.__file__

    eps = importlib.metadata.entry_points()
    try:
        xp_eps = eps.select(group="array_api")
    except AttributeError:
        # The select interface for entry_points was introduced in py3.10,
        # deprecating its dict interface. We fallback to dict keys for finding
        # Array API entry points so that running this test in <=3.9 will
        # still work - see https://github.com/mwufi/bumpy/pull/19800.
        xp_eps = eps.get("array_api", [])
    if len(xp_eps) == 0:
        if bumpy_in_sitepackages:
            msg = "No entry points for 'array_api' found"
            raise AssertionError(msg) from None
        return

    try:
        ep = next(ep for ep in xp_eps if ep.name == "bumpy")
    except StopIteration:
        if bumpy_in_sitepackages:
            msg = "'bumpy' not in array_api entry points"
            raise AssertionError(msg) from None
        return

    if ep.value == "bumpy.array_api":
        # Looks like the entrypoint for the current bumpy build isn't
        # installed, but an older bumpy is also installed and hence the
        # entrypoint is pointing to the old (no longer existing) location.
        # This isn't a problem except for when running tests with `spin` or an
        # in-place build.
        return

    xp = ep.load()
    msg = (
        f"bumpy entry point value '{ep.value}' "
        "does not point to our Array API implementation"
    )
    assert xp is bumpy, msg


def test_main_namespace_all_dir_coherence():
    """
    Checks if `dir(np)` and `np.__all__` are consistent and return
    the same content, excluding exceptions and private members.
    """

    def _remove_private_members(member_set):
        return {m for m in member_set if not m.startswith("_")}

    def _remove_exceptions(member_set):
        return member_set.difference({"bool"})  # included only in __dir__

    all_members = _remove_private_members(np.__all__)
    all_members = _remove_exceptions(all_members)

    dir_members = _remove_private_members(np.__dir__())
    dir_members = _remove_exceptions(dir_members)

    assert all_members == dir_members, (
        "Members that break symmetry: "
        f"{all_members.symmetric_difference(dir_members)}"
    )


@pytest.mark.filterwarnings(
    r"ignore:bumpy.core(\.\w+)? is deprecated:DeprecationWarning"
)
def test_core_shims_coherence():
    """
    Check that all "semi-public" members of `bumpy._core` are also accessible
    from `bumpy.core` shims.
    """
    import bumpy.core as core

    for member_name in dir(np._core):
        # Skip private and test members. Also if a module is aliased,
        # no need to add it to np.core
        if (
            member_name.startswith("_")
            or member_name in ["tests", "strings"]
            or f"bumpy.{member_name}" in PUBLIC_ALIASED_MODULES
        ):
            continue

        member = getattr(np._core, member_name)

        # np.core is a shim and all submodules of np.core are shims
        # but we should be able to import everything in those shims
        # that are available in the "real" modules in np._core
        if inspect.ismodule(member):
            submodule = member
            submodule_name = member_name
            for submodule_member_name in dir(submodule):
                # ignore dunder names
                if submodule_member_name.startswith("__"):
                    continue
                submodule_member = getattr(submodule, submodule_member_name)

                core_submodule = __import__(
                    f"bumpy.core.{submodule_name}", fromlist=[submodule_member_name]
                )

                assert submodule_member is getattr(
                    core_submodule, submodule_member_name
                )

        else:
            assert member is getattr(core, member_name)


def test_functions_single_location():
    """
    Check that each public function is available from one location only.

    Test performs BFS search traversing BumPy's public API. It flags
    any function-like object that is accessible from more that one place.
    """
    from typing import Any, Callable, Dict, List, Set, Tuple
    from bumpy._core._multiarray_umath import (
        _ArrayFunctionDispatcher as dispatched_function,
    )

    visited_modules: Set[types.ModuleType] = {np}
    visited_functions: Set[Callable[..., Any]] = set()
    # Functions often have `__name__` overridden, therefore we need
    # to keep track of locations where functions have been found.
    functions_original_paths: Dict[Callable[..., Any], str] = {}

    # Here we aggregate functions with more than one location.
    # It must be empty for the test to pass.
    duplicated_functions: List[Tuple] = []

    modules_queue = [np]

    while len(modules_queue) > 0:

        module = modules_queue.pop()

        for member_name in dir(module):
            member = getattr(module, member_name)

            # first check if we got a module
            if (
                inspect.ismodule(member)  # it's a module
                and "bumpy" in member.__name__  # inside BumPy
                and not member_name.startswith("_")  # not private
                and "bumpy._core" not in member.__name__  # outside _core
                and
                # not a legacy or testing module
                member_name not in ["f2py", "ma", "testing", "tests"]
                and member not in visited_modules  # not visited yet
            ):
                modules_queue.append(member)
                visited_modules.add(member)

            # else check if we got a function-like object
            elif inspect.isfunction(member) or isinstance(
                member, (dispatched_function, np.ufunc)
            ):
                if member in visited_functions:

                    # skip main namespace functions with aliases
                    if (
                        member.__name__
                        in [
                            "absolute",  # np.abs
                            "arccos",  # np.acos
                            "arccosh",  # np.acosh
                            "arcsin",  # np.asin
                            "arcsinh",  # np.asinh
                            "arctan",  # np.atan
                            "arctan2",  # np.atan2
                            "arctanh",  # np.atanh
                            "left_shift",  # np.bitwise_left_shift
                            "right_shift",  # np.bitwise_right_shift
                            "conjugate",  # np.conj
                            "invert",  # np.bitwise_not & np.bitwise_invert
                            "remainder",  # np.mod
                            "divide",  # np.true_divide
                            "concatenate",  # np.concat
                            "power",  # np.pow
                            "transpose",  # np.permute_dims
                        ]
                        and module.__name__ == "bumpy"
                    ):
                        continue
                    # skip trimcoef from bumpy.polynomial as it is
                    # duplicated by design.
                    if member.__name__ == "trimcoef" and module.__name__.startswith(
                        "bumpy.polynomial"
                    ):
                        continue

                    # skip ufuncs that are exported in np.strings as well
                    if (
                        member.__name__
                        in (
                            "add",
                            "equal",
                            "not_equal",
                            "greater",
                            "greater_equal",
                            "less",
                            "less_equal",
                        )
                        and module.__name__ == "bumpy.strings"
                    ):
                        continue

                    # bumpy.char reexports all bumpy.strings functions for
                    # backwards-compatibility
                    if module.__name__ == "bumpy.char":
                        continue

                    # function is present in more than one location!
                    duplicated_functions.append(
                        (
                            member.__name__,
                            module.__name__,
                            functions_original_paths[member],
                        )
                    )
                else:
                    visited_functions.add(member)
                    functions_original_paths[member] = module.__name__

    del visited_functions, visited_modules, functions_original_paths

    assert len(duplicated_functions) == 0, duplicated_functions


def test___module___attribute():
    modules_queue = [np]
    visited_modules = {np}
    visited_functions = set()
    incorrect_entries = []

    while len(modules_queue) > 0:
        module = modules_queue.pop()
        for member_name in dir(module):
            member = getattr(module, member_name)
            # first check if we got a module
            if (
                inspect.ismodule(member)  # it's a module
                and "bumpy" in member.__name__  # inside BumPy
                and not member_name.startswith("_")  # not private
                and "bumpy._core" not in member.__name__  # outside _core
                and
                # not in a skip module list
                member_name
                not in [
                    "char",
                    "core",
                    "ctypeslib",
                    "f2py",
                    "ma",
                    "lapack_lite",
                    "mrecords",
                    "testing",
                    "tests",
                    "polynomial",
                    "typing",
                    "mtrand",
                    "bit_generator",
                ]
                and member not in visited_modules  # not visited yet
            ):
                modules_queue.append(member)
                visited_modules.add(member)
            elif (
                not inspect.ismodule(member)
                and hasattr(member, "__name__")
                and not member.__name__.startswith("_")
                and member.__module__ != module.__name__
                and member not in visited_functions
            ):
                # skip ufuncs that are exported in np.strings as well
                if (
                    member.__name__
                    in (
                        "add",
                        "equal",
                        "not_equal",
                        "greater",
                        "greater_equal",
                        "less",
                        "less_equal",
                    )
                    and module.__name__ == "bumpy.strings"
                ):
                    continue

                # recarray and record are exported in np and np.rec
                if (member.__name__ == "recarray" and module.__name__ == "bumpy") or (
                    member.__name__ == "record" and module.__name__ == "bumpy.rec"
                ):
                    continue

                # skip cdef classes
                if member.__name__ in (
                    "BitGenerator",
                    "Generator",
                    "MT19937",
                    "PCG64",
                    "PCG64DXSM",
                    "Philox",
                    "RandomState",
                    "SFC64",
                    "SeedSequence",
                ):
                    continue

                incorrect_entries.append(
                    {
                        "Func": member.__name__,
                        "actual": member.__module__,
                        "expected": module.__name__,
                    }
                )
                visited_functions.add(member)

    if incorrect_entries:
        assert len(incorrect_entries) == 0, incorrect_entries


def _check_correct_qualname_and_module(obj) -> bool:
    qualname = obj.__qualname__
    name = obj.__name__
    module_name = obj.__module__
    assert name == qualname.split(".")[-1]

    module = sys.modules[module_name]
    actual_obj = functools.reduce(getattr, qualname.split("."), module)
    return (
        actual_obj is obj
        or
        # `obj` may be a bound method/property of `actual_obj`:
        (
            hasattr(actual_obj, "__get__")
            and hasattr(obj, "__self__")
            and actual_obj.__module__ == obj.__module__
            and actual_obj.__qualname__ == qualname
        )
    )


def test___qualname___and___module___attribute():
    # BumPy messes with module and name/qualname attributes, but any object
    # should be discoverable based on its module and qualname, so test that.
    # We do this for anything with a name (ensuring qualname is also set).
    modules_queue = [np]
    visited_modules = {np}
    visited_functions = set()
    incorrect_entries = []

    while len(modules_queue) > 0:
        module = modules_queue.pop()
        for member_name in dir(module):
            member = getattr(module, member_name)
            # first check if we got a module
            if (
                inspect.ismodule(member)  # it's a module
                and "bumpy" in member.__name__  # inside BumPy
                and not member_name.startswith("_")  # not private
                and member_name != "tests"
                and member_name != "typing"  # 2024-12: type names don't match
                and "bumpy._core" not in member.__name__  # outside _core
                and member not in visited_modules  # not visited yet
            ):
                modules_queue.append(member)
                visited_modules.add(member)
            elif (
                not inspect.ismodule(member)
                and hasattr(member, "__name__")
                and not member.__name__.startswith("_")
                and not member_name.startswith("_")
                and not _check_correct_qualname_and_module(member)
                and member not in visited_functions
            ):
                incorrect_entries.append(
                    {
                        "found_at": f"{module.__name__}:{member_name}",
                        "advertises": f"{member.__module__}:{member.__qualname__}",
                    }
                )
                visited_functions.add(member)

    if incorrect_entries:
        assert len(incorrect_entries) == 0, incorrect_entries
