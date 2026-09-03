# AWS Certified Cloud Practitioner (CLF-C02) - Domains 1 & 2 Focused Drill

**Certification:** AWS Certified Cloud Practitioner (CLF-C02)  
**Questions:** 40  
**Time limit:** 55 minutes  
**Passing score:** 700 / 1000 (scaled) on the real exam; 70% here

A focused drill, not a full mock. It covers only Cloud Concepts and Security and Compliance, which together are 54% of the real exam. The two domains appear in the same 24:30 proportion to each other that the official blueprint uses, and the time limit keeps the real exam's pace of about 1 minute 23 seconds per question.

## Exam composition

| Domain | Share of this exam | Share of the real exam | Questions |
| --- | --- | --- | --- |
| 1. Cloud Concepts | 45% | 24% | 18 |
| 2. Security and Compliance | 55% | 30% | 22 |
| **Total** | **100%** | **54%** | **40** |

Answer every question. Questions that say *Choose TWO* require exactly two
selections and are scored all-or-nothing, exactly as on the real exam.

---

## Questions

**1.** A company responds to increased demand by adding more Amazon EC2 instances to its web tier rather than moving to a larger instance size. What is this approach called?

- A. Vertical scaling
- B. Horizontal scaling
- C. Fault tolerance
- D. Loose coupling

**2.** An on-premises company buys servers sized for its busiest day of the year. For the remaining 360 days most of that hardware sits idle. Which advantage of cloud computing solves this problem?

- A. Stop guessing capacity
- B. Benefit from massive economies of scale
- C. Go global in minutes
- D. Increase physical security

**3.** Which design principle belongs to the Security pillar of the AWS Well-Architected Framework?

- A. Apply security at all layers
- B. Measure overall efficiency
- C. Adopt a consumption model
- D. Make frequent, small, reversible changes

**4.** A company wants to attribute AWS spending to individual business units so each team can see what its workloads cost. Which Well-Architected pillar does this practice belong to?

- A. Operational Excellence
- B. Reliability
- C. Cost Optimization
- D. Performance Efficiency

**5.** A team regularly tests new instance types and database engines to see whether they serve a workload better than the current choice. Which Well-Architected pillar does this reflect?

- A. Performance Efficiency
- B. Sustainability
- C. Reliability
- D. Security

**6.** During a cloud migration, an organization must address staff training, new role definitions, and change management. Which AWS Cloud Adoption Framework perspective covers this work?

- A. Platform
- B. People
- C. Operations
- D. Governance

**7.** A company moves a self-managed MySQL database from a data center onto Amazon RDS for MySQL. The application's code is unchanged, but the database is now a managed service. Which migration strategy is this?

- A. Rehosting
- B. Replatforming
- C. Refactoring
- D. Retaining

**8.** A company retires its self-hosted CRM application and moves its users to a subscription-based CRM product from AWS Marketplace. Which migration strategy is this?

- A. Repurchasing
- B. Rehosting
- C. Relocating
- D. Refactoring

**9.** Employees use a web-based email and productivity suite. They manage only their own documents and settings; the vendor handles everything else. Which cloud computing model is this?

- A. Infrastructure as a service (IaaS)
- B. Platform as a service (PaaS)
- C. Software as a service (SaaS)
- D. Serverless

**10.** An application is designed so that the failure of any single component causes no interruption and no loss of function at all, with redundant components already running. Which characteristic does this describe?

- A. Elasticity
- B. Fault tolerance
- C. Agility
- D. Scalability

**11.** A startup wants to test five different product ideas this quarter and shut down whichever ones fail, without buying hardware for any of them. Which pair of cloud benefits BEST supports this plan?

- A. Increased agility and a variable expense model
- B. Physical security and regulatory compliance
- C. Economies of scale and data residency control
- D. Fault tolerance and disaster recovery

**12.** Which are benefits of deploying a workload across multiple AWS Availability Zones within a Region? (Choose TWO.)

- A. The workload survives the loss of a single data center
- B. Data is automatically copied to every AWS Region
- C. Low-latency network links connect the Availability Zones
- D. AWS assumes responsibility for the customer's application code
- E. The workload no longer needs any backups

**13.** A company shuts down development and test environments outside working hours and consolidates lightly used workloads onto fewer instances. Which Well-Architected pillar does this MOST directly support, besides Cost Optimization?

- A. Reliability
- B. Sustainability
- C. Security
- D. Operational Excellence

**14.** A team deploys changes as small, frequent, reversible updates defined entirely in templates, and runs regular game days to rehearse failures. Which Well-Architected pillar are they practicing?

- A. Operational Excellence
- B. Cost Optimization
- C. Performance Efficiency
- D. Sustainability

**15.** A company builds a new application entirely on AWS managed services, with no on-premises components at any tier. Which deployment model is this?

- A. Hybrid
- B. Cloud-native (all-in cloud)
- C. Private cloud
- D. Community cloud

**16.** Which statements describe characteristics of cloud computing? (Choose TWO.)

