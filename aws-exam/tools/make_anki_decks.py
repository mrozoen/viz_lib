#!/usr/bin/env python3
"""Generate Anki decks (.apkg) from the CLF-C02 review packet.

Four separate decks, matching sections of review-packet.html:

  1. Cost Tools                    - Part One, section 4
  2. Hybrid Connectivity           - Part One, section 5
  3. Global Infrastructure & Edge  - Part One, section 6
  4. Signal Words                  - Part Two, built from the packet's own table

The signal deck is extracted from the HTML so it cannot drift from the packet.
The three concept decks are written here, drawn from the same sections.

Usage:
    python3 make_anki_decks.py [-o OUTPUT_DIR] [--packet path/to/review-packet.html]
"""

import argparse
import re
from pathlib import Path

import genanki

# Stable IDs: regenerating the decks updates the existing ones in Anki rather
# than creating duplicates. Do not change these once the decks have been imported.
MODEL_ID = 1607392319
DECK_IDS = {
    "cost": 2059400110,
    "hybrid": 2059400111,
    "global": 2059400112,
    "signals": 2059400113,
}

MODEL = genanki.Model(
    MODEL_ID,
    "CLF-C02 Basic",
    fields=[{"name": "Front"}, {"name": "Back"}, {"name": "Note"}],
    templates=[{
        "name": "Recall",
        "qfmt": '<div class="front">{{Front}}</div>',
        "afmt": '<div class="front">{{Front}}</div><hr id="answer">'
                '<div class="back">{{Back}}</div>'
                '{{#Note}}<div class="note">{{Note}}</div>{{/Note}}',
    }],
    css="""
.card {
  font-family: -apple-system, "Segoe UI", Roboto, sans-serif;
  font-size: 20px;
  text-align: left;
  color: #182430;
  background: #ffffff;
  padding: 18px 20px;
  line-height: 1.5;
}
.front { font-size: 21px; }
.back { font-size: 22px; font-weight: 600; color: #b85c0c; margin-top: 4px; }
.note { font-size: 16px; color: #445260; margin-top: 14px; line-height: 1.5; }
hr#answer { border: 0; border-top: 1px solid #dce2e8; margin: 16px 0; }
.nightMode .card { color: #e6edf3; background: #18202a; }
.nightMode .back { color: #e08b3e; }
.nightMode .note { color: #a9b7c4; }
.nightMode hr#answer { border-top-color: #2b3742; }
""",
)

# --- Part One, section 4: the three cost tools -------------------------------

COST = [
    ("A company is still entirely on-premises and wants to know whether moving to AWS would cost less. Which tool?",
     "TCO Calculator",
     "Comparing on-premises against AWS is the TCO Calculator specifically. Either way it is not Cost Explorer - there is no AWS spend yet."),
    ("A customer without an AWS account wants to estimate what a proposed architecture will cost. Which tool?",
     "AWS Pricing Calculator",
     "Estimating AWS costs = Pricing Calculator (it replaced the Simple Monthly Calculator). Comparing with on-premises = TCO Calculator."),
    ("Pricing Calculator vs TCO Calculator",
     "Pricing Calculator estimates AWS costs. TCO Calculator compares AWS against on-premises.",
     "Both are used before you are on AWS. The tell is whether on-premises is being compared."),
    ("Visualise the last 12 months of AWS spend, broken down by service, with a forecast of next month. Which tool?",
     "AWS Cost Explorer", ""),
    ("Email the team as soon as forecast spending will exceed $5,000 this month. Which tool?",
     "AWS Budgets", ""),
    ("When is the Pricing / TCO Calculator the answer?",
     "Before you are on AWS",
     "Estimating a proposed architecture, or comparing costs against on-premises."),
    ("When is Cost Explorer the answer?",
     "You are already on AWS",
     "Visualise, break down and forecast spend that has actually happened."),
    ("When is AWS Budgets the answer?",
     "You want a threshold and an alert",
     "Set a cost, usage, reservation or Savings Plans budget and be notified when actual or forecast spend crosses it."),
    ("Signal words: 'migrating' · 'estimate' · 'compare to on-premises'",
     "AWS Pricing / TCO Calculator", ""),
    ("Signal words: 'over time' · 'visualize' · 'trends' · 'forecast'",
     "AWS Cost Explorer", ""),
    ("Signal words: 'alert' · 'notify' · 'exceeds' · 'threshold'",
     "AWS Budgets", ""),
    ("The one question that separates all three cost tools",
     "Are they on AWS yet?",
     "If the company is still on-premises and considering a move, it cannot be Cost Explorer."),
    ("'A user wants guidance on possible savings when migrating from on-premises to AWS.' Which tool?",
     "AWS TCO Calculator",
     "You answered Cost Explorer twice on this. Migrating = not on AWS yet."),
    ("'Visualize, understand and manage AWS costs and usage over time.' Which tool?",
     "AWS Cost Explorer",
     "You answered Budgets on this one. Budgets alerts; Cost Explorer shows."),
    ("What does the AWS Pricing Calculator (formerly Simple Monthly Calculator) do?",
     "Estimates monthly billing based on projected usage",
     "Produces a cost estimate for an architecture before anything is deployed."),
    ("One bill across many AWS accounts, volume discounts, central governance",
     "AWS Organizations (consolidated billing)",
     "Create a new management account, then invite the existing accounts to join."),
]

