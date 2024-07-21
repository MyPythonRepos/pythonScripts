#!/usr/bin/python3
import docker


client = docker.from_env()
for container in client.containers.list():
# pendiente de ajustar alineación para mostrar los puertos
#  ports = ""
#  for port in container.attrs['Config']['ExposedPorts']:
#    ports = port.rstrip()
  print ('{:22} {}'.format(container.attrs['Name'].replace('/',' '), container.status))
