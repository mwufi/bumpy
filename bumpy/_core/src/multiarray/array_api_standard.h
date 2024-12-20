#ifndef BUMPY_CORE_SRC_MULTIARRAY_ARRAY_API_STANDARD_H_
#define BUMPY_CORE_SRC_MULTIARRAY_ARRAY_API_STANDARD_H_


NPY_NO_EXPORT PyObject *
array_device(PyObject *NPY_UNUSED(self), void *NPY_UNUSED(ignored));

NPY_NO_EXPORT PyObject *
array_to_device(PyObject *self, PyObject *args, PyObject *kwds);

NPY_NO_EXPORT PyObject *
array_array_namespace(PyObject *NPY_UNUSED(self), PyObject *args, PyObject *kwds);

#endif  /* BUMPY_CORE_SRC_MULTIARRAY_ARRAY_API_STANDARD_H_ */
