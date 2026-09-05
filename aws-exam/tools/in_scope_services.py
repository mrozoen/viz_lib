#!/usr/bin/env python3
"""The CLF-C02 in-scope services and features, and how the corpus uses them.

The catalogue below is the appendix of the CLF-C02 exam guide ("In-scope AWS
services and features"), grouped by the exam guide's own category headings.
Each entry carries a regex that matches how the practice corpus writes the
service, so the two can be joined.

Run it to see, for every in-scope service, how often it is the *correct*
answer in the corpus, how often it appears only as a decoy, and the stems it
answers -- which is what the signal tables in the study guide are built from:

    python3 in_scope_services.py                # summary table
    python3 in_scope_services.py --stems S3     # stems a service answers
    python3 in_scope_services.py --json out.json
"""

import argparse
import collections
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from parse_practice_exams import parse_file  # noqa: E402
from practice import default_dir  # noqa: E402

# name -> pattern. A pattern of None means the name itself, matched literally
# and case-insensitively. Patterns are matched against option text.
CATALOGUE = {
    "Analytics": [
        ("Amazon Athena", r"\bAthena\b"),
        ("AWS Data Exchange", r"Data Exchange"),
        ("Amazon EMR", r"\bEMR\b|Elastic MapReduce"),
        ("AWS Glue", r"AWS Glue|\bGlue\b"),
        ("Amazon Kinesis", r"\bKinesis\b"),
        ("Amazon MSK", r"\bMSK\b|Managed Streaming for Apache Kafka"),
        ("Amazon OpenSearch Service", r"OpenSearch|Elasticsearch Service"),
        ("Amazon QuickSight", r"QuickSight"),
        ("Amazon Redshift", r"Redshift"),
    ],
    "Application Integration": [
        ("Amazon EventBridge", r"EventBridge|CloudWatch Events"),
        ("Amazon SNS", r"\bSNS\b|Simple Notification Service"),
        ("Amazon SQS", r"\bSQS\b|Simple Queue Service"),
        ("AWS Step Functions", r"Step Functions"),
    ],
    "Business Applications": [
        ("Amazon Connect", r"Amazon Connect"),
        ("Amazon SES", r"\bSES\b|Simple Email Service"),
    ],
    "Cloud Financial Management": [
        ("AWS Billing Conductor", r"Billing Conductor"),
        ("AWS Budgets", r"AWS Budgets|\bBudgets\b"),
        ("AWS Cost and Usage Report", r"Cost and Usage [Rr]eport"),
        ("AWS Cost Explorer", r"Cost Explorer"),
        ("AWS Marketplace", r"AWS Marketplace|\bMarketplace\b"),
        ("AWS Pricing Calculator", r"Pricing Calculator|Simple Monthly Calculator"),
    ],
    "Compute": [
        ("AWS Batch", r"AWS Batch"),
        ("Amazon EC2", r"\bEC2\b|Elastic Compute Cloud"),
        ("AWS Elastic Beanstalk", r"Elastic Beanstalk"),
        ("Amazon Lightsail", r"Lightsail"),
        ("AWS Local Zones", r"Local Zones"),
        ("AWS Outposts", r"Outposts"),
        ("AWS Wavelength", r"Wavelength"),
    ],
    "Containers": [
        ("Amazon ECS", r"\bECS\b|Elastic Container Service"),
        ("Amazon ECR", r"\bECR\b|Elastic Container Registry"),
        ("Amazon EKS", r"\bEKS\b|Elastic Kubernetes Service"),
    ],
    "Customer Engagement": [
        ("AWS Activate for Startups", r"AWS Activate"),
        ("AWS IQ", r"AWS IQ"),
        ("AWS Managed Services (AMS)", r"AWS Managed Services|\bAMS\b"),
        ("AWS Support", r"AWS Support|Support plan|Concierge"),
    ],
    "Database": [
        ("Amazon Aurora", r"Aurora"),
        ("Amazon DocumentDB", r"DocumentDB"),
        ("Amazon DynamoDB", r"DynamoDB"),
        ("Amazon ElastiCache", r"ElastiCache"),
        ("Amazon MemoryDB for Redis", r"MemoryDB"),
        ("Amazon Neptune", r"Neptune"),
        ("Amazon RDS", r"\bRDS\b|Relational Database Service"),
    ],
    "Developer Tools": [
        ("AWS AppConfig", r"AppConfig"),
        ("AWS CLI", r"\bCLI\b|command line interface"),
        ("AWS Cloud9", r"Cloud9"),
        ("AWS CloudShell", r"CloudShell"),
        ("AWS CodeArtifact", r"CodeArtifact"),
        ("AWS CodeBuild", r"CodeBuild"),
        ("AWS CodeCommit", r"CodeCommit"),
        ("AWS CodeDeploy", r"CodeDeploy"),
        ("AWS CodePipeline", r"CodePipeline"),
        ("AWS CodeStar", r"CodeStar"),
        ("AWS X-Ray", r"X-Ray"),
    ],
    "End-User Computing": [
        ("Amazon AppStream 2.0", r"AppStream"),
        ("Amazon WorkSpaces", r"WorkSpaces"),
    ],
    "Frontend Web and Mobile": [
        ("AWS Amplify", r"Amplify"),
        ("AWS AppSync", r"AppSync"),
        ("Amazon Pinpoint", r"Pinpoint"),
    ],
    "Internet of Things": [
        ("AWS IoT Core", r"IoT Core"),
        ("AWS IoT Greengrass", r"Greengrass"),
    ],
    "Machine Learning": [
        ("Amazon Comprehend", r"Comprehend"),
        ("Amazon Kendra", r"Kendra"),
        ("Amazon Lex", r"\bLex\b"),
        ("Amazon Polly", r"Polly"),
        ("Amazon Rekognition", r"Rekognition"),
        ("Amazon SageMaker", r"SageMaker"),
        ("Amazon Textract", r"Textract"),
        ("Amazon Transcribe", r"Transcribe"),
        ("Amazon Translate", r"Translate"),
    ],
    "Management and Governance": [
        ("AWS Auto Scaling", r"Auto Scaling|Autoscaling"),
        ("AWS CloudFormation", r"CloudFormation"),
        ("AWS CloudTrail", r"CloudTrail"),
        ("Amazon CloudWatch", r"CloudWatch"),
        ("AWS Compute Optimizer", r"Compute Optimizer"),
        ("AWS Config", r"AWS Config\b"),
        ("AWS Control Tower", r"Control Tower"),
        ("AWS Health Dashboard", r"Health Dashboard|Service Health|Personal Health"),
        ("AWS License Manager", r"License Manager"),
        ("Amazon Managed Grafana", r"Grafana"),
        ("Amazon Managed Service for Prometheus", r"Prometheus"),
        ("AWS Management Console", r"Management Console"),
        ("AWS Organizations", r"Organizations|consolidated billing"),
        ("AWS Resource Groups and Tag Editor", r"Resource Group|Tag Editor"),
        ("AWS Service Catalog", r"Service Catalog"),
        ("AWS Systems Manager", r"Systems Manager|\bSSM\b"),
        ("AWS Trusted Advisor", r"Trusted Advisor"),
        ("AWS Well-Architected Tool", r"Well-Architected"),
    ],
    "Migration and Transfer": [
        ("AWS Application Discovery Service", r"Application Discovery"),
        ("AWS Application Migration Service", r"Application Migration Service|\bMGN\b"),
        ("AWS Database Migration Service (DMS)", r"Database Migration Service|\bDMS\b"),
        ("AWS DataSync", r"DataSync"),
        ("AWS Migration Hub", r"Migration Hub"),
        ("AWS Schema Conversion Tool (SCT)", r"Schema Conversion"),
        ("AWS Snow Family", r"Snowball|Snowmobile|Snowcone|Snow Family"),
        ("AWS Transfer Family", r"Transfer Family|AWS Transfer for"),
    ],
    "Networking and Content Delivery": [
        ("Amazon API Gateway", r"API Gateway"),
        ("Amazon CloudFront", r"CloudFront"),
        ("AWS Direct Connect", r"Direct Connect"),
        ("AWS Global Accelerator", r"Global Accelerator"),
        ("Amazon Route 53", r"Route\s*53"),
        ("Amazon VPC", r"\bVPC\b|Virtual Private Cloud"),
        ("AWS VPN", r"AWS VPN|Site-to-Site VPN|Client VPN|\bVPN\b"),
        ("Elastic Load Balancing", r"Elastic Load Balanc|\bELB\b|Load Balancer"),
        ("AWS PrivateLink", r"PrivateLink"),
        ("AWS Transit Gateway", r"Transit Gateway"),
    ],
    "Security, Identity, and Compliance": [
        ("AWS Artifact", r"AWS Artifact|\bArtifact\b"),
        ("AWS Audit Manager", r"Audit Manager"),
        ("AWS Certificate Manager (ACM)", r"Certificate Manager|\bACM\b"),
        ("AWS CloudHSM", r"CloudHSM"),
        ("Amazon Cognito", r"Cognito"),
        ("Amazon Detective", r"Amazon Detective"),
        ("AWS Directory Service", r"Directory Service"),
        ("AWS Firewall Manager", r"Firewall Manager"),
        ("Amazon GuardDuty", r"GuardDuty"),
        ("AWS IAM", r"\bIAM\b|Identity and Access Management"),
        ("AWS IAM Identity Center", r"IAM Identity Center|Single Sign-On|\bSSO\b"),
        ("Amazon Inspector", r"Amazon Inspector|\bInspector\b"),
        ("AWS KMS", r"\bKMS\b|Key Management Service"),
        ("Amazon Macie", r"Macie"),
        ("AWS Network Firewall", r"Network Firewall"),
        ("AWS RAM", r"Resource Access Manager|\bRAM\b"),
        ("AWS Secrets Manager", r"Secrets Manager"),
        ("AWS Security Hub", r"Security Hub"),
        ("AWS Shield", r"AWS Shield|\bShield\b"),
        ("AWS WAF", r"\bWAF\b|Web Application Firewall"),
    ],
    "Serverless": [
        ("AWS Lambda", r"Lambda"),
        ("AWS Fargate", r"Fargate"),
    ],
    "Storage": [
        ("AWS Backup", r"AWS Backup"),
        ("Amazon EBS", r"\bEBS\b|Elastic Block Store"),
        ("AWS Elastic Disaster Recovery", r"Elastic Disaster Recovery|\bDRS\b"),
        ("Amazon EFS", r"\bEFS\b|Elastic File System"),
        ("Amazon FSx", r"\bFSx\b"),
        ("Amazon S3", r"\bS3\b(?!\s*Glacier)|Simple Storage Service"),
        ("Amazon S3 Glacier", r"Glacier"),
        ("AWS Storage Gateway", r"Storage Gateway"),
    ],
}


