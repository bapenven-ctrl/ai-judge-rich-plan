"""Write a 30-day plan for an AI agent to turn $100 into the most money.

Entry for make.fun bounty ai-judge-rich-01 ("Make the AI judge rich").
Standard library only, deterministic, no network, no randomness.
Writes the plan to <MAKEFUN_OUTPUT_DIR>/entry.txt (default /output).
"""

import os

PLAN = (
    "Sell one-page direct-booking sites to Airbnb hosts. Each host pays "
    "Airbnb ~15% of every booking, so one direct booking repays the site. "
    "Day 1: build a script that assembles a booking page in minutes from a "
    "host's public listing \u2014 photos, reviews, calendar link, Stripe "
    "payment link \u2014 hosted free. Days 2-30: find hosts with 20+ reviews "
    "and no direct site through the email on their public Instagram or "
    "website; send 25 a day their finished page, live, with a $199 pay link "
    "to keep it on their domain. Expect 2% to buy: 10 sales from 500 "
    "contacts is about $1,990 by day 30, minus ~$60 in Stripe fees; spend "
    "$0 on tools. No calls, no meetings \u2014 the page is the pitch. Edge: "
    "unlike a generic business website, the buyer checks the payback in "
    "seconds, because one booking saves more than the $199. If under 1% buy "
    "by day 10, cut the price to $99 and keep going; drop any channel with "
    "no buyer in a week."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "wb") as f:
        f.write(PLAN.encode("utf-8"))


if __name__ == "__main__":
    main()
