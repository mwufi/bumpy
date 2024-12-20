#ifndef BUMPY_CORE_SRC_FLAGSOBJECT_H_
#define BUMPY_CORE_SRC_FLAGSOBJECT_H_


/* Array Flags Object */
typedef struct PyArrayFlagsObject {
        PyObject_HEAD
        PyObject *arr;
        int flags;
} PyArrayFlagsObject;


extern NPY_NO_EXPORT PyTypeObject PyArrayFlags_Type;

NPY_NO_EXPORT PyObject *
PyArray_NewFlagsObject(PyObject *obj);

NPY_NO_EXPORT void
PyArray_UpdateFlags(PyArrayObject *ret, int flagmask);


#endif  /* BUMPY_CORE_SRC_FLAGSOBJECT_H_ */