- A. Resources can be provisioned on demand without human interaction from the provider
- B. Usage is metered, and customers pay only for what they consume
- C. Capacity must be reserved a quarter in advance
- D. Each customer receives dedicated physical hardware by default
- E. Costs are fixed for the life of the contract

**17.** Before a major launch, a company wants a structured review of one workload against AWS best practices, producing a prioritized list of risks. What should the company do?

- A. Open a support case requesting that AWS certify the workload
- B. Run a Well-Architected Review of the workload using the AWS Well-Architected Tool
- C. Enable AWS Config rules and treat any noncompliant resource as a risk
- D. Migrate the workload to a different AWS Region

**18.** Which statement BEST distinguishes elasticity from scalability?

- A. They are different words for the same capability
- B. Scalability is the ability to grow to handle more load; elasticity is doing so automatically in both directions as demand changes
- C. Elasticity applies only to storage, and scalability applies only to compute
- D. Scalability is an AWS service and elasticity is a billing model

**19.** A company runs a database on Amazon RDS. Who is responsible for patching the operating system underlying the database instance?

- A. The customer, using AWS Systems Manager Patch Manager
- B. AWS
- C. The customer, by logging in over SSH
- D. Neither party; the OS never requires patching

**20.** Which of the following is ALWAYS the customer's responsibility, regardless of which AWS services are used?

- A. Decommissioning physical storage media
- B. Classifying the company's own data and controlling who can access it
- C. Maintaining the network infrastructure between Availability Zones
- D. Patching the hypervisor

**21.** Which tasks does AWS perform as part of its responsibility for security OF the cloud? (Choose TWO.)

- A. Controlling physical access to data centers
- B. Configuring IAM permissions for the customer's users
- C. Managing the hardware and software of the global infrastructure
- D. Encrypting the customer's application data
- E. Choosing which AWS Region a workload runs in

**22.** A new analyst needs to read objects from one Amazon S3 bucket to build reports. Which approach follows AWS security best practices?

- A. Attach the AdministratorAccess policy so the analyst is never blocked
- B. Grant read-only access to that specific bucket and nothing more
- C. Share an existing administrator's credentials for the duration of the project
- D. Add the analyst to the account as a second root user

**23.** Which task can ONLY be performed by the AWS account root user?

- A. Creating an Amazon S3 bucket
- B. Changing the AWS Support plan or closing the AWS account
- C. Launching an Amazon EC2 instance
- D. Creating an IAM role

**24.** A company has a production account and an auditing account. Auditors in the auditing account need temporary read access to resources in the production account. What is the recommended way to grant it?

- A. Create IAM users in the production account and email the access keys to the auditors
- B. Create an IAM role in the production account that the auditing account is trusted to assume
- C. Share the production account's root user credentials with the audit team
- D. Make the production resources publicly readable during the audit

**25.** An IAM user belongs to a group whose policy allows s3:DeleteObject. A separate policy attached directly to the user explicitly denies s3:DeleteObject. What is the result?

- A. The user can delete objects, because an explicit allow overrides a deny
- B. The user cannot delete objects, because an explicit deny always wins
- C. The result depends on which policy was attached most recently
- D. The user is prompted to choose which policy applies

**26.** A company with 60 AWS accounts wants its employees to sign in once with corporate credentials and then select which account and role to use. Which service provides this?

- A. AWS IAM Identity Center
- B. Amazon Cognito
- C. AWS Directory Service for Microsoft Active Directory only
- D. An IAM user created in each of the 60 accounts

**27.** An organization wants to guarantee that no account in its Sandbox organizational unit can ever use Amazon EC2, even if a local administrator grants themselves full permissions. What should it use?

- A. An IAM policy attached to each user in those accounts
- B. A service control policy applied to the Sandbox organizational unit
- C. A security group rule
- D. An AWS Config rule

**28.** A security team wants to be alerted when an IAM access key is used from an unusual location or when an EC2 instance starts communicating with a known command-and-control server. Which service should it enable?

- A. Amazon Inspector
- B. Amazon GuardDuty
- C. AWS Config
- D. AWS Certificate Manager

**29.** A company must produce a list of unpatched software packages with known CVEs on its running Amazon EC2 instances. Which service does this?

- A. Amazon GuardDuty
- B. Amazon Macie
- C. Amazon Inspector
- D. Amazon Detective

**30.** A company must find out whether any customer credit card numbers or national ID numbers have been uploaded to its Amazon S3 buckets. Which service should it use?

- A. Amazon Macie
- B. AWS Config
- C. Amazon Inspector
- D. AWS CloudTrail

**31.** After GuardDuty raises a finding, a security analyst needs to explore the related events and resource behavior over time to determine the root cause. Which service is purpose-built for this investigation?

- A. AWS Security Hub
- B. Amazon Detective
- C. AWS Trusted Advisor
- D. Amazon CloudWatch

**32.** A company wants one place to see security findings from several AWS security services across all of its accounts, with automated checks against the CIS AWS Foundations Benchmark. Which service should it use?

