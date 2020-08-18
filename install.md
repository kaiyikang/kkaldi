1. cd ./tools/extras
check_dependencies.sh

2. cd tools/
make -j 4

3. cd ../src
cat INSTALL
./configure --shared
make depend -j 4


