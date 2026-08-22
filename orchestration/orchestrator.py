from AGENTS import classification_agent, documentation_agent, trade_review_agent, trade_risk_agent, transaction_intake_agent
from safety.policy import authorize


def run(context: dict) -> dict:
    """Run trade specialists and apply fail-closed trade-compliance governance."""
    results = []
    for agent in [transaction_intake_agent, classification_agent, documentation_agent, trade_risk_agent, trade_review_agent]:
        results.append(agent.run(context))

    governance = authorize("trade_support_release", context)
    return {
        "system": "F107",
        "results": results,
        "governance": governance,
        "release_allowed": governance["allowed"],
        "human_trade_review_required": True,
        "autonomous_filing_authority": False,
        "autonomous_sanctions_authority": False,
        "autonomous_customs_authority": False,
    }
