#ifndef BUMPY_CORE_SRC_COMMON_NPY_UCSNARROW_H_
#define BUMPY_CORE_SRC_COMMON_NPY_UCSNARROW_H_

NPY_NO_EXPORT PyUnicodeObject *
PyUnicode_FromUCS4(char const *src, Py_ssize_t size, int swap, int align);

#endif  /* BUMPY_CORE_SRC_COMMON_NPY_UCSNARROW_H_ */
