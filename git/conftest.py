from testcontainers.compose import DockerCompose


def setup_git_server():
    with DockerCompose("git",
                    compose_file_name=["docker-compose-git.yml"],
                    pull=True) as compose:
        print("STARTED")
        host = compose.get_service_host("git", 2222)
        port = compose.get_service_port("git", 2222)
        print(f"{host}:{port}")
        print("STOPPED")


if __name__ == "__main__":
    container = setup_git_server()
    container.stop()