- A. Amazon Detective
- B. AWS Security Hub
- C. AWS Artifact
- D. Amazon GuardDuty

**33.** A company needs to block requests from IP addresses that exceed 2,000 requests in five minutes, and to filter requests containing malicious SQL fragments. Which service provides these controls?

- A. AWS Shield Standard
- B. Security groups
- C. AWS WAF
- D. AWS Network Firewall

**34.** Which statement about AWS Shield Standard is correct?

- A. It must be purchased separately and configured before it protects any resource
- B. It is enabled automatically for all AWS customers at no additional charge
- C. It includes 24/7 access to the AWS Shield Response Team
- D. It protects only Amazon EC2 instances

**35.** A regulated customer must manage its encryption keys in single-tenant hardware security modules that it controls exclusively, meeting FIPS 140-2 Level 3. Which service meets this requirement?

- A. AWS Key Management Service (AWS KMS)
- B. AWS CloudHSM
- C. AWS Secrets Manager
- D. AWS Certificate Manager

**36.** An application currently reads its database password from a plaintext configuration file. The company wants the password stored encrypted, retrieved at runtime, and rotated automatically every 30 days. Which service should it use?

- A. AWS Key Management Service (AWS KMS)
- B. AWS Secrets Manager
- C. Amazon S3 with default encryption
- D. AWS Systems Manager Session Manager

**37.** An engineer needs to see what a security group's inbound rules looked like three weeks ago and how they have changed since. Which service provides this?

- A. AWS CloudTrail
- B. AWS Config
- C. Amazon CloudWatch Logs
- D. AWS Trusted Advisor

**38.** A healthcare customer needs to accept a Business Associate Addendum (BAA) with AWS and download the current ISO 27001 certification. Where are both of these available?

- A. AWS Artifact
- B. AWS Audit Manager
- C. AWS Security Hub
- D. The AWS Support Center

**39.** A company must protect data both while it moves across the network and while it is stored. Which pair of measures addresses these two requirements? (Choose TWO.)

- A. Serving the application over HTTPS with a TLS certificate from AWS Certificate Manager
- B. Enabling server-side encryption on the Amazon S3 buckets holding the data
- C. Adding a second Availability Zone to the deployment
- D. Enabling Amazon CloudWatch detailed monitoring
- E. Placing the instances in a public subnet

**40.** A company must block all traffic from one specific malicious IP address to every instance in a subnet. Which control can do this directly?

- A. A security group inbound rule that denies the IP address
- B. A network ACL inbound rule that denies the IP address
- C. An IAM policy denying the IP address
- D. An Amazon Route 53 record removing the IP address

---

## Answer key

| # | Domain | Answer | Topic |
| --- | --- | --- | --- |
| 1 | Cloud Concepts | B | Horizontal vs vertical scaling |
| 2 | Cloud Concepts | A | Stop guessing capacity |
| 3 | Cloud Concepts | A | Well-Architected: Security pillar |
| 4 | Cloud Concepts | C | Well-Architected: Cost Optimization |
| 5 | Cloud Concepts | A | Well-Architected: Performance Efficiency |
| 6 | Cloud Concepts | B | AWS Cloud Adoption Framework (CAF) |
| 7 | Cloud Concepts | B | Migration strategies: replatform |
| 8 | Cloud Concepts | A | Migration strategies: repurchase |
| 9 | Cloud Concepts | C | Cloud service models |
| 10 | Cloud Concepts | B | Fault tolerance vs high availability |
| 11 | Cloud Concepts | A | Agility and the cost of experimentation |
| 12 | Cloud Concepts | A, C | Benefits of the AWS global infrastructure |
| 13 | Cloud Concepts | B | Sustainability pillar |
| 14 | Cloud Concepts | A | Operational Excellence |
| 15 | Cloud Concepts | B | Cloud deployment models |
| 16 | Cloud Concepts | A, B | Characteristics of cloud computing |
| 17 | Cloud Concepts | B | AWS Well-Architected Review |
| 18 | Cloud Concepts | B | Elasticity vs scalability |
| 19 | Security and Compliance | B | Shared responsibility: managed services |
| 20 | Security and Compliance | B | Shared responsibility: customer duties |
| 21 | Security and Compliance | A, C | Shared responsibility model |
| 22 | Security and Compliance | B | Principle of least privilege |
| 23 | Security and Compliance | B | Root user: tasks requiring root |
| 24 | Security and Compliance | B | IAM roles for cross-account access |
| 25 | Security and Compliance | B | IAM policy evaluation |
| 26 | Security and Compliance | A | AWS IAM Identity Center |
| 27 | Security and Compliance | B | Service control policies |
| 28 | Security and Compliance | B | Amazon GuardDuty |
| 29 | Security and Compliance | C | Amazon Inspector |
| 30 | Security and Compliance | A | Amazon Macie |
| 31 | Security and Compliance | B | Amazon Detective |
| 32 | Security and Compliance | B | AWS Security Hub |
| 33 | Security and Compliance | C | AWS WAF |
| 34 | Security and Compliance | B | AWS Shield Standard |
| 35 | Security and Compliance | B | AWS KMS vs AWS CloudHSM |
| 36 | Security and Compliance | B | AWS Secrets Manager |
| 37 | Security and Compliance | B | AWS Config vs AWS CloudTrail |
| 38 | Security and Compliance | A | AWS Artifact |
| 39 | Security and Compliance | A, B | Encryption in transit and at rest |
| 40 | Security and Compliance | B | Security groups vs network ACLs |

