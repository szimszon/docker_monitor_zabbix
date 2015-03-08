#!/usr/bin/env python

import sys
import simplejson
from docker import Client
c = Client(base_url='unix://var/run/docker.sock')

containers=c.containers()

if not containers:
  sys.exit(0)

container_list=[{"{#ID}":container["Id"],
                 "{#NAME}":container["Names"][0]} for container in containers]
discovery={"data": container_list}
print simplejson.dumps(discovery)


