# F107 | Agentic International Trade | L3 Gold Standard | v1.0

A governed five-agent reference architecture for international trade workflow support across transaction scoping, tariff and trade classification research, origin and customs valuation review, documentation, restricted-party screening, sanctions and export-control risk triage, evidence provenance, and qualified human trade approval.

F107 is support-only. It organizes trade facts, evidence, risks, and review workflows without exercising binding customs, sanctions, export-control, licensing, classification, filing, or external-submission authority.

## International trade lifecycle

```text
Transaction Intake
      -> Classification Research
      -> Origin and Valuation Review
      -> Restricted-Party / Sanctions / Export Review
      -> Documentation and Evidence Review
      -> Trade Risk Triage
      -> Qualified Human Trade Approval
```

The workflow fails closed when material trade facts, evidence, jurisdictional analysis, or qualified review remain incomplete.

## Five-agent architecture

| Agent | Responsibility | Core question |
|---|---|---|
| Transaction Intake Agent | Structures goods, parties, destinations, transaction purpose, jurisdictions, and known trade facts | What transaction is actually being reviewed? |
| Classification Agent | Supports tariff and trade-classification research and records uncertainty | What classification candidates are supported by the available product facts? |
| Documentation Agent | Reviews trade documents, required fields, consistency, and provenance | Is the documentation package complete, attributable, and internally consistent? |
| Trade Risk Agent | Triages origin, valuation, restricted-party, sanctions, embargo, export, licensing, and other material trade risks | What requires escalation or specialist review? |
| Trade Review Agent | Performs independent readiness review before a support package can be released | Has the package received all required qualified-human review? |

Agents provide structured support. They do not replace customs brokers, trade counsel, export-control professionals, sanctions specialists, authorized corporate officers, government agencies, or other qualified authorities.

## Repository structure

```text
AGENTS/
├── transaction_intake_agent.py
├── classification_agent.py
├── documentation_agent.py
├── trade_risk_agent.py
└── trade_review_agent.py

SKILLS/
├── transaction_scoping.py
├── classification_research.py
├── document_review.py
├── risk_triage.py
└── human_review.py

TOOLS/
├── goods_register.py
├── party_register.py
├── document_checklist.py
├── evidence_tracker.py
└── risk_matrix.py

orchestration/
memory/
observability/
evals/
benchmarks/
examples/
docs/
prompts/
config/
safety/
tests/
.github/workflows/ci.yml
run.py
pyproject.toml
README.md
```

The architecture separates agent reasoning from deterministic registers, checklists, evidence tracking, risk matrices, safety policy, evaluation, and observability.

## Transaction scoping

`SKILLS/transaction_scoping.py` supports structured intake before trade conclusions are considered.

A transaction record can include:

```text
transaction_id
seller
buyer
consignee
end_user
intermediaries
goods
technology_or_software
quantity
value
currency
origin
ship_from
ship_to
ultimate_destination
intended_end_use
known_end_user
incoterm
transport_mode
jurisdictions
dates
supporting_documents
```

Missing facts should remain missing. F107 must not invent product composition, party identity, end use, destination, origin, value, licensing status, or government authorization.

## Goods register

`TOOLS/goods_register.py` provides a deterministic surface for recording goods and relevant product facts.

Useful attributes can include:

- product name and model
- technical description
- materials or composition
- function
- manufacturing process
- dimensions or capacity
- embedded software or encryption
- country of manufacture
- supplier information
- classification candidates
- evidence references

Product descriptions should be sufficiently specific for qualified review. Marketing names alone may be inadequate for classification.

## Party register

`TOOLS/party_register.py` organizes transaction participants.

Party records can include:

```text
legal_name
aliases
address
country
role
ownership_information
known_affiliates
screening_reference
screening_date
screening_result
review_status
```

The register supports screening workflow and traceability. It does not itself establish that a party is legally cleared to transact.

## Tariff and trade classification

`SKILLS/classification_research.py` supports research into candidate classifications using product facts and available authoritative sources.

Classification review can consider:

- product identity
- composition
- principal function
- technical characteristics
- headings and subheadings
- explanatory material
- relevant rulings or guidance
- jurisdiction
- effective date
- competing classifications

The system should preserve competing candidates and uncertainty rather than forcing a single code when the evidence is insufficient.

`classification_uncertain` is an explicit governance blocker.

