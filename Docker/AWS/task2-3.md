1. Main difference between Security Groups and NACLs

Security Groups and Network ACLs both control traffic, but they work at different levels and behave differently. A Security Group is attached to an EC2 instance and controls traffic at the instance level, while a NACL is attached to a subnet and controls traffic for all resources inside that subnet. Security Groups only allow traffic and are easier to manage, whereas NACLs can both allow and deny traffic and act as an additional layer of security at the subnet level.

2. What does "stateful" mean in Security Groups?

Stateful means that Security Groups automatically allow response traffic if a request is allowed. For example, if you allow incoming HTTP traffic to your server, the response from the server is automatically allowed to go back to the client, even if there is no explicit outbound rule. You don’t need to manually define both directions, which makes Security Groups simple and less error-prone.

3. What does "stateless" mean in NACLs?

Stateless means that NACLs do not remember previous traffic, so you must explicitly allow both inbound and outbound traffic. If you allow incoming traffic but forget to allow outgoing traffic, the response will be blocked and the connection will fail. This makes NACLs more powerful but also easier to misconfigure compared to Security Groups.

4. Which is evaluated first — NACL or Security Group?

NACL is evaluated first, and then the Security Group is checked. When traffic enters a subnet, it must first pass through the NACL rules. Only if it is allowed by the NACL will it reach the Security Group attached to the instance. If the NACL blocks the traffic, the Security Group never even gets a chance to evaluate it.

5. Why are Security Groups preferred in most production setups?

Security Groups are preferred because they are simpler, stateful, and less likely to cause mistakes. Since they automatically allow return traffic, developers don’t have to manage inbound and outbound rules separately. This reduces the chance of breaking applications due to misconfiguration, which is very common with NACLs.

6. Example where NACL misconfiguration breaks an application

A common example is allowing inbound HTTP traffic but not allowing outbound traffic. In this case, the user’s request reaches the server successfully, but the server’s response is blocked by the NACL. From the user’s perspective, the application appears to be down or not loading, even though the server is actually running. This kind of issue is difficult to debug and happens frequently in real-world systems.