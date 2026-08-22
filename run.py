from orchestration.orchestrator import run

REFERENCE_CONTEXT = {
    "transaction_scope_reviewed": True,
    "classification_reviewed": True,
    "origin_valuation_reviewed": True,
    "restricted_party_screening_reviewed": True,
    "sanctions_export_reviewed": True,
    "documentation_reviewed": True,
    "evidence_provenance_reviewed": True,
    "qualified_trade_approval": True,
}

if __name__ == "__main__":
    print(run(REFERENCE_CONTEXT))
