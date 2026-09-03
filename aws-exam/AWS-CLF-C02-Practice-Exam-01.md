# AWS Certified Cloud Practitioner (CLF-C02) - Practice Exam 1

**Certification:** AWS Certified Cloud Practitioner (CLF-C02)  
**Questions:** 65  
**Time limit:** 90 minutes  
**Passing score:** 700 / 1000 (scaled)

The real exam contains 50 scored questions and 15 unscored questions. The unscored questions are indistinguishable from scored ones, so all 65 are presented here as a single set. Domain counts below mirror the official CLF-C02 exam guide weightings.

## Exam composition

| Domain | Official weighting | Questions in this exam |
| --- | --- | --- |
| 1. Cloud Concepts | 24% | 16 |
| 2. Security and Compliance | 30% | 19 |
| 3. Cloud Technology and Services | 34% | 22 |
| 4. Billing, Pricing, and Support | 12% | 8 |
| **Total** | **100%** | **65** |

Answer every question. Questions that say *Choose TWO* require exactly two
selections and are scored all-or-nothing, exactly as on the real exam.

---

## Questions

**1.** A company is moving its on-premises workloads to the AWS Cloud. Which financial benefit will the company realize as a direct result of this move?

- A. Fixed monthly costs that never change regardless of usage
- B. A shift from capital expense to variable operational expense
- C. Elimination of all costs associated with running applications
- D. Automatic tax exemption on all technology spending

**2.** An e-commerce site sees traffic spike 10x during a flash sale and return to normal an hour later. Which cloud characteristic allows the company to add capacity for the spike and release it immediately afterward?

- A. Elasticity
- B. Fault tolerance
- C. High availability
- D. Loose coupling

**3.** Which pillar of the AWS Well-Architected Framework focuses on the ability to run and monitor systems to deliver business value and to continually improve supporting processes and procedures?

- A. Reliability
- B. Performance Efficiency
- C. Operational Excellence
- D. Cost Optimization

**4.** A development team currently waits 10 weeks for hardware to be procured and installed before it can test a new idea. Which benefit of the AWS Cloud most directly addresses this problem?

- A. Increased agility through rapid provisioning of resources
- B. Reduced total cost of ownership through hardware discounts
- C. Improved physical security of the data center
- D. Guaranteed regulatory compliance in every industry

**5.** AWS has reduced the price of its services more than 100 times since launch. Which cloud computing advantage best explains these ongoing price reductions?

- A. Pay-as-you-go pricing
- B. Massive economies of scale
- C. Global deployment in minutes
- D. Trading fixed expense for variable expense

**6.** A company plans to move a legacy application to AWS by moving the virtual machines as-is, without modifying the application code. Which migration strategy is this?

- A. Refactoring
- B. Repurchasing
- C. Rehosting
- D. Retiring

**7.** A company keeps its customer database in its own data center for regulatory reasons but runs its public web tier on AWS, with a private network connection between the two. Which deployment model is the company using?

- A. Cloud (all-in)
- B. Hybrid
- C. On-premises (private cloud)
- D. Multi-tenant

**8.** A company based in the United States is expanding to Europe and Asia and wants to reduce latency for its new users. Which benefit of the AWS Cloud allows the company to do this quickly?

- A. The ability to go global in minutes by deploying into additional AWS Regions
- B. The ability to purchase discounted transatlantic network circuits from AWS
- C. The ability to have AWS build a private data center in each country
- D. The ability to replicate all data automatically to every Region by default

**9.** Which of the following are perspectives defined in the AWS Cloud Adoption Framework (AWS CAF)? (Choose TWO.)

- A. Business
- B. Sustainability
- C. Governance
- D. Reliability
- E. Cost Optimization

**10.** An architect deploys an application across three Availability Zones behind a load balancer so that the loss of a single Availability Zone does not take the application offline. Which design goal is being met?

- A. Elasticity
- B. High availability
- C. Cost optimization
- D. Vertical scaling

**11.** Which design principle recommends that application components communicate through a queue or a load balancer rather than referencing each other's IP addresses directly?

- A. Design for failure
- B. Loose coupling
- C. Vertical scaling
- D. Monolithic design

**12.** A company wants to review its existing AWS workloads against architectural best practices and receive a report of identified risks at no additional charge. Which service should it use?

- A. AWS Well-Architected Tool
- B. AWS Config
- C. AWS Systems Manager
- D. AWS Compute Optimizer

**13.** Which of the following is a design principle of the Reliability pillar of the AWS Well-Architected Framework?

- A. Automatically recover from failure
- B. Adopt a consumption model
- C. Use managed services to reduce your environmental impact
- D. Perform operations as code

**14.** Which of the following are advantages of cloud computing as described by AWS? (Choose TWO.)

- A. Stop guessing capacity
- B. Increase the time spent on undifferentiated heavy lifting
- C. Benefit from massive economies of scale
- D. Eliminate the need to secure your applications
- E. Guarantee that costs will decrease every month

**15.** A company uses Amazon EC2 and is responsible for choosing the operating system, installing patches, and configuring the application runtime. Which cloud computing model does this describe?

- A. Software as a service (SaaS)
- B. Platform as a service (PaaS)
- C. Infrastructure as a service (IaaS)
- D. Function as a service (FaaS)

**16.** A company wants to minimize the environmental impact of its AWS workloads. Which action aligns with the Sustainability pillar of the AWS Well-Architected Framework?

- A. Purchasing Reserved Instances for all workloads
- B. Maximizing utilization of provisioned resources and right-sizing instances
- C. Storing all data in the AWS Region closest to company headquarters
- D. Enabling multi-factor authentication for all IAM users

**17.** Under the AWS shared responsibility model, who is responsible for installing security patches on the guest operating system of an Amazon EC2 instance?

- A. AWS is solely responsible
- B. The customer is responsible
- C. Responsibility is shared equally between AWS and the customer
- D. The Amazon EC2 service patches the guest OS automatically

**18.** Which task is the responsibility of AWS under the shared responsibility model?

- A. Configuring security group rules
- B. Managing physical security of the data centers
- C. Encrypting data stored in an Amazon S3 bucket
- D. Rotating IAM user access keys

**19.** An application running on an Amazon EC2 instance needs to read objects from an Amazon S3 bucket. What is the MOST secure way to grant this access?

- A. Store an IAM user's access key and secret key in a configuration file on the instance
- B. Attach an IAM role with the required permissions to the EC2 instance
- C. Make the S3 bucket publicly readable
- D. Embed the AWS account root user credentials in the application code

**20.** Which actions are AWS best practices for protecting the AWS account root user? (Choose TWO.)

- A. Enable multi-factor authentication (MFA) on the root user
- B. Share the root user password with all administrators so work is not blocked
- C. Create an IAM identity with appropriate permissions for everyday administrative tasks
- D. Attach an IAM policy directly to the root user to limit its permissions
- E. Generate root user access keys for use in automation scripts

