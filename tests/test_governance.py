from orchestration.orchestrator import run
from safety.policy import authorize


def valid_context():
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


def test_complete_review_can_release_trade_support():
    result = run(valid_context())
    assert result["release_allowed"] is True
    assert result["autonomous_customs_authority"] is False


def test_missing_qualified_review_fails_closed():
    context = valid_context()
    context["qualified_trade_approval"] = False
    assert run(context)["release_allowed"] is False


def test_sanctions_determination_is_never_autonomous():
    assert authorize("sanctions_determination", valid_context())["allowed"] is False


def test_classification_uncertainty_blocks_release():
    context = valid_context()
    context["classification_uncertain"] = True
    assert run(context)["release_allowed"] is False


def test_restricted_party_hit_blocks_release():
    context = valid_context()
    context["restricted_party_hit_unresolved"] = True
    assert run(context)["release_allowed"] is False


def test_sanctions_risk_blocks_release():
    context = valid_context()
    context["sanctions_risk_unresolved"] = True
    assert run(context)["release_allowed"] is False


def test_license_uncertainty_blocks_release():
    context = valid_context()
    context["license_requirement_uncertain"] = True
    assert run(context)["release_allowed"] is False


def test_missing_document_provenance_blocks_release():
    context = valid_context()
    context["documentation_provenance_missing"] = True
    assert run(context)["release_allowed"] is False
