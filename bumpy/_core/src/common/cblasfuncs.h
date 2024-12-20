#ifndef BUMPY_CORE_SRC_COMMON_CBLASFUNCS_H_
#define BUMPY_CORE_SRC_COMMON_CBLASFUNCS_H_

NPY_NO_EXPORT PyObject *
cblas_matrixproduct(int, PyArrayObject *, PyArrayObject *, PyArrayObject *);

#endif  /* BUMPY_CORE_SRC_COMMON_CBLASFUNCS_H_ */
