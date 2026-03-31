1. What is Docker?

Docker is a platform that allows you to run applications inside containers, which are isolated environments that package the application along with its dependencies while sharing the host operating system kernel.

2. What is the Docker daemon, and what is its responsibility?

The Docker daemon is the background service (dockerd) that performs all Docker operations. It is responsible for pulling images, creating containers, running them, and managing Docker resources like networks and volumes.

It is the actual worker, not the CLI.

3. What is the Docker CLI?

The Docker CLI is the command-line interface (docker) used by the user to interact with Docker. It sends commands to the Docker daemon but does not execute them itself.

4. How does the Docker CLI communicate with the Docker daemon?

The Docker CLI communicates with the Docker daemon using a REST API, typically through a Unix socket (/var/run/docker.sock).

 Flow: CLI → API → Daemon

5. What is a Docker registry?

A Docker registry is a storage system for Docker images. It allows users to pull and push images.

Example: Docker Hub

6. Explain Docker architecture (client, daemon, registry)

Docker has three main components:

Client (CLI): where commands are given
Daemon: executes the commands
Registry: stores Docker images

Flow:
 CLI sends request → daemon processes it → pulls image from registry if needed → runs container

7. Why is Docker considered lightweight compared to virtual machines?

Docker is lightweight because containers share the host operating system kernel, whereas virtual machines run a full operating system for each instance. This reduces memory usage and improves performance.

8. What parts are packaged inside a Docker image, and what parts are shared from the host OS?

Inside the Docker image:

application code
dependencies
runtime

Shared from host:

operating system kernel
9. Why did hello-world run and then exit?

The hello-world container runs a simple program that prints a message and then stops. Since there is no long-running process, the container exits after execution.

 Container runs only as long as the main process runs.

10. Why is verifying Docker setup important?

Verifying Docker setup ensures that the Docker CLI, daemon, and registry communication are all working correctly. If the setup is incorrect, future tasks like building and running containers will fail and become difficult to debug.