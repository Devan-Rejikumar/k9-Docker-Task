1. What is a Docker bridge network?

A Docker bridge network is a private internal network created by Docker that allows multiple containers to communicate with each other while remaining isolated from the host and other networks. Each container connected to a bridge network gets its own internal IP address, and Docker handles routing between them. In user-defined bridge networks, Docker also provides built-in DNS, allowing containers to communicate using names instead of IP addresses.

2. Why was a custom Docker network created in this task?

A custom network was created to enable proper communication between containers using Docker’s internal DNS system. Unlike the default bridge network, a user-defined network allows containers to resolve each other by name, making communication more reliable and production-friendly. It also provides better isolation and control, ensuring that only containers in the same network can interact.

3. Why does localhost not work for container-to-container communication?

Localhost inside a container refers only to that container itself, not to other containers. Each container runs in its own isolated environment with its own network namespace. So if PhpMyAdmin tries to connect to localhost, it is trying to connect to itself, not the MySQL container. That is why localhost cannot be used for communication between containers.

4. Why does using the container name mysql-net-demo work?

The container name works because Docker provides an internal DNS system in user-defined networks. When PhpMyAdmin uses mysql-net-demo as the host, Docker automatically resolves that name to the internal IP address of the MySQL container. This allows containers to communicate reliably without needing to know or manage IP addresses manually.

5. How does Docker resolve one container name to another container on the same network?

Docker runs an internal DNS service for each user-defined network. When a container tries to connect to another container using its name, Docker intercepts the request and resolves that name to the corresponding container’s IP address within the network. This process is automatic and happens only if both containers are attached to the same network.

6. Why is using container names better than using hardcoded IP addresses?

Container names are stable, while IP addresses are dynamic and can change whenever a container is restarted or recreated. If you hardcode an IP, your system becomes fragile and breaks easily. Using container names ensures that communication remains consistent, readable, and maintainable, which is essential in real-world systems where containers are frequently restarted or scaled.

7. What did docker network inspect app-net show you?

This command showed all the details of the custom network, including the list of connected containers, their internal IP addresses, and network configuration such as subnet and gateway. It confirmed that both MySQL and PhpMyAdmin were attached to the same network, which is necessary for communication between them.

8. What did docker inspect mysql-net-demo show about networking?

This command showed that the MySQL container was connected to the custom network and had an assigned internal IP address. It also revealed that the container had DNS names, including its container name, which other containers can use to connect to it. This confirmed that MySQL was properly configured for network communication.

9. Why was PhpMyAdmin exposed to the host, but MySQL was not?

PhpMyAdmin was exposed because it is a web interface that needs to be accessed through a browser from the host system. MySQL, on the other hand, is an internal service that should only be accessed by other containers within the network. Exposing MySQL would be unnecessary and could create security risks, so it is kept internal.

10. What is the purpose of docker port in this task?

The docker port command shows how a container’s internal ports are mapped to the host machine. In this task, it confirmed that PhpMyAdmin’s internal port 80 was mapped to port 8081 on the host, allowing browser access. It helps verify that external access to a container is correctly configured.

11. What is the purpose of docker stats in this task?

The docker stats command provides real-time information about container resource usage, such as CPU, memory, and network usage. In this task, it was used to observe how much system resources each container consumes, which is important for monitoring performance and understanding how services behave under load.

12. What would happen if the two containers were not attached to the same network?

If the containers were on different networks, they would not be able to communicate directly because Docker isolates networks from each other. The PhpMyAdmin container would not be able to resolve or connect to the MySQL container, and the database connection would fail.

13. Why is this task important before learning Docker Compose?

Docker Compose is used to manage multi-container applications, but it relies heavily on networking concepts like service names and shared networks. Without understanding how containers communicate and how networks work, it becomes difficult to configure and debug Compose setups properly.

14. How does this task reflect real multi-service application design?

Real-world applications consist of multiple services such as frontend, backend, databases, and caches that need to communicate with each other. This task simulates that setup by connecting a UI service (PhpMyAdmin) with a database (MySQL), showing how services interact over a network in a structured way.

15. How does this task help later in debugging service connectivity problems?

This task teaches how to inspect networks, verify container connections, and check configuration details like environment variables and DNS resolution. These skills are essential for diagnosing issues such as failed connections, incorrect hostnames, or misconfigured networks in real systems.