## Binding classification boundary

`binding_classification` is a protected action.

F107 may organize classification research and evidence, but it cannot autonomously assign a legally binding tariff, customs, export-control, or other trade classification. Binding determinations remain with authorized humans and competent authorities.

## Country of origin

Origin analysis can affect tariffs, marking, trade remedies, preferences, sanctions, procurement, and other requirements.

Review can consider:

- manufacturing location
- transformation steps
- component origins
- applicable origin rule
- preferential versus non-preferential context
- certificates or supplier declarations
- jurisdiction-specific requirements

`origin_uncertain` blocks release when a material origin determination remains unresolved.

The system must not treat ship-from country as country of origin without supporting analysis.

## Customs valuation

Valuation review can consider:

- transaction value
- assists
- royalties or license fees
- commissions
- packing
- related-party considerations
- proceeds
- freight or insurance treatment where relevant
- alternative valuation methods

A `valuation_gap` blocks release when the customs valuation analysis is incomplete.

F107 should distinguish commercial invoice value, accounting value, transfer price, and customs value rather than assuming they are interchangeable.

## Restricted-party screening

Restricted-party screening can involve multiple lists, jurisdictions, ownership rules, aliases, and changing government designations.

The workflow should preserve:

```text
party searched
search terms / aliases
source
source version or date
match result
potential-match rationale
reviewer
resolution
```

A potential match is not automatically a confirmed legal match. Conversely, an unresolved potential match must not be silently cleared.

`restricted_party_hit_unresolved` blocks release.

## Sanctions and embargo risk

Sanctions analysis may depend on parties, ownership, location, goods, services, end use, financial flows, facilitation, and applicable jurisdiction.

`sanctions_risk_unresolved` blocks release.

F107 can surface sanctions risk and route it for review. `sanctions_determination` is a protected action, so the system cannot make a binding sanctions-clearance determination.

## Export-control considerations

Trade review may require analysis of goods, software, technology, technical data, destination, end user, end use, nationality or access context, and jurisdiction-specific export-control rules.

The system can organize candidate classifications, licensing questions, exceptions, exemptions, and evidence. It must not invent an export authorization or assume that a transaction is uncontrolled merely because the product is commercially available.

## End-use and end-user review

Risk review can consider:

- stated end use
- known end user
- military or government involvement
- proliferation-sensitive context
- diversion indicators
- unusual routing
- inconsistent customer explanations
- transaction anomalies

Material uncertainty should be escalated rather than normalized.

## Licensing requirements and exceptions

Licensing can depend on classification, destination, parties, end use, end user, transaction structure, and applicable jurisdiction.

`license_requirement_uncertain` is an explicit blocker.

`license_determination` is protected. F107 can prepare a licensing research package but cannot autonomously determine that a license is or is not required, claim an exception applies, or exercise an authorization.

## Trade documentation

`SKILLS/document_review.py` and `TOOLS/document_checklist.py` support review of trade-document completeness and consistency.

Documents can include, depending on the transaction:

- commercial invoice
- packing list
- transport document
- certificate of origin
- customs documentation
- export documentation
- licenses or authorizations
- product specifications
- supplier declarations
- end-use statements
- screening evidence
- valuation support

Required documents vary by jurisdiction and transaction. The checklist should therefore be treated as a configurable review aid rather than universal legal requirements.

## Documentation provenance

`TOOLS/evidence_tracker.py` supports evidence provenance.

Useful metadata includes:

```text
evidence_id
source
document_type
transaction_id
issuer
date
version
review_state
limitations
```

`documentation_provenance_missing` blocks release when material trade documentation or source provenance is incomplete.

F107 must not fabricate certificates, licenses, rulings, customs records, screening evidence, origin statements, government correspondence, or approvals.

## Documentation consistency

Cross-document review can compare:

- party names and addresses
- product descriptions
- quantities
- values and currencies
- origin
- classification
- dates
- destinations
- end-use statements
- authorization references

Inconsistencies should be surfaced for review rather than automatically reconciled by guessing.

## Evidence discipline

Material trade conclusions should distinguish among:

```text
verified transaction fact
party assertion
supplier declaration
government source
commercial document
system inference
unresolved question
qualified-human determination
```

Evidence quantity does not guarantee evidence sufficiency. Relevance, currency, authority, completeness, and provenance matter.

## Trade risk triage

