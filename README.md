# docker-scripts
A collection of Dockerfiles, Docker composer files, and other scripts.

## Running the containers inside a docker network

### Create a network (e.g. 'http_network')

```docker network create http_network```

It will default to 'bridge' type.

### Attach a container to a network

You can either:
```docker network connect http_network kamailio```
(where `kamailio` is the container name).

or when you run the container add `--net=http_network` to the command line (see READMEs in Dockerfiles).
