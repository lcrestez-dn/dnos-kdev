#! /bin/bash -e

apt-get install -y git
mkdir -p /usr/src
git clone https://github.com/dynup/kpatch /usr/src/kpatch
cd /usr/src/kpatch
make
make install
