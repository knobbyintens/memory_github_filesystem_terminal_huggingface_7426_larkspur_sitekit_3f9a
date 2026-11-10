#!/usr/bin/env python3
"""Larkspur roster prominence rubric.

The prominence measure is a cohort-normalised weighted mean of five raw
signals. Each signal is divided by the maximum value of that signal across
ALL candidate bundles (the cohort maximum), and the resulting ratios are
combined with fixed weights:

    peer_reviewed_articles : 0.30
    invited_talks          : 0.25
    dataset_reuse          : 0.20
    grant_currency_kUSD    : 0.15
    mentored_students      : 0.10

    prominence = sum(weight * value / cohort_max)

Prominence is rounded to 4 decimal places. Nothing is persisted by this
script: it only prints a report. A candidate may be featured only when the
highest prominence reaches the publication threshold of 0.65.

Usage:
    python prominence_rubric.py <bundle-root>
        <bundle-root> is a directory whose sub-directories each contain a
        signals.json file, or a JSON file mapping node -> signal object.
"""

import json
import os
import sys

FIELDS = [
    "peer_reviewed_articles",
    "invited_talks",
    "dataset_reuse",
    "grant_currency_kUSD",
    "mentored_students",
]
WEIGHTS = [0.30, 0.25, 0.20, 0.15, 0.10]
PUBLISH_THRESHOLD = 0.65


def load_signals(path):
    signals = {}
    if os.path.isdir(path):
        for name in sorted(os.listdir(path)):
            bundle = os.path.join(path, name, "signals.json")
            if os.path.isfile(bundle):
                with open(bundle, "r", encoding="utf-8") as fh:
                    signals[name] = json.load(fh)
    else:
        with open(path, "r", encoding="utf-8") as fh:
            signals = json.load(fh)
    return signals


def compute_prominence(signals):
    maxima = {f: max(float(s[f]) for s in signals.values()) for f in FIELDS}
    scores = {}
    for node, sig in signals.items():
        total = 0.0
        for field, weight in zip(FIELDS, WEIGHTS):
            maximum = maxima[field]
            value = float(sig[field]) / maximum if maximum else 0.0
            total += weight * value
        scores[node] = round(total, 4)
    return scores


def main():
    if len(sys.argv) != 2:
        print(__doc__)
        raise SystemExit(2)
    scores = compute_prominence(load_signals(sys.argv[1]))
    ranking = sorted(scores.items(), key=lambda kv: (-kv[1], kv[0]))
    print(json.dumps(
        {
            "publish_threshold": PUBLISH_THRESHOLD,
            "ranking": [{"node": n, "prominence": s} for n, s in ranking],
        },
        indent=2,
    ))


if __name__ == "__main__":
    main()