---

## Explanations

### 1. Horizontal vs vertical scaling

**Correct answer: B** — *Domain 1: Cloud Concepts*

> B. Horizontal scaling

Horizontal scaling, or scaling out, adds more instances of a resource. Vertical scaling, or scaling up, replaces a resource with a larger one. The Reliability pillar recommends scaling horizontally so that the failure of any single instance affects a smaller share of the workload.

> **Signal:** 'adding more instances' means horizontal (scale out); 'a larger instance size' means vertical (scale up). AWS best practice favors horizontal scaling because it also improves availability.

**Why the other options are wrong:** Vertical scaling is the opposite approach. Fault tolerance and loose coupling are design goals, not scaling directions.

### 2. Stop guessing capacity

**Correct answer: A** — *Domain 1: Cloud Concepts*

> A. Stop guessing capacity

Provisioning for peak demand means paying for idle capacity most of the time, and provisioning for average demand means failing at peak. In the cloud you scale capacity up and down on demand, so the guess disappears.

> **Signal:** 'sized for the busiest day' plus 'sits idle' is the capacity-guessing problem. Do not jump to 'economies of scale' just because the question mentions wasted money.

**Why the other options are wrong:** Economies of scale explain why AWS unit prices are low, not why idle hardware is wasteful. Global reach and physical security are unrelated to this scenario.

### 3. Well-Architected: Security pillar

**Correct answer: A** — *Domain 1: Cloud Concepts*

> A. Apply security at all layers

'Apply security at all layers' is a Security pillar principle, describing defense in depth across the network, instance, application and data layers.

> **Signal:** Security pillar principles read as: identity foundation, traceability, security at all layers, automate, protect data in transit and at rest, prepare for events.

**Why the other options are wrong:** 'Measure overall efficiency' is Performance Efficiency, 'adopt a consumption model' is Cost Optimization, and 'make frequent, small, reversible changes' is Operational Excellence.

### 4. Well-Architected: Cost Optimization

**Correct answer: C** — *Domain 1: Cloud Concepts*

> C. Cost Optimization

Cost Optimization includes analyzing and attributing expenditure, adopting a consumption model, measuring overall efficiency, and stopping spending on undifferentiated heavy lifting.

> **Signal:** 'attribute expenditure' and 'adopt a consumption model' are Cost Optimization phrases straight out of the framework.

**Why the other options are wrong:** The other pillars address how systems are run, how they survive failure, and how efficiently they use resources, not how spend is allocated.

### 5. Well-Architected: Performance Efficiency

**Correct answer: A** — *Domain 1: Cloud Concepts*

> A. Performance Efficiency

Performance Efficiency is about using computing resources efficiently and continuing to do so as demand changes and technologies evolve. Experimenting more often is one of its design principles, because in the cloud a test costs minutes rather than a procurement cycle.

> **Signal:** 'experiment more often' and 'use advanced technologies as a service' are Performance Efficiency principles. The giveaway is comparing resource types for fit.

**Why the other options are wrong:** Sustainability would frame the same action in terms of energy per unit of work. Reliability and Security address failure and protection respectively.

### 6. AWS Cloud Adoption Framework (CAF)

**Correct answer: B** — *Domain 1: Cloud Concepts*

> B. People

The People perspective bridges technology and business, covering culture, organizational structure, leadership, and workforce skills during cloud adoption.

> **Signal:** Training, culture, roles and org change map to the People perspective. The six CAF perspectives are Business, People, Governance, Platform, Security and Operations.

**Why the other options are wrong:** Platform covers the architecture and the landing zone, Operations covers running services to meet business needs, and Governance covers managing and measuring the initiative's business outcomes and risk.

### 7. Migration strategies: replatform

**Correct answer: B** — *Domain 1: Cloud Concepts*

> B. Replatforming

Replatforming makes a few cloud optimizations to gain a tangible benefit, such as moving to a managed database, without changing the application's core architecture.

> **Signal:** 'lift, tinker and shift' — some optimization, no code rewrite. Moving a self-managed engine onto its managed equivalent is the textbook replatform example.

**Why the other options are wrong:** Rehosting would move the database server as-is onto EC2. Refactoring would re-architect the application. Retaining means leaving it where it is for now.

### 8. Migration strategies: repurchase

**Correct answer: A** — *Domain 1: Cloud Concepts*

> A. Repurchasing

Repurchasing replaces an existing application with a different product, most often a SaaS offering, rather than migrating the original software.

