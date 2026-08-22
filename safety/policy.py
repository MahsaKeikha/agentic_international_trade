"""Fail-closed trade-compliance governance for F107 International Trade."""

PROTECTED_ACTIONS = {
    "trade_filing",
    "sanctions_determination",
    "customs_submission",
    "license_determination",
    "binding_classification",
    "external_submission",
}

REQUIRED_REVIEWS = (
    "transaction_scope_reviewed",
    "classification_reviewed",
    "origin_valuation_reviewed",
    "restricted_party_screening_reviewed",
    "sanctions_export_reviewed",
    "documentation_reviewed",
    "evidence_provenance_reviewed",
    "qualified_trade_approval",
)


def authorize(action: str, context: dict | None = None) -> dict:
    context = context or {}
    if action in PROTECTED_ACTIONS:
        return {"allowed": False, "reason": "binding trade authority is outside reference-system scope"}

    missing = [key for key in REQUIRED_REVIEWS if not context.get(key)]
    if missing:
        return {"allowed": False, "reason": "missing required international-trade review", "missing": missing}

    blockers = []
    if context.get("classification_uncertain"):
        blockers.append("tariff or trade classification remains uncertain")
    if context.get("origin_uncertain"):
        blockers.append("country-of-origin determination remains uncertain")
    if context.get("valuation_gap"):
        blockers.append("customs valuation analysis is incomplete")
    if context.get("restricted_party_hit_unresolved"):
        blockers.append("restricted-party screening hit is unresolved")
    if context.get("sanctions_risk_unresolved"):
        blockers.append("sanctions or embargo risk is unresolved")
    if context.get("license_requirement_uncertain"):
        blockers.append("license requirement or exception remains uncertain")
    if context.get("documentation_provenance_missing"):
        blockers.append("trade documentation or source provenance is incomplete")
    if context.get("unsupported_trade_conclusion"):
        blockers.append("trade-compliance conclusion exceeds reviewed evidence or authority")

    if blockers:
        return {"allowed": False, "reason": "international-trade governance blocker", "blockers": blockers}

    return {"allowed": True, "reason": "trade-support package approved after qualified human review"}


def review_required(action: str) -> bool:
    return action in PROTECTED_ACTIONS


def enforce(action: str, approved: bool) -> None:
    if review_required(action) and not approved:
        raise PermissionError("Qualified human approval is required for this action.")
