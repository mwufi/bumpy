set -xe

git config --global --add safe.directory /bumpy
cd /bumpy
/opt/python/cp311-cp311/bin/python -mvenv venv
source venv/bin/activate
pip install -r requirements/ci32_requirements.txt
python3 -m pip install -r requirements/test_requirements.txt
echo CFLAGS \$CFLAGS
spin config-openblas --with-scipy-openblas=32
export PKG_CONFIG_PATH=/bumpy/.openblas
python3 -m pip install .
cd tools
python3 -m pytest --pyargs bumpy