# --- Part One, section 5: hybrid connectivity --------------------------------

HYBRID = [
    ("Dedicated, private connection with consistent performance that does NOT use the public internet",
     "AWS Direct Connect", ""),
    ("Encrypted tunnel to AWS over the public internet",
     "AWS VPN", ""),
    ("Extends on-premises storage into AWS",
     "AWS Storage Gateway", ""),
    ("The isolated network in AWS where hybrid connections terminate; provides subnets and network ACLs",
     "Amazon VPC", ""),
    ("'Securely connect to AWS resources over the public internet.' Which service?",
     "AWS VPN — never Direct Connect",
     "Not using the public internet is Direct Connect's defining property. You picked DX here."),
    ("Which TWO services extend an on-premises architecture into the AWS Cloud?",
     "AWS Direct Connect + AWS Storage Gateway",
     "This question repeats three times in the practice corpus. You got half marks on it twice."),
    ("A small company wants an encrypted link from its office to its VPC, set up this week, using its existing internet connection",
     "AWS VPN",
     "Direct Connect is a physical circuit and takes weeks to provision."),
    ("Does AWS Direct Connect traverse the public internet?",
     "No",
     "That is exactly what distinguishes it from AWS VPN."),
    ("Direct Connect vs VPN, in one line each",
     "DX = dedicated private line, consistent performance, slow to provision. VPN = encrypted over the internet, quick and cheap.",
     ""),
    ("Which service provides inbound and outbound network ACLs to control traffic to EC2 instances?",
     "Amazon VPC",
     "Network ACLs are a VPC feature. You answered API Gateway on this."),
    ("Recurring wrong answers in 'extend on-premises' questions",
     "Route 53, CloudFront, Amazon EBS, Amazon Connect",
     "All four appear as decoys in this question family. None of them is a hybrid connectivity service."),
    ("What do VPC peering and AWS Transit Gateway connect?",
     "AWS networks to each other — not on-premises to AWS",
     ""),
]

# --- Part One, section 6: global infrastructure and the edge -----------------

