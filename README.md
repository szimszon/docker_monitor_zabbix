# Monitoring Docker with Zabbix

Tested with Zabbix 2.4 (http://www.zabbix.com/) and Docker 1.5 (https://www.docker.com/).

## Install

1. Add a line from 'sudo' file to your sudo config
2. copy 'zabbix-docker-discovery.py' and 'zabbix-docker-stats.py' to '/usr/local/bin'
3. make it executable with root user
4. copy 'userparameter_docker.conf' to '/etc/zabbix/zabbix_agentd.d/'
5. You need to have 'EnableRemoteCommands=1' in Zabbix agent config
6. restart zabbix-agent
7. Import 'docker_zbx_export_templates.xml' into Zabbix and configure it

## The template contains

### Discover docker containers

#### Items

* {#NAME} kernelmode cpu usage
* {#NAME} memory fail count
* {#NAME} memory max usage
* {#NAME} memory total
* {#NAME} memory usage
* {#NAME} network received bytes
* {#NAME} network received packages
* {#NAME} network received packages dropped
* {#NAME} network received packages errors
* {#NAME} network transmitted bytes
* {#NAME} network transmitted packages
* {#NAME} network transmitted packages dropped
* {#NAME} network transmitted packages errors
* {#NAME} stats scheduler
* {#NAME} system cpu usage
* {#NAME} total cpu usage
* {#NAME} usermode cpu usage

#### Graphs

* {#NAME} CPU
* {#NAME} Memory
* {#NAME} network

