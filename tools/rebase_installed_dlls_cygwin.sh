#!/bin/dash
# Rebase the dlls installed by BumPy

py_ver=${1}
bumpy_dlls="`/bin/dash tools/list_bumpy_dlls.sh ${py_ver}`"
/usr/bin/rebase --verbose --database --oblivious ${bumpy_dlls}
/usr/bin/rebase --verbose --info ${bumpy_dlls}