> **Signal:** 'move to a different product', usually a SaaS subscription, is repurchase — sometimes called 'drop and shop'.

**Why the other options are wrong:** Rehosting and relocating move the existing workload unchanged. Refactoring rewrites it.

### 9. Cloud service models

**Correct answer: C** — *Domain 1: Cloud Concepts*

> C. Software as a service (SaaS)

SaaS delivers a completed product that the provider runs and manages. The customer thinks only about how they use the software.

> **Signal:** 'a finished application the user just signs into' is SaaS. If the customer manages the OS it is IaaS; if they deploy code but not the OS it is PaaS.

**Why the other options are wrong:** IaaS gives the customer the operating system, PaaS gives them a managed runtime for their own code, and serverless describes how a service is operated rather than a service model in this taxonomy.

### 10. Fault tolerance vs high availability

**Correct answer: B** — *Domain 1: Cloud Concepts*

> B. Fault tolerance

Fault tolerance means the system continues operating with no loss of function when a component fails, because redundancy is already in place. High availability accepts brief disruption while the system recovers.

> **Signal:** 'no interruption at all' is fault tolerance. 'Minimal downtime' or 'recovers quickly' is high availability. The exam separates these two on the words 'no' versus 'minimal'.

**Why the other options are wrong:** Elasticity and scalability describe capacity changes. Agility describes speed of delivery.

### 11. Agility and the cost of experimentation

**Correct answer: A** — *Domain 1: Cloud Concepts*

> A. Increased agility and a variable expense model

Provisioning in minutes lowers the cost of trying an idea, and paying only for what is consumed means an abandoned experiment stops costing money as soon as it is shut down.

> **Signal:** 'test and shut down' plus 'without buying hardware' is agility (provision in minutes) combined with paying only for what you use.

**Why the other options are wrong:** The other pairs are real cloud benefits but none of them address the speed and disposability of experiments.

### 12. Benefits of the AWS global infrastructure

**Correct answer: A, C** — *Domain 1: Cloud Concepts*

> A. The workload survives the loss of a single data center

> C. Low-latency network links connect the Availability Zones

Availability Zones are physically separated but connected by high-bandwidth, low-latency links, so a workload spread across them stays available when one zone fails and can still replicate synchronously.

> **Signal:** Multi-AZ answers are about surviving a data center failure with low-latency links between zones. Any option promising automatic global replication or the end of backups is a distractor.

**Why the other options are wrong:** Cross-Region copying happens only when configured. AWS never takes responsibility for customer code, and redundancy is not a substitute for backups.

### 13. Sustainability pillar

**Correct answer: B** — *Domain 1: Cloud Concepts*

> B. Sustainability

The Sustainability pillar aims to reduce the energy and resources consumed per unit of work. Maximizing utilization and eliminating idle capacity is one of its primary practices, which is why it so often overlaps with Cost Optimization.

> **Signal:** 'maximize utilization' and 'reduce idle resources' serve Sustainability as well as cost. Sustainability language is about energy and resources per unit of work.

**Why the other options are wrong:** Reliability, Security and Operational Excellence are unaffected by consolidating idle instances.

### 14. Operational Excellence

**Correct answer: A** — *Domain 1: Cloud Concepts*

> A. Operational Excellence

Operational Excellence covers running and monitoring systems and continuously improving processes. Defining operations as code and rehearsing failure are two of its design principles.

> **Signal:** 'perform operations as code', 'small reversible changes', 'anticipate failure' and 'learn from all operational failures' are Operational Excellence principles.

**Why the other options are wrong:** The other pillars address spend, resource fit, and environmental impact rather than how changes are delivered and rehearsed.

### 15. Cloud deployment models

**Correct answer: B** — *Domain 1: Cloud Concepts*

> B. Cloud-native (all-in cloud)

An all-in cloud or cloud-native deployment runs every part of the application in the cloud, often using managed and serverless services from the outset.

> **Signal:** 'no on-premises components' rules out hybrid. Hybrid always requires something still running in a data center.

**Why the other options are wrong:** Hybrid mixes cloud with on-premises. A private cloud runs on infrastructure dedicated to one organization, typically on-premises.

### 16. Characteristics of cloud computing

**Correct answer: A, B** — *Domain 1: Cloud Concepts*

> A. Resources can be provisioned on demand without human interaction from the provider

> B. Usage is metered, and customers pay only for what they consume

On-demand self-service means resources are provisioned automatically through an API or console, and measured service means usage is metered and billed by consumption.

> **Signal:** On-demand self-service and measured (metered) service are the standard characteristics. Anything describing advance reservations, dedicated hardware by default, or fixed costs is describing the on-premises model.

**Why the other options are wrong:** Advance capacity reservation and fixed contracts describe traditional data center procurement. Dedicated hardware is available on AWS but is an exception, not the default.

### 17. AWS Well-Architected Review

**Correct answer: B** — *Domain 1: Cloud Concepts*

