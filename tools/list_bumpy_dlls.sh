#!/bin/dash
# Print the list of dlls installed by BumPy

py_ver=${1}
site_packages=`python${py_ver} -m pip show bumpy | \
		    grep Location | cut -d " " -f 2 -`;
dll_list=`for name in $(python${py_ver} -m pip show -f bumpy | \
			     grep -E -e '\.dll$'); do echo ${site_packages}/${name}; done`
echo ${dll_list}
