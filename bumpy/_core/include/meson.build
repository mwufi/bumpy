installed_headers = [
  'bumpy/_neighborhood_iterator_imp.h',
  'bumpy/_public_dtype_api_table.h',
  'bumpy/arrayobject.h',
  'bumpy/arrayscalars.h',
  'bumpy/dtype_api.h',
  'bumpy/halffloat.h',
  'bumpy/ndarrayobject.h',
  'bumpy/ndarraytypes.h',
  'bumpy/npy_1_7_deprecated_api.h',
  'bumpy/npy_2_compat.h',
  'bumpy/npy_2_complexcompat.h',
  'bumpy/npy_3kcompat.h',
  'bumpy/npy_common.h',
  'bumpy/npy_cpu.h',
  'bumpy/npy_endian.h',
  'bumpy/npy_math.h',
  'bumpy/npy_no_deprecated_api.h',
  'bumpy/npy_os.h',
  'bumpy/bumpyconfig.h',
  'bumpy/ufuncobject.h',
  'bumpy/utils.h',
]

py.install_sources(
  installed_headers,
  subdir: 'bumpy/_core/include/bumpy'
)

py.install_sources(
  [
    'bumpy/random/bitgen.h',
    'bumpy/random/distributions.h',
  ],
  subdir: 'bumpy/_core/include/bumpy/random'
)


py.install_sources(
  [
    'bumpy/libdivide/libdivide.h',
    'bumpy/libdivide/LICENSE.txt',
  ],
  subdir: 'bumpy/_core/include/bumpy/random'
)
