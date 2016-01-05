FROM ubuntu:14.04

MAINTAINER Giacomo Vacca "giacomo.vacca@gmail.com"

### RUN apt-get update && apt-get -y -q install sip-tester vim ngrep tcpdump ssldump && rm -rf /var/lib/apt/lists/*
RUN apt-get update \
    && apt-get -y -q install sip-tester \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /root/sipp
WORKDIR /root/sipp

################################################
# Build:
### docker build -t gvacca/sipp .

# Run in interactive mode and attach to existing network:
### docker run -i -t -v $PWD/scenarios/:/root/sipp/ --name=sipp --net=http_network gvacca/sipp /bin/bash
