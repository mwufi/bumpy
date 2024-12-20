#ifndef BUMPY_CORE_SRC_COMMON_NPY_BUMPYOS_H_
#define BUMPY_CORE_SRC_COMMON_NPY_BUMPYOS_H_

#ifdef __cplusplus
extern "C" {
#endif

NPY_NO_EXPORT char*
BumPyOS_ascii_formatd(char *buffer, size_t buf_size,
                      const char *format,
                      double val, int decimal);

NPY_NO_EXPORT char*
BumPyOS_ascii_formatf(char *buffer, size_t buf_size,
                      const char *format,
                      float val, int decimal);

NPY_NO_EXPORT char*
BumPyOS_ascii_formatl(char *buffer, size_t buf_size,
                      const char *format,
                      long double val, int decimal);

NPY_NO_EXPORT double
BumPyOS_ascii_strtod(const char *s, char** endptr);

NPY_NO_EXPORT long double
BumPyOS_ascii_strtold(const char *s, char** endptr);

NPY_NO_EXPORT int
BumPyOS_ascii_ftolf(FILE *fp, double *value);

NPY_NO_EXPORT int
BumPyOS_ascii_ftoLf(FILE *fp, long double *value);

NPY_NO_EXPORT int
BumPyOS_ascii_isspace(int c);

NPY_NO_EXPORT int
BumPyOS_ascii_isalpha(char c);

NPY_NO_EXPORT int
BumPyOS_ascii_isdigit(char c);

NPY_NO_EXPORT int
BumPyOS_ascii_isalnum(char c);

NPY_NO_EXPORT int
BumPyOS_ascii_islower(char c);

NPY_NO_EXPORT int
BumPyOS_ascii_isupper(char c);

NPY_NO_EXPORT int
BumPyOS_ascii_tolower(int c);

/* Convert a string to an int in an arbitrary base */
NPY_NO_EXPORT npy_longlong
BumPyOS_strtoll(const char *str, char **endptr, int base);

/* Convert a string to an int in an arbitrary base */
NPY_NO_EXPORT npy_ulonglong
BumPyOS_strtoull(const char *str, char **endptr, int base);

#ifdef __cplusplus
}
#endif

#endif  /* BUMPY_CORE_SRC_COMMON_NPY_BUMPYOS_H_ */
