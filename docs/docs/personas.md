

# Personas

An AI system is easy to conceptualise and quickly developed. However to scale and sustain such system in a trustworthy manner require a wide array of personas actively collaborating. This section lists typical roles across the organisation, divided into *core*, *adjacent* and *external* - depending on their level of active participation in developing and managing the system. 

??? trustably "Note"
    - Not all these roles are required to start AI journey. As the organisation transitions across various levels of maturity, more of these personas will be needed to manage and operate. 
    - It is generally common, and even desired, that some these personas are assumed by same person. It is still important to recognise the role they are performing so that required responsibilities can be carried out correctly 



## Core Personas


??? trustably   "AI Solution Designer"
    AI Solution Designers are responsible for translating business objectives and requirements into coherent AI solution concepts, including agent roles, workflows, and interaction patterns. They define how agentic AI capabilities are embedded into business processes and decision flows. This role balances functional effectiveness, usability, and risk considerations at the solution level. AI Solution Designers collaborate closely with architects, product managers, and business stakeholders to ensure alignment with enterprise standards. They also ensure that design choices support explainability, controllability, and appropriate human oversight. Their work directly shapes how value and risk are realized through agentic systems.

??? trustably   "AI Architects"
    AI Architects define the end-to-end technical architecture for agentic AI systems, including models, agents, orchestration layers, integrations, and control mechanisms. They ensure architectural alignment with enterprise standards, scalability requirements, and security principles. This role is accountable for addressing non-determinism, autonomy, and emergent behaviors through appropriate architectural patterns. AI Architects evaluate trade-offs between capability, performance, and risk exposure. They work closely with enterprise and cloud architects to ensure ecosystem consistency. Their decisions materially influence system resilience and governability.

??? trustably   "Business Owners"
    System Owners hold accountability for the overall lifecycle, performance, and risk posture of agentic AI systems in production. They are responsible for ensuring systems meet business objectives while operating within approved risk appetite and compliance boundaries. System Owners approve use cases, changes, and operating conditions for AI agents. They coordinate across technical, legal, and operational teams to manage incidents and escalations. This role ensures clear ownership for outcomes driven by agentic behavior. System Owners serve as the primary point of accountability to executive leadership.


??? trustably   "Data Engineers"
    Data Engineers design, build, and operate data pipelines that supply agentic AI systems with reliable and timely data. They ensure data availability, quality, and lineage across the AI lifecycle. This role implements controls for data ingestion, transformation, and access. Data Engineers collaborate with data architects and ML teams to support scalable and secure data flows. Their work directly impacts model performance and agent behavior. They are critical to operational stability.

??? trustably   "Data Scientists"
    Data Scientists develop analytical models and experiments that inform or power agentic AI capabilities. They explore data patterns, define features, and evaluate model behavior. This role contributes to understanding model limitations, biases, and uncertainties. Data Scientists work closely with ML and AI engineers to transition models into production. They support performance monitoring and continuous improvement. Their insights shape decision quality and system effectiveness.

??? trustably   "Data and AI Architects"
    Data Architects define the enterprise data structures, standards, and governance models supporting agentic AI systems. They ensure consistency, interoperability, and compliance across data domains. This role aligns data design with business semantics and regulatory requirements. Data Architects guide data platform evolution to support AI workloads. They collaborate with enterprise architects to ensure strategic alignment. Their work enables sustainable and governed data use.

??? trustably   "Application Developers"
    Application Developers build and maintain the software components that integrate agentic AI systems into business applications. They implement user interfaces, APIs, and orchestration logic. This role ensures secure and reliable interaction between users, agents, and backend systems. Application Developers collaborate with AI engineers to manage invocation patterns and error handling. They are responsible for performance and maintainability. Their work directly affects user experience.

??? trustably   "Human-Centric Application Designers"
    Human-Centric Application Designers focu"s on the interaction between humans and agentic AI systems. They design experiences that promote clarity, trust, and appropriate reliance on AI outputs. This role ensures human oversight and intervention points are well defined. Designers account for cognitive load and decision support needs. They collaborate with risk and ethics teams to mitigate misuse. Their work supports responsible adoption.


??? trustably   "ML Engineers"
    ML Engineers operationalize machine learning models within agentic AI systems. They manage model deployment, versioning, monitoring, and retraining. This role ensures models perform reliably at scale. ML Engineers implement safeguards against model drift and degradation. They collaborate with platform and AI engineers on infrastructure. Their work underpins production stability.

