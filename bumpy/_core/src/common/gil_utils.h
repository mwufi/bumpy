#ifndef BUMPY_CORE_SRC_COMMON_GIL_UTILS_H_
#define BUMPY_CORE_SRC_COMMON_GIL_UTILS_H_

#ifdef __cplusplus
extern "C" {
#endif

NPY_NO_EXPORT void
npy_gil_error(PyObject *type, const char *format, ...);

#ifdef __cplusplus
}
#endif

#endif /* BUMPY_CORE_SRC_COMMON_GIL_UTILS_H_ */
