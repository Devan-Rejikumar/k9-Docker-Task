1. Why are Docker containers stateless by default?

Containers are stateless because they are designed to be ephemeral and replaceable units of execution, not long-term storage systems. When a container runs, it gets its own writable filesystem layer on top of an image. This layer exists only for the lifetime of that container. Once the container is removed, that layer is destroyed along with any data inside it.

This design is intentional. Containers are meant to be easily created, destroyed, and recreated without worrying about leftover state. This makes scaling, deployment, and recovery simpler. But the tradeoff is that any data stored inside the container is not reliable, which is why persistence must be handled separately.

2. What is a Docker volume?

A Docker volume is a dedicated storage mechanism managed by Docker that exists independently of containers. Unlike container storage, a volume is not tied to any single container’s lifecycle.

When you create a volume, Docker allocates a space on the host machine (like /var/lib/docker/volumes/...) and manages it. Containers can then mount this volume and read/write data to it. Even if all containers using that volume are deleted, the volume and its data remain intact until explicitly removed.

3. How is a Docker volume different from normal container storage?

Normal container storage is part of the container’s writable layer. It is tightly coupled to the container lifecycle. When the container is deleted, this storage is also deleted automatically.

A Docker volume, on the other hand, is external to the container. When mounted, it replaces a specific path inside the container and redirects all read/write operations to a location on the host. Because of this separation, deleting the container does not affect the volume or its data. This is the key difference: container storage is temporary, volume storage is persistent.

4. Why does MySQL need persistent storage?

MySQL is a database, and databases are fundamentally designed to store and preserve data over time. The whole purpose of a database is to ensure that data remains available even after restarts, crashes, or system changes.

If MySQL runs inside a container without persistent storage, all database files (tables, indexes, records) are stored inside the container’s filesystem. If that container is removed, the entire database is lost. This makes the system useless in real-world scenarios.

That’s why MySQL must use persistent storage, so that data durability is guaranteed independently of the container lifecycle.

5. What does -v mysql-data:/var/lib/mysql mean?

This flag creates a mapping between a Docker volume and a directory inside the container.

mysql-data → the volume on the host
/var/lib/mysql → the directory inside the container where MySQL stores data

When this mapping is applied, Docker mounts the volume into that path. From the container’s perspective, MySQL is writing to /var/lib/mysql. But in reality, the data is being written to the volume’s location on the host.

So this command effectively redirects MySQL’s storage from temporary container storage to persistent volume storage.

6. What is the purpose of docker volume create?

The purpose of this command is to explicitly create a named volume that can be reused across containers. It ensures that storage is prepared and identifiable before attaching it to any container.

By creating a named volume, you gain control over:

Reusability across multiple containers
Clear identification (mysql-data)
Persistence independent of container lifecycle

It separates storage management from container execution.

7. What is the purpose of docker volume inspect?

This command provides detailed information about the volume, including where it is physically stored on the host, what driver it uses, and other metadata.

The most important field is the Mountpoint, which shows the actual path where the data resides. This helps you verify that:

The volume exists
Data is stored outside the container
Docker is managing the storage correctly

It’s a verification tool, not just informational.

8. What did docker inspect show about mounts?

docker inspect showed how the volume is attached to the container. Specifically, it revealed a mapping between:

Source → host location of the volume
Destination → path inside the container

This confirms that when the container accesses /var/lib/mysql, it is actually reading from and writing to the host storage. It proves that the volume is correctly mounted and actively being used by the container.

9. Why did the data survive after container deletion?

The data survived because it was stored in a Docker volume, not in the container’s filesystem. When the container was deleted, only its internal filesystem was removed. The volume remained untouched because it is managed separately by Docker.

When a new container was created and the same volume was mounted again, MySQL simply accessed the existing data in the volume. From MySQL’s perspective, nothing changed, because the storage location still contained all previous data.

10. Difference between deleting a container and deleting a volume?

Deleting a container removes the container and its internal filesystem, but it does not affect any volumes attached to it. The data stored in volumes remains intact.

Deleting a volume, however, removes the actual storage location on the host. This means all data stored inside that volume is permanently lost. So the container controls execution, while the volume controls data persistence.

11. Why is it dangerous to run a database without persistent storage?

Running a database without persistent storage means all data is stored inside the container. If the container crashes, is deleted, or is recreated, all data is lost instantly.

In production systems, this is unacceptable because it leads to data loss, system failure, and potential business impact. Persistent storage ensures that even if the application layer fails, the data layer remains safe.

12. Why was docker exec useful in this task?

docker exec allowed you to enter the running container and interact with it directly. Without it, you wouldn’t be able to access the MySQL client inside the container.

This is important because it lets you:

Run commands inside the container
Verify application behavior
Create and inspect real data

It bridges the gap between the host and the container environment.

13. What did docker stats and docker top show?

docker stats showed the runtime resource usage of the container, such as CPU, memory, disk I/O, and process count. This helps you understand how the container behaves under load.

docker top showed the actual processes running inside the container. In this case, it showed the mysqld process, which is the MySQL server.

Together, they provide visibility into:

What is running
How much resource it consumes
14. How does this help for Docker Compose and Kubernetes?

This task introduces the concept of decoupling storage from compute, which is fundamental in modern systems.

In Docker Compose, you will define volumes in a configuration file and attach them to services. In Kubernetes, this concept becomes Persistent Volumes (PV) and Persistent Volume Claims (PVC), which handle storage across distributed systems.

Without understanding volumes, you cannot properly design stateful applications in these environments.

15. What happens if the volume is removed?

If the volume is removed, the actual stored data is deleted permanently from the host. Any container that later tries to use that volume will start with empty storage.

This means:

All database data is lost
Any dependent applications lose their state

This is why deleting volumes is considered a critical and potentially destructive operation.