GLOBAL = [
    ("What are the components of the AWS global infrastructure?",
     "Regions, Availability Zones and edge locations",
     "Nothing else. Resource groups, security groups and AMIs are account-level features and common decoys."),
    ("What is an Availability Zone?",
     "One or more discrete data centers with redundant power, networking and connectivity, within a Region",
     ""),
    ("High availability always means…",
     "Multiple Availability Zones",
     "Not multiple Regions, not a VPC, not global reach."),
    ("High availability vs fault tolerance",
     "HA = minimal downtime, it recovers. FT = no loss of function at all, redundancy already running.",
     "The words 'minimal' and 'no' in the stem are doing the work."),
    ("Which services run at AWS edge locations?",
     "CloudFront, Route 53, AWS Shield, AWS WAF, Global Accelerator",
     ""),
    ("Do Amazon EC2 and Amazon RDS run at edge locations?",
     "No — they run in Availability Zones",
     "You picked EC2 as an edge service on a Choose TWO."),
    ("Which AWS services are global rather than regional?",
     "IAM, Route 53, CloudFront, AWS Organizations",
     ""),
    ("Is Amazon S3 global or regional?",
     "Regional",
     "Buckets live in a Region; the console just lists them all together. You picked S3 as global."),
    ("Availability Zones in a Region are joined by low-latency links. What does that enable?",
     "Synchronous replication of data",
     "It does not give you anything 'global' — AZs are all inside one Region."),
    ("Cache static content closer to distant users",
     "Amazon CloudFront",
     "ElastiCache is in-memory caching for a database. The word 'cache' is the trap."),
    ("Monitor endpoint health and route traffic to healthy regional endpoints, using static anycast IPs",
     "AWS Global Accelerator", ""),
    ("Multiple Regions or multiple Availability Zones — which is the standard high availability answer?",
     "Multiple Availability Zones within one Region",
     "Multiple Regions is for disaster recovery or global latency, not routine HA."),
    ("Can Elastic Load Balancing distribute traffic across AWS Regions?",
     "No — ELB is a regional service",
     "Cross-Region traffic distribution is Route 53 or Global Accelerator. You picked this false option twice."),
    ("A company deploys web servers in multiple AWS Regions. What is being increased?",
     "Availability", ""),
]


def build_notes(rows, tag):
    return [genanki.Note(model=MODEL, fields=[f, b, n], tags=[tag]) for f, b, n in rows]


def signal_rows(packet_path):
    """Pull Part Two's signal table out of the packet so the deck cannot drift."""
    html = Path(packet_path).read_text()
    part2 = html.split("Signals that give the answer away")[1].split('<span class="n">Part Three</span>')[0]
    strip = lambda s: re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", s)) \
        .replace("&middot;", "·").replace("&mdash;", "—").strip()

    rows, group = [], None
    pattern = (r'<tr class="group-head"><td colspan="2">(.*?)</td>'
               r'|<tr><td class="sig">(.*?)</td><td class="ans">(.*?)</td></tr>')
    for m in re.finditer(pattern, part2, re.S):
        if m.group(1):
            group = strip(m.group(1))
        else:
            rows.append((f"When the stem says:<br><br>{strip(m.group(2))}",
                         strip(m.group(3)), group))
    if not rows:
        raise SystemExit("no signal rows found - has the packet's markup changed?")
    return rows


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    here = Path(__file__).parent
    ap.add_argument("--packet", default=here.parent / "review-packet.html")
    ap.add_argument("-o", "--out", default=".")
    args = ap.parse_args()

    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)

    decks = [
        ("cost", "AWS CLF-C02::1 Cost Tools", COST, "cost-tools"),
        ("hybrid", "AWS CLF-C02::2 Hybrid Connectivity", HYBRID, "hybrid-connectivity"),
        ("global", "AWS CLF-C02::3 Global Infrastructure", GLOBAL, "global-infrastructure"),
        ("signals", "AWS CLF-C02::4 Signal Words", signal_rows(args.packet), "signal-words"),
    ]

    for key, name, rows, tag in decks:
        deck = genanki.Deck(DECK_IDS[key], name)
        for note in build_notes(rows, tag):
            deck.add_note(note)
        filename = out / (name.split("::")[-1].replace(" ", "-") + ".apkg")
        genanki.Package(deck).write_to_file(filename)
        print(f"{len(rows):>3} cards  ->  {filename}")


if __name__ == "__main__":
    main()
