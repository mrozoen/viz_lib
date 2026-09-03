#!/usr/bin/env python3
"""Parse the kananinirav/aws-certified-cloud-practitioner-notes practice exams
into a normalized question bank this repo's tooling can grade against.

That repository (MIT licensed) publishes 20+ CLF-C02 practice exams as Markdown,
each question followed by a collapsed <details> block holding the answer key.
This script extracts questions, options and answers, and tags each question with
a domain and topic so a wrong-answer analysis can be grouped by exam domain.

Usage:
    python3 parse_practice_exams.py /path/to/repo/practice-exam [-o parsed.json]

The parsed output is written outside the repo by default: it is someone else's
content, and this project stores the tool rather than a copy of the corpus.
"""

import argparse
import json
import re
from collections import Counter
from pathlib import Path

# A question starts at column 0 with "12. " and runs to the next such line.
QUESTION_RE = re.compile(r"^(\d+)\.\s+(.*)$")
OPTION_RE = re.compile(r"^\s*[-*]\s*([A-Z])[.)]\s+(.*)$")
ANSWER_RE = re.compile(r"correct answer\s*:?\s*([A-Z](?:\s*,\s*[A-Z])*)", re.I)

# Topic classification. Order matters: the first matching rule wins, so the more
# specific patterns are listed before the general ones. Domain ids match the
# CLF-C02 exam guide used elsewhere in this repo.
RULES = [
    # --- Domain 1: unambiguous concept markers, checked before service names ---
    (1, "Well-Architected Framework", r"well-architected|operational excellence|performance efficiency|\bpillar\b|sustainability pillar"),
    (1, "Cloud Adoption Framework", r"cloud adoption framework|\bCAF\b|business perspective|people perspective|governance perspective|platform perspective"),
    (1, "Migration strategies", r"lift and shift|rehost|replatform|refactor|repurchas|\bretire\b|\brelocate\b|migration strategy"),
    (1, "Cloud economics", r"capital expense|operational expense|\bcapex\b|\bopex\b|economies of scale|pay-as-you-go|pay as you go|variable expense|trading fixed expense"),
    (1, "Deployment and service models", r"\bIaaS\b|\bPaaS\b|\bSaaS\b|deployment model|cloud computing model|\bhybrid (cloud|deployment)"),
    (1, "Benefits of the cloud", r"benefits? of (the )?(aws )?cloud|advantages? of (the )?(aws )?cloud|cloud computing (benefit|advantage)|why .* cloud"),
    (1, "Elasticity and scalability", r"\belasticity\b|horizontal scal|vertical scal|scale out|scale up|\bagility\b|stop guessing capacity"),

    # --- Domain 4: Billing, Pricing and Support ---
    (4, "Support plans", r"\bsupport plan|technical account manager|\bTAM\b|business support|enterprise support|developer support|basic support|concierge"),
    (4, "Pricing models", r"reserved instance|savings plan|spot instance|on-demand|dedicated host|\bRI\b\b"),
    (4, "Cost management tools", r"cost explorer|aws budgets|cost and usage report|pricing calculator|\bTCO\b|total cost of ownership|cost allocation tag|billing dashboard|cost anomaly"),
    (4, "Consolidated billing", r"consolidated billing|volume discount|master account|management account|payer account"),
    (4, "Free tier", r"free tier"),
    (4, "Marketplace", r"aws marketplace"),

    # --- Domain 2: Security and Compliance ---
    (2, "Shared responsibility model", r"shared responsibility|responsibility of aws|customer'?s responsibility|responsible for patching|security of the cloud|security in the cloud"),
    (2, "Threat detection", r"guardduty|amazon inspector|amazon macie|amazon detective|security hub"),
    (2, "DDoS and web protection", r"\bshield\b|\bWAF\b|web application firewall|ddos"),
    (2, "Encryption and keys", r"\bKMS\b|key management service|cloudhsm|secrets manager|encryption|encrypt|certificate manager|\bACM\b"),
    (2, "Identity and access management", r"\bIAM\b|identity center|single sign-on|\bSSO\b|root user|\bMFA\b|multi-factor|least privilege|access key|iam role|iam policy|service control polic|\bSCP\b|cognito"),
    (2, "Auditing and governance", r"cloudtrail|aws config|audit manager|aws artifact|compliance report|\bSOC\b|\bPCI\b|\bHIPAA\b|\bGDPR\b|ISO 27001|penetration test"),
    (2, "Network security", r"security group|network acl|\bNACL\b|firewall manager|network firewall"),
    (2, "Security services (general)", r"\bsecurity\b|\bcompliance\b|\bencrypt"),

    # --- Domain 3: Cloud Technology and Services ---
    (3, "Global infrastructure", r"availability zone|\bregion\b|edge location|local zone|outposts|wavelength|point of presence"),
    (3, "Compute", r"\bEC2\b|lambda|elastic beanstalk|\bECS\b|\bEKS\b|fargate|lightsail|auto scaling|batch|outpost"),
    (3, "Storage", r"\bS3\b|\bEBS\b|\bEFS\b|\bFSx\b|glacier|storage gateway|snowball|snowcone|snowmobile|instance store|\bbackup\b"),
    (3, "Databases", r"\bRDS\b|aurora|dynamodb|redshift|elasticache|documentdb|neptune|\bQLDB\b|timestream|memorydb|database migration"),
    (3, "Networking and content delivery", r"\bVPC\b|cloudfront|route 53|direct connect|\bVPN\b|transit gateway|load balanc|\bELB\b|\bALB\b|\bNLB\b|global accelerator|subnet|internet gateway|\bNAT\b"),
    (3, "Monitoring and management", r"cloudwatch|cloudformation|systems manager|trusted advisor|opsworks|service catalog|control tower|organizations|\bSDK\b|\bCLI\b|management console|infrastructure as code"),
    (3, "Application integration", r"\bSQS\b|\bSNS\b|eventbridge|step functions|\bMQ\b|appsync|api gateway"),
    (3, "Analytics and machine learning", r"athena|\bglue\b|kinesis|quicksight|\bEMR\b|sagemaker|rekognition|comprehend|polly|lex|translate|textract|forecast|data pipeline|lake formation"),
    (3, "Developer tools", r"codecommit|codebuild|codedeploy|codepipeline|cloud9|x-ray|codestar|\bCI/CD\b"),

    # --- Domain 1: Cloud Concepts ---
    (1, "Well-Architected Framework", r"well-architected|operational excellence|performance efficiency|cost optimization pillar|sustainability|\bpillar\b"),
    (1, "Cloud Adoption Framework", r"cloud adoption framework|\bCAF\b|perspective"),
    (1, "Migration strategies", r"lift and shift|rehost|replatform|refactor|repurchas|retire|retain|relocate|migration strategy|\b7 Rs\b|\b6 Rs\b"),
    (1, "Cloud economics", r"capital expense|operational expense|\bcapex\b|\bopex\b|economies of scale|pay-as-you-go|pay as you go|variable expense|upfront"),
    (1, "Elasticity and scalability", r"elasticity|elastic|scalab|scale out|scale up|horizontal scal|vertical scal|agility"),
    (1, "Availability and resilience", r"high availability|fault toleran|disaster recovery|redundan|resilien|single point of failure|\bRTO\b|\bRPO\b"),
    (1, "Deployment and service models", r"\bhybrid\b|on-premises|\bIaaS\b|\bPaaS\b|\bSaaS\b|deployment model|cloud computing model"),
    (1, "Benefits of the cloud", r"benefit|advantage|\bcloud computing\b"),
]