??? trustably   "AI Engineers"
    AI Engineers build and integrate agentic capabilities, including reasoning, planning, and action execution. They design agent behaviors, tool usage, and control logic. This role addresses reliability and safety in autonomous operations. AI Engineers work closely with architects to implement governance controls. They continuously refine agent performance. Their work defines system autonomy.

??? trustably   "Product Manager"
    Product Managers define the vision, roadmap, and success metrics for agentic AI products. They balance customer value, feasibility, and risk considerations. This role prioritizes features and manages trade-offs. Product Managers align stakeholders across functions. They ensure outcomes meet business objectives. Their decisions drive adoption.

??? trustably   "AI Governance Lead "
    This role owns the enterprise-wide AI governance framework and ensures consistent application across business units. It acts as the single point of accountability for AI risk posture, policy interpretation, and exception management. Without this role, ownership is often fragmented between IT, Legal, and Risk functions. The AI Governance Lead typically reports to a risk or technology executive. This role is especially critical for coordinating decisions related to agent autonomy.

??? trustably   "AI Security Lead"
    While security responsibilities are often distributed, agentic AI systems introduce novel attack surfaces. This role focuses on AI-specific threats such as prompt injection, data exfiltration, model abuse, and agent hijacking. It coordinates detection, response, and recovery. This role works closely with SOC teams. It is critical for operational resilience.

??? trustably   "AI Operations (AIOps) Lead"
    This role owns operational response to AI-related incidents, including runaway agents, unintended actions, or harmful outputs. It defines escalation paths and kill-switch mechanisms. Traditional IT incident management is often insufficient for agentic behavior. This role ensures rapid containment and remediation. It protects business continuity.


## Adjacent Personas 

??? trustably   "Data Source Owners/Experts"
    Data Source Owners and Experts are accountable for the accuracy, quality, and appropriate use of specific data assets consumed by agentic AI systems. They define data meaning, constraints, and usage conditions. This role ensures data aligns with business intent and compliance requirements. They support impact assessments when data is used for new AI purposes. Data Source Owners provide critical domain knowledge. Their stewardship reduces downstream risk.

??? trustably   "Cloud Platform Engineers"
    Cloud Platform Engineers operate the underlying infrastructure supporting agentic AI systems. They ensure availability, scalability, and security of compute and services. This role implements operational controls and monitoring. Cloud Platform Engineers support cost management and resilience. They collaborate with security and architecture teams. Their work ensures production readiness.

??? trustably   "Cloud Platform Architects"
    Cloud Platform Architects design cloud environments optimized for agentic AI workloads. They define reference architectures, security patterns, and integration standards. This role ensures alignment with enterprise cloud strategy. Cloud Platform Architects address scalability and resilience. They collaborate with AI and enterprise architects. Their designs enable sustainable growth.

??? trustably   "Enterprise Architects"
    Enterprise Architects ensure agentic AI systems align with enterprise strategy, operating models, and technology standards. They evaluate cross-domain impacts and dependencies. This role ensures coherence across portfolios. Enterprise Architects guide long-term capability evolution. They balance innovation with standardization. Their oversight reduces fragmentation.

??? trustably   "Enterprise Security Architect"
    The Security Architect defines and governs the security architecture for AI platforms and agentic AI systems across the enterprise. This role establishes security principles and control patterns to address AI-specific risks such as model abuse, data leakage, prompt injection, and unauthorized autonomous actions. They ensure security is embedded into system design through zero-trust, least-privilege, and defense-in-depth approaches. The Security Architect collaborates with AI, cloud, and enterprise architects to align controls with enterprise standards and regulatory requirements. This role is accountable for maintaining a security posture consistent with the organization’s risk appetite.

??? trustably   "Third Party Solution Providers"
    Third Party Solution Providers deliver external AI models, platforms, or services used within agentic AI systems. They are accountable for meeting contractual, security, and compliance requirements. This role introduces dependency and supply-chain risk. Providers must support transparency and assurance. Their solutions influence system behavior. Effective vendor governance is essential.

??? trustably   "Change Manager"
    Change Managers oversee organizational readiness for adopting agentic AI systems. They manage communication, training, and stakeholder engagement. This role addresses behavioral and cultural impacts. Change Managers mitigate resistance and misuse. They ensure smooth transition into operations. Their work supports sustained value.

