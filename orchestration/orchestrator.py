from AGENTS import transaction_intake_agent,classification_agent,documentation_agent,trade_risk_agent,trade_review_agent

def run(context): return [a.run(context) for a in [transaction_intake_agent,classification_agent,documentation_agent,trade_risk_agent,trade_review_agent]]