**21.** An auditor requests a copy of the AWS SOC 2 report and the PCI DSS Attestation of Compliance. Where can the company download these documents?

- A. AWS Artifact
- B. AWS Trusted Advisor
- C. AWS Security Hub
- D. AWS CloudTrail

**22.** Which AWS service continuously monitors CloudTrail events, VPC Flow Logs and DNS logs to detect malicious activity such as cryptocurrency mining or communication with known bad IP addresses?

- A. Amazon Inspector
- B. Amazon GuardDuty
- C. Amazon Macie
- D. AWS Shield

**23.** A company wants to automatically scan its Amazon EC2 instances and container images in Amazon ECR for known software vulnerabilities (CVEs). Which service should it use?

- A. Amazon Macie
- B. AWS Config
- C. Amazon Inspector
- D. Amazon Detective

**24.** Which AWS service uses machine learning to discover and classify sensitive data, such as personally identifiable information, stored in Amazon S3?

- A. Amazon Macie
- B. Amazon GuardDuty
- C. AWS Secrets Manager
- D. AWS Key Management Service (AWS KMS)

**25.** A public-facing web application must be protected against large-scale distributed denial of service (DDoS) attacks, and the company wants 24/7 access to the AWS DDoS Response Team plus cost protection for scaling charges during an attack. Which service should it use?

- A. AWS Shield Standard
- B. AWS Shield Advanced
- C. AWS WAF
- D. Amazon GuardDuty

**26.** A company needs to block SQL injection and cross-site scripting attempts against an application behind an Application Load Balancer. Which service provides this protection?

- A. AWS WAF
- B. Network ACLs
- C. Security groups
- D. AWS Firewall Manager

**27.** Which AWS service allows a company to create and control the cryptographic keys used to encrypt data across AWS services, with usage logged to AWS CloudTrail?

- A. AWS Certificate Manager (ACM)
- B. AWS Key Management Service (AWS KMS)
- C. AWS Secrets Manager
- D. AWS IAM Identity Center

**28.** A company wants to store database credentials securely and rotate them automatically on a schedule without changing application code. Which service should it use?

- A. AWS Systems Manager Parameter Store standard parameters
- B. AWS Secrets Manager
- C. Amazon S3 with server-side encryption
- D. AWS Key Management Service (AWS KMS)

**29.** A security investigator needs to determine which IAM identity deleted an Amazon EC2 instance last Tuesday, and from which IP address. Which service provides this information?

- A. Amazon CloudWatch
- B. AWS CloudTrail
- C. AWS Config
- D. VPC Flow Logs

**30.** A company must continuously evaluate whether all Amazon S3 buckets have public access blocked and be alerted when a bucket becomes noncompliant. Which service should it use?

- A. AWS Config
- B. AWS CloudTrail
- C. AWS Trusted Advisor
- D. Amazon Inspector

**31.** Which statements about security groups and network ACLs are correct? (Choose TWO.)

- A. Security groups are stateful; return traffic is automatically allowed
- B. Security groups support both allow and deny rules
- C. Network ACLs are stateless; return traffic must be explicitly allowed
- D. Network ACLs operate at the instance level
- E. Security groups apply to an entire subnet by default

**32.** A company with 4,000 employees wants users to sign in to AWS with their existing corporate Active Directory credentials instead of creating separate IAM users. Which approach should it use?

- A. Create an IAM user for each employee and synchronize passwords manually
- B. Use AWS IAM Identity Center with the corporate identity source for single sign-on
- C. Share a single IAM user across each department
- D. Give each employee limited access to the account root user

**33.** Which AWS service provisions, manages and renews the public SSL/TLS certificates used to encrypt traffic to an Application Load Balancer at no additional cost?

- A. AWS Key Management Service (AWS KMS)
- B. AWS Certificate Manager (ACM)
- C. AWS CloudHSM
- D. Amazon Route 53

**34.** A company runs 30 AWS accounts and wants a single dashboard that aggregates security findings from GuardDuty, Inspector and Macie and checks resources against standards such as CIS AWS Foundations Benchmark. Which service should it use?

- A. AWS Security Hub
- B. Amazon Detective
- C. AWS Organizations
- D. AWS Audit Manager

**35.** Which statement about encrypting data at rest in Amazon S3 is correct?

- A. Encryption at rest is not available in Amazon S3
- B. Amazon S3 applies server-side encryption to new objects by default, and customers may also supply their own keys
- C. Customers must decrypt objects manually before every read
- D. Only objects larger than 5 GB can be encrypted

**36.** What is an AWS Availability Zone?

- A. A single data center in a specific city
- B. One or more discrete data centers with redundant power, networking and connectivity within an AWS Region
- C. A cache location used only by Amazon CloudFront
- D. A logical grouping of AWS accounts

**37.** A media company hosts video files in Amazon S3 in us-east-1 but has viewers worldwide who report slow load times. Which service should the company add to reduce latency?

- A. Amazon CloudFront
- B. AWS Direct Connect
- C. Amazon Route 53 health checks
- D. Elastic Load Balancing

**38.** Which factors should a company consider when choosing an AWS Region for a new workload? (Choose TWO.)

- A. Data sovereignty and compliance requirements
- B. The number of IAM users in the account
- C. Proximity to end users to reduce latency
- D. The AWS account's support plan tier
- E. The color scheme of the AWS Management Console

**39.** A company runs a batch scientific simulation that is heavily CPU-bound and uses very little memory or storage. Which Amazon EC2 instance family is the BEST fit?

- A. Memory optimized
- B. Compute optimized
- C. Storage optimized
- D. General purpose burstable

**40.** A company wants to run a short image-processing function each time a file is uploaded to Amazon S3, without provisioning or managing any servers, and pay only for the compute time consumed. Which service should it use?

- A. Amazon EC2 with Auto Scaling
- B. AWS Lambda
- C. AWS Batch
- D. Amazon Lightsail

**41.** A company wants to run Docker containers on AWS without provisioning or managing the underlying EC2 instances. Which service provides this?

- A. AWS Fargate
- B. Amazon EC2 Auto Scaling
- C. AWS Elastic Beanstalk
- D. Amazon EMR

**42.** Which service automatically adds Amazon EC2 instances when application load increases and removes them when load decreases?

- A. Elastic Load Balancing
- B. Amazon EC2 Auto Scaling
- C. AWS Auto Scaling groups in Amazon Route 53
- D. AWS CloudFormation

**43.** A web application runs on multiple Amazon EC2 instances in two Availability Zones. Which service should be used to distribute incoming HTTPS traffic across the healthy instances?

- A. Amazon CloudFront
- B. Elastic Load Balancing
- C. AWS Global Accelerator
- D. Amazon Route 53 simple routing

