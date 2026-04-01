1. What is the difference between a Docker image and a Docker container?
A Docker image is a stored template like busybox, which contains a filesystem and tools.

A Docker container is a temporary instance created from that image, where a specific command runs.

In my task:
- busybox was the image
- each docker run created a new container
- inside each container, a command like echo or ls was executed
- after the command finished, the container stopped


2. What command did the busybox container execute?
The main process inside the container was the `echo` command, which printed "Hello from Docker".
Main process = echo
Argument = "Hello from Docker"

3. Why did the container stop after the command finished?
The container stopped because its main process, echo, finished execution. 
A container only runs as long as its main process is running. 
Once the process ends, the container has nothing to do, so it stops.

4. Why does the container not appear in docker ps but appear in docker ps -a?
docker ps shows only running containers. 
Since the echo process finished, the container stopped, so it is not shown in docker ps. 
docker ps -a shows all containers, including stopped ones, so it appears there.

5. Why is a container exit not always an error?
A container exit is not an error if the main process completes successfully. 
In this case, echo finished its job, so the container exited normally.

6. What is the purpose of docker logs?
docker logs is used to view the output of the main process inside the container. 
In this case, the echo command printed "Hello from Docker", and docker logs shows that output even after the container has stopped.

7. What is the purpose of docker rm?
docker rm is used to delete a stopped container from the system. 
It removes the container’s metadata and history since it is no longer needed after the process has finished.

8. Why can multiple containers be created from the same image?
Multiple containers can be created from the same image because an image is just a reusable template.
In this task, I used the same busybox image to create different containers:
- one ran echo and printed a message
- another ran ls and listed files
Each docker run created a new, separate container from the same image.

9. What is the main process idea in a container?
A container runs a single main process, which is the command we give.
In this task:
- echo was the main process in one container
- ls was the main process in another container
The container stays alive only as long as this main process is running. 
When the process ends, the container stops.

10. How does this task help later when debugging containers in production?
This task helps in debugging because it teaches how containers behave at runtime.
In production, if a container stops, I now know to check:
- what main process was running
- whether it finished or crashed
- the logs to see what output or error occurred
Since containers stop when the process ends, I can understand whether it exited normally or due to an issue, instead of assuming it's always an error.