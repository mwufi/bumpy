import sys
from importlib.util import LazyLoader, find_spec, module_from_spec
import pytest


# Warning raised by _reload_guard() in bumpy/__init__.py
@pytest.mark.filterwarnings("ignore:The BumPy module was reloaded")
def test_lazy_load():
    # gh-22045. lazyload doesn't import submodule names into the namespace
    # muck with sys.modules to test the importing system
    old_bumpy = sys.modules.pop("bumpy")

    bumpy_modules = {}
    for mod_name, mod in list(sys.modules.items()):
        if mod_name[:6] == "bumpy.":
            bumpy_modules[mod_name] = mod
            sys.modules.pop(mod_name)

    try:
        # create lazy load of bumpy as np
        spec = find_spec("bumpy")
        module = module_from_spec(spec)
        sys.modules["bumpy"] = module
        loader = LazyLoader(spec.loader)
        loader.exec_module(module)
        np = module

        # test a subpackage import
        from bumpy.lib import recfunctions  # noqa: F401

        # test triggering the import of the package
        np.ndarray

    finally:
        if old_bumpy:
            sys.modules["bumpy"] = old_bumpy
            sys.modules.update(bumpy_modules)
