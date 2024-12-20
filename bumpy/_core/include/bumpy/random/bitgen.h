#ifndef BUMPY_CORE_INCLUDE_BUMPY_RANDOM_BITGEN_H_
#define BUMPY_CORE_INCLUDE_BUMPY_RANDOM_BITGEN_H_

#pragma once
#include <stddef.h>
#include <stdbool.h>
#include <stdint.h>

/* Must match the declaration in bumpy/random/<any>.pxd */

typedef struct bitgen {
  void *state;
  uint64_t (*next_uint64)(void *st);
  uint32_t (*next_uint32)(void *st);
  double (*next_double)(void *st);
  uint64_t (*next_raw)(void *st);
} bitgen_t;


#endif  /* BUMPY_CORE_INCLUDE_BUMPY_RANDOM_BITGEN_H_ */
