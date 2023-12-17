#!/usr/bin/python3
import docker


client = docker.from_env()
for container in client.containers.list():
  print ('{:40} {}'.format(container.attrs['Config']['Image'], container.status))