def classify(stem, options_text=""):
    """Return (domain_id, topic) for a question.

    The stem is matched first and alone: distractor options routinely name
    services the question is not about, and letting them vote drags concept
    questions into whichever service a wrong answer happens to mention.
    """
    for text in (stem, f"{stem} {options_text}"):
        if not text.strip():
            continue
        for domain, topic, pattern in RULES:
            if re.search(pattern, text, re.I):
                return domain, topic
    return 0, "Unclassified"


def split_questions(lines):
    """Yield (number, block_of_lines) for each numbered question in a file."""
    current_num, block = None, []
    for line in lines:
        match = QUESTION_RE.match(line)
        if match:
            if current_num is not None:
                yield current_num, block
            current_num, block = int(match.group(1)), [match.group(2)]
        elif current_num is not None:
            block.append(line)
    if current_num is not None:
        yield current_num, block


def parse_file(path):
    lines = path.read_text(encoding="utf-8").splitlines()
    questions, problems = [], []

    for number, block in split_questions(lines):
        body = "\n".join(block)

        options = {}
        stem_parts = []
        for line in block:
            option = OPTION_RE.match(line)
            if option:
                options[option.group(1)] = option.group(2).strip()
            elif not options and not line.strip().startswith("<"):
                stem_parts.append(line.strip())

        answer_match = ANSWER_RE.search(body)
        answers = (
            [a.strip() for a in answer_match.group(1).split(",")]
            if answer_match else []
        )

        stem = " ".join(p for p in stem_parts if p).strip()
        domain, topic = classify(stem, " ".join(options.values()))

        record = {
            "number": number,
            "stem": stem,
            "options": options,
            "answers": answers,
            "type": "multi" if len(answers) > 1 else "single",
            "domain": domain,
            "topic": topic,
        }

        if not options:
            problems.append(f"Q{number}: no options found")
        elif not answers:
            problems.append(f"Q{number}: no answer key found")
        elif any(a not in options for a in answers):
            problems.append(f"Q{number}: answer {answers} not among options {sorted(options)}")

        questions.append(record)

    # Some files use lazy Markdown numbering, writing every item as "1." and
    # letting the renderer count. Trust document order over the literal number
    # whenever the literal sequence is not already 1..N.
    literal = [q["number"] for q in questions]
    if literal != list(range(1, len(questions) + 1)):
        for position, question in enumerate(questions, 1):
            question["number"] = position
            question["renumbered"] = True

    return questions, problems


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("folder", help="path to the repo's practice-exam folder")
    parser.add_argument("-o", "--out", default="practice_exams_parsed.json")
    args = parser.parse_args()

    folder = Path(args.folder)
    files = sorted(
        folder.glob("practice-exam-*.md"),
        key=lambda p: int(re.search(r"(\d+)", p.stem).group(1)),
    )
    if not files:
        raise SystemExit(f"no practice-exam-*.md files under {folder}")

    exams, report = {}, []
    for path in files:
        number = int(re.search(r"(\d+)", path.stem).group(1))
        questions, problems = parse_file(path)
        usable = [q for q in questions if q["options"] and q["answers"]]
        exams[str(number)] = {
            "exam": number,
            "source": f"practice-exam/{path.name}",
            "question_count": len(questions),
            "usable_count": len(usable),
            "questions": questions,
        }
        report.append((number, len(questions), len(usable), problems))

    out = Path(args.out)
    out.write_text(json.dumps({
        "source_repo": "kananinirav/aws-certified-cloud-practitioner-notes (MIT)",
        "exams": exams,
    }, indent=1))

    print(f"{'exam':>5}  {'questions':>9}  {'gradable':>8}  problems")
    for number, total, usable, problems in report:
        note = "" if not problems else f"{len(problems)} ({problems[0]})"
        print(f"{number:>5}  {total:>9}  {usable:>8}  {note}")

    all_q = [q for e in exams.values() for q in e["questions"] if q["answers"]]
    print(f"\ntotal gradable questions: {len(all_q)}")
    print(f"multi-response: {sum(1 for q in all_q if q['type'] == 'multi')}")
    print(f"unclassified:   {sum(1 for q in all_q if q['domain'] == 0)}")
    by_domain = Counter(q["domain"] for q in all_q)
    for domain in sorted(by_domain):
        share = by_domain[domain] / len(all_q) * 100
        print(f"  domain {domain}: {by_domain[domain]:>4}  ({share:.0f}%)")
    print(f"\nwrote {out}")


if __name__ == "__main__":
    main()
