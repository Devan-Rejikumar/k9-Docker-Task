1. What is Docker Compose?

Docker Compose is a tool that allows you to define and run multiple containers together using a single YAML file called docker-compose.yml. Instead of starting containers one by one using separate commands, you describe all the services, configurations, networks, and volumes in one place. Then with a single command, Docker Compose creates and runs the entire application stack. It basically converts manual setup into a structured and repeatable configuration.

2. Why is Compose preferred over manually running multiple containers?

Running multiple containers manually is messy and error-prone because you have to remember many things like network creation, environment variables, ports, and the correct startup order. If you make a mistake, the system may not work. Docker Compose solves this by letting you define everything in one file, so the setup becomes consistent, reusable, and easier to manage. It saves time, reduces errors, and makes the system easier to understand and maintain.

3. What is a service in Docker Compose?

A service in Docker Compose represents a single container definition. It includes details like which image to use, what environment variables to pass, what ports to expose, and how it connects to other services. For example, in this task, db, wordpress, and phpmyadmin are all services. Each service runs as its own container, but they are managed together as one application.
A service defines:

Which image to run
Environment variables
Ports
Volumes
Network

👉 For that one component only

4. How does Compose handle networking by default?

Docker Compose automatically creates a network and connects all services to it, enabling them to communicate using service names. All containers are connected to this shared network, which allows them to communicate with each other. You don’t need to manually create or connect networks. This automatic networking makes service-to-service communication simple and reliable.

5. Why does db work as the database host for WordPress and PhpMyAdmin?

In Docker Compose, each service name acts as a hostname inside the network. So the service named db becomes accessible using the name db. Docker provides internal DNS resolution, which means when WordPress or PhpMyAdmin tries to connect to db, Docker automatically maps it to the correct container. This removes the need to use IP addresses, which can change and are not reliable.

6. What is the purpose of depends_on?

The depends_on keyword is used to define the startup order of services. It tells Docker Compose to start one service before another. For example, WordPress depends on the database, so depends_on: db ensures the database container starts first. However, it only controls the order of starting, not whether the service is fully ready.

7. What is the purpose of the named volume in this task?

The named volume is used to store MySQL database data outside the container. Containers are temporary, so if a container is removed, its internal data is lost. By using a volume, the data is stored on the host system, which means it persists even if the container stops or is deleted. This is essential for databases because data should never be lost.

8. What did docker compose logs help you observe?

The docker compose logs command helped observe how each service started and whether they were working correctly. It showed messages from MySQL, WordPress, and PhpMyAdmin, confirming that the database was initialized, WordPress connected to it, and all services were running without errors. Logs are important for debugging and understanding system behavior.

9. What did docker network inspect reveal?

The docker network inspect command showed that all the containers were connected to the same network and had internal IP addresses. It also showed that each container was part of the Compose-created network. This confirmed that the services could communicate with each other using service names instead of IP addresses.

10. What did docker volume inspect reveal?

The docker volume inspect command showed that the database data is stored in a specific location on the host system, not inside the container. It provided details like the volume name and its mount path. This confirmed that the data is persistent and independent of the container lifecycle.

11. What is the difference between docker compose up -d and docker compose down?

The command docker compose up -d is used to start all the services defined in the Compose file in detached mode, meaning they run in the background. On the other hand, docker compose down stops and removes all the containers and the network created by Compose. So, one command starts the system, and the other shuts it down.

12. What remains after docker compose down, and why?

After running docker compose down, the containers and network are removed, but the volumes remain. This happens because Docker is designed to protect persistent data. Since volumes store important data like databases, they are not deleted automatically to prevent accidental data loss.

13. What happens if docker compose down -v is used?

When you use docker compose down -v, it removes everything, including the volumes. This means all persistent data stored in the volume will be deleted permanently. In this task, it would delete the MySQL database data, resulting in complete data loss.

14. Why is this task important before learning more advanced orchestration platforms?

This task is important because it teaches the core concepts of managing multiple services, such as networking, service communication, environment configuration, and lifecycle management. These are the same concepts used in advanced tools like Kubernetes. Without understanding Docker Compose, it becomes difficult to understand how larger systems are managed.

15. How does this task reflect real multi-service application management?

In real-world applications, systems are made up of multiple services like frontend, backend, database, and monitoring tools. This task reflects that by running WordPress, MySQL, and PhpMyAdmin together as one system. It shows how services interact, how they are configured, and how the entire application can be managed as a single unit, which is exactly how modern applications are built and deployed.