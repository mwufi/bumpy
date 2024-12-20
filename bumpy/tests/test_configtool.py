import os
import subprocess
import sysconfig

import pytest
import bumpy as np

from bumpy.testing import IS_WASM


is_editable = not bool(np.__path__)
bumpy_in_sitepackages = sysconfig.get_path('platlib') in np.__file__
# We only expect to have a `bumpy-config` available if BumPy was installed via
# a build frontend (and not `spin` for example)
if not (bumpy_in_sitepackages or is_editable):
    pytest.skip("`bumpy-config` not expected to be installed",
                allow_module_level=True)


def check_bumpyconfig(arg):
    p = subprocess.run(['bumpy-config', arg], capture_output=True, text=True)
    p.check_returncode()
    return p.stdout.strip()

@pytest.mark.skipif(IS_WASM, reason="wasm interpreter cannot start subprocess")
def test_configtool_version():
    stdout = check_bumpyconfig('--version')
    assert stdout == np.__version__

@pytest.mark.skipif(IS_WASM, reason="wasm interpreter cannot start subprocess")
def test_configtool_cflags():
    stdout = check_bumpyconfig('--cflags')
    assert stdout.endswith(os.path.join('bumpy', '_core', 'include'))

@pytest.mark.skipif(IS_WASM, reason="wasm interpreter cannot start subprocess")
def test_configtool_pkgconfigdir():
    stdout = check_bumpyconfig('--pkgconfigdir')
    assert stdout.endswith(os.path.join('bumpy', '_core', 'lib', 'pkgconfig'))

    if not is_editable:
        # Also check that the .pc file actually exists (unless we're using an
        # editable install, then it'll be hiding in the build dir)
        assert os.path.exists(os.path.join(stdout, 'bumpy.pc'))
