1. What is Public Cloud?

Public cloud refers to a model where computing infrastructure such as servers, storage, and networking is owned and managed by a cloud provider like Amazon Web Services and made available to users over the internet. Instead of buying and maintaining physical hardware, organizations can provision resources on demand and pay only for what they use. The key problem it solves is the cost and complexity of managing physical infrastructure. It removes the need for upfront investment, reduces operational overhead, and allows systems to scale quickly. In this model, AWS handles the underlying hardware, data centers, and availability, while the user is responsible for configuring and managing their own applications and resources on top of it.

2. What is a VPC?

A VPC, or Virtual Private Cloud, is a logically isolated network within AWS where you can launch and manage your resources. It acts like your own private data center inside the cloud, where you control the IP address range, create subnets, and define how traffic flows. The purpose of a VPC is to give you full control over networking while still using shared cloud infrastructure. Without a VPC, you would not be able to structure or secure your application properly. It allows you to separate different parts of your system, control communication, and build scalable architectures in a controlled environment.

3. Why is CIDR planning important?

CIDR planning is important because it defines the size and structure of your network. When you choose a CIDR block, you are deciding how many IP addresses your VPC will have and how you can divide that space into subnets. A poorly chosen CIDR can lead to serious limitations, such as running out of IP addresses or being unable to create additional subnets later. It can also cause problems when connecting multiple networks if address ranges overlap. Proper CIDR planning ensures that your network is scalable, organized, and flexible enough to support future growth without requiring major redesign.

4. What makes a subnet “public”?

A subnet is considered public not because of its name or location, but because of its routing configuration. Specifically, a subnet becomes public when it is associated with a route table that has a route directing external traffic, typically 0.0.0.0/0, to an Internet Gateway. This route provides a path for resources inside the subnet to communicate with the internet. Without this route, even if an Internet Gateway exists, the subnet remains private because there is no defined path for external communication. So the defining factor of a public subnet is the presence of a route to the Internet Gateway.

5. What role does the Internet Gateway play?

An Internet Gateway is a component that enables communication between a VPC and the internet. It acts as a bridge that allows traffic to flow in and out of the VPC. However, it does not control or initiate traffic by itself. It only works when the route table directs traffic to it. This means that even if an Internet Gateway is attached to a VPC, it remains unused unless there is a proper route configured. Its role is purely to provide a connection point, making it possible for resources in public subnets to send requests to the internet and receive responses.

6. Why should we avoid using the default VPC in production?

The default VPC is automatically created by AWS to help beginners quickly launch resources without manual configuration. While it is convenient, it is not suitable for production environments because it is preconfigured with permissive settings and lacks proper structure. It does not enforce clear separation between public and private resources, and it limits control over network design. In production, we need well-defined architecture, controlled access, and proper segmentation of resources. Creating a custom VPC ensures that the network is designed according to specific requirements, making it more secure, scalable, and maintainable.