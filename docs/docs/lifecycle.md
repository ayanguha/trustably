

# AI System Lifecycle


![Framework](images/lifecycle.png){ width="600" }


??? trustably "Design"

    The Design phase establishes the foundational intent, scope, and governance posture of the AI solution. This includes defining business objectives, value hypotheses, target users, decision boundaries, and ethical considerations. Architectural principles, security-by-design requirements, data classification, and regulatory obligations are incorporated upfront to ensure compliance and traceability. Clear ownership, funding accountability, and success criteria are formalized to support downstream assurance activities.

??? trustably "DataOps"
    DataOps represents the governed, end-to-end management of data assets that underpin AI and analytics systems, encompassing both data sourcing and data preparation activities. It establishes standardized controls for data acquisition, validation, transformation, lineage, and stewardship to ensure data is trustworthy, compliant, and fit for purpose. Operating as a cross-functional capability, DataOps enforces alignment with enterprise data governance, security, privacy, and regulatory requirements while enabling scalable and repeatable data pipelines. Through automation, monitoring, and accountability mechanisms, DataOps reduces operational risk, improves data quality, and provides a reliable foundation for downstream model development and decision-making.

    ??? quote inline  "Data Sources"
        This section governs the identification, acquisition, and authorization of data inputs used across the AI lifecycle. Data sources are assessed for quality, provenance, sensitivity, licensing constraints, and regulatory compliance (e.g., privacy, data residency, sectoral obligations). Controls are established to ensure lawful access, appropriate consent, and alignment with enterprise data governance standards. Ongoing monitoring ensures continued fitness-for-purpose as source systems evolve.

    ??? quote inline  "Data Preparation"
         Data Preparation focuses on transforming raw data into model-ready datasets through cleansing, normalization, enrichment, and feature engineering. This stage enforces data integrity, bias mitigation, lineage documentation, and reproducibility controls. Governance oversight ensures that preprocessing decisions are transparent, auditable, and aligned with approved use cases. Data handling practices are validated against security, privacy, and retention policies.


??? trustably "AI/MLOps"

    AI/MLOps is the enterprise capability responsible for the governed lifecycle management of AI and machine learning models, encompassing model selection, evaluation, deployment, and ongoing performance oversight. It establishes standardized processes, tooling, and controls to ensure models are developed, validated, operated, and evolved in a consistent, secure, and auditable manner. AI/MLOps enforces alignment with enterprise risk management, security, compliance, and responsible AI principles, while enabling scalable and repeatable model operations. By integrating monitoring, automation, and human-in-the-loop governance, AI/MLOps ensures models remain performant, reliable, and compliant throughout their operational lifespan.

    ??? quote inline  "Model Selection & Evaluation"
        This section governs the selection of algorithms, architectures, and training approaches appropriate to the defined business and risk context. Models are evaluated against standardized criteria including accuracy, robustness, explainability, fairness, and operational constraints. Comparative testing, validation methodologies, and approval gates are applied to ensure defensible model choices. Decisions are documented to support auditability and regulatory review.

    ??? quote inline  "Model Performance Management"
         Model Performance Management ensures continuous oversight of model behavior throughout its lifecycle. Performance metrics, drift indicators, bias signals, and reliability thresholds are defined and monitored. Governance controls mandate periodic reviews, retraining triggers, and escalation procedures when performance deviates from approved tolerances. This function supports accountability for ongoing model risk and business outcomes.


??? trustably "DevSecOps"

    DevSecOps is the enterprise capability that embeds security, risk, and compliance controls across the design, build, deployment, and operation of AI-enabled platforms and services. It integrates secure engineering practices, automated control enforcement, and continuous assurance into development and operational workflows, ensuring security is treated as a shared responsibility rather than a downstream activity. DevSecOps establishes consistent standards for identity, access management, infrastructure security, code integrity, and vulnerability management across environments. By aligning with enterprise security architecture and governance frameworks, DevSecOps enables resilient, compliant, and scalable delivery of AI systems while maintaining a strong and measurable security posture.

    ??? quote inline  "Deployment & Serving"
        Deployment & Serving governs the controlled release of models into production environments. This includes infrastructure security, access control, version management, and integration with enterprise systems. Approval workflows ensure that only validated and authorized models are deployed. Runtime safeguards, logging, and observability mechanisms are implemented to maintain operational resilience and compliance.

    ??? quote inline  "Automation"
        Automation addresses the orchestration of pipelines across data ingestion, training, testing, deployment, and monitoring. Governance ensures automation is implemented with appropriate guardrails, human-in-the-loop controls, and exception handling. Automated processes are designed to reduce operational risk while preserving transparency and intervention capability. Change management and rollback procedures are embedded to maintain system stability.

??? trustably "Enhance and Operate"

    This section represents the steady-state operation and continuous improvement of the AI system. It includes incident management, user feedback incorporation, cost optimization, and capability enhancement. Governance mechanisms ensure changes are assessed for risk, approved through formal controls, and aligned with strategic objectives. This phase reinforces accountability for long-term value realization and responsible AI operation.