> B. Run a Well-Architected Review of the workload using the AWS Well-Architected Tool

The AWS Well-Architected Tool walks a workload through questions for each pillar and returns identified high and medium risks with an improvement plan, at no cost.

> **Signal:** 'review a workload against best practices' plus 'list of risks' is always the Well-Architected Tool. AWS does not certify or approve customer architectures.

**Why the other options are wrong:** AWS does not certify workloads. Config checks resource configuration but does not perform an architectural review, and changing Region reviews nothing.

### 18. Elasticity vs scalability

**Correct answer: B** — *Domain 1: Cloud Concepts*

> B. Scalability is the ability to grow to handle more load; elasticity is doing so automatically in both directions as demand changes

Scalability is the capacity to handle growth, whether by scaling up or out. Elasticity adds the automatic, bidirectional match of supply to demand, including releasing resources when they are no longer needed.

> **Signal:** Scalability = can grow. Elasticity = grows and shrinks automatically with demand. When a stem stresses releasing resources afterward, the answer is elasticity.

**Why the other options are wrong:** The terms are related but not identical, neither is limited to one resource type, and neither is a service or a billing model.

### 19. Shared responsibility: managed services

**Correct answer: B** — *Domain 2: Security and Compliance*

> B. AWS

For managed services such as Amazon RDS, Lambda and DynamoDB, AWS operates the underlying infrastructure and operating system. The customer's responsibility narrows to data, access control, and configuration such as encryption settings and security groups.

> **Signal:** The shared responsibility line moves with the service. If the customer has no OS access, AWS patches it. Amazon RDS gives no SSH access, so the OS is AWS's responsibility.

**Why the other options are wrong:** This is the exact inverse of Amazon EC2, where the customer patches the guest OS. Watch for the service name before answering an OS-patching question.

### 20. Shared responsibility: customer duties

**Correct answer: B** — *Domain 2: Security and Compliance*

> B. Classifying the company's own data and controlling who can access it

The customer always owns their content, the classification of that content, and the identity and access management decisions around it. This part of the model does not change with the service.

> **Signal:** Customer data, its classification, and who may access it never transfer to AWS. Anything physical or infrastructure-level is AWS's.

**Why the other options are wrong:** Media decommissioning, inter-AZ networking and hypervisor patching are all part of security 'of' the cloud, which is AWS's responsibility.

### 21. Shared responsibility model

**Correct answer: A, C** — *Domain 2: Security and Compliance*

> A. Controlling physical access to data centers

> C. Managing the hardware and software of the global infrastructure

AWS operates, manages and controls the components from the host operating system and virtualization layer down to the physical security of the facilities.

> **Signal:** Security OF the cloud = the physical facilities, hardware, and the software that runs AWS services. Security IN the cloud = identity, data, configuration, and Region choice, all customer decisions.

**Why the other options are wrong:** IAM configuration, data encryption and Region selection are all customer decisions and are part of security in the cloud.

### 22. Principle of least privilege

**Correct answer: B** — *Domain 2: Security and Compliance*

> B. Grant read-only access to that specific bucket and nothing more

Least privilege means granting only the permissions needed for the task, scoped to the specific resource, and widening them only if a genuine need appears.

> **Signal:** 'only the permissions required to perform the task' is least privilege. Any option offering broad access for convenience is wrong by definition on this exam.

**Why the other options are wrong:** Administrator access is far broader than the task requires, shared credentials destroy accountability, and an account has exactly one root user that cannot be duplicated.

### 23. Root user: tasks requiring root

**Correct answer: B** — *Domain 2: Security and Compliance*

> B. Changing the AWS Support plan or closing the AWS account

A small set of account and billing management tasks require root credentials. Everything operational should be done by an IAM identity with appropriate permissions.

> **Signal:** Root-only tasks are account-level administration: changing the support plan, closing the account, changing the account name or email, and restoring IAM user permissions after they are revoked.

**Why the other options are wrong:** Creating buckets, launching instances and creating roles are all ordinary tasks any suitably permissioned IAM identity can perform.

### 24. IAM roles for cross-account access

**Correct answer: B** — *Domain 2: Security and Compliance*

> B. Create an IAM role in the production account that the auditing account is trusted to assume

A cross-account IAM role with a trust policy naming the other account lets identities there assume the role and receive temporary credentials, with no keys to distribute or rotate.

> **Signal:** 'cross-account', 'temporary', and 'no long-term credentials' all point to an IAM role that is assumed. Roles issue short-lived credentials; users carry long-lived keys.

**Why the other options are wrong:** Distributing access keys creates long-lived credentials in a second account, root credentials must never be shared, and public access exposes data to everyone.

### 25. IAM policy evaluation

**Correct answer: B** — *Domain 2: Security and Compliance*

> B. The user cannot delete objects, because an explicit deny always wins

IAM evaluates all applicable policies together. Access is denied by default, an allow grants access, and an explicit deny anywhere overrides every allow.

> **Signal:** In IAM evaluation an explicit deny always overrides any allow, from any policy. There is no ordering, recency or precedence question to reason about.