`SKILLS/risk_triage.py` and `TOOLS/risk_matrix.py` support structured prioritization.

Potential risk dimensions include:

- classification uncertainty
- origin uncertainty
- valuation gaps
- restricted-party matches
- sanctions or embargo exposure
- export-control sensitivity
- licensing uncertainty
- end-use or end-user concerns
- diversion risk
- documentation gaps
- trade-remedy exposure
- unusual routing
- inconsistent facts

Automated risk scores are prioritization aids. They are not binding trade determinations.

## Customs duties, tariffs, and trade remedies

Classification and origin can affect duties, special tariffs, quotas, antidumping or countervailing measures, safeguards, and other trade remedies.

F107 can organize research inputs and identify questions for qualified review. It should not represent a calculated amount as legally final when classification, origin, valuation, effective date, or remedy applicability remains uncertain.

## Preferential trade treatment

Preferential treatment may require specific origin rules, documentation, certification, recordkeeping, and direct-shipment or other conditions.

The system should not infer eligibility solely from the countries involved. Eligibility requires applicable-rule and evidence review.

## Import and export jurisdiction boundaries

A single transaction may implicate multiple jurisdictions and authorities.

The workflow should identify which jurisdictional assumptions support each conclusion. Rules from one country should not be silently generalized to another.

## Effective dates and regulatory change

Tariffs, sanctions, restricted-party lists, license requirements, exceptions, and customs rules can change.

A governed implementation should preserve:

- source date
- effective date
- version
- review date
- transaction date
- known superseding authority

Material rule changes should trigger re-review rather than silently inheriting an earlier conclusion.

## Recordkeeping

Trade programs often require retention of transaction records and supporting evidence.

F107 can support record indexing, provenance, and retention metadata, but organization-specific retention periods should be configured from applicable requirements rather than invented by the system.

## Brokers, freight forwarders, and intermediaries

Third-party service providers may support customs or logistics workflows, but delegation does not eliminate organizational compliance responsibilities.

F107 should preserve which facts came from the importer, exporter, broker, carrier, supplier, customer, or other intermediary.

## Incoterms and commercial terms

Commercial terms can affect responsibilities, costs, risk transfer, and document preparation, but they do not by themselves determine customs valuation, importer/exporter status, sanctions responsibility, or legal compliance.

The system should avoid using Incoterms as a substitute for jurisdiction-specific trade analysis.

## Screening false positives and false negatives

Name screening can produce false positives and can also miss relevant parties when data is incomplete.

The workflow should preserve match rationale, aliases, identifiers, ownership information where available, and qualified resolution. A low similarity score alone should not become autonomous legal clearance.

## Ownership and control considerations

Some sanctions and restricted-party regimes can extend restrictions through ownership or control rules.

F107 can flag ownership questions and preserve supporting information, but material uncertainty should be escalated to qualified professionals.

## Technology and intangible transfers

International trade compliance can involve software, source code, technical data, cloud access, remote support, demonstrations, and other intangible transfers in addition to physical shipments.

The transaction scope should therefore not assume that no physical shipment means no trade-control issue.

## Deemed-export and access boundaries

Where applicable law regulates access to controlled technology by particular persons or locations, F107 can organize relevant facts and questions. It cannot make binding nationality, licensing, or authorization determinations.

## Humanitarian, personal, or other exceptions

Trade regimes can contain exceptions, exemptions, general authorizations, or special rules. Their applicability is fact-specific.

The system must not claim an exception applies without reviewed authority and facts.

## Anti-boycott, anti-corruption, and adjacent compliance

International transactions may intersect with anti-boycott, anti-corruption, AML, tax, procurement, privacy, cybersecurity, and other compliance domains.

F107 should flag adjacent issues for specialist routing rather than pretending that trade review resolves them.

## Unsupported trade conclusions

`unsupported_trade_conclusion` blocks release when a conclusion exceeds reviewed evidence or authority.

Examples include unsupported claims that:

- a party is legally cleared
- sanctions do not apply
- no export license is required
- a classification is binding
- origin is conclusively established
- customs value is final
- a preference is available
- a filing is legally complete

The system should state uncertainty explicitly.

## Required reviews

The reference policy requires all eight conditions:

```text
transaction_scope_reviewed
classification_reviewed
origin_valuation_reviewed
restricted_party_screening_reviewed
sanctions_export_reviewed
documentation_reviewed
evidence_provenance_reviewed
qualified_trade_approval
```