??? trustably   "Risk Managers"
    Risk Managers identify, assess, and monitor risks associated with agentic AI systems. They ensure risks remain within approved appetite. This role integrates AI risks into enterprise risk frameworks. Risk Managers advise on controls and mitigations. They support decision-making and escalation. Their oversight enables responsible deployment.


??? trustably   "Quality Assurance Experts"
    Quality Assurance Experts validate that agentic AI systems perform as intended across functional, non-functional, and risk-related dimensions. They design and execute testing strategies that account for probabilistic behavior, edge cases, and failure modes. This role ensures system behavior remains within defined tolerances under varying conditions. QA Experts collaborate with engineering and risk teams to identify defects and unintended outcomes. They contribute to release readiness and ongoing assurance. Their work supports system reliability and user trust.

??? trustably   "Executive Sponsor"
    The Executive Sponsor provides strategic oversight, funding approval, and organizational sponsorship for agentic AI initiatives. This role ensures alignment between AI investments and enterprise strategy, risk appetite, and ethical commitments. Executive Sponsors resolve cross-functional conflicts and remove organizational barriers. They are accountable for ensuring appropriate governance structures are in place. Their visible support drives adoption and accountability across the organization. Executive Sponsors represent AI initiatives at the board and executive committee level.

??? trustably   "Decision Authority Role"
    This role formally represents the “human-in-the-loop” or “human-on-the-loop” accountability. It has authority to approve, override, or halt agent actions. Without explicit designation, human accountability becomes ambiguous. This role is critical for regulatory defensibility. It ensures meaningful human control.

??? trustably   "Training & Enablement Owner"
    This role ensures all stakeholders interacting with agentic AI systems are adequately trained. It defines competency requirements and certification. Misuse risk often stems from poor understanding rather than system flaws. This role reduces operational and reputational risk. It supports safe adoption at scale.



## External Personas

??? trustably   "End User"
    End Users are individuals or groups who interact directly or indirectly with agentic AI systems in the course of performing business or operational activities. They consume system outputs, recommendations, or actions and may initiate inputs that influence agent behavior. End Users are accountable for using AI-enabled capabilities in accordance with defined policies, usage guidelines, and decision rights. Their feedback is critical for identifying usability issues, unintended behaviors, and emerging risks in real-world contexts. End Users also play a role in validating whether agentic AI actions align with business intent and ethical expectations. Proper enablement and training are essential to ensure informed and responsible use.

??? trustably   "Corporate Functions"
    Corporate Functions such as HR, Finance, and Procurement support agentic AI initiatives through policy, funding, and governance mechanisms. They ensure alignment with corporate controls and ethics. This role enables enterprise-wide consistency. Corporate Functions manage workforce and financial impacts. They support compliance and reporting. Their involvement ensures organizational alignment.

??? trustably   "Social Stakeholders"
    Social Stakeholders include communities and groups indirectly affected by agentic AI systems. They may experience societal, environmental, or economic impacts. This role represents external perspectives and expectations. Engagement supports social license to operate. Social Stakeholders influence public trust. Their concerns must be considered.

??? trustably   "Stake/Shareholders"
    Stakeholders and Shareholders have an interest in the outcomes, performance, and risk exposure associated with agentic AI systems. They include internal and external parties affected by AI-driven decisions. This role expects transparency, accountability, and value realization. Stakeholders influence priorities through governance and oversight mechanisms. Their trust is essential for sustained adoption. They are impacted by both benefits and failures.

??? trustably   "Third Party Solution Consumers"
    Third Party Solution Consumers use agentic AI capabilities exposed by the organization. They rely on system outputs to inform decisions or actions. This role requires clear usage terms and accountability boundaries. Consumers may introduce reputational risk through misuse. Proper onboarding and controls are necessary. Their behavior impacts trust.

??? trustably   "Legal/Compliance/Audit Experts"
    Legal, Compliance, and Audit Experts ensure that agentic AI systems adhere to applicable laws, regulations, contractual obligations, and internal policies. They assess legal exposure arising from autonomous actions, data usage, and decision-making impacts. This role evaluates governance controls, documentation, and auditability of AI systems. They advise on regulatory readiness, cross-border considerations, and third-party risk. Their involvement is critical in defining acceptable boundaries for agent autonomy. They provide independent assurance to executives and regulators.
