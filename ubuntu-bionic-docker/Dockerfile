FROM ubuntu:18.04

ARG DEBIAN_FRONTEND=noninteractive

# Based on https://wiki.ubuntu.com/Debug%20Symbol%20Packages
RUN apt-get update
RUN printf "\
deb http://ddebs.ubuntu.com bionic main restricted universe multiverse \n\
deb http://ddebs.ubuntu.com bionic-updates main restricted universe multiverse \n\
deb http://ddebs.ubuntu.com bionic-proposed main restricted universe multiverse \n\
" > /etc/apt/sources.list.d/ddebs.list
RUN apt-get install -y --no-install-recommends gnupg
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys F2EDC64DC5AEE1F6B9C621F0C8CAB6595FDFF622
RUN apt-get update

SHELL ["/bin/bash", "-c"]
ARG UBUNTU_KERNEL_VERSION=4.15.0-23-generic
ARG UBUNTU_GCC_VERSION=4:7.3.0-3ubuntu2
ARG UBUNTU_GCC7_VERSION=7.3.0-16ubuntu3
RUN apt-get install -y --no-install-recommends \
    {gcc,cpp,g++}=${UBUNTU_GCC_VERSION} \
    {gcc-7,cpp-7,libgcc-7-dev,gcc-7-base,libasan4,libubsan0,libcilkrts5,g++-7,libstdc++-7-dev}=${UBUNTU_GCC7_VERSION} \
    linux-headers-${UBUNTU_KERNEL_VERSION} \
    linux-image-${UBUNTU_KERNEL_VERSION} \
    linux-image-${UBUNTU_KERNEL_VERSION}-dbgsym \
    ca-certificates \
    dumb-init \
    fakeroot \
    git \
    kpatch \
    kpatch-build \
    systemtap

RUN mkdir -p /usr/src

ARG SYSTEMTAP_GIT_VERSION=release-4.5
RUN git clone https://sourceware.org/git/systemtap.git -b $SYSTEMTAP_GIT_VERSION /usr/src/systemtap
RUN cd /usr/src/systemtap && \
    ./configure --without-python2-probes && \
    make && \
    make install

ARG KPATCH_GIT_VERSION=v0.9.3
RUN git clone https://github.com/dynup/kpatch -b $KPATCH_GIT_VERSION /usr/src/kpatch
RUN cd /usr/src/kpatch && \
    make && \
    make install

ENTRYPOINT ["/usr/bin/dumb-init", "--"]
