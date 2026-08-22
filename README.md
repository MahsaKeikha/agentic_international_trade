# F107 | Agentic International Trade | L3 Gold Standard | v1.0

A governed multi-agent reference system for international trade workflow support, including transaction intake, tariff and classification research, origin and valuation review, documentation checks, restricted-party and sanctions risk triage, and qualified human trade review.

## Five-agent architecture

- Transaction Intake Agent
- Classification Agent
- Documentation Agent
- Trade Risk Agent
- Trade Review Agent

## Gold-standard trade governance

F107 is fail closed and support only. Release requires reviewed transaction scope, classification, origin and valuation, restricted-party screening, sanctions and export considerations, documentation, evidence provenance, and explicit qualified-human trade approval.

Release is blocked for uncertain classification, unresolved origin or valuation issues, restricted-party hits, sanctions or embargo risk, uncertain licensing requirements or exceptions, missing documentation provenance, or unsupported trade-compliance conclusions.

The reference system cannot autonomously make binding customs or sanctions determinations, make licensing decisions, file trade or customs submissions, assign binding classifications, or submit externally. Final trade and legal judgments remain with qualified professionals and authorized parties.

## Verification gates

CI runs on Python 3.10, 3.11, and 3.12 and requires:

```bash
ruff check . --select E9,F63,F7,F82
python -m pytest -q
python evals/held_out.py
python run.py
```

The behavioral verification layer includes eight direct governance tests and a 10-scenario held-out international-trade governance suite.