def load_corpus():
    d = Path(default_dir())
    out = []
    for f in sorted(d.glob("practice-exam-*.md"),
                    key=lambda p: int(re.search(r"\d+", p.name).group())):
        n = int(re.search(r"\d+", f.name).group())
        qs, _ = parse_file(f)
        for q in qs:
            q["exam"] = n
            out.append(q)
    return out


def squash(text):
    return re.sub(r"\s+", " ", re.sub(r"<br\s*/?>", " ", text)).strip()


def analyse():
    questions = load_corpus()
    stats = {}
    for category, entries in CATALOGUE.items():
        for name, pattern in entries:
            stats[name] = {"category": category, "pattern": pattern,
                           "correct": 0, "decoy": 0, "stems": []}

    for q in questions:
        if not q["options"] or not q["answers"]:
            continue
        right = {l: t for l, t in q["options"].items() if l in q["answers"]}
        wrong = {l: t for l, t in q["options"].items() if l not in q["answers"]}
        for name, s in stats.items():
            rx = re.compile(s["pattern"], re.I)
            if any(rx.search(t) for t in right.values()):
                s["correct"] += 1
                s["stems"].append((q["exam"], q["number"], squash(q["stem"])))
            elif any(rx.search(t) for t in wrong.values()):
                s["decoy"] += 1
    return stats, len(questions)


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--stems", help="print every stem this service answers")
    ap.add_argument("--json", help="write the full analysis to a JSON file")
    ap.add_argument("--min", type=int, default=0, help="hide services below N correct")
    args = ap.parse_args()

    stats, total = analyse()

    if args.json:
        Path(args.json).write_text(json.dumps(stats, indent=1))
        print(f"{len(stats)} services over {total} questions -> {args.json}")
        return

    if args.stems:
        hits = [k for k in stats if args.stems.lower() in k.lower()]
        for name in hits:
            s = stats[name]
            print(f"\n=== {name}  ({s['correct']} correct, {s['decoy']} decoy)")
            for exam, num, stem in s["stems"]:
                print(f"  [{exam}.{num}] {stem[:150]}")
        if not hits:
            print(f"no in-scope service matching {args.stems!r}")
        return

    by_cat = collections.defaultdict(list)
    for name, s in stats.items():
        by_cat[s["category"]].append((name, s))
    print(f"{sum(len(v) for v in by_cat.values())} in-scope services "
          f"across {total} corpus questions\n")
    for category, items in by_cat.items():
        print(f"-- {category}")
        for name, s in sorted(items, key=lambda kv: -kv[1]["correct"]):
            if s["correct"] < args.min:
                continue
            flag = "  <- never correct" if s["correct"] == 0 and s["decoy"] else ""
            print(f"   {s['correct']:>4} correct  {s['decoy']:>4} decoy   {name}{flag}")
        print()


if __name__ == "__main__":
    main()
