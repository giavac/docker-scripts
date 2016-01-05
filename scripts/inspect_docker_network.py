#!/usr/bin/python

# Get the output of 'docker network inspect' for a given network
# and return containers names and their IP address

import json
import subprocess
import sys

network_name = sys.argv[1]
network_json = subprocess.check_output(["docker", "network", "inspect", network_name])
network = json.loads(network_json)
containers = network[0]['Containers']

for container_id in containers:
    container_name = subprocess.check_output(["docker", "inspect", "--format", "'{{ .Name }}'", container_id])
    print container_id + " " + container_name.strip() + ": " + containers[container_id]['IPv4Address']