**44.** Which AWS service provides durable object storage that can also host a static website consisting of HTML, CSS and JavaScript files?

- A. Amazon Elastic Block Store (Amazon EBS)
- B. Amazon Elastic File System (Amazon EFS)
- C. Amazon S3
- D. Amazon FSx for Windows File Server

**45.** A company must retain compliance archives for 10 years. The data is almost never accessed, and a retrieval time of up to 12 hours is acceptable. Which S3 storage class offers the LOWEST cost?

- A. S3 Standard
- B. S3 Standard-Infrequent Access
- C. S3 Glacier Flexible Retrieval
- D. S3 Glacier Deep Archive

**46.** Which AWS storage service provides persistent block storage volumes that are attached to a single Amazon EC2 instance and can be backed up with snapshots to Amazon S3?

- A. Amazon S3
- B. Amazon Elastic Block Store (Amazon EBS)
- C. Amazon Elastic File System (Amazon EFS)
- D. AWS Storage Gateway

**47.** Several Linux Amazon EC2 instances across multiple Availability Zones need concurrent read/write access to the same file system, which must grow and shrink automatically. Which service meets this requirement?

- A. Amazon EBS Multi-Attach
- B. Amazon Elastic File System (Amazon EFS)
- C. Amazon S3 Glacier
- D. Instance store volumes

**48.** A company wants its Amazon RDS database to fail over automatically to a standby copy in another Availability Zone if the primary instance fails. Which feature should it enable?

- A. Read replicas
- B. Multi-AZ deployment
- C. Automated snapshots
- D. Amazon RDS Proxy

**49.** A mobile gaming application needs a fully managed NoSQL key-value database that delivers single-digit millisecond performance at any scale, with no servers to manage. Which service should be used?

- A. Amazon RDS for MySQL
- B. Amazon Redshift
- C. Amazon DynamoDB
- D. Amazon Neptune

**50.** A company needs to run complex analytical SQL queries and generate business intelligence reports across petabytes of historical sales data. Which service is designed for this workload?

- A. Amazon Redshift
- B. Amazon DynamoDB
- C. Amazon ElastiCache
- D. Amazon RDS for PostgreSQL

**51.** A company wants to place its database servers in a network segment that has no direct route to or from the internet, while its web servers remain reachable from the internet. What should the company configure?

- A. Two AWS accounts, one for each tier
- B. Public and private subnets within an Amazon VPC
- C. Two AWS Regions, one for each tier
- D. An AWS Direct Connect connection for the database tier

**52.** A company needs a dedicated, private network connection between its on-premises data center and AWS that provides consistent network performance and does not traverse the public internet. Which service should it use?

- A. AWS Site-to-Site VPN
- B. AWS Direct Connect
- C. Amazon VPC peering
- D. AWS Transit Gateway

**53.** Which AWS service provides domain name registration, DNS routing and health checking for application endpoints?

- A. Amazon CloudFront
- B. AWS Global Accelerator
- C. Amazon Route 53
- D. Elastic Load Balancing

**54.** An order-processing application must continue accepting orders even when the downstream fulfillment component is temporarily unavailable. Which service should be placed between the two components?

- A. Amazon SQS
- B. Amazon SNS
- C. AWS Step Functions
- D. Amazon EventBridge Scheduler

**55.** A company wants to define its AWS infrastructure in a template file, place it in version control, and deploy identical environments for development, test and production. Which service should it use?

- A. AWS CloudFormation
- B. AWS CodeDeploy
- C. AWS Systems Manager Session Manager
- D. AWS Config

**56.** An operations team needs to be notified when the average CPU utilization of a group of Amazon EC2 instances exceeds 80 percent for five minutes. Which service should it use?

- A. AWS CloudTrail
- B. Amazon CloudWatch alarms
- C. AWS Trusted Advisor
- D. AWS X-Ray

**57.** A company wants to automatically detect objects and text in images uploaded by users, without building or training its own machine learning model. Which service should it use?

- A. Amazon SageMaker AI
- B. Amazon Rekognition
- C. Amazon Comprehend
- D. Amazon Textract

**58.** A company runs a fault-tolerant image-rendering job that can be interrupted and restarted at any time. Which Amazon EC2 purchasing option provides the LOWEST cost?

- A. On-Demand Instances
- B. Reserved Instances
- C. Spot Instances
- D. Dedicated Hosts

**59.** A company runs a steady, predictable production workload on Amazon EC2 that will run continuously for the next three years. Which option provides the greatest cost savings?

- A. On-Demand Instances
- B. Spot Instances
- C. A three-year Compute Savings Plan with all upfront payment
- D. Dedicated Hosts billed hourly

**60.** Which statement about the AWS Free Tier is correct?

- A. It includes only 12-month trials that begin at account creation
- B. It includes three types of offer: always free, 12 months free, and short-term trials
- C. It makes all AWS services free for the first year
- D. It is available only to customers on the Business Support plan

**61.** A finance team wants to receive an email alert when the company's monthly AWS spending is forecast to exceed 10,000 US dollars. Which service should it use?

- A. AWS Budgets
- B. AWS Cost Explorer
- C. AWS Pricing Calculator
- D. AWS Cost and Usage Report

**62.** A manager wants to view AWS spending trends over the past 12 months, broken down by service and by cost allocation tag, and see a forecast of next month's costs. Which tool provides this?

- A. AWS Budgets
- B. AWS Cost Explorer
- C. AWS Trusted Advisor
- D. AWS Compute Optimizer

**63.** Which are benefits of using consolidated billing in AWS Organizations? (Choose TWO.)

- A. A single bill covering all member accounts
- B. Combined usage across accounts that can qualify for volume pricing tiers
- C. Automatic elimination of data transfer charges between accounts
- D. Unlimited free usage for all member accounts
- E. Free Enterprise Support for every member account

**64.** A company requires a designated Technical Account Manager (TAM) and a 15-minute response time for business-critical system down cases. Which AWS Support plan meets these requirements?

- A. Basic Support
- B. Developer Support
- C. Business Support
- D. Enterprise Support

**65.** Before migrating to AWS, a company wants to model the monthly cost of a proposed architecture consisting of EC2 instances, EBS volumes and an RDS database. Which tool should it use?

- A. AWS Pricing Calculator
- B. AWS Cost Explorer
- C. AWS Billing Conductor
- D. AWS Cost Anomaly Detection

---

## Answer key

