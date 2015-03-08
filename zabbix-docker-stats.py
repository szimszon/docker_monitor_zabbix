#!/usr/bin/env python

import sys
import simplejson
import os
from docker import Client

not_want=[
"docker.memory_stats.stats",
"docker.blkio_stats",
"docker.cpu_stats.throttling_data"
]

class ErrorSendingValues(RuntimeError):
    """ An error occured while sending the values to the Zabbix 
    server using zabbix_sender. 
    """

def send_data(key,value):
  print "["+str(key)+"] {"+str(value)+"}"
  key=str(key)+"["+str(sys.argv[1])+"]"
  r = os.system("%s -c '%s' -k '%s' -o '%s' -vv" % ('/usr/bin/zabbix_sender', '/etc/zabbix/zabbix_agentd.conf', str(key), str(value)))
  if r != 0:
    pass
    #raise ErrorSendingValues, "An error occured sending the values to the server ["+str(key)+"]"


def unfold_data(key,obj):
  if key in not_want:
    return True
  if isinstance(obj,dict):
    for k in obj:
      lkey=str(key)+"."+str(k)
      if lkey in not_want:
        continue
      unfold_data(lkey,obj[k])
  else:
    send_data(key,obj)

c = Client(base_url='unix://var/run/docker.sock')

stats_obj = c.stats(sys.argv[1])

for stat in stats_obj:
  stat=simplejson.loads(stat)
  unfold_data("docker",stat)
  sys.exit(0)


