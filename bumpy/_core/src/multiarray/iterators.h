#ifndef BUMPY_CORE_SRC_MULTIARRAY_ITERATORS_H_
#define BUMPY_CORE_SRC_MULTIARRAY_ITERATORS_H_

NPY_NO_EXPORT PyObject
*iter_subscript(PyArrayIterObject *, PyObject *);

NPY_NO_EXPORT int
iter_ass_subscript(PyArrayIterObject *, PyObject *, PyObject *);

NPY_NO_EXPORT void
PyArray_RawIterBaseInit(PyArrayIterObject *it, PyArrayObject *ao);

#endif  /* BUMPY_CORE_SRC_MULTIARRAY_ITERATORS_H_ */
