1. What is a Docker image layer?

A Docker image layer is a read-only snapshot created for each instruction in a Dockerfile. Every command like FROM, COPY, or RUN creates a new layer, and these layers stack on top of each other to form the final image. This layered structure allows Docker to reuse unchanged parts of the image instead of rebuilding everything again.

2. How does Docker decide whether a cached step can be reused?

Docker checks three things: the instruction itself, the files involved in that step, and all previous layers. If the command is the same and the files used in that step have not changed, Docker reuses the cached layer. But if anything changes, that layer becomes invalid and must be rebuilt.

3. Why was the second build faster when nothing changed?

The second build was faster because Docker reused all the previously built layers from cache. Since there were no changes in the Dockerfile or project files, Docker didn’t execute any commands again and simply reused the existing layers, saving time.

4. Why did changing app.py rebuild fewer layers than changing requirements.txt?

Changing app.py affects only the layer where the application code is copied. So Docker rebuilds that layer and the ones after it, but earlier layers like dependency installation remain cached. On the other hand, changing requirements.txt affects an earlier step, so dependency installation runs again and all subsequent layers also rebuild.

5. Why does changing one step often cause later steps to rebuild too?

Docker builds images sequentially from top to bottom. Each layer depends on the previous one. So if one layer changes, all layers after it are based on a different state and must be rebuilt, even if their instructions didn’t change.

6. Why does Docker process the Dockerfile top to bottom?

Docker processes instructions in order because each step builds on the result of the previous step. This ensures consistency and correctness. If Docker skipped steps or changed the order, the final image would not be predictable or reliable.

7. Why is requirements.txt usually copied before application source files?

requirements.txt is copied earlier so that dependency installation can be cached. Since dependencies don’t change frequently, this allows Docker to reuse the expensive pip install layer even if application code changes later, making builds faster.

8. Why should frequently changing files usually be copied later in the Dockerfile?

Files that change often, like application code, should be copied later so that only the last few layers need rebuilding. If they are copied early, even small changes will invalidate many layers and cause unnecessary rebuilds, slowing down the process.

9. What does docker history help you understand?

docker history shows all the layers in an image, along with the command that created each layer and their sizes. It helps you understand how the image was built and identify which steps are large or expensive, which is useful for optimization.

10. How does Docker build cache help in CI/CD pipelines?

In CI/CD pipelines, Docker cache reduces build time by reusing unchanged layers instead of rebuilding everything. This makes deployments faster, reduces resource usage, and improves overall efficiency of the pipeline.

11. Why does Dockerfile instruction order matter in production?

The order of instructions affects how much of the image can be cached. If the order is poor, small changes can trigger large rebuilds, increasing build time and cost. In production, this directly impacts deployment speed and scalability.

12. How does this task prepare the learner for later image optimization work?

This task builds the foundation for optimization by teaching how layers and caching work. Once you understand which steps are expensive and how cache behaves, you can design better Dockerfiles, reduce image size, and improve build performance in real-world projects.