1. What is the main process inside a Docker container?
The main process inside a Docker container is the primary application or command defined by the image using CMD or ENTRYPOINT. Docker runs this process as PID 1 inside the container. The container’s lifecycle depends on this process, so as long as the main process is running, the container stays alive, and when it exits, the container stops.

2. Why does a container stop when the main process exits?
A Docker container runs only a single main process and does not have a background operating system to keep it alive. So when that main process exits, there is nothing left for Docker to run, and the container automatically stops.

3. Why did the busybox container exit immediately?
The busybox container exited immediately because its main process was the echo command, which runs, prints the message, and finishes instantly. Since the main process completed execution, there was no process left running inside the container, so Docker stopped the container.

4. Why did the nginx container keep running?
The nginx container kept running because its main process is the nginx web server, which is a long-running process that continuously listens for incoming requests. Since this process does not exit on its own, the container remains running as long as the nginx process is active.

5. What is the difference between a normal exit and a manual stop?
A normal exit occurs when the main process completes its execution on its own. A manual stop occurs when the user or Docker sends a signal, such as SIGTERM, to terminate the process externally. In both cases the container stops, but the reason differs: one is natural completion, the other is an external interruption.

6. What does exit code 0 usually indicate?
Exit code 0 indicates that the main process completed its execution successfully without any errors.

7. What is the purpose of docker logs in lifecycle debugging?
Docker logs are used to view the output of the main process running inside a container. They help in debugging by showing what the application is doing, including startup messages, runtime behavior, and any errors or crashes that occur.

8. What is the purpose of docker inspect in lifecycle debugging?
Docker inspect is used to get detailed internal information about a container in JSON format. It helps in lifecycle debugging by providing key data such as container state, exit code, start and stop timestamps, and configuration details, which allow us to understand how and when the container ran or stopped.

9. What is the purpose of docker top?
Docker top is used to view the running processes inside a container. It helps in debugging by allowing us to verify whether the correct main process is running and to identify any unexpected or missing processes inside the container.

10. What is the difference between docker start and docker run?
Docker run creates a new container from an image and starts it, whereas docker start is used to restart an existing stopped container without creating a new one.

11. What is the difference between docker stop and docker rm?
Docker stop is used to terminate the running container by stopping its main process, but the container still exists in a stopped state. Docker rm is used to permanently delete a stopped container from the system.

12. What is the difference between docker start and docker restart?
Docker start is used to start a container that is already stopped. Docker restart is used to restart a running container by first stopping it (sending a signal like SIGTERM) and then starting it again.

13. Why is it important to understand lifecycle state before debugging production containers?
It is important to understand the container lifecycle before debugging because it helps avoid wrong assumptions and identify the real cause of failure. By checking the container’s state, exit code, logs, and timestamps, we can determine whether the container stopped due to a normal exit, an error, or a manual stop, which makes debugging more accurate and efficient.

14. How is a container lifecycle different from a virtual machine lifecycle?
A container’s lifecycle is tied to its main process, and it does not have its own operating system or background services. So when the process stops, the container also stops. In contrast, a virtual machine runs a full operating system with background processes, so it continues running even if an application inside it stops.

15. How does this task prepare the learner for real Docker troubleshooting?
This task prepares the learner for real Docker troubleshooting by teaching how to understand container lifecycle behavior and use debugging tools effectively. It helps in identifying why a container started or stopped by using logs, inspect, and exit codes, and builds the ability to analyze issues instead of guessing. This makes debugging in production more accurate and structured.