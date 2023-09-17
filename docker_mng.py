import docker

def run():
    client = docker.DockerClient(base_url='tcp://192.168.1.212:2375', tls=False)
    #images = client.images.list()
    #i = 1
    #for image in images:
    #    print(f"{i}: {image.id}")
    #    i=i+1

    #client.images.pull('busybox', tag='stable')
    print("############################")
    print("Información sobre el cluster")
    print("############################")
    print(client.swarm.attrs['JoinTokens']['Manager'])
    print("#########################################")
    print("Información sobre los nodos de un cluster")
    print("#########################################")
    nodes = client.nodes.list()
    for node in nodes:
        print(f'id: {node.id} y short id: {node.short_id}. hostname: {node.attrs["Description"]["Hostname"]}' )

    print("###########################################")
    print("Información sobre los servicios desplegados")
    print("###########################################")
    services_list = client.services.list()
    for service in services_list:
        ports = service.attrs["Endpoint"]["Spec"]["Ports"][0]["PublishedPort"]
        print(f'Servicio {service.name} - version: {service.version} - {ports}' )


if __name__ == "__main__":
    run()
