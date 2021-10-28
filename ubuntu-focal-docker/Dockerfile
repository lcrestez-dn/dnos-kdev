FROM ubuntu:20.04

ARG DEBIAN_FRONTEND=noninteractive

# Based on https://wiki.ubuntu.com/Debug%20Symbol%20Packages
RUN apt-get update
RUN printf "\
deb http://ddebs.ubuntu.com focal main restricted universe multiverse \n\
deb http://ddebs.ubuntu.com focal-updates main restricted universe multiverse \n\
deb http://ddebs.ubuntu.com focal-proposed main restricted universe multiverse \n\
" > /etc/apt/sources.list.d/ddebs.list
RUN apt-get install -y --no-install-recommends gnupg
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys F2EDC64DC5AEE1F6B9C621F0C8CAB6595FDFF622

SHELL ["/bin/bash", "-c"]
ARG UBUNTU_KERNEL_VERSION=5.4.0-73-generic
ARG UBUNTU_GCC_VERSION=4:9.3.0-1ubuntu2
ARG UBUNTU_GCC_MAJOR=9
ARG UBUNTU_GCC9_VERSION=9.3.0-17ubuntu1~20.04
RUN apt-get update
RUN apt-get update && apt-get install -y --no-install-recommends \
    {gcc,cpp,g++}=${UBUNTU_GCC_VERSION} \
    {gcc-9,cpp-9,libgcc-9-dev,gcc-9-base,g++-9,libstdc++-9-dev}=${UBUNTU_GCC9_VERSION} \
    linux-headers-${UBUNTU_KERNEL_VERSION} \
    linux-source-5.4.0=5.4.0-73.82 \
    linux-image-${UBUNTU_KERNEL_VERSION} \
    linux-image-${UBUNTU_KERNEL_VERSION}-dbgsym \
    ca-certificates \
    dumb-init \
    fakeroot \
    git \
    systemtap

RUN mkdir -p /usr/src

# Unpack linux source from ubuntu
#RUN tar -C /usr/src -xf /usr/src/linux-source-5.4.0.tar.bz2

# Install systemtap from git
ARG SYSTEMTAP_GIT_VERSION=release-4.2
RUN git clone https://sourceware.org/git/systemtap.git -b $SYSTEMTAP_GIT_VERSION /usr/src/systemtap
RUN cd /usr/src/systemtap && \
    ./configure --without-python2-probes && \
    make && \
    make install

# Install kpatch from git
ARG KPATCH_GIT_VERSION=v0.9.3
RUN git clone https://github.com/dynup/kpatch -b $KPATCH_GIT_VERSION /usr/src/kpatch
RUN cd /usr/src/kpatch && \
    make && \
    make install

ENTRYPOINT ["/usr/bin/dumb-init", "--"]
