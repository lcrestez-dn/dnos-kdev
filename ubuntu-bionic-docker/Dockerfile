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

RUN apt-get install -y --no-install-recommends \
    dumb-init \
    kpatch \
    linux-headers-4.15.0-23-generic \
    linux-image-4.15.0-23-generic \
    linux-image-4.15.0.23-generic-dbgsym \
    systemtap

ENTRYPOINT ["/usr/bin/dumb-init", "--"]