| # | Domain | Answer | Topic |
| --- | --- | --- | --- |
| 1 | Cloud Concepts | B | Cloud economics (CapEx vs OpEx) |
| 2 | Cloud Concepts | A | Elasticity vs scalability |
| 3 | Cloud Concepts | C | AWS Well-Architected Framework |
| 4 | Cloud Concepts | A | Agility / speed to market |
| 5 | Cloud Concepts | B | Economies of scale |
| 6 | Cloud Concepts | C | Cloud migration strategies (the 6 R's) |
| 7 | Cloud Concepts | B | Cloud deployment models |
| 8 | Cloud Concepts | A | Global reach |
| 9 | Cloud Concepts | A, C | AWS Cloud Adoption Framework (CAF) |
| 10 | Cloud Concepts | B | High availability vs fault tolerance |
| 11 | Cloud Concepts | B | Cloud architecture design principles |
| 12 | Cloud Concepts | A | AWS Well-Architected Tool |
| 13 | Cloud Concepts | A | Reliability pillar |
| 14 | Cloud Concepts | A, C | Benefits of cloud computing |
| 15 | Cloud Concepts | C | Cloud service models |
| 16 | Cloud Concepts | B | Sustainability pillar |
| 17 | Security and Compliance | B | Shared responsibility model |
| 18 | Security and Compliance | B | Shared responsibility model |
| 19 | Security and Compliance | B | IAM roles |
| 20 | Security and Compliance | A, C | Root user protection |
| 21 | Security and Compliance | A | AWS Artifact |
| 22 | Security and Compliance | B | Amazon GuardDuty |
| 23 | Security and Compliance | C | Amazon Inspector |
| 24 | Security and Compliance | A | Amazon Macie |
| 25 | Security and Compliance | B | AWS Shield |
| 26 | Security and Compliance | A | AWS WAF |
| 27 | Security and Compliance | B | AWS KMS |
| 28 | Security and Compliance | B | AWS Secrets Manager |
| 29 | Security and Compliance | B | AWS CloudTrail |
| 30 | Security and Compliance | A | AWS Config |
| 31 | Security and Compliance | A, C | Security groups vs network ACLs |
| 32 | Security and Compliance | B | AWS IAM Identity Center / federation |
| 33 | Security and Compliance | B | Encryption in transit |
| 34 | Security and Compliance | A | AWS Security Hub |
| 35 | Security and Compliance | B | Encryption at rest |
| 36 | Cloud Technology and Services | B | AWS global infrastructure |
| 37 | Cloud Technology and Services | A | Amazon CloudFront |
| 38 | Cloud Technology and Services | A, C | Selecting an AWS Region |
| 39 | Cloud Technology and Services | B | Amazon EC2 instance types |
| 40 | Cloud Technology and Services | B | AWS Lambda |
| 41 | Cloud Technology and Services | A | Containers on AWS |
| 42 | Cloud Technology and Services | B | Amazon EC2 Auto Scaling |
| 43 | Cloud Technology and Services | B | Elastic Load Balancing |
| 44 | Cloud Technology and Services | C | Amazon S3 |
| 45 | Cloud Technology and Services | D | S3 storage classes |
| 46 | Cloud Technology and Services | B | Amazon EBS |
| 47 | Cloud Technology and Services | B | Amazon EFS |
| 48 | Cloud Technology and Services | B | Amazon RDS Multi-AZ |
| 49 | Cloud Technology and Services | C | Amazon DynamoDB |
| 50 | Cloud Technology and Services | A | Amazon Redshift |
| 51 | Cloud Technology and Services | B | Amazon VPC |
| 52 | Cloud Technology and Services | B | AWS Direct Connect |
| 53 | Cloud Technology and Services | C | Amazon Route 53 |
| 54 | Cloud Technology and Services | A | Amazon SQS |
| 55 | Cloud Technology and Services | A | AWS CloudFormation |
| 56 | Cloud Technology and Services | B | Amazon CloudWatch |
| 57 | Cloud Technology and Services | B | AWS machine learning services |
| 58 | Billing, Pricing, and Support | C | Amazon EC2 Spot Instances |
| 59 | Billing, Pricing, and Support | C | Savings Plans and Reserved Instances |
| 60 | Billing, Pricing, and Support | B | AWS Free Tier |
| 61 | Billing, Pricing, and Support | A | AWS Budgets |
| 62 | Billing, Pricing, and Support | B | AWS Cost Explorer |
| 63 | Billing, Pricing, and Support | A, B | Consolidated billing and AWS Organizations |
| 64 | Billing, Pricing, and Support | D | AWS Support plans |
| 65 | Billing, Pricing, and Support | A | AWS Pricing Calculator |

---

## Explanations

### 1. Cloud economics (CapEx vs OpEx)

**Correct answer: B** — *Domain 1: Cloud Concepts*

> B. A shift from capital expense to variable operational expense

Buying and racking hardware is a capital expense (CapEx) paid up front. In the cloud you pay only for the resources you consume, which converts that spend into a variable operational expense (OpEx). This is one of the six core advantages of cloud computing.

**Why the other options are wrong:** A is wrong because cloud spend varies with consumption. C is wrong because you still pay for what you use. D is unrelated to cloud adoption.

### 2. Elasticity vs scalability

**Correct answer: A** — *Domain 1: Cloud Concepts*

> A. Elasticity

Elasticity is the ability to acquire resources as you need them and release them when you no longer need them, automatically matching supply to demand.

**Why the other options are wrong:** Fault tolerance and high availability are about surviving failure, not matching capacity to demand. Loose coupling is an architectural design principle that reduces dependencies between components.

### 3. AWS Well-Architected Framework

**Correct answer: C** — *Domain 1: Cloud Concepts*

> C. Operational Excellence

Operational Excellence covers running and monitoring systems, managing change through automation, and continually improving processes and procedures.

**Why the other options are wrong:** Reliability covers recovery from failure. Performance Efficiency covers using computing resources efficiently. Cost Optimization covers avoiding unnecessary spend.

### 4. Agility / speed to market

**Correct answer: A** — *Domain 1: Cloud Concepts*

> A. Increased agility through rapid provisioning of resources

AWS resources can be provisioned in minutes rather than weeks, which increases agility and dramatically lowers the cost of experimentation and failure.

**Why the other options are wrong:** B, C and D may be benefits of the cloud in general, but none of them address procurement lead time.

### 5. Economies of scale

**Correct answer: B** — *Domain 1: Cloud Concepts*

> B. Massive economies of scale

Because hundreds of thousands of customers aggregate their usage in the cloud, AWS achieves higher economies of scale than any single organization could, and passes the resulting lower per-unit costs on as price reductions.

**Why the other options are wrong:** The other options are genuine cloud advantages but they describe how you are billed or where you deploy, not why unit prices keep falling.

### 6. Cloud migration strategies (the 6 R's)

**Correct answer: C** — *Domain 1: Cloud Concepts*

> C. Rehosting

Rehosting, commonly called 'lift and shift', moves an application to the cloud without changing it. It is the fastest strategy and is often used for large-scale migrations that will be optimized later.

**Why the other options are wrong:** Refactoring re-architects the application. Repurchasing moves to a different product, often SaaS. Retiring decommissions the application entirely.

### 7. Cloud deployment models

**Correct answer: B** — *Domain 1: Cloud Concepts*

> B. Hybrid

A hybrid deployment connects cloud resources to on-premises infrastructure, which is common when data must stay in a specific location or when a company is migrating in phases.

**Why the other options are wrong:** An all-in cloud deployment has no on-premises component. A private cloud runs entirely on-premises. Multi-tenant is not a deployment model.

### 8. Global reach

**Correct answer: A** — *Domain 1: Cloud Concepts*

> A. The ability to go global in minutes by deploying into additional AWS Regions

AWS operates Regions worldwide, so a workload can be deployed closer to users in minutes to reduce latency, without negotiating contracts or building facilities.

**Why the other options are wrong:** B and C are not AWS offerings. D is false: data stays in the Region you choose unless you explicitly configure replication.

### 9. AWS Cloud Adoption Framework (CAF)

**Correct answer: A, C** — *Domain 1: Cloud Concepts*

> A. Business

> C. Governance

The AWS CAF organizes guidance into six perspectives: Business, People, Governance, Platform, Security, and Operations. Business and Governance are two of them.

**Why the other options are wrong:** Sustainability, Reliability and Cost Optimization are pillars of the Well-Architected Framework, not CAF perspectives. Knowing which framework a term belongs to is a frequent exam distinction.

### 10. High availability vs fault tolerance

**Correct answer: B** — *Domain 1: Cloud Concepts*

> B. High availability

High availability means the system remains operational, with minimal downtime, when a component fails. Spreading instances across Availability Zones is the standard way to achieve it on AWS.

**Why the other options are wrong:** Elasticity is about matching capacity to demand. Vertical scaling means resizing a single instance, which does not protect against an AZ failure.

### 11. Cloud architecture design principles

**Correct answer: B** — *Domain 1: Cloud Concepts*

> B. Loose coupling

Loose coupling reduces interdependencies so that a failure or change in one component does not cascade to others. Queues and load balancers act as intermediaries that absorb change.

**Why the other options are wrong:** Design for failure is a broader principle about assuming components will fail. Vertical scaling and monolithic design are not communication patterns.

### 12. AWS Well-Architected Tool

**Correct answer: A** — *Domain 1: Cloud Concepts*

> A. AWS Well-Architected Tool

The AWS Well-Architected Tool provides a free, self-service review of workloads against the pillars of the Well-Architected Framework and produces an improvement plan.

**Why the other options are wrong:** AWS Config records resource configurations. Systems Manager manages operations at scale. Compute Optimizer recommends instance right-sizing only.

### 13. Reliability pillar

**Correct answer: A** — *Domain 1: Cloud Concepts*

> A. Automatically recover from failure

Reliability design principles include automatically recovering from failure, testing recovery procedures, scaling horizontally, stopping guessing capacity, and managing change through automation.

**Why the other options are wrong:** Adopting a consumption model belongs to Cost Optimization, reducing environmental impact to Sustainability, and performing operations as code to Operational Excellence.

### 14. Benefits of cloud computing

**Correct answer: A, C** — *Domain 1: Cloud Concepts*

> A. Stop guessing capacity

> C. Benefit from massive economies of scale

'Stop guessing capacity' and 'benefit from massive economies of scale' are two of the six advantages of cloud computing, alongside trading capital expense for variable expense, increasing speed and agility, stopping spending money running and maintaining data centers, and going global in minutes.

**Why the other options are wrong:** The cloud reduces undifferentiated heavy lifting rather than increasing it, security remains a shared responsibility, and cost outcomes depend on how you use the platform.

### 15. Cloud service models

**Correct answer: C** — *Domain 1: Cloud Concepts*

> C. Infrastructure as a service (IaaS)

IaaS provides the basic building blocks of compute, storage and networking and gives the customer the highest level of flexibility and control over IT resources, including the operating system.

**Why the other options are wrong:** With PaaS, such as AWS Elastic Beanstalk, AWS manages the underlying OS and runtime. SaaS delivers a finished application. FaaS, such as AWS Lambda, runs code without any server management.

### 16. Sustainability pillar

**Correct answer: B** — *Domain 1: Cloud Concepts*

> B. Maximizing utilization of provisioned resources and right-sizing instances

The Sustainability pillar focuses on reducing the energy and resources consumed per unit of work, primarily by maximizing utilization, right-sizing, and using managed and serverless services.

**Why the other options are wrong:** Reserved Instances are a pricing decision, Region choice by headquarters location is not a sustainability practice, and MFA belongs to the Security pillar.

### 17. Shared responsibility model

**Correct answer: B** — *Domain 2: Security and Compliance*

> B. The customer is responsible

For EC2, the customer controls the guest operating system and is responsible for patching and hardening it. AWS is responsible for the hypervisor and the underlying host infrastructure.

**Why the other options are wrong:** AWS patches the guest OS only for managed services such as Amazon RDS or Lambda, where the customer has no OS access.

### 18. Shared responsibility model

**Correct answer: B** — *Domain 2: Security and Compliance*

> B. Managing physical security of the data centers

AWS is responsible for security 'of' the cloud, which includes the physical facilities, hardware, and the global infrastructure of Regions, Availability Zones and edge locations.

**Why the other options are wrong:** Security groups, data encryption choices, and credential rotation are all customer responsibilities, which fall under security 'in' the cloud.

### 19. IAM roles

**Correct answer: B** — *Domain 2: Security and Compliance*

> B. Attach an IAM role with the required permissions to the EC2 instance

An IAM role attached to the instance supplies temporary, automatically rotated credentials to the application, so no long-term keys are ever stored on disk. This is the AWS best practice.

**Why the other options are wrong:** Long-term keys on disk can be stolen, public buckets expose data to everyone, and root credentials should never be used by applications.

### 20. Root user protection

**Correct answer: A, C** — *Domain 2: Security and Compliance*

> A. Enable multi-factor authentication (MFA) on the root user

> C. Create an IAM identity with appropriate permissions for everyday administrative tasks

AWS recommends enabling MFA on the root user, locking away its credentials, and creating separate identities with least-privilege permissions for daily work.

**Why the other options are wrong:** Sharing root credentials destroys accountability, root access keys should not be created, and you cannot restrict the root user's permissions with an IAM policy (only Organizations SCPs can limit a member account root).

### 21. AWS Artifact

**Correct answer: A** — *Domain 2: Security and Compliance*

> A. AWS Artifact

AWS Artifact is the self-service portal for on-demand access to AWS compliance reports and agreements, including SOC reports, PCI documents and ISO certifications.

**Why the other options are wrong:** Trusted Advisor gives optimization checks, Security Hub aggregates security findings, and CloudTrail records API activity.

### 22. Amazon GuardDuty

**Correct answer: B** — *Domain 2: Security and Compliance*

> B. Amazon GuardDuty

Amazon GuardDuty is a managed threat detection service that analyzes log sources with machine learning and threat intelligence feeds to produce security findings.

**Why the other options are wrong:** Inspector scans for software vulnerabilities, Macie discovers sensitive data in S3, and Shield protects against DDoS attacks.

### 23. Amazon Inspector

**Correct answer: C** — *Domain 2: Security and Compliance*

> C. Amazon Inspector

Amazon Inspector continually scans EC2 instances, container images in Amazon ECR, and Lambda functions for software vulnerabilities and unintended network exposure.

**Why the other options are wrong:** Macie targets sensitive data in S3, Config evaluates resource configuration compliance, and Detective analyzes findings to investigate the root cause of security issues.

### 24. Amazon Macie

**Correct answer: A** — *Domain 2: Security and Compliance*

> A. Amazon Macie

Amazon Macie discovers, classifies and helps protect sensitive data such as PII in Amazon S3 buckets, and reports on bucket security posture.

**Why the other options are wrong:** GuardDuty detects threats, Secrets Manager stores and rotates secrets, and KMS manages encryption keys.

### 25. AWS Shield

**Correct answer: B** — *Domain 2: Security and Compliance*

> B. AWS Shield Advanced

AWS Shield Advanced is a paid tier that adds enhanced DDoS protections, 24/7 access to the Shield Response Team, detailed attack diagnostics, and cost protection for scaling that occurs during an attack.

**Why the other options are wrong:** Shield Standard is free and automatic but has none of those extras. AWS WAF filters layer 7 web requests. GuardDuty is threat detection, not mitigation.

### 26. AWS WAF

**Correct answer: A** — *Domain 2: Security and Compliance*

> A. AWS WAF

AWS WAF is a web application firewall that inspects HTTP and HTTPS requests and blocks common exploits such as SQL injection and cross-site scripting using managed or custom rules.

**Why the other options are wrong:** Network ACLs and security groups filter on IP, protocol and port, not request content. Firewall Manager centrally administers WAF rules across accounts but is not itself the inspection engine.

### 27. AWS KMS

**Correct answer: B** — *Domain 2: Security and Compliance*

> B. AWS Key Management Service (AWS KMS)

AWS KMS creates and manages KMS keys, integrates with most AWS services for encryption at rest, and logs every key usage request to CloudTrail for auditing.

**Why the other options are wrong:** ACM provisions TLS certificates, Secrets Manager stores credentials, and IAM Identity Center manages workforce sign-in.

### 28. AWS Secrets Manager

**Correct answer: B** — *Domain 2: Security and Compliance*

> B. AWS Secrets Manager

AWS Secrets Manager stores secrets encrypted with KMS and provides built-in automatic rotation for supported databases, so applications retrieve the current credential at runtime.

**Why the other options are wrong:** Parameter Store can store secure strings but does not provide native managed rotation. S3 is object storage, and KMS manages keys rather than secrets.

### 29. AWS CloudTrail

**Correct answer: B** — *Domain 2: Security and Compliance*

> B. AWS CloudTrail

AWS CloudTrail records API activity across the account, capturing who made each call, when, from which source IP address, and what the request parameters were.

**Why the other options are wrong:** CloudWatch collects performance metrics and logs, Config tracks configuration state over time, and VPC Flow Logs record network traffic metadata.

### 30. AWS Config

**Correct answer: A** — *Domain 2: Security and Compliance*

> A. AWS Config

AWS Config records the configuration of resources over time and evaluates them against rules, flagging resources as compliant or noncompliant and reporting configuration drift.

**Why the other options are wrong:** CloudTrail records the API calls that caused a change but does not evaluate ongoing compliance. Trusted Advisor performs periodic checks against a fixed set of best practices, and Inspector scans for vulnerabilities.

### 31. Security groups vs network ACLs

**Correct answer: A, C** — *Domain 2: Security and Compliance*

> A. Security groups are stateful; return traffic is automatically allowed

> C. Network ACLs are stateless; return traffic must be explicitly allowed

Security groups act at the instance (elastic network interface) level and are stateful, so responses to allowed requests are permitted automatically. Network ACLs act at the subnet level and are stateless, so inbound and outbound rules must both be defined.

**Why the other options are wrong:** Security groups support allow rules only. The instance-level and subnet-level roles in options D and E are reversed.

### 32. AWS IAM Identity Center / federation

**Correct answer: B** — *Domain 2: Security and Compliance*

> B. Use AWS IAM Identity Center with the corporate identity source for single sign-on

AWS IAM Identity Center provides single sign-on to AWS accounts and applications using an existing identity source such as Active Directory or an external IdP, so no per-employee IAM users are needed.

**Why the other options are wrong:** Per-user IAM accounts do not scale and duplicate identity management. Sharing credentials removes accountability, and root access must never be delegated.

### 33. Encryption in transit

**Correct answer: B** — *Domain 2: Security and Compliance*

> B. AWS Certificate Manager (ACM)

AWS Certificate Manager issues and automatically renews public TLS certificates for use with integrated services such as ELB, CloudFront and API Gateway, at no charge for the certificates.

**Why the other options are wrong:** KMS manages data encryption keys, CloudHSM provides dedicated hardware security modules, and Route 53 is DNS.

### 34. AWS Security Hub

**Correct answer: A** — *Domain 2: Security and Compliance*

> A. AWS Security Hub

AWS Security Hub aggregates, organizes and prioritizes security findings from multiple AWS security services and partner products, and runs automated best-practice checks against security standards.

**Why the other options are wrong:** Detective investigates the root cause of specific findings, Organizations manages accounts and policies, and Audit Manager automates evidence collection for audits.

### 35. Encryption at rest

**Correct answer: B** — *Domain 2: Security and Compliance*

> B. Amazon S3 applies server-side encryption to new objects by default, and customers may also supply their own keys

Amazon S3 encrypts new objects with server-side encryption by default (SSE-S3), and customers can choose SSE-KMS with customer-managed keys or SSE-C with customer-provided keys for additional control.

**Why the other options are wrong:** Decryption is handled transparently for authorized requests, and there is no object size requirement for encryption.

### 36. AWS global infrastructure

**Correct answer: B** — *Domain 3: Cloud Technology and Services*

> B. One or more discrete data centers with redundant power, networking and connectivity within an AWS Region

An Availability Zone consists of one or more discrete data centers with redundant power, networking and connectivity, physically separated from other AZs in the same Region but connected by low-latency links.

**Why the other options are wrong:** A single data center is not an AZ, edge locations serve CloudFront, and account groupings are organizational units in AWS Organizations.

### 37. Amazon CloudFront

**Correct answer: A** — *Domain 3: Cloud Technology and Services*

> A. Amazon CloudFront

Amazon CloudFront is a content delivery network that caches content at edge locations close to viewers, reducing latency and offloading traffic from the origin.

**Why the other options are wrong:** Direct Connect provides a private link from a corporate data center, Route 53 health checks monitor endpoints, and ELB distributes traffic within a Region.

### 38. Selecting an AWS Region

**Correct answer: A, C** — *Domain 3: Cloud Technology and Services*

> A. Data sovereignty and compliance requirements

> C. Proximity to end users to reduce latency

The standard Region selection criteria are compliance and data residency, latency to users, service availability in the Region, and price, which varies by Region.

**Why the other options are wrong:** IAM users are global to the account, and the support plan and console appearance have no bearing on Region choice.

### 39. Amazon EC2 instance types

**Correct answer: B** — *Domain 3: Cloud Technology and Services*

> B. Compute optimized

Compute optimized instances provide a high ratio of vCPU to memory and are designed for compute-bound workloads such as batch processing, scientific modeling and high-performance web servers.

**Why the other options are wrong:** Memory optimized suits in-memory databases, storage optimized suits high sequential disk I/O, and burstable instances are for workloads with low baseline CPU usage.

### 40. AWS Lambda

**Correct answer: B** — *Domain 3: Cloud Technology and Services*

> B. AWS Lambda

AWS Lambda runs code in response to events, such as an S3 object upload, with no servers to manage and billing based on the number of requests and the duration of execution.

**Why the other options are wrong:** EC2 and Lightsail require server management. AWS Batch is for large-scale, long-running batch jobs rather than short event-driven functions.

### 41. Containers on AWS

**Correct answer: A** — *Domain 3: Cloud Technology and Services*

> A. AWS Fargate

AWS Fargate is the serverless compute engine for containers. It works with Amazon ECS and Amazon EKS and removes the need to provision, patch or scale container hosts.

**Why the other options are wrong:** EC2 Auto Scaling manages EC2 capacity you still own, Elastic Beanstalk deploys applications onto EC2 instances you can see, and EMR runs big data frameworks.

### 42. Amazon EC2 Auto Scaling

**Correct answer: B** — *Domain 3: Cloud Technology and Services*

> B. Amazon EC2 Auto Scaling

Amazon EC2 Auto Scaling maintains a desired number of healthy instances and scales the group out or in based on demand, health checks or a schedule.

**Why the other options are wrong:** ELB distributes traffic across existing instances but does not create them. Route 53 has no Auto Scaling groups, and CloudFormation provisions infrastructure from templates.

### 43. Elastic Load Balancing

**Correct answer: B** — *Domain 3: Cloud Technology and Services*

> B. Elastic Load Balancing

Elastic Load Balancing automatically distributes incoming traffic across multiple targets in one or more Availability Zones and routes only to targets that pass health checks.

**Why the other options are wrong:** CloudFront caches content at the edge, Global Accelerator improves global network paths, and simple DNS routing does not perform health-aware load distribution across instances.

### 44. Amazon S3

**Correct answer: C** — *Domain 3: Cloud Technology and Services*

> C. Amazon S3

Amazon S3 stores objects with 11 nines of durability and can serve a static website directly from a bucket.

**Why the other options are wrong:** EBS is block storage attached to a single EC2 instance, and EFS and FSx are file systems mounted by instances; none of them serve websites directly.

### 45. S3 storage classes

**Correct answer: D** — *Domain 3: Cloud Technology and Services*

> D. S3 Glacier Deep Archive

S3 Glacier Deep Archive is the lowest-cost storage class in Amazon S3 and is designed for data accessed once or twice a year with retrieval times of 12 hours or more.

**Why the other options are wrong:** S3 Standard and Standard-IA cost far more per GB, and Glacier Flexible Retrieval is more expensive than Deep Archive because it offers faster retrieval options.

### 46. Amazon EBS

**Correct answer: B** — *Domain 3: Cloud Technology and Services*

> B. Amazon Elastic Block Store (Amazon EBS)

Amazon EBS provides block-level storage volumes for EC2 instances. Volumes persist independently of the instance lifecycle and support point-in-time snapshots stored in Amazon S3.

**Why the other options are wrong:** S3 is object storage, EFS is a shared file system, and Storage Gateway connects on-premises environments to AWS storage.

### 47. Amazon EFS

**Correct answer: B** — *Domain 3: Cloud Technology and Services*

> B. Amazon Elastic File System (Amazon EFS)

Amazon EFS is a fully managed, elastic NFS file system that can be mounted concurrently by thousands of EC2 instances across multiple Availability Zones.

**Why the other options are wrong:** EBS volumes live in a single AZ and Multi-Attach is limited to a few instances in one AZ, Glacier is archival object storage, and instance store is ephemeral local disk.

### 48. Amazon RDS Multi-AZ

**Correct answer: B** — *Domain 3: Cloud Technology and Services*

> B. Multi-AZ deployment

A Multi-AZ deployment maintains a synchronous standby replica in a different Availability Zone and fails over to it automatically, which is a high availability feature.

**Why the other options are wrong:** Read replicas scale read traffic and are asynchronous, snapshots are backups that must be restored manually, and RDS Proxy pools connections.

### 49. Amazon DynamoDB

**Correct answer: C** — *Domain 3: Cloud Technology and Services*

> C. Amazon DynamoDB

Amazon DynamoDB is a serverless NoSQL key-value and document database that provides consistent single-digit millisecond latency at virtually any scale.

**Why the other options are wrong:** RDS is relational, Redshift is a data warehouse for analytics, and Neptune is a graph database.

### 50. Amazon Redshift

**Correct answer: A** — *Domain 3: Cloud Technology and Services*

> A. Amazon Redshift

Amazon Redshift is a fully managed, petabyte-scale cloud data warehouse optimized for online analytical processing (OLAP) and business intelligence reporting.

**Why the other options are wrong:** DynamoDB is optimized for high-volume transactional key lookups, ElastiCache is an in-memory cache, and RDS is tuned for transactional (OLTP) workloads.

### 51. Amazon VPC

**Correct answer: B** — *Domain 3: Cloud Technology and Services*

> B. Public and private subnets within an Amazon VPC

Within a VPC, a public subnet has a route to an internet gateway while a private subnet does not. Placing databases in private subnets isolates them from inbound internet traffic.

**Why the other options are wrong:** Separate accounts or Regions add complexity without solving the routing requirement, and Direct Connect links an on-premises network to AWS.

### 52. AWS Direct Connect

**Correct answer: B** — *Domain 3: Cloud Technology and Services*

> B. AWS Direct Connect

AWS Direct Connect provides a dedicated private physical connection from an on-premises location to AWS, delivering more consistent network performance than internet-based connections.

**Why the other options are wrong:** Site-to-Site VPN is encrypted but runs over the public internet. VPC peering and Transit Gateway connect AWS networks to each other, not to a data center.

### 53. Amazon Route 53

**Correct answer: C** — *Domain 3: Cloud Technology and Services*

> C. Amazon Route 53

Amazon Route 53 is a highly available and scalable DNS web service that also registers domain names and performs health checks with multiple routing policies.

**Why the other options are wrong:** CloudFront is a CDN, Global Accelerator provides static anycast IPs over the AWS network, and ELB balances traffic within a Region.

### 54. Amazon SQS

**Correct answer: A** — *Domain 3: Cloud Technology and Services*

> A. Amazon SQS

Amazon SQS is a fully managed message queue that decouples components. Messages are retained until the consumer processes them, so a slow or offline consumer does not stop the producer.

**Why the other options are wrong:** SNS is a publish/subscribe notification service that pushes to subscribers, Step Functions orchestrates workflows, and EventBridge Scheduler triggers scheduled events.

### 55. AWS CloudFormation

**Correct answer: A** — *Domain 3: Cloud Technology and Services*

> A. AWS CloudFormation

AWS CloudFormation is the infrastructure as code service. Templates describe resources declaratively and are deployed as stacks, so environments can be recreated consistently and repeatably.

**Why the other options are wrong:** CodeDeploy deploys application code, Session Manager provides shell access to instances, and Config assesses resource configurations.

### 56. Amazon CloudWatch

**Correct answer: B** — *Domain 3: Cloud Technology and Services*

> B. Amazon CloudWatch alarms

Amazon CloudWatch collects metrics and logs, and CloudWatch alarms trigger actions or notifications when a metric crosses a defined threshold for a specified period.

**Why the other options are wrong:** CloudTrail logs API calls, Trusted Advisor gives best-practice recommendations, and X-Ray traces requests through distributed applications.

### 57. AWS machine learning services

**Correct answer: B** — *Domain 3: Cloud Technology and Services*

> B. Amazon Rekognition

Amazon Rekognition is a pretrained computer vision service that analyzes images and video to detect objects, scenes, faces and text with a simple API call.

**Why the other options are wrong:** SageMaker AI is for building and training custom models, Comprehend performs natural language processing on text, and Textract extracts data specifically from scanned documents and forms.

### 58. Amazon EC2 Spot Instances

**Correct answer: C** — *Domain 4: Billing, Pricing, and Support*

> C. Spot Instances

Spot Instances use spare EC2 capacity at discounts of up to 90 percent compared to On-Demand pricing, and are ideal for fault-tolerant, flexible or stateless workloads that tolerate interruption.

**Why the other options are wrong:** On-Demand has no commitment but no discount, Reserved Instances require a one or three year commitment, and Dedicated Hosts are the most expensive option and are used for licensing or compliance.

### 59. Savings Plans and Reserved Instances

**Correct answer: C** — *Domain 4: Billing, Pricing, and Support*

> C. A three-year Compute Savings Plan with all upfront payment

Savings Plans and Reserved Instances offer up to about 72 percent savings over On-Demand in exchange for a one or three year commitment to a consistent amount of usage, with the largest discount for a three-year all-upfront term.

**Why the other options are wrong:** On-Demand offers no discount, Spot is unsuitable for a workload that cannot be interrupted, and Dedicated Hosts are the most expensive option.

### 60. AWS Free Tier

**Correct answer: B** — *Domain 4: Billing, Pricing, and Support*

> B. It includes three types of offer: always free, 12 months free, and short-term trials

The AWS Free Tier consists of always-free offers such as the AWS Lambda monthly request allowance, 12-months-free offers that start when the account is created, and short-term free trials for specific services.

**Why the other options are wrong:** Not every service is included, and the Free Tier is available to all new accounts regardless of support plan.

### 61. AWS Budgets

**Correct answer: A** — *Domain 4: Billing, Pricing, and Support*

> A. AWS Budgets

AWS Budgets lets you set custom cost, usage, reservation and Savings Plans budgets and sends alerts when actual or forecast spend exceeds a defined threshold.

**Why the other options are wrong:** Cost Explorer visualizes historical spend, the Pricing Calculator estimates costs before deployment, and the Cost and Usage Report is a detailed billing data export.

### 62. AWS Cost Explorer

**Correct answer: B** — *Domain 4: Billing, Pricing, and Support*

> B. AWS Cost Explorer

AWS Cost Explorer provides an interactive interface for visualizing, understanding and forecasting AWS costs and usage over time, with filtering and grouping by dimensions such as service, account and tag.

**Why the other options are wrong:** Budgets creates thresholds and alerts, Trusted Advisor gives best-practice checks, and Compute Optimizer recommends resource right-sizing.

### 63. Consolidated billing and AWS Organizations

**Correct answer: A, B** — *Domain 4: Billing, Pricing, and Support*

> A. A single bill covering all member accounts

> B. Combined usage across accounts that can qualify for volume pricing tiers

Consolidated billing produces one bill for the organization and aggregates usage across all accounts, so the organization can reach volume discount tiers and share Reserved Instance and Savings Plans benefits.

**Why the other options are wrong:** Data transfer charges still apply, there is no free usage allowance, and support plans are purchased separately.

### 64. AWS Support plans

**Correct answer: D** — *Domain 4: Billing, Pricing, and Support*

> D. Enterprise Support

Enterprise Support includes a designated Technical Account Manager and a response time target of 15 minutes for business-critical system down cases, along with concierge support and access to all Trusted Advisor checks.

**Why the other options are wrong:** Basic offers no technical case support, Developer offers business-hours guidance only, and Business provides 24/7 support with a one-hour target for production system down cases but no designated TAM.

### 65. AWS Pricing Calculator

**Correct answer: A** — *Domain 4: Billing, Pricing, and Support*

> A. AWS Pricing Calculator

The AWS Pricing Calculator produces cost estimates for planned architectures before any resources are deployed, and the estimates can be saved and shared.

**Why the other options are wrong:** Cost Explorer and Cost Anomaly Detection analyze spending that has already occurred, and Billing Conductor produces customized billing views for end customers.

---

## Scoring this exam

Mark each question right or wrong, then score by domain to find where to study:

| Domain | Questions | Your score | % correct |
| --- | --- | --- | --- |
| 1. Cloud Concepts | 16 | ____ | ____ |
| 2. Security and Compliance | 19 | ____ | ____ |
| 3. Cloud Technology and Services | 22 | ____ | ____ |
| 4. Billing, Pricing, and Support | 8 | ____ | ____ |
| **Total** | **65** | ____ | ____ |

The real exam is scaled to 100-1000 with a pass at 700, which works out to
roughly 70% of the scored questions. Treat anything under 80% on this practice
exam as a signal to review that domain before booking the real thing.

