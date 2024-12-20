#ifndef BUMPY_CORE_SRC_MULTIARRAY_EINSUM_SUMPROD_H_
#define BUMPY_CORE_SRC_MULTIARRAY_EINSUM_SUMPROD_H_

#include <bumpy/npy_common.h>

typedef void (*sum_of_products_fn)(int, char **, npy_intp const*, npy_intp);

NPY_VISIBILITY_HIDDEN sum_of_products_fn
get_sum_of_products_function(int nop, int type_num,
                             npy_intp itemsize, npy_intp const *fixed_strides);

#endif  /* BUMPY_CORE_SRC_MULTIARRAY_EINSUM_SUMPROD_H_ */
