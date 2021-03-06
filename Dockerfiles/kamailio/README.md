# Dockerfiles to prepare a base image to build Kamailio

## Build
```docker build -t gvacca/kamailio_async:ubuntu14 -f Dockerfile.ubuntu14 .```

## Run interactively inside an existing network (e.g. 'http_network'):
```docker run -i -t --net=http_network --name=kamailio_async_ubuntu -v $PWD:/root/kamailio/ gvacca/kamailio_async:ubuntu14 /bin/bash```

where you assume `$PWD` contains the source code you're going to change/build.

Then inside the container you'll want to do something like:

```make cfg && make all && make install```

and edit configuration as needed

## Enter inside the running container:
```docker exec -i -t kamailio_async_ubuntu /bin/bash```

## Run in other ways (ensure the source code is reachable from /root/kamailio):
```docker run -d -p 6050:5060/udp gvacca/kamailio_async_ubuntu14```
```docker run -i -t -p 6050:5060/udp gvacca/kamailio_async_ubuntu14 /bin/bash```
