FROM ubuntu:18.04

ENV DEBIAN_FRONTEND=noninteractive

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

RUN bash -c "apt-get install -y --no-install-recommends \
    {gcc-7,cpp-7,libgcc-7-dev,gcc-7-base,libasan4,libubsan0,libcilkrts5}=7.3.0-16ubuntu3 \
    {gcc,cpp}=4:7.3.0-3ubuntu2 \
    linux-headers-4.15.0-23-generic \
    linux-image-4.15.0-23-generic \
    linux-image-4.15.0.23-generic-dbgsym \
    dumb-init \
    kpatch \
    fakeroot \
    kpatch-build \
    systemtap \
"
COPY build-kpatch.sh .
RUN ./build-kpatch.sh

ENTRYPOINT ["/usr/bin/dumb-init", "--"]
