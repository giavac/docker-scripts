# Prepare a container to run sipp

## Build

```docker build -t gvacca/sipp .```

## Run in interactive mode and attach to existing network (e.g. 'http_network')

```docker run -i -t -v $PWD/scenarios/:/root/sipp/ --name=sipp --net=http_network gvacca/sipp /bin/bash```

Scenarios are expected at `$PWD/scenarios/`