**Why the other options are wrong:** Policy attachment order is irrelevant, and IAM never prompts a user to resolve a conflict.

### 26. AWS IAM Identity Center

**Correct answer: A** — *Domain 2: Security and Compliance*

> A. AWS IAM Identity Center

AWS IAM Identity Center provides single sign-on across all accounts in an organization, using an existing corporate identity source, and presents users with a portal of the accounts and roles available to them.

> **Signal:** 'workforce', 'sign in once', 'multiple accounts' means IAM Identity Center. Amazon Cognito is for your application's end users (customers), not employees.

**Why the other options are wrong:** Cognito handles customer identity for applications. Directory Service supplies a directory but is not itself the multi-account sign-on layer, and per-account IAM users are exactly what this replaces.

### 27. Service control policies

**Correct answer: B** — *Domain 2: Security and Compliance*

> B. A service control policy applied to the Sandbox organizational unit

Service control policies in AWS Organizations set the permission ceiling for member accounts. An action denied by an SCP cannot be performed no matter what the account's own IAM policies say.

> **Signal:** 'even if a local administrator allows it' or 'maximum permissions' means an SCP. IAM grants permissions; SCPs cap what IAM in that account is able to grant.

**Why the other options are wrong:** IAM policies can be changed by an account administrator, security groups filter network traffic, and Config reports noncompliance after the fact rather than preventing the action.

### 28. Amazon GuardDuty

**Correct answer: B** — *Domain 2: Security and Compliance*

> B. Amazon GuardDuty

GuardDuty continuously analyzes CloudTrail events, VPC Flow Logs and DNS logs with machine learning and threat intelligence to flag anomalous and malicious behavior.

> **Signal:** 'unusual', 'unexpected', 'malicious', 'compromised', 'known bad IP' — behavioral threat detection is GuardDuty. It watches activity, not software versions.

**Why the other options are wrong:** Inspector looks at software vulnerabilities rather than behavior, Config looks at resource configuration, and ACM manages certificates.

### 29. Amazon Inspector

**Correct answer: C** — *Domain 2: Security and Compliance*

> C. Amazon Inspector

Amazon Inspector continually scans EC2 instances, container images in Amazon ECR, and Lambda functions for known software vulnerabilities and unintended network exposure.

> **Signal:** 'vulnerability', 'CVE', 'unpatched', 'scan' means Inspector. Compare with GuardDuty, which detects behavior, and Macie, which finds sensitive data.

**Why the other options are wrong:** GuardDuty detects malicious activity, Macie classifies sensitive data in S3, and Detective investigates the cause of findings that other services raise.

### 30. Amazon Macie

**Correct answer: A** — *Domain 2: Security and Compliance*

> A. Amazon Macie

Amazon Macie uses machine learning and pattern matching to discover and classify sensitive data in Amazon S3, and reports on the security posture of the buckets holding it.

> **Signal:** 'sensitive data', 'PII', 'credit card numbers', 'classify' plus 'S3' is always Macie.

**Why the other options are wrong:** Config evaluates configuration, Inspector scans for vulnerabilities, and CloudTrail records who called which API.

### 31. Amazon Detective

**Correct answer: B** — *Domain 2: Security and Compliance*

> B. Amazon Detective

Amazon Detective automatically builds a linked data set from CloudTrail, VPC Flow Logs and GuardDuty findings so analysts can visualize and drill into the behavior behind a finding.

> **Signal:** 'investigate', 'root cause', 'after a finding' is Detective. 'Aggregate findings in one place' is Security Hub. Detect, then aggregate, then investigate: GuardDuty, Security Hub, Detective.

**Why the other options are wrong:** Security Hub aggregates and prioritizes findings but does not perform the deep investigation. Trusted Advisor and CloudWatch serve different purposes entirely.

### 32. AWS Security Hub

**Correct answer: B** — *Domain 2: Security and Compliance*

> B. AWS Security Hub

AWS Security Hub aggregates findings from GuardDuty, Inspector, Macie and partner tools, normalizes them, and runs continuous best-practice checks against security standards.

> **Signal:** 'single pane of glass', 'aggregate findings', 'security standard' or a named benchmark means Security Hub.

**Why the other options are wrong:** Detective investigates individual findings, Artifact supplies compliance documents, and GuardDuty produces findings rather than aggregating them.

### 33. AWS WAF

**Correct answer: C** — *Domain 2: Security and Compliance*

> C. AWS WAF

AWS WAF inspects HTTP and HTTPS requests at layer 7 and supports rate-based rules that block source IPs exceeding a request threshold, plus managed rule groups for common exploits.

> **Signal:** Inspecting the content of HTTP requests, rate-based rules, SQL injection, XSS and bad bots are all AWS WAF. Shield handles volumetric DDoS; WAF handles the request itself.

**Why the other options are wrong:** Shield Standard mitigates network and transport layer DDoS automatically but does not inspect request content. Security groups filter by IP, protocol and port only.

