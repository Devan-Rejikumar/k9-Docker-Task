1. What is a Dockerfile?
A Dockerfile is a set of instructions used to build a Docker image. It defines the base environment, application code, dependencies, and the command to run when a container starts.

2. Why is a Dockerfile required when packaging an application into an image?
A Dockerfile is required to define a reproducible and consistent way to build an image. It ensures that the application, its dependencies, and environment are packaged the same way every time, making it portable and reliable across systems.

3. What does docker build do?
Docker build reads the Dockerfile and executes its instructions step by step to create a Docker image. Each step forms a layer, making the image reusable and efficient to rebuild.

4. What does docker run do?
Docker run creates and starts a container from an image. It also applies runtime configurations like port mapping, naming, and environment settings.

5. What is the purpose of requirements.txt in this task?
The requirements.txt file defines the application’s dependencies so they can be installed during the image build. It ensures the same environment is recreated inside the container every time.

6. Why must the Flask app bind to 0.0.0.0 inside the container?
Binding to 0.0.0.0 allows the Flask app to accept requests from outside the container, while 127.0.0.1 would restrict it to inside the container only.

7. What does -p 5000:5000 mean?
The -p 5000:5000 flag maps the host port 5000 to the container port 5000, allowing requests from the host machine to reach the application running inside the container.

8. What is the purpose of WORKDIR in the Dockerfile?
WORKDIR sets the default folder inside the container, so all following commands run from that location.

9. Difference between RUN and CMD
RUN and CMD serve different purposes in a Dockerfile. RUN is used during the image build process to execute commands like installing dependencies and setting up the environment, and it creates layers in the image. CMD is used when the container starts and defines the default command or main process that runs inside the container. While RUN has no effect at runtime, CMD controls the container’s lifecycle, so when the CMD process stops, the container also stops. 

10. Which project files are included in the Docker image?
The project files included in the Docker image are the ones copied using the COPY instruction in the Dockerfile. In this task, that includes app.py, requirements.txt, and any other files present in the project directory.


11. What is the purpose of docker logs in this task?
Docker logs is used to view the output of a running container, including application logs, errors, and request details. In this task, it helps verify that the Flask app started correctly and to debug any issues if the application is not working as expected.

12. What is the purpose of docker inspect in this task?
Docker inspect is used to view detailed metadata about a container. In this task, it helps check information like the container’s IP address, port mappings, and current state to understand how the container is running.

13. What is the purpose of docker exec in this task?
Docker exec is used to run commands inside a running container. In this task, it allows us to enter the container and inspect its internal files and environment, which helps in debugging and verifying that the application is set up correctly.

14. Why did the Flask container stay running?
The container stays running because the main process defined by CMD, which is the Flask application, runs continuously in the foreground. Since Docker ties the container’s lifecycle to this process, the container remains active as long as the process is running, and stops immediately when the process exits.

15. Why does removing the container not remove the image?
Removing a container does not remove the image because a container is just a running instance of an image. The image acts as a blueprint, and multiple containers can be created from the same image. Since they have separate lifecycles, deleting a container does not affect the underlying image.

16. How does this task prepare the learner for production container workflows?
This task prepares the learner for production workflows by teaching how to package an application into a Docker image, run it as a container, and verify its behavior. It also introduces essential debugging practices using commands like docker logs, inspect, and exec. These are fundamental skills used in real-world environments to deploy, monitor, and troubleshoot containerized applications reliably.