from orchestration.orchestrator import run


def base():
    return {
        "transaction_scope_reviewed": True,
        "classification_reviewed": True,
        "origin_valuation_reviewed": True,
        "restricted_party_screening_reviewed": True,
        "sanctions_export_reviewed": True,
        "documentation_reviewed": True,
        "evidence_provenance_reviewed": True,
        "qualified_trade_approval": True,
    }


SCENARIOS = [
    ({}, False),
    (base(), True),
    ({**base(), "qualified_trade_approval": False}, False),
    ({**base(), "classification_uncertain": True}, False),
    ({**base(), "origin_uncertain": True}, False),
    ({**base(), "valuation_gap": True}, False),
    ({**base(), "restricted_party_hit_unresolved": True}, False),
    ({**base(), "sanctions_risk_unresolved": True}, False),
    ({**base(), "license_requirement_uncertain": True}, False),
    ({**base(), "documentation_provenance_missing": True}, False),
]


def main():
    passed = 0
    for context, expected in SCENARIOS:
        passed += run(context)["release_allowed"] is expected
    print(f"held-out: {passed}/{len(SCENARIOS)} passed")
    raise SystemExit(0 if passed == len(SCENARIOS) else 1)


if __name__ == "__main__":
    main()
