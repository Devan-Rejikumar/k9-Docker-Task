1. Did the broken Dockerfile fail at build time, runtime, or both?
The broken Dockerfile did not fail at build time or runtime. The image built successfully and the container ran without any errors. However, it was incorrect in terms of design because it did not use requirements.txt for dependency management and only copied a single file, making it non-reproducible and not scalable.

2. What did you observe during the first docker build attempt?
During the first docker build, the image was built successfully without any errors. Docker pulled the base image, set the working directory, copied app.py into the container, and installed Flask using pip. Since all required instructions were valid and no files were missing, the build completed successfully.

3. What did you observe when running the broken container?
When running the broken container, it started successfully and remained in the running state. The container did not exit or crash. The application was accessible through the mapped port, indicating that there was no runtime failure.

4. What did docker logs reveal?
Docker logs showed that the Flask application started successfully. It displayed messages indicating that the app was running on 0.0.0.0:5000 and there were no errors or crashes in the logs.

5. What did docker inspect reveal?
Docker inspect revealed that the container state was running and the application was active. It also showed that port 5000 inside the container was correctly mapped to port 5000 on the host, confirming that networking was properly configured.

6. What exactly was wrong in the original Dockerfile?
The original Dockerfile had two main issues. It did not use requirements.txt for dependency installation and instead installed Flask directly, which makes it non-reproducible. It also copied only app.py into the container instead of the entire project, which makes it non-scalable and can lead to missing files in larger applications.

7. Why is installing dependencies from requirements.txt better than installing them ad hoc?
Installing dependencies from requirements.txt ensures that all required packages are installed consistently with specific versions. This makes the build reproducible and prevents missing dependency issues, whereas installing dependencies manually can lead to incomplete or inconsistent setups.

8. Why must required files be copied into the image explicitly?
Required files must be copied into the image explicitly because Docker containers are isolated environments and do not have access to the host file system. If files are not copied, they will not exist inside the container, leading to runtime errors.

9. What specific changes fixed the issue?
The issue was fixed by adding COPY requirements.txt and installing dependencies using pip install -r requirements.txt instead of installing Flask directly. Additionally, the Dockerfile was updated to copy the entire project using COPY . . instead of copying only app.py.

10. What is the difference between a build-time problem and a run-time problem?
A build-time problem occurs during the docker build process when the image is being created, such as missing files or dependency installation failures. A run-time problem occurs when the container is running, such as application crashes or service not being accessible.

11. Why is docker logs important in container debugging?
Docker logs are important because they show the output of the application running inside the container. They help identify runtime issues such as errors, crashes, or misconfigurations by providing direct insight into what the application is doing.

12. Why is docker inspect important in container debugging?
Docker inspect is important because it provides detailed metadata about the container, including its state, configuration, and networking. It helps verify whether the container is running correctly and whether ports and other settings are properly configured.

13. Why is docker exec useful during debugging?
Docker exec is useful because it allows us to enter a running container and interact with it directly. This helps in debugging by inspecting files, checking installed dependencies, and running commands inside the container environment.

14. Why should you apply minimal fixes instead of rewriting everything blindly?
Minimal fixes should be applied to isolate the root cause of the issue. Rewriting everything blindly can introduce new errors and makes it difficult to identify what actually solved the problem.

15. How does this task help in real production Docker troubleshooting?
This task helps in real production troubleshooting by teaching an evidence-based debugging approach. It shows how to use tools like docker logs and docker inspect to analyze container behavior and identify issues, even when the application appears to be working. It also emphasizes applying minimal fixes and understanding root causes instead of guessing.

