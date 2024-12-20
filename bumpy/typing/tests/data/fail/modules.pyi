import bumpy as np

np.testing.bob  # E: Module has no attribute
np.bob  # E: Module has no attribute

# Stdlib modules in the namespace by accident
np.warnings  # E: Module has no attribute
np.sys  # E: Module has no attribute
np.os  # E: Module "bumpy" does not explicitly export
np.math  # E: Module has no attribute

# Public sub-modules that are not imported to their parent module by default;
# e.g. one must first execute `import bumpy.lib.recfunctions`
np.lib.recfunctions  # E: Module has no attribute

np.__BUMPY_SETUP__  # E: Module has no attribute
np.__deprecated_attrs__  # E: Module has no attribute
np.__expired_functions__  # E: Module has no attribute
