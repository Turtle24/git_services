from testcontainers.compose import DockerCompose


def setup_bitbucket_server():
    with DockerCompose("bitbucket",
                    compose_file_name=["docker-compose-bitbucket.yml"],
                    pull=True) as compose:
        print("STARTED")
        host = compose.get_service_host("bitbucket", 4000)
        port = compose.get_service_port("bitbucket", 4000)
        print(f"{host}:{port}")
        print("STOPPED")


if __name__ == "__main__":
    setup_bitbucket_server()