### 34. AWS Shield Standard

**Correct answer: B** — *Domain 2: Security and Compliance*

> B. It is enabled automatically for all AWS customers at no additional charge

AWS Shield Standard is included at no cost for all customers and automatically defends against the most common network and transport layer DDoS attacks.

> **Signal:** Shield Standard is free and automatic for everyone. Anything about the Shield Response Team, cost protection, or detailed attack diagnostics belongs to Shield Advanced, which is paid.

**Why the other options are wrong:** The Shield Response Team and cost protection are Shield Advanced features. Shield Standard is not limited to EC2.

### 35. AWS KMS vs AWS CloudHSM

**Correct answer: B** — *Domain 2: Security and Compliance*

> B. AWS CloudHSM

AWS CloudHSM provides dedicated, single-tenant hardware security modules in the customer's VPC, where the customer alone controls the keys and users. KMS is multi-tenant and managed by AWS.

> **Signal:** 'dedicated', 'single-tenant', 'you control the hardware', 'FIPS 140-2 Level 3' means CloudHSM. Plain 'create and manage keys, integrated with AWS services' means KMS.

**Why the other options are wrong:** KMS is the default choice for most workloads but does not offer dedicated single-tenant HSMs. Secrets Manager stores secrets, and ACM manages certificates.

### 36. AWS Secrets Manager

**Correct answer: B** — *Domain 2: Security and Compliance*

> B. AWS Secrets Manager

AWS Secrets Manager stores secrets encrypted with KMS, serves them to applications through an API call, and provides built-in scheduled rotation for supported databases.

> **Signal:** The word 'rotate' next to a credential is the Secrets Manager tell. KMS manages the keys that encrypt the secret; it does not store or rotate the secret itself.

**Why the other options are wrong:** KMS manages encryption keys rather than credentials, S3 is object storage, and Session Manager provides shell access to instances.

### 37. AWS Config vs AWS CloudTrail

**Correct answer: B** — *Domain 2: Security and Compliance*

> B. AWS Config

AWS Config records point-in-time configurations of resources and maintains a configuration timeline, so you can view historical state and see exactly what changed.

> **Signal:** 'what did the resource look like' and 'how has it changed' is Config, which records configuration state over time. 'Who called the API' is CloudTrail. Both are audit services; the stem's noun decides which.

**Why the other options are wrong:** CloudTrail tells you which identity made the change and when, but not the resulting configuration state over time. CloudWatch Logs stores log data, and Trusted Advisor runs best-practice checks.

### 38. AWS Artifact

**Correct answer: A** — *Domain 2: Security and Compliance*

> A. AWS Artifact

AWS Artifact provides on-demand access to AWS security and compliance reports, such as SOC and ISO certifications, and to online agreements including the BAA.

> **Signal:** Compliance reports and legal agreements you download from AWS are always AWS Artifact. Audit Manager collects evidence about YOUR workloads; Artifact supplies AWS's own documents.

**Why the other options are wrong:** Audit Manager automates evidence collection for the customer's own audits, Security Hub aggregates findings, and support cases are not the distribution channel for these documents.

### 39. Encryption in transit and at rest

**Correct answer: A, B** — *Domain 2: Security and Compliance*

> A. Serving the application over HTTPS with a TLS certificate from AWS Certificate Manager

> B. Enabling server-side encryption on the Amazon S3 buckets holding the data

TLS protects data in transit between the client and the application, while server-side encryption protects the stored objects at rest. The exam frequently pairs these two requirements in a single stem.

> **Signal:** 'in transit' maps to TLS/HTTPS/ACM/VPN. 'At rest' maps to server-side encryption, EBS/S3/RDS encryption and KMS. Options about availability or monitoring are not encryption at all.

**Why the other options are wrong:** A second Availability Zone improves availability, detailed monitoring improves observability, and a public subnet is a networking choice; none of them encrypt anything.

### 40. Security groups vs network ACLs

**Correct answer: B** — *Domain 2: Security and Compliance*

> B. A network ACL inbound rule that denies the IP address

Network ACLs operate at the subnet level and support both allow and deny rules evaluated in number order, so they can block a specific source IP for every instance in the subnet.

> **Signal:** The word 'deny' or 'block a specific IP' rules out security groups entirely, because security groups support allow rules only. Deny plus subnet-wide means network ACL.

**Why the other options are wrong:** Security groups have no deny rules; they can only permit traffic. IAM controls API access, not packet filtering, and Route 53 is DNS.

---

## Scoring this exam

Mark each question right or wrong, then score by domain to find where to study:

| Domain | Questions | Your score | % correct |
| --- | --- | --- | --- |
| 1. Cloud Concepts | 18 | ____ | ____ |
| 2. Security and Compliance | 22 | ____ | ____ |
| **Total** | **40** | ____ | ____ |

The real exam is scaled to 100-1000 with a pass at 700, which works out to
roughly 70% of the scored questions. Treat anything under 80% on this practice
exam as a signal to review that domain before booking the real thing.