Missing any required review fails closed.

## Fail-closed governance

The implemented safety policy blocks release when any of the following is present:

- tariff or trade classification remains uncertain
- country-of-origin determination remains uncertain
- customs valuation analysis is incomplete
- restricted-party screening hit is unresolved
- sanctions or embargo risk is unresolved
- license requirement or exception remains uncertain
- trade documentation or source provenance is incomplete
- trade-compliance conclusion exceeds reviewed evidence or authority
- any required review is missing
- qualified trade approval is missing

A support package is releasable only after required reviews are satisfied and blockers are cleared by appropriate human review.

## Protected actions

The safety policy permanently protects:

```text
trade_filing
sanctions_determination
customs_submission
license_determination
binding_classification
external_submission
```

These actions remain outside autonomous authority even if every review flag is satisfied.

## Customs submission boundary

`customs_submission` is protected.

F107 can prepare and validate a draft support package but cannot autonomously transmit customs declarations or representations to a customs authority.

## Trade filing boundary

`trade_filing` is protected.

Government filings can create legal representations, certifications, deadlines, and liabilities. Submission must remain with an authorized human or appropriately governed external system.

## External-submission boundary

`external_submission` is protected.

The reference architecture does not autonomously send declarations, applications, certificates, filings, responses, or other representations to governments, customers, brokers, banks, or other outside parties.

## Human authority boundaries

F107 must not autonomously:

- make binding customs determinations
- make binding sanctions determinations
- make licensing decisions
- assign binding classifications
- clear restricted-party matches as a legal conclusion
- certify origin
- approve customs valuation
- exercise a license or exception
- submit customs or trade filings
- sign certifications
- communicate as an authorized government or corporate representative
- provide binding legal advice

Final trade and legal judgments remain with qualified professionals and authorized parties.

## Qualified review and escalation

`SKILLS/human_review.py` supports explicit human review.

Depending on the matter, escalation can include:

- trade compliance
- customs professionals
- licensed customs brokers
- export-control specialists
- sanctions specialists
- legal counsel
- tax or transfer-pricing specialists
- logistics teams
- security or compliance teams
- authorized corporate officers

The appropriate reviewer depends on jurisdiction, transaction, issue, and organizational governance.

## Privacy and confidentiality

Trade records can contain customer data, supplier information, pricing, technical specifications, controlled technical information, government identifiers, contracts, and commercially sensitive material.

Implementations should apply data minimization, role-based access, secure storage, retention controls, and appropriate confidentiality safeguards.

## Separation of facts and conclusions

A governed trade package should clearly separate:

```text
transaction facts
source documents
screening results
classification candidates
risk flags
system analysis
open questions
qualified-human conclusions
binding government determinations
```

This separation reduces the risk that a preliminary machine-generated analysis is mistaken for legal clearance.

## Versioning and change impact

Trade records should preserve relevant versions of:

- product specifications
- classifications
- origin evidence
- valuation evidence
- party data
- screening sources
- sanctions lists
- licenses or authorizations
- transaction documents
- reviewer decisions

Material changes should trigger appropriate re-review.

Examples include a changed destination, end user, product specification, supplier, origin, value, party ownership, sanctions status, or regulation.

## Observability

The `observability/` layer supports traceability across the workflow.

Useful telemetry includes:

- transaction scope status
- classification review state
- origin and valuation status
- screening results
- sanctions/export review state
- documentation completeness
- provenance gaps
- risk flags
- unresolved blockers
- qualified approval state
- protected-action attempts

Observability supports accountability but does not create compliance authority.

## Memory and state

The `memory/` layer can preserve structured workflow state across agent stages.

State should distinguish verified facts, party-provided facts, documents, automated inferences, screening results, reviewer conclusions, and unresolved questions.

Sensitive trade information should not be retained beyond operational, contractual, legal, or regulatory need.

## Explicit failure states

Useful explicit states include:

```text
TRANSACTION SCOPE INCOMPLETE
CLASSIFICATION UNCERTAIN
ORIGIN UNCERTAIN
VALUATION GAP
RESTRICTED PARTY HIT UNRESOLVED
SANCTIONS RISK UNRESOLVED
LICENSE REQUIREMENT UNCERTAIN
DOCUMENTATION INCOMPLETE
DOCUMENTATION PROVENANCE MISSING
TRADE CONCLUSION UNSUPPORTED
QUALIFIED TRADE APPROVAL REQUIRED
BINDING CLASSIFICATION PROHIBITED
SANCTIONS DETERMINATION PROHIBITED
LICENSE DETERMINATION PROHIBITED
CUSTOMS SUBMISSION PROHIBITED
TRADE FILING PROHIBITED
EXTERNAL SUBMISSION PROHIBITED
```

The system should never fabricate classifications, rulings, licenses, certificates, screening results, customs values, origin determinations, government communications, approvals, or filings.

## End-to-end reference workflow

A typical F107 workflow follows this sequence:

1. Capture transaction parties, goods, destinations, purpose, and jurisdictions.
2. Register product facts and evidence.
3. Research candidate tariff or trade classifications.
4. Review country of origin and customs valuation.
5. Screen relevant parties and preserve screening provenance.
6. Review sanctions, embargo, export-control, end-use, and licensing considerations.
7. Review required trade documents and cross-document consistency.
8. Preserve evidence provenance and limitations.
9. Triage material trade risks and unresolved questions.
10. Route uncertain or high-risk matters to qualified specialists.
11. Perform independent trade readiness review.
12. Apply fail-closed governance gates.
13. Require explicit qualified-human trade approval.
14. Keep binding classifications, sanctions determinations, licensing decisions, filings, customs submissions, and external submissions outside autonomous authority.

## Evaluation and held-out governance suite

The repository contains evaluation logic under `evals/` and benchmark cases under `benchmarks/`.

Evaluation should test both workflow usefulness and governance behavior, including:

- transaction-scope completeness
- classification uncertainty detection
- origin uncertainty detection
- valuation-gap detection
- restricted-party escalation
- sanctions-risk escalation
- licensing-uncertainty enforcement
- documentation provenance
- unsupported-conclusion detection
- qualified-human approval enforcement
- protected-action enforcement

The behavioral verification layer includes eight direct governance tests and a 10-scenario held-out international-trade governance suite.

## Verification gates

CI runs on Python 3.10, 3.11, and 3.12 and requires:

```bash
ruff check . --select E9,F63,F7,F82
python -m pytest -q
python evals/held_out.py
python run.py
```

These gates verify syntax-critical linting, governance behavior, held-out scenarios, and execution of the governed reference workflow.

## Reproducibility

Install development dependencies:

```bash
python -m pip install -e .
```

Then run:

```bash
ruff check . --select E9,F63,F7,F82
python -m pytest -q
python evals/held_out.py
python run.py
```

## Extension points

Organization-specific implementations can add governed integrations for:

- product master data
- ERP systems
- customs platforms
- restricted-party screening services
- sanctions data
- tariff databases
- export-classification repositories
- broker portals
- logistics systems
- document repositories
- license-management systems
- trade analytics

Integrations should preserve source provenance, effective dates, access control, human authority, and fail-closed behavior.

## Example applications

Potential governed uses include:

- transaction intake and trade-readiness review
- classification research support
- origin and valuation evidence organization
- restricted-party screening workflow
- sanctions and export-control triage
- licensing-question preparation
- trade-document quality review
- customs broker package preparation
- trade-compliance training and simulation

F107 is not a customs authority, sanctions authority, licensing authority, customs broker, law firm, or autonomous filing system.

## Design principles

F107 follows these principles:

1. Scope the transaction before drawing trade conclusions.
2. Preserve product, party, document, and regulatory provenance.
3. Keep classification, origin, valuation, sanctions, and licensing uncertainty explicit.
4. Treat screening results as evidence requiring review, not automatic legal clearance.
5. Separate research support from binding trade authority.
6. Escalate material risks and conflicting evidence.
7. Fail closed when required reviews or evidence are incomplete.
8. Keep filings, submissions, binding classifications, sanctions determinations, and licensing decisions under qualified human authority.

## Scope statement

F107 demonstrates a governed multi-agent architecture for international trade support. It combines specialized agents, deterministic trade tools, evidence discipline, risk triage, observability, evaluation, and fail-closed governance while preserving strict boundaries around customs, sanctions, export-control, licensing, and external-submission authority.

It is a reference implementation for governed trade workflow engineering, not a substitute for qualified professional or government judgment.