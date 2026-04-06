1. Why do we need a NAT Gateway?

A NAT Gateway is used when we have instances inside a private subnet that need to access the internet, but we don’t want the internet to directly access those instances. Since private subnets don’t have a route to the Internet Gateway, they cannot go out by themselves. So the NAT Gateway acts like a middle layer placed in the public subnet. The private instance sends its request to the NAT Gateway, and the NAT Gateway sends it to the internet on its behalf. The response comes back through the NAT, keeping the private instance hidden and secure.

2. Why is one NAT Gateway for multiple AZs a bad design?

Using one NAT Gateway for multiple Availability Zones is a bad design because it creates a dependency on a single AZ. If that AZ goes down, all private subnets in other AZs lose internet access even though they are healthy. Also, traffic from other AZs has to cross AZ boundaries, which increases latency and cost. In production, we always keep one NAT per AZ so that each AZ works independently and avoids failure impact.

3. What happens if NAT in AZ1 fails in your current setup?

In the current setup, each AZ has its own NAT Gateway and route table. So if the NAT Gateway in AZ1 fails, only the private subnet in AZ1 loses internet access. The private subnet in AZ2 will continue working normally because it uses its own NAT Gateway. This ensures fault isolation and high availability, which is the main goal of this design.

4. Why do we need separate route tables per AZ?

We need separate route tables per AZ so that each private subnet can route traffic to its own NAT Gateway. If we use a single route table, both subnets may end up using the same NAT, which breaks the isolation and creates cross-AZ dependency. By having separate route tables, we ensure that traffic from AZ1 goes only to NAT-az1 and traffic from AZ2 goes only to NAT-az2, making the system more reliable and scalable.

5. What is a blackhole route and why is it dangerous?

A blackhole route is a route that points to a resource that no longer exists, like a deleted NAT Gateway. AWS marks it as “blackhole” because traffic sent through that route will be dropped. This is dangerous because everything may look fine in configuration, but traffic will silently fail. In production, this can cause outages and is considered poor infrastructure hygiene, so such routes should always be cleaned up.

6. Why can’t a private subnet directly use an Internet Gateway?

A private subnet cannot directly use an Internet Gateway because it is designed to not have direct internet exposure. Internet Gateway requires instances to have public IPs, which private subnet instances don’t have. Also, allowing direct IGW access would defeat the purpose of having a private subnet. Instead, private subnets use NAT Gateway so they can access the internet securely without being exposed.

7. How does traffic flow from private EC2 to the internet?

When a private EC2 instance wants to access the internet, the request first goes to its route table. The route table sends the traffic to the NAT Gateway configured for that AZ. The NAT Gateway, which is in a public subnet, then forwards the request to the Internet Gateway. From there, it reaches the internet. When the response comes back, it follows the same path in reverse, going through the NAT Gateway and then back to the private EC2 instance. This ensures secure outbound access without exposing the instance.