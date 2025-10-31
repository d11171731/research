# Configuration Management Performance Assessment Framework
## For Fintech Organizations in Vietnam & Southeast Asia

**Version:** 1.0
**Date:** 2025-10-30
**Context:** ITIL/ITSM Configuration Management Maturity Assessment
**Target:** Fast-growing Fintech Organizations

---

## Table of Contents

1. [Executive Summary](#executive-summary)
2. [Assessment Overview](#assessment-overview)
3. [Maturity Model Definition](#maturity-model-definition)
4. [Dimension 1: Governance (Quản trị)](#dimension-1-governance)
5. [Dimension 2: Process (Quy trình)](#dimension-2-process)
6. [Dimension 3: Tool & Data](#dimension-3-tool--data)
7. [Dimension 4: Measurement](#dimension-4-measurement)
8. [Dimension 5: People](#dimension-5-people)
9. [Dimension 6: Improvement](#dimension-6-improvement)
10. [Dimension 7: Integration](#dimension-7-integration)
11. [Dimension 8: Compliance](#dimension-8-compliance)
12. [Scoring Methodology](#scoring-methodology)
13. [Interview Guide & Schedule](#interview-guide--schedule)

---

## Executive Summary

### Purpose
This framework enables fintech organizations to assess and improve their Configuration Management (CM) capabilities according to ITIL/ITSM best practices and Vietnamese regulatory requirements (SBV Circular 41/2018, Decree 85/2019).

### Assessment Scope
Evaluation across **8 critical dimensions** with **60+ assessment criteria** and **100+ targeted interview questions** to determine CM maturity level (0-5 scale).

### Key Benefits
- **Quantified Maturity**: Clear scoring methodology with industry benchmarks
- **Actionable Insights**: Specific gaps and improvement recommendations
- **Regulatory Alignment**: Mapped to Vietnamese financial regulations
- **Risk Identification**: Critical CMDB accuracy and audit readiness gaps
- **Practical Roadmap**: Phased improvement plan (Quick Wins → Strategic Initiatives)

### Target Interviewees
- **Executive Level**: CIO, CTO, Head of IT Operations
- **Management Level**: IT Service Manager, Change Manager, Configuration Manager, Security Manager
- **Operational Level**: Configuration Analysts, System Administrators, DevOps Engineers, Service Desk Team
- **Business Stakeholders**: Compliance Officer, Internal Audit, Business Unit Managers

---

## Assessment Overview

### Assessment Dimensions

| Dimension | Focus Area | Weight | Critical for Fintech |
|-----------|-----------|--------|---------------------|
| **1. Governance** | Policies, roles, ownership, CAB integration | 15% | Yes - Regulatory compliance |
| **2. Process** | CI lifecycle, relationships, baseline management | 20% | Yes - Change control |
| **3. Tool & Data** | CMDB accuracy, integration, automation | 20% | Yes - System reliability |
| **4. Measurement** | KPIs, reporting, dashboards | 10% | Medium - Performance tracking |
| **5. People** | Skills, training, roles, responsibilities | 10% | Medium - Capability building |
| **6. Improvement** | Continuous improvement, problem resolution | 10% | Medium - Operational excellence |
| **7. Integration** | Cross-process integration | 10% | Yes - End-to-end visibility |
| **8. Compliance** | Audit readiness, regulatory requirements | 15% | Yes - SBV/regulatory mandates |

**Total Weight:** 100%

### Assessment Timeline

| Phase | Duration | Activities |
|-------|----------|-----------|
| **Discovery** | 1-2 days | Executive interviews, document review |
| **Deep Dive** | 3-5 days | Process walkthroughs, CMDB analysis, staff interviews |
| **Analysis** | 2-3 days | Maturity scoring, gap analysis, benchmarking |
| **Reporting** | 2-3 days | Report development, recommendations, roadmap |
| **Presentation** | 1 day | Executive presentation, working session |

**Total Duration:** 10-15 days

---

## Maturity Model Definition

### Maturity Levels (0-5 Scale)

| Level | Name | Description | CMDB Accuracy | Risk Level |
|-------|------|-------------|---------------|------------|
| **0** | Non-existent | No CMDB or CM process exists | N/A | Critical |
| **1** | Initial | Ad-hoc, reactive, spreadsheet-based | <60% | High |
| **2** | Developing | Basic CMDB, manual updates, inconsistent | 60-75% | High-Medium |
| **3** | Defined | Standardized process, documented, trained | 75-85% | Medium |
| **4** | Managed | Metrics-driven, integrated, automated discovery | 85-95% | Low-Medium |
| **5** | Optimizing | Predictive, AI-driven, continuous optimization | >95% | Low |

### Fintech Industry Benchmarks

| Organization Profile | Typical Maturity | CMDB Accuracy | Key Characteristics |
|---------------------|------------------|---------------|---------------------|
| **Early Stage (<2 years)** | 1.0-2.0 | 50-70% | Manual tracking, limited tooling |
| **Growth Stage (2-5 years)** | 2.0-3.5 | 70-85% | ITSM tool implemented, process gaps |
| **Mature (>5 years)** | 3.5-4.5 | 85-95% | Automated discovery, strong governance |
| **Industry Leader** | 4.5-5.0 | >95% | Predictive analytics, full automation |

**Target for Regulated Fintech:** Minimum Level 3.0 (85% CMDB accuracy) for audit readiness

---

## Dimension 1: Governance (Quản trị)

### Overview
Assessment of policies, organizational structure, roles, responsibilities, and decision-making framework for Configuration Management.

### Assessment Criteria

| Criterion ID | Criterion | Weight | Maturity Indicators |
|--------------|-----------|--------|---------------------|
| **GOV-01** | CM Policy & Standards | High | L1: No policy / L3: Documented policy / L5: Living policy with continuous review |
| **GOV-02** | Organizational Structure & Roles | High | L1: No defined roles / L3: Clear RACI matrix / L5: Specialized CM team |
| **GOV-03** | Configuration Control Board (CCB) | Medium | L1: No CCB / L3: Regular CCB meetings / L5: Integrated with CAB |
| **GOV-04** | CM Ownership & Accountability | High | L1: No owner / L3: Named CM Manager / L5: Executive sponsorship |
| **GOV-05** | Authorization & Access Control | Critical | L1: Open access / L3: Role-based access / L5: Automated entitlement mgmt |
| **GOV-06** | Regulatory Compliance Mapping | Critical | L1: No mapping / L3: Documented mapping / L5: Continuous compliance monitoring |
| **GOV-07** | Budget & Resource Allocation | Medium | L1: No budget / L3: Annual budget / L5: Value-based investment |
| **GOV-08** | Strategic Alignment | Medium | L1: No alignment / L3: IT strategy linkage / L5: Business outcome-driven |

### Interview Questions

| Question ID | Question | Target Interviewee | Purpose | Maturity Evidence |
|-------------|----------|-------------------|---------|-------------------|
| **GOV-Q01** | Is there a formal Configuration Management policy approved by executive management? When was it last reviewed? | IT Director, Configuration Manager | Assess policy existence and currency | L1: No policy / L3: Approved policy <2 years old / L5: Annual review cycle |
| **GOV-Q02** | Who is the designated Configuration Manager? What is their authority and reporting line? | CIO, Configuration Manager | Determine ownership and authority level | L1: No owner / L3: Dedicated CM Manager / L5: Reports to CIO/CTO |
| **GOV-Q03** | How are Configuration Items (CIs) authorized for addition to the CMDB? What approval process exists? | Configuration Manager, Change Manager | Assess control framework | L1: No process / L3: CCB approval / L5: Automated workflow with audit trail |
| **GOV-Q04** | What is the composition and meeting frequency of the Configuration Control Board (CCB)? | Configuration Manager, IT Service Manager | Evaluate governance structure | L1: No CCB / L3: Monthly CCB with IT representation / L5: Weekly CCB integrated with CAB |
| **GOV-Q05** | How is CM integrated with Change Management governance (e.g., Change Advisory Board)? | Change Manager, Configuration Manager | Assess cross-process governance | L1: No integration / L3: CCB rep attends CAB / L5: Unified governance model |
| **GOV-Q06** | What access controls exist for viewing and modifying CMDB data? How are they enforced? | Configuration Manager, Security Manager | Evaluate security controls | L1: Open access / L3: Role-based access control / L5: Automated access reviews quarterly |
| **GOV-Q07** | How does CM policy address State Bank of Vietnam (SBV) Circular 41/2018 requirements for asset management? | Compliance Officer, Configuration Manager | Assess regulatory compliance | L1: No awareness / L3: Documented mapping / L5: Automated compliance reporting |
| **GOV-Q08** | What budget and resources are allocated specifically for Configuration Management activities? | IT Director, Configuration Manager | Determine investment level | L1: No budget / L3: Annual tool + staff budget / L5: Multi-year investment roadmap |
| **GOV-Q09** | How are CM roles and responsibilities defined (RACI matrix)? How is this communicated? | Configuration Manager, IT Service Manager | Assess role clarity | L1: No RACI / L3: Documented RACI / L5: RACI in ITSM tool with training |
| **GOV-Q10** | How is CM performance reported to executive management? What metrics are shared? | CIO, Configuration Manager | Evaluate executive visibility | L1: No reporting / L3: Quarterly reports / L5: Real-time dashboard with KPIs |
| **GOV-Q11** | What is the escalation path for CM-related issues or conflicts (e.g., CMDB accuracy disputes)? | Configuration Manager, IT Service Manager | Assess issue resolution framework | L1: Ad-hoc / L3: Documented escalation path / L5: SLA-driven escalation with tracking |
| **GOV-Q12** | How does the organization ensure CM policy adherence across all IT teams (DevOps, Infra, Security)? | IT Director, Configuration Manager | Evaluate policy enforcement | L1: No enforcement / L3: Periodic audits / L5: Automated compliance checks |

### Governance Maturity Indicators by Level

**Level 1 (Initial) - Score 1.0-1.9:**
- No formal CM policy or governance structure
- CM activities performed ad-hoc by various teams
- No designated Configuration Manager
- No budget or resource allocation
- Unclear roles and responsibilities

**Level 2 (Developing) - Score 2.0-2.9:**
- Basic CM policy documented but not consistently followed
- Configuration Manager role exists but limited authority
- Informal governance meetings (irregular)
- Minimal budget allocation
- RACI defined but not widely communicated

**Level 3 (Defined) - Score 3.0-3.9:**
- Formal CM policy approved and reviewed regularly
- Dedicated Configuration Manager with clear authority
- Regular CCB meetings with documented decisions
- Annual budget for CM tools and resources
- Clear RACI matrix communicated to all stakeholders
- Compliance mapping to SBV regulations documented

**Level 4 (Managed) - Score 4.0-4.9:**
- CM policy integrated with IT governance framework
- CM Manager reports to senior leadership (CIO/CTO)
- CCB integrated with Change Advisory Board
- Multi-year CM investment roadmap
- Role-based access control with automated reviews
- Quarterly compliance reporting to executive management

**Level 5 (Optimizing) - Score 5.0:**
- Living CM policy with continuous improvement cycles
- Executive sponsorship with CM on IT leadership agenda
- Unified governance model across all IT processes
- Value-based CM investment with ROI tracking
- Automated access management with AI-driven anomaly detection
- Continuous compliance monitoring with predictive risk assessment

---

## Dimension 2: Process (Quy trình)

### Overview
Assessment of CI lifecycle management, relationship mapping, baseline management, and operational procedures.

### Assessment Criteria

| Criterion ID | Criterion | Weight | Maturity Indicators |
|--------------|-----------|--------|---------------------|
| **PROC-01** | CI Identification & Registration | Critical | L1: No standard / L3: Naming convention / L5: Auto-discovery |
| **PROC-02** | CI Lifecycle Management | High | L1: No lifecycle / L3: Documented lifecycle / L5: Automated state mgmt |
| **PROC-03** | CI Relationship Mapping | Critical | L1: No relationships / L3: Key relationships / L5: Full dependency map |
| **PROC-04** | Baseline Management | High | L1: No baselines / L3: Manual baselines / L5: Automated baseline mgmt |
| **PROC-05** | CI Verification & Audit | Critical | L1: No audit / L3: Periodic audits / L5: Continuous verification |
| **PROC-06** | CI Ownership Assignment | High | L1: No owner / L3: Owner assigned / L5: Automated ownership tracking |
| **PROC-07** | Configuration Snapshot & Recovery | High | L1: No snapshots / L3: Manual snapshots / L5: Automated version control |
| **PROC-08** | Decommissioning Process | Medium | L1: No process / L3: Documented process / L5: Automated retirement workflow |

### Interview Questions

| Question ID | Question | Target Interviewee | Purpose | Maturity Evidence |
|-------------|----------|-------------------|---------|-------------------|
| **PROC-Q01** | What types of Configuration Items (CIs) are tracked in your CMDB? (Hardware, Software, Services, Documents, People) | Configuration Manager, Configuration Analyst | Determine CI scope | L1: <3 types / L3: 5+ types / L5: Comprehensive CI taxonomy |
| **PROC-Q02** | How are CIs identified and named? Is there a standard naming convention? | Configuration Analyst, System Administrator | Assess CI identification standards | L1: No standard / L3: Documented convention / L5: Auto-generated IDs |
| **PROC-Q03** | What is the process for adding a new CI to the CMDB? Who is responsible? How long does it take? | Configuration Analyst, Configuration Manager | Evaluate registration process | L1: No process / L3: Documented process <1 day / L5: Auto-discovery <1 hour |
| **PROC-Q04** | How do you track the lifecycle states of CIs (e.g., Ordered, In Stock, In Use, Retired)? | Configuration Analyst, Asset Manager | Assess lifecycle management | L1: No tracking / L3: Manual status updates / L5: Automated state transitions |
| **PROC-Q05** | How are relationships between CIs captured and maintained? (e.g., Server → Application → Service) | Configuration Analyst, Configuration Manager | Evaluate relationship mapping | L1: No relationships / L3: Manual relationship entry / L5: Auto-discovered dependencies |
| **PROC-Q06** | Can you demonstrate the full dependency chain for a critical service (e.g., payment processing)? | Configuration Manager, Service Manager | Test relationship completeness | L1: Cannot show / L3: Partial chain / L5: Complete multi-tier dependency map |
| **PROC-Q07** | How are configuration baselines established and managed (e.g., production release baseline)? | Configuration Manager, Release Manager | Assess baseline management | L1: No baselines / L3: Manual baseline snapshots / L5: Automated baseline with version control |
| **PROC-Q08** | What is the frequency of CMDB audits? How are discrepancies identified and resolved? | Configuration Manager, Configuration Analyst | Evaluate verification process | L1: No audits / L3: Annual audits / L5: Continuous automated reconciliation |
| **PROC-Q09** | How do you verify CMDB accuracy? What is the current accuracy rate? | Configuration Manager, CMDB Administrator | Quantify accuracy | L1: No measurement / L3: Periodic sample audit 75-85% / L5: Real-time monitoring >95% |
| **PROC-Q10** | How is CI ownership assigned and tracked? How do you ensure owners keep data current? | Configuration Manager, IT Service Manager | Assess ownership model | L1: No owners / L3: Owners assigned, manual reminders / L5: Automated ownership with SLA |
| **PROC-Q11** | When a CI is decommissioned, what is the process for updating the CMDB and archiving data? | Configuration Analyst, Asset Manager | Evaluate retirement process | L1: No process / L3: Manual update checklist / L5: Automated retirement workflow |
| **PROC-Q12** | How do you handle emergency changes that bypass normal CM processes? How is CMDB updated? | Change Manager, Configuration Manager | Assess exception handling | L1: CMDB not updated / L3: Post-change update / L5: Real-time emergency update protocol |
| **PROC-Q13** | How are CI attributes and fields standardized? Who defines the CMDB schema? | Configuration Manager, CMDB Administrator | Evaluate data model governance | L1: No standard / L3: Documented schema / L5: Governed data model with change control |
| **PROC-Q14** | How do you ensure consistency of CI data across different tools (monitoring, ITSM, asset mgmt)? | Configuration Manager, Integration Specialist | Assess data synchronization | L1: No sync / L3: Manual reconciliation / L5: Automated federation/sync |

### Process Maturity Indicators by Level

**Level 1 (Initial) - Score 1.0-1.9:**
- No formal CI identification or registration process
- Limited CI types tracked (typically hardware only)
- No relationship mapping or dependency tracking
- No baselines or configuration snapshots
- No CMDB audit or verification process
- CMDB accuracy <60%

**Level 2 (Developing) - Score 2.0-2.9:**
- Basic CI registration process (manual)
- 3-5 CI types tracked (hardware, software, some services)
- Ad-hoc relationship documentation
- Manual baseline creation for major releases
- Annual CMDB audits with sample-based verification
- CMDB accuracy 60-75%

**Level 3 (Defined) - Score 3.0-3.9:**
- Standardized CI naming convention and lifecycle
- Comprehensive CI taxonomy (hardware, software, services, documents)
- Documented process for relationship mapping
- Regular baseline management for key configurations
- Quarterly CMDB audits with defined remediation process
- CI ownership assigned with documented responsibilities
- CMDB accuracy 75-85%

**Level 4 (Managed) - Score 4.0-4.9:**
- Automated CI discovery for major infrastructure
- Full lifecycle management with state tracking
- Complete dependency mapping for critical services
- Automated baseline management integrated with release mgmt
- Monthly automated verification with exception reporting
- Workflow-driven ownership model with SLAs
- CMDB accuracy 85-95%

**Level 5 (Optimizing) - Score 5.0:**
- Real-time auto-discovery across all environments
- Predictive lifecycle management with AI-driven recommendations
- Dynamic dependency mapping with impact analysis
- Continuous baseline monitoring with drift detection
- Real-time verification with automated remediation
- Self-service CI management with automated workflows
- CMDB accuracy >95% with continuous optimization

---

## Dimension 3: Tool & Data

### Overview
Assessment of CMDB platform, data quality, integration capabilities, and automation level.

### Assessment Criteria

| Criterion ID | Criterion | Weight | Maturity Indicators |
|--------------|-----------|--------|---------------------|
| **TOOL-01** | CMDB Platform Capability | Critical | L1: Spreadsheet / L3: ITSM CMDB module / L5: Dedicated CMDB/CMS |
| **TOOL-02** | Data Quality & Accuracy | Critical | L1: <60% / L3: 75-85% / L5: >95% |
| **TOOL-03** | Auto-Discovery & Integration | High | L1: No auto-discovery / L3: Basic discovery / L5: Full automation |
| **TOOL-04** | Data Model & Schema | High | L1: Flat structure / L3: Normalized model / L5: Enterprise data model |
| **TOOL-05** | CI Attributes Completeness | High | L1: <50% / L3: 70-80% / L5: >90% |
| **TOOL-06** | API & Integration Capability | High | L1: No API / L3: REST API / L5: Event-driven integration |
| **TOOL-07** | Visualization & Reporting | Medium | L1: No visualization / L3: Basic reports / L5: Interactive dashboards |
| **TOOL-08** | Scalability & Performance | Medium | L1: <1K CIs / L3: 10K-50K CIs / L5: >100K CIs with performance |

### Interview Questions

| Question ID | Question | Target Interviewee | Purpose | Maturity Evidence |
|-------------|----------|-------------------|---------|-------------------|
| **TOOL-Q01** | What tool/platform is used for the CMDB? (Spreadsheet, ServiceNow, Jira, BMC, custom) | Configuration Manager, CMDB Administrator | Identify tooling capability | L1: Excel/Sheets / L3: ITSM tool CMDB / L5: ServiceNow/BMC/iTop |
| **TOOL-Q02** | How many Configuration Items (CIs) are currently in the CMDB? | Configuration Manager, CMDB Administrator | Assess scale | L1: <500 / L3: 1K-10K / L5: >50K |
| **TOOL-Q03** | What is the measured CMDB accuracy rate? How is it calculated? | Configuration Manager, Configuration Analyst | Quantify data quality | L1: Unknown / L3: 75-85% sampled / L5: >95% automated verification |
| **TOOL-Q04** | How many mandatory CI attributes are defined? What is the completeness rate? | Configuration Analyst, CMDB Administrator | Assess data completeness | L1: <10 fields / L3: 20-30 fields, 70-80% / L5: 40+ fields, >90% |
| **TOOL-Q05** | Is automated discovery used? What tools? (Nmap, Qualys, ServiceNow Discovery, etc.) | Configuration Manager, System Administrator | Evaluate automation level | L1: No discovery / L3: Basic network scan / L5: Multi-tool federation |
| **TOOL-Q06** | How frequently does auto-discovery run? What CI types are auto-discovered? | Configuration Analyst, DevOps Engineer | Assess discovery frequency | L1: N/A / L3: Weekly infra scan / L5: Real-time cloud + infra |
| **TOOL-Q07** | What integrations exist between CMDB and other tools? (Monitoring, ITSM, Asset Mgmt, Cloud) | Configuration Manager, Integration Specialist | Evaluate integration maturity | L1: No integration / L3: 2-3 integrations / L5: 10+ with data federation |
| **TOOL-Q08** | Does the CMDB have a published API? Is it used by other systems? | CMDB Administrator, Developer | Assess API capability | L1: No API / L3: REST API / L5: GraphQL + webhooks |
| **TOOL-Q09** | How is CMDB data validated and quality checked? Are there automated validation rules? | Configuration Analyst, CMDB Administrator | Evaluate data quality controls | L1: No validation / L3: Manual spot checks / L5: Automated validation rules |
| **TOOL-Q10** | Can you visualize CI relationships and dependencies? Demonstrate with a critical service. | Configuration Manager, Configuration Analyst | Test visualization capability | L1: No visualization / L3: Static diagrams / L5: Interactive dependency maps |
| **TOOL-Q11** | What reports are generated from the CMDB? Who consumes them? | Configuration Manager, IT Service Manager | Assess reporting maturity | L1: No reports / L3: Monthly reports / L5: Real-time dashboards |
| **TOOL-Q12** | How does the CMDB handle multi-cloud environments (AWS, Azure, GCP)? | Configuration Manager, Cloud Engineer | Evaluate cloud support | L1: No cloud / L3: Manual cloud CI entry / L5: Cloud API integration |
| **TOOL-Q13** | What is the CMDB query performance for complex searches? (e.g., find all CIs for a service) | CMDB Administrator, Configuration Analyst | Assess performance | L1: N/A / L3: <5 sec for simple queries / L5: <2 sec for complex queries |
| **TOOL-Q14** | How is CMDB access provisioned and controlled? (Role-based, attribute-based access control) | Configuration Manager, Security Manager | Evaluate access control | L1: Shared account / L3: RBAC / L5: ABAC with dynamic policies |

### Tool & Data Maturity Indicators by Level

**Level 1 (Initial) - Score 1.0-1.9:**
- Spreadsheet-based or no CMDB
- <500 CIs tracked
- No automated discovery
- CMDB accuracy <60% (unknown)
- No integrations with other tools
- Flat data structure with <10 attributes per CI
- No API or visualization capability

**Level 2 (Developing) - Score 2.0-2.9:**
- Basic ITSM tool with CMDB module (Jira, Freshservice)
- 500-2,000 CIs tracked manually
- Limited auto-discovery (network scans)
- CMDB accuracy 60-75%
- 1-2 integrations (usually monitoring or asset mgmt)
- Basic normalized data model
- Simple list-based reports

**Level 3 (Defined) - Score 3.0-3.9:**
- Enterprise ITSM tool with CMDB (ServiceNow, BMC Helix)
- 2,000-10,000 CIs tracked
- Regular auto-discovery (weekly/daily for infrastructure)
- CMDB accuracy 75-85%
- 3-5 integrations (monitoring, ITSM, asset, cloud)
- Standardized data model with 20-30 attributes
- REST API available and documented
- Basic relationship visualization
- Scheduled reports (monthly/quarterly)

**Level 4 (Managed) - Score 4.0-4.9:**
- Advanced CMDB/CMS platform
- 10,000-100,000 CIs tracked
- Real-time auto-discovery for cloud and critical infra
- CMDB accuracy 85-95%
- 5-10 integrations with data federation
- Enterprise data model with 30-40 attributes, 80%+ completeness
- RESTful API with extensive use by other systems
- Interactive dependency mapping and impact analysis
- Real-time dashboards and self-service reports
- Automated data quality validation

**Level 5 (Optimizing) - Score 5.0:**
- Best-in-class CMDB with AI/ML capabilities
- >100,000 CIs with excellent performance
- Continuous auto-discovery across all environments (cloud, on-prem, SaaS)
- CMDB accuracy >95% with continuous verification
- 10+ integrations with event-driven architecture
- Comprehensive enterprise data model with 40+ attributes, >90% completeness
- GraphQL API with webhooks and real-time subscriptions
- AI-powered dependency mapping with predictive impact analysis
- Real-time interactive dashboards with drill-down
- Self-healing data quality with automated remediation
- Multi-tenant support with data segregation

---

## Dimension 4: Measurement

### Overview
Assessment of KPIs, metrics, reporting framework, and performance monitoring for Configuration Management.

### Assessment Criteria

| Criterion ID | Criterion | Weight | Maturity Indicators |
|--------------|-----------|--------|---------------------|
| **MEAS-01** | KPI Definition & Tracking | High | L1: No KPIs / L3: 5-7 KPIs / L5: Comprehensive scorecard |
| **MEAS-02** | CMDB Accuracy Measurement | Critical | L1: No measurement / L3: Quarterly audit / L5: Real-time tracking |
| **MEAS-03** | CI Completeness Tracking | High | L1: No tracking / L3: Monthly review / L5: Automated monitoring |
| **MEAS-04** | Relationship Coverage | Medium | L1: Unknown / L3: Manual count / L5: Automated dependency score |
| **MEAS-05** | Process Performance Metrics | Medium | L1: No metrics / L3: Manual tracking / L5: Automated dashboards |
| **MEAS-06** | Reporting & Dashboards | High | L1: No reports / L3: Monthly reports / L5: Real-time dashboards |
| **MEAS-07** | Benchmarking & Targets | Medium | L1: No targets / L3: Internal targets / L5: Industry benchmarks |
| **MEAS-08** | Value Measurement & ROI | Low | L1: No measurement / L3: Cost tracking / L5: Value realization |

### Interview Questions

| Question ID | Question | Target Interviewee | Purpose | Maturity Evidence |
|-------------|----------|-------------------|---------|-------------------|
| **MEAS-Q01** | What Key Performance Indicators (KPIs) are tracked for Configuration Management? | Configuration Manager, IT Service Manager | Identify KPI framework | L1: None / L3: 5-7 KPIs / L5: 10+ KPIs with targets |
| **MEAS-Q02** | How is CMDB accuracy measured? What is the current accuracy rate? | Configuration Manager, Configuration Analyst | Quantify accuracy | L1: Unknown / L3: 75-85% quarterly / L5: >95% real-time |
| **MEAS-Q03** | How frequently are accuracy audits conducted? What is the sample size? | Configuration Analyst, CMDB Administrator | Assess audit frequency | L1: Never / L3: Quarterly, 5-10% sample / L5: Continuous, 100% verification |
| **MEAS-Q04** | What is the CI completeness rate (% of mandatory attributes populated)? | Configuration Analyst, CMDB Administrator | Measure data completeness | L1: Unknown / L3: 70-80% / L5: >90% |
| **MEAS-Q05** | How many CIs have defined relationships vs. standalone CIs? What is the relationship coverage? | Configuration Manager, Configuration Analyst | Assess relationship maturity | L1: <20% / L3: 50-70% / L5: >90% |
| **MEAS-Q06** | What is the average time to register a new CI in the CMDB? | Configuration Analyst, Configuration Manager | Measure process efficiency | L1: >1 week / L3: 1-2 days / L5: <1 hour (auto) |
| **MEAS-Q07** | How many unauthorized CIs (discovered but not in CMDB) exist? | Configuration Manager, Security Manager | Identify shadow IT | L1: Unknown / L3: <10% / L5: <2% with auto-remediation |
| **MEAS-Q08** | What is the CI update frequency (last modified date distribution)? | Configuration Analyst, CMDB Administrator | Assess data freshness | L1: Unknown / L3: 60% <90 days / L5: 90% <30 days |
| **MEAS-Q09** | How is CM performance reported to management? How often? | Configuration Manager, IT Director | Evaluate reporting maturity | L1: No reports / L3: Quarterly slides / L5: Real-time dashboard |
| **MEAS-Q10** | What reports or dashboards are available for CMDB users? Who accesses them? | Configuration Manager, IT Service Manager | Assess reporting accessibility | L1: None / L3: 3-5 static reports / L5: Self-service dashboards |
| **MEAS-Q11** | Are there defined targets for CM KPIs (e.g., CMDB accuracy >95%)? How are they set? | Configuration Manager, IT Director | Evaluate target-setting | L1: No targets / L3: Internal targets / L5: Industry-benchmarked targets |
| **MEAS-Q12** | How is the business value or ROI of Configuration Management measured? | IT Director, Configuration Manager | Assess value measurement | L1: Not measured / L3: Cost tracking / L5: Value realization (incident reduction) |
| **MEAS-Q13** | What trend analysis is performed on CM metrics (e.g., accuracy trend over 12 months)? | Configuration Manager, Configuration Analyst | Evaluate analytical maturity | L1: No trends / L3: Quarterly trends / L5: Predictive analytics |

### Measurement Maturity Indicators by Level

**Level 1 (Initial) - Score 1.0-1.9:**
- No KPIs or metrics defined for CM
- CMDB accuracy unknown
- No reporting or dashboards
- No targets or benchmarks
- No value measurement

**Level 2 (Developing) - Score 2.0-2.9:**
- 1-3 basic KPIs tracked manually (e.g., CI count)
- CMDB accuracy measured annually, <75%
- Ad-hoc reports created on request
- No defined targets
- Cost tracking only

**Level 3 (Defined) - Score 3.0-3.9:**
- 5-7 KPIs tracked regularly (accuracy, completeness, update time)
- CMDB accuracy measured quarterly, 75-85%
- Monthly CM reports to management
- Internal targets set for key metrics
- CI completeness tracked (70-80%)
- Basic trend analysis (quarter-over-quarter)

**Level 4 (Managed) - Score 4.0-4.9:**
- 8-10 KPIs tracked with automated collection
- CMDB accuracy measured monthly, 85-95%
- Real-time dashboards for CM team
- Quarterly scorecards to executive management
- Industry-benchmarked targets
- CI completeness >80%
- Relationship coverage tracked (70-80%)
- Advanced trend analysis with root cause investigation

**Level 5 (Optimizing) - Score 5.0:**
- Comprehensive CM scorecard with 10+ KPIs
- CMDB accuracy measured continuously, >95%
- Real-time interactive dashboards for all stakeholders
- Automated anomaly detection and alerting
- Industry-leading targets with continuous improvement
- CI completeness >90%
- Relationship coverage >90%
- Predictive analytics and forecasting
- Value realization measurement (incident reduction, change success)
- ROI tracking for CM investments

### Key Performance Indicators (KPIs) - Target Benchmarks

| KPI | Description | Target (Level 3) | Target (Level 5) |
|-----|-------------|------------------|------------------|
| **CMDB Accuracy** | % of CIs with correct attributes | 80-85% | >95% |
| **CI Completeness** | % of mandatory attributes populated | 75-80% | >90% |
| **Relationship Coverage** | % of CIs with at least one relationship | 60-70% | >90% |
| **Unauthorized CI Rate** | % of discovered CIs not in CMDB | <15% | <2% |
| **CI Registration Time** | Avg time to add new CI to CMDB | <2 days | <1 hour |
| **Data Freshness** | % of CIs updated in last 90 days | 60-70% | >85% |
| **Audit Frequency** | Frequency of CMDB audits | Quarterly | Continuous |
| **CI Ownership** | % of CIs with assigned owner | 70-80% | >95% |
| **Auto-Discovery Rate** | % of CIs added via auto-discovery | 20-40% | >70% |
| **Change-CI Linkage** | % of changes linked to CIs | 60-75% | >95% |

---

## Dimension 5: People

### Overview
Assessment of skills, competencies, training, roles, and organizational capacity for Configuration Management.

### Assessment Criteria

| Criterion ID | Criterion | Weight | Maturity Indicators |
|--------------|-----------|--------|---------------------|
| **PPL-01** | CM Team Structure & Size | High | L1: No team / L3: 1-2 FTE / L5: Specialized team |
| **PPL-02** | Skills & Competencies | High | L1: No CM skills / L3: Basic ITIL / L5: ITIL Expert + certifications |
| **PPL-03** | Training & Development | Medium | L1: No training / L3: Annual training / L5: Continuous learning |
| **PPL-04** | Role Clarity & RACI | Medium | L1: Unclear / L3: Documented RACI / L5: Tool-enforced roles |
| **PPL-05** | CI Owner Engagement | High | L1: No owners / L3: Assigned owners / L5: Active ownership culture |
| **PPL-06** | Knowledge Management | Medium | L1: Tribal knowledge / L3: Documentation / L5: Knowledge base |
| **PPL-07** | Organizational Change Readiness | Low | L1: Resistant / L3: Neutral / L5: Change champions |
| **PPL-08** | Succession Planning | Low | L1: Single person / L3: Documentation / L5: Redundancy + cross-training |

### Interview Questions

| Question ID | Question | Target Interviewee | Purpose | Maturity Evidence |
|-------------|----------|-------------------|---------|-------------------|
| **PPL-Q01** | How many FTEs are dedicated to Configuration Management? What are their roles? | IT Director, Configuration Manager | Assess team size and structure | L1: 0 FTE / L3: 1-2 FTE / L5: 3+ FTE with specialization |
| **PPL-Q02** | What ITIL or CM certifications do team members hold? | Configuration Manager, HR/Learning | Evaluate skill level | L1: No certifications / L3: ITIL Foundation / L5: ITIL Expert, CMDB certifications |
| **PPL-Q03** | What training has the CM team received in the last 12 months? | Configuration Manager, Configuration Analyst | Assess continuous learning | L1: No training / L3: 1-2 courses / L5: Quarterly training + conferences |
| **PPL-Q04** | How are CM responsibilities distributed across the team? Is there a RACI matrix? | Configuration Manager, IT Service Manager | Evaluate role clarity | L1: No RACI / L3: Documented RACI / L5: RACI in tool with workflow |
| **PPL-Q05** | How are CI owners identified and engaged? What are their responsibilities? | Configuration Manager, Configuration Analyst | Assess ownership model | L1: No owners / L3: Owners assigned, unclear duties / L5: Active owners with SLA |
| **PPL-Q06** | What is the CI owner response rate for data quality reviews (e.g., quarterly validation requests)? | Configuration Analyst, Configuration Manager | Measure owner engagement | L1: <30% / L3: 50-70% / L5: >90% |
| **PPL-Q07** | Where is CM knowledge documented (procedures, runbooks, FAQs)? | Configuration Manager, Knowledge Manager | Evaluate knowledge management | L1: Tribal knowledge / L3: Shared drives / L5: Knowledge base with search |
| **PPL-Q08** | How are new team members onboarded to CM processes? How long does it take? | Configuration Manager, Configuration Analyst | Assess onboarding maturity | L1: No process, >1 month / L3: Checklist, 2-3 weeks / L5: Structured program, <1 week |
| **PPL-Q09** | What is the level of CM awareness across IT teams (DevOps, Infra, Security, Support)? | IT Service Manager, DevOps Manager | Evaluate organizational awareness | L1: Low / L3: Medium (aware of CMDB) / L5: High (active participants) |
| **PPL-Q10** | How does the organization handle single points of failure (e.g., only one person knows CMDB admin)? | IT Director, Configuration Manager | Assess succession risk | L1: High risk / L3: Documentation / L5: Cross-training + redundancy |
| **PPL-Q11** | Is there a CM champion or advocate in each IT team/department? | Configuration Manager, IT Service Manager | Evaluate change network | L1: No / L3: Informal / L5: Formal champion network |
| **PPL-Q12** | How receptive is the organization to CM process changes or improvements? | IT Director, Configuration Manager | Assess change readiness | L1: Resistant / L3: Neutral / L5: Proactive improvement culture |

### People Maturity Indicators by Level

**Level 1 (Initial) - Score 1.0-1.9:**
- No dedicated CM resources (0 FTE)
- No CM training or certifications
- Tribal knowledge, no documentation
- No CI owners or unclear responsibilities
- Low organizational awareness of CM
- Single points of failure

**Level 2 (Developing) - Score 2.0-2.9:**
- Part-time CM resources (<1 FTE)
- Basic ITIL awareness, no formal training
- Ad-hoc documentation
- CI owners assigned but not engaged
- Limited CM awareness outside IT Ops
- Documentation exists but not maintained

**Level 3 (Defined) - Score 3.0-3.9:**
- 1-2 dedicated CM resources
- ITIL Foundation certification (at least 1 team member)
- Annual CM training
- Documented RACI matrix
- CI owners assigned with defined responsibilities
- CM procedures documented and accessible
- Structured onboarding process (2-3 weeks)
- Medium organizational awareness

**Level 4 (Managed) - Score 4.0-4.9:**
- 2-3 dedicated CM resources with specialization
- ITIL Intermediate/Practitioner certifications
- Quarterly training and skill development
- RACI enforced through workflows
- Active CI owner engagement (70-80% response rate)
- Knowledge base with search and FAQs
- Rapid onboarding (<1 week)
- CM champions in key IT teams
- Cross-training and succession planning

**Level 5 (Optimizing) - Score 5.0:**
- 3+ dedicated CM resources with deep specialization
- ITIL Expert and vendor certifications (ServiceNow, BMC)
- Continuous learning culture (quarterly training, conferences)
- Dynamic role-based access with automated workflows
- Highly engaged CI owners (>90% response, proactive updates)
- Comprehensive knowledge management with AI-powered search
- Self-paced onboarding with e-learning (<1 week)
- Formal CM champion network across all departments
- Robust succession planning with 2+ backups for critical roles
- Proactive improvement culture with regular retrospectives

---

## Dimension 6: Improvement

### Overview
Assessment of continuous improvement practices, problem resolution, lessons learned, and innovation in Configuration Management.

### Assessment Criteria

| Criterion ID | Criterion | Weight | Maturity Indicators |
|--------------|-----------|--------|---------------------|
| **IMP-01** | Continuous Improvement Framework | Medium | L1: No framework / L3: Periodic review / L5: Kaizen culture |
| **IMP-02** | Problem & Root Cause Analysis | High | L1: No analysis / L3: Post-incident review / L5: Predictive analysis |
| **IMP-03** | Lessons Learned & Knowledge Capture | Medium | L1: No capture / L3: Documented / L5: Automated capture |
| **IMP-04** | CM Performance Review Frequency | Medium | L1: Never / L3: Quarterly / L5: Monthly with action plans |
| **IMP-05** | Innovation & Automation Initiatives | Medium | L1: None / L3: 1-2 per year / L5: Continuous automation |
| **IMP-06** | Stakeholder Feedback Collection | Low | L1: No feedback / L3: Annual survey / L5: Continuous feedback |
| **IMP-07** | Benchmarking & Best Practices | Low | L1: No benchmarking / L3: Ad-hoc / L5: Regular benchmarking |
| **IMP-08** | Action Tracking & Closure | Medium | L1: No tracking / L3: Manual tracking / L5: Automated workflow |

### Interview Questions

| Question ID | Question | Target Interviewee | Purpose | Maturity Evidence |
|-------------|----------|-------------------|---------|-------------------|
| **IMP-Q01** | Is there a formal continuous improvement process for Configuration Management? | Configuration Manager, IT Service Manager | Assess improvement framework | L1: No process / L3: Annual review / L5: Monthly improvement cycles |
| **IMP-Q02** | How frequently is CM performance reviewed? Who participates? | Configuration Manager, IT Director | Evaluate review frequency | L1: Never / L3: Quarterly / L5: Monthly with action plans |
| **IMP-Q03** | When CMDB inaccuracies are identified, how is root cause analysis performed? | Configuration Manager, Problem Manager | Assess problem-solving maturity | L1: No RCA / L3: Basic 5-Whys / L5: Formal RCA with preventive actions |
| **IMP-Q04** | Can you provide examples of CM improvements implemented in the last 12 months? | Configuration Manager, Configuration Analyst | Validate improvement activity | L1: None / L3: 2-3 improvements / L5: 5+ with metrics |
| **IMP-Q05** | How are lessons learned from CM issues captured and shared? | Configuration Manager, Knowledge Manager | Evaluate learning culture | L1: Not captured / L3: Meeting minutes / L5: Knowledge base with tags |
| **IMP-Q06** | What automation initiatives are underway or planned for CM? | Configuration Manager, DevOps Engineer | Assess innovation mindset | L1: None / L3: 1-2 initiatives / L5: Automation roadmap |
| **IMP-Q07** | How is stakeholder feedback on CM processes collected? | Configuration Manager, IT Service Manager | Evaluate feedback mechanism | L1: No feedback / L3: Annual survey / L5: Continuous feedback with NPS |
| **IMP-Q08** | Are CM metrics trended over time to identify improvement opportunities? | Configuration Manager, Configuration Analyst | Assess analytical maturity | L1: No trends / L3: Quarterly trends / L5: Predictive analytics |
| **IMP-Q09** | How does the CM team stay informed of industry best practices and trends? | Configuration Manager, IT Director | Evaluate external awareness | L1: No awareness / L3: Ad-hoc research / L5: Regular benchmarking, conferences |
| **IMP-Q10** | Are there formal action plans from CM performance reviews? How are they tracked? | Configuration Manager, IT Service Manager | Assess action tracking | L1: No actions / L3: Manual list / L5: Workflow-driven tracking |
| **IMP-Q11** | How quickly are identified CM issues remediated? What is the average closure time? | Configuration Analyst, Configuration Manager | Measure responsiveness | L1: >1 month / L3: 1-2 weeks / L5: <3 days with SLA |
| **IMP-Q12** | Is there a CM improvement backlog or roadmap? How is it prioritized? | Configuration Manager, IT Director | Evaluate planning maturity | L1: No roadmap / L3: Annual plan / L5: Agile backlog with prioritization |

### Improvement Maturity Indicators by Level

**Level 1 (Initial) - Score 1.0-1.9:**
- No continuous improvement framework
- CM performance never reviewed
- Issues not analyzed for root cause
- No lessons learned captured
- No automation or innovation initiatives
- No stakeholder feedback collected

**Level 2 (Developing) - Score 2.0-2.9:**
- Ad-hoc improvement discussions
- Annual or semi-annual CM review
- Basic issue investigation (no formal RCA)
- Lessons learned in meeting notes only
- 1 automation initiative per year
- Informal feedback from key users

**Level 3 (Defined) - Score 3.0-3.9:**
- Quarterly CM performance reviews
- Basic root cause analysis for major issues
- Lessons learned documented and shared
- 2-3 improvement initiatives per year with tracking
- Annual stakeholder survey
- CM metrics trended quarterly
- Action plans created but tracked manually
- Some benchmarking against industry standards

**Level 4 (Managed) - Score 4.0-4.9:**
- Monthly CM performance reviews with action plans
- Formal root cause analysis with preventive actions
- Knowledge base with lessons learned and best practices
- 4-6 improvement initiatives per year with metrics
- Bi-annual stakeholder feedback with NPS
- Monthly trend analysis with predictive insights
- Action tracking workflow with SLAs (<2 weeks closure)
- Regular benchmarking and best practice sharing
- Automation roadmap with quarterly milestones

**Level 5 (Optimizing) - Score 5.0:**
- Continuous improvement culture (Kaizen)
- Weekly CM standups with improvement focus
- Predictive analytics to prevent issues before occurrence
- Automated lessons learned capture from incidents/changes
- Continuous automation initiatives with business case
- Real-time stakeholder feedback mechanism
- Proactive trend analysis with AI-driven recommendations
- Automated action tracking with <3 day SLA
- Regular benchmarking against industry leaders
- Innovation lab for CM experimentation
- Quarterly improvement retrospectives with executive sponsorship

---

## Dimension 7: Integration

### Overview
Assessment of Configuration Management integration with other ITSM processes (Incident, Problem, Change, Release, Service Level Management).

### Assessment Criteria

| Criterion ID | Criterion | Weight | Maturity Indicators |
|--------------|-----------|--------|---------------------|
| **INT-01** | Integration with Incident Management | Critical | L1: No link / L3: Manual linkage / L5: Auto-populate |
| **INT-02** | Integration with Change Management | Critical | L1: No link / L3: CI mandatory / L5: Impact analysis |
| **INT-03** | Integration with Problem Management | High | L1: No link / L3: CI reference / L5: Trend analysis |
| **INT-04** | Integration with Release Management | High | L1: No link / L3: Release baseline / L5: Automated deployment tracking |
| **INT-05** | Integration with Service Level Management | Medium | L1: No link / L3: CI-to-service map / L5: SLA impact analysis |
| **INT-06** | Integration with Asset Management | High | L1: Separate systems / L3: Manual sync / L5: Unified platform |
| **INT-07** | Integration with Monitoring Tools | High | L1: No integration / L3: Alert CI matching / L5: Auto-discovery sync |
| **INT-08** | Integration with DevOps/CI-CD | Medium | L1: No integration / L3: Manual update / L5: Pipeline integration |

### Interview Questions

| Question ID | Question | Target Interviewee | Purpose | Maturity Evidence |
|-------------|----------|-------------------|---------|-------------------|
| **INT-Q01** | When an incident is logged, are affected CIs automatically identified and linked? | Service Desk Manager, Incident Manager | Assess incident-CM integration | L1: No link / L3: Manual selection / L5: Auto-suggested based on alert |
| **INT-Q02** | Can you demonstrate how to find all open incidents for a specific CI? | Service Desk Analyst, Incident Manager | Test query capability | L1: Cannot / L3: Manual query / L5: One-click CI dashboard |
| **INT-Q03** | Are CIs mandatory when submitting a change request? How is CI impact assessed? | Change Manager, Change Analyst | Evaluate change-CM integration | L1: Not required / L3: Mandatory CI field / L5: Automated impact analysis |
| **INT-Q04** | How does the Change Advisory Board use CMDB data for change approval decisions? | Change Manager, Configuration Manager | Assess governance integration | L1: Not used / L3: Manual CI review / L5: Real-time impact dashboard |
| **INT-Q05** | When a problem is identified, how are related CIs and historical incidents linked? | Problem Manager, Configuration Manager | Evaluate problem-CM integration | L1: No link / L3: Manual research / L5: Auto-populated correlation |
| **INT-Q06** | How are configuration baselines created and tracked for major releases? | Release Manager, Configuration Manager | Assess release-CM integration | L1: No baselines / L3: Manual snapshot / L5: Automated baseline with version control |
| **INT-Q07** | Can you show the CI dependency chain for a critical service (e.g., payment processing)? | Service Manager, Configuration Manager | Test service mapping | L1: Cannot show / L3: Manual diagram / L5: Dynamic service map |
| **INT-Q08** | How does SLA reporting use CMDB data (e.g., availability by service/CI)? | Service Level Manager, Configuration Manager | Evaluate SLM-CM integration | L1: No usage / L3: Manual correlation / L5: Automated SLA reports |
| **INT-Q09** | Is there a unified view of asset and configuration data, or are they managed separately? | Asset Manager, Configuration Manager | Assess asset-CM integration | L1: Separate systems / L3: Manual reconciliation / L5: Unified CMDB/AMDB |
| **INT-Q10** | How are monitoring alerts matched to CIs in the CMDB? | Monitoring Engineer, Configuration Manager | Evaluate monitoring integration | L1: No matching / L3: Manual lookup / L5: Auto-match with CI enrichment |
| **INT-Q11** | When monitoring discovers new infrastructure, is the CMDB automatically updated? | System Administrator, Configuration Manager | Assess discovery automation | L1: No / L3: Weekly batch update / L5: Real-time sync |
| **INT-Q12** | How are CI changes tracked when deployments occur via CI/CD pipelines? | DevOps Engineer, Configuration Manager | Evaluate DevOps integration | L1: Not tracked / L3: Manual post-deploy update / L5: Pipeline webhook to CMDB |
| **INT-Q13** | Can you demonstrate cross-process workflows (e.g., change → deployment → CMDB update → monitoring)? | IT Service Manager, Configuration Manager | Test end-to-end integration | L1: Cannot / L3: Manual handoffs / L5: Automated workflow |

### Integration Maturity Indicators by Level

**Level 1 (Initial) - Score 1.0-1.9:**
- No integration between CMDB and other ITSM processes
- CIs not linked to incidents, changes, or problems
- Separate asset and configuration management systems
- No integration with monitoring tools
- Manual processes with no automation

**Level 2 (Developing) - Score 2.0-2.9:**
- Basic CI linking in incidents and changes (optional)
- Manual CI selection with no validation
- Separate CMDB and asset management with ad-hoc reconciliation
- No monitoring integration
- CI data used occasionally in decision-making

**Level 3 (Defined) - Score 3.0-3.9:**
- CIs mandatory for changes, optional for incidents
- Manual CI impact analysis for changes
- CIs referenced in problem records
- Configuration baselines for major releases
- CI-to-service mapping documented
- Manual synchronization with asset management
- Basic monitoring alert CI matching (manual)
- Post-deployment CMDB updates (manual)

**Level 4 (Managed) - Score 4.0-4.9:**
- Automated CI suggestion for incidents based on alerts
- Automated change impact analysis using dependency map
- Problem trend analysis by CI
- Automated baseline creation integrated with release mgmt
- Dynamic service mapping with CI dependencies
- Weekly automated sync with asset management
- Monitoring alerts auto-matched to CIs (80%+ match rate)
- CI/CD pipeline webhooks for CMDB updates
- Cross-process dashboards with CMDB data

**Level 5 (Optimizing) - Score 5.0:**
- Real-time incident CI population from monitoring/alerting
- Predictive change impact analysis with ML-driven risk scoring
- Automated problem identification based on CI incident patterns
- Continuous baseline monitoring with drift detection
- Real-time service maps with health status
- Unified CMDB/AMDB platform with single source of truth
- 100% monitoring alert-to-CI matching with auto-enrichment
- Full CI/CD integration with automated CMDB updates
- End-to-end process automation across all ITSM domains
- Event-driven architecture with real-time data synchronization

### Integration Assessment Matrix

| ITSM Process | Integration Points | Maturity Level 3 | Maturity Level 5 |
|--------------|-------------------|------------------|------------------|
| **Incident Management** | CI linkage, impact assessment | Manual CI selection, 60% linking rate | Auto-suggested CI, 95%+ linking rate |
| **Change Management** | CI impact analysis, approval | Mandatory CI field, manual impact review | Automated dependency impact analysis |
| **Problem Management** | Related CIs, trend analysis | Manual CI research | Auto-correlated CIs with incident history |
| **Release Management** | Configuration baselines, deployment | Manual baseline snapshot | Automated baseline with version control |
| **Service Level Management** | CI-to-service mapping, SLA reporting | Manual service map | Dynamic service map with SLA dashboards |
| **Asset Management** | Asset-CI reconciliation | Monthly manual reconciliation | Unified CMDB/AMDB platform |
| **Monitoring** | Alert-CI matching, discovery sync | Weekly discovery batch update | Real-time discovery and alert enrichment |
| **DevOps/CI-CD** | Deployment tracking, CMDB updates | Manual post-deploy update | Pipeline webhook integration |

---

## Dimension 8: Compliance

### Overview
Assessment of audit readiness, regulatory compliance, control mapping, and evidence collection for Configuration Management.

### Assessment Criteria

| Criterion ID | Criterion | Weight | Maturity Indicators |
|--------------|-----------|--------|---------------------|
| **COMP-01** | Regulatory Requirement Mapping | Critical | L1: No mapping / L3: Documented mapping / L5: Continuous monitoring |
| **COMP-02** | Audit Evidence Collection | Critical | L1: Manual / L3: Documented procedure / L5: Automated evidence |
| **COMP-03** | Access Control & Segregation of Duties | Critical | L1: No controls / L3: RBAC / L5: ABAC with reviews |
| **COMP-04** | Change Audit Trail | Critical | L1: No trail / L3: Manual logging / L5: Immutable audit log |
| **COMP-05** | Data Retention & Archiving | High | L1: No policy / L3: Documented policy / L5: Automated archiving |
| **COMP-06** | Compliance Reporting | High | L1: Ad-hoc / L3: Quarterly / L5: Real-time dashboards |
| **COMP-07** | Third-Party Audit Readiness | High | L1: Not ready / L3: 80% ready / L5: Audit-ready 24/7 |
| **COMP-08** | Control Testing & Validation | Medium | L1: No testing / L3: Annual / L5: Continuous testing |

### Interview Questions

| Question ID | Question | Target Interviewee | Purpose | Maturity Evidence |
|-------------|----------|-------------------|---------|-------------------|
| **COMP-Q01** | Has Configuration Management been mapped to Vietnamese regulatory requirements (SBV Circular 41/2018, Decree 85/2019)? | Compliance Officer, Configuration Manager | Assess regulatory mapping | L1: No mapping / L3: Documented in policy / L5: Control matrix with evidence |
| **COMP-Q02** | What audit evidence is collected for CM (e.g., CMDB accuracy reports, access logs, change records)? | Configuration Manager, Internal Audit | Evaluate evidence collection | L1: Ad-hoc / L3: Quarterly reports / L5: Automated daily collection |
| **COMP-Q03** | How is CMDB access controlled? Is there segregation of duties (read vs. write vs. admin)? | Configuration Manager, Security Manager | Assess access control | L1: Shared account / L3: RBAC with 3 roles / L5: ABAC with quarterly reviews |
| **COMP-Q04** | Are all CMDB changes logged with timestamp, user, and reason? Can you demonstrate the audit trail? | CMDB Administrator, Configuration Manager | Test audit trail capability | L1: No logging / L3: Application logs / L5: Immutable audit log with SIEM |
| **COMP-Q05** | What is the data retention policy for CMDB records? How are retired CIs archived? | Configuration Manager, Compliance Officer | Assess data management | L1: No policy / L3: 3-year retention / L5: Automated archiving per regulation |
| **COMP-Q06** | How frequently is compliance status reported to management and regulators? | Compliance Officer, IT Director | Evaluate reporting frequency | L1: Never / L3: Quarterly / L5: Real-time compliance dashboard |
| **COMP-Q07** | Has CM undergone external audit (ISO 20000, SOC 2, SBV)? What were the findings? | IT Director, Internal Audit | Assess audit history | L1: Never audited / L3: 1-2 minor findings / L5: Clean audit |
| **COMP-Q08** | How prepared is the organization for an external CM audit with 2 weeks' notice? | Configuration Manager, Compliance Officer | Test audit readiness | L1: Not prepared / L3: 80% ready / L5: Audit-ready 24/7 |
| **COMP-Q09** | Are CM controls tested regularly (design + operating effectiveness)? | Internal Audit, Configuration Manager | Assess control testing | L1: No testing / L3: Annual testing / L5: Quarterly + continuous monitoring |
| **COMP-Q10** | How does CM support incident reporting requirements (e.g., SBV 12-24 hour incident notification)? | Configuration Manager, Security Manager | Evaluate incident support | L1: No support / L3: Manual CI lookup / L5: Auto-generated impact report |
| **COMP-Q11** | Are there documented procedures for producing compliance reports (e.g., asset inventory for regulator)? | Configuration Manager, Compliance Officer | Assess reporting procedures | L1: No procedure / L3: Manual process / L5: One-click report generation |
| **COMP-Q12** | How is CMDB data protected (encryption, backup, disaster recovery)? | Configuration Manager, Security Manager | Evaluate data protection | L1: No protection / L3: Database backup / L5: Encryption + DR tested |
| **COMP-Q13** | What evidence can you provide that CM supports PCI-DSS Requirement 2 (Do not use vendor-supplied defaults)? | Configuration Manager, Security Manager | Test specific compliance | L1: No evidence / L3: Manual verification / L5: Automated config validation |

### Compliance Maturity Indicators by Level

**Level 1 (Initial) - Score 1.0-1.9:**
- No mapping to regulatory requirements
- No audit evidence collection
- No access controls (shared accounts)
- No audit trail for CMDB changes
- No data retention policy
- No compliance reporting
- Not prepared for external audit

**Level 2 (Developing) - Score 2.0-2.9:**
- Basic awareness of regulatory requirements
- Ad-hoc audit evidence collection
- Basic access control (single login per user)
- Application-level change logs
- Informal data retention (no enforcement)
- Annual compliance reporting
- <50% prepared for external audit

**Level 3 (Defined) - Score 3.0-3.9:**
- Documented mapping to SBV Circular 41/2018 and Decree 85/2019
- Quarterly audit evidence collection and archiving
- Role-based access control with 3+ roles
- Comprehensive audit trail for all CMDB changes
- Documented data retention policy (3+ years)
- Quarterly compliance reporting to management
- 70-85% prepared for external audit
- Annual control testing (design)

**Level 4 (Managed) - Score 4.0-4.9:**
- Control matrix mapping CM to all applicable regulations
- Automated monthly audit evidence collection
- Advanced RBAC with segregation of duties
- Audit trail integrated with SIEM
- Automated data retention enforcement
- Monthly compliance dashboards
- 85-95% prepared for external audit
- Quarterly control testing (design + operating effectiveness)
- Clean findings from recent audits

**Level 5 (Optimizing) - Score 5.0:**
- Continuous compliance monitoring with automated controls
- Real-time audit evidence collection and retention
- Attribute-based access control with quarterly reviews
- Immutable audit log with blockchain/WORM storage
- Fully automated archiving per regulatory requirements
- Real-time compliance dashboards with predictive alerts
- 100% audit-ready with evidence repository
- Continuous control testing with automated validation
- Zero material findings from external audits
- Automated compliance reports for regulators (one-click)

### Vietnamese Fintech Regulatory Mapping

| Regulation | Requirement | CM Control | Evidence Required |
|------------|-------------|-----------|-------------------|
| **SBV Circular 41/2018** | Article 9: Asset Management | CMDB with asset lifecycle tracking | Asset inventory report, CMDB accuracy audit |
| **SBV Circular 41/2018** | Article 11: Access Control | Role-based CMDB access | Access control matrix, quarterly access reviews |
| **SBV Circular 41/2018** | Article 13: Incident Response | CI-to-service mapping for impact | Incident reports with CI linkage, service maps |
| **SBV Circular 41/2018** | Article 18: Audit Trails | CMDB change audit logs | Audit log reports, change history |
| **Decree 85/2019** | Article 26: System Documentation | CI documentation and relationships | CMDB export, service documentation |
| **Decree 85/2019** | Article 28: Data Retention | CMDB data retention 2+ years | Data retention policy, archived CI records |
| **ISO/IEC 20000-1** | 8.1: Configuration Management | Full CMDB with CIs, relationships, baselines | ISO 20000 audit evidence, CMDB reports |
| **ISO/IEC 27001** | A.8: Asset Management | CMDB integrated with asset management | Asset register, CMDB-AMDB reconciliation |
| **PCI-DSS** | Requirement 2: Config Standards | CI configuration validation | Config compliance reports, hardening evidence |
| **PCI-DSS** | Requirement 11: Network Inventory | Network CI tracking | Network device inventory, quarterly scans |
| **SOC 2** | CC6.1: Logical Access Controls | CMDB access control and audit | Access logs, quarterly reviews, RBAC matrix |
| **SOC 2** | CC7.2: System Monitoring | Monitoring-CMDB integration | Alert-CI matching reports, discovery logs |

### Audit Evidence Checklist

| Evidence Type | Description | Frequency | Responsible Role |
|---------------|-------------|-----------|------------------|
| **CMDB Accuracy Report** | CI sample audit with accuracy % | Quarterly | Configuration Analyst |
| **CI Inventory by Type** | Count of CIs by type/status | Monthly | Configuration Manager |
| **Access Control Matrix** | RACI for CMDB access levels | Annual (or on change) | Configuration Manager |
| **Access Review Log** | Quarterly access recertification | Quarterly | Security Manager |
| **Audit Trail Report** | Sample of CMDB change logs | Monthly | CMDB Administrator |
| **Relationship Coverage Report** | % of CIs with relationships | Monthly | Configuration Analyst |
| **CI Owner Assignment Report** | % of CIs with assigned owners | Monthly | Configuration Manager |
| **Data Retention Evidence** | Archived CI records >2 years old | Annual | Configuration Manager |
| **Integration Testing Results** | Change-CI, Incident-CI linkage tests | Quarterly | IT Service Manager |
| **Compliance Mapping Document** | CM controls to regulations | Annual review | Compliance Officer |
| **CCB Meeting Minutes** | Configuration Control Board decisions | Per meeting | Configuration Manager |
| **Training Attendance Records** | CM training completion | Per training | HR/Learning |

---

## Scoring Methodology

### Overall Maturity Score Calculation

**Step 1: Score Each Criterion (0-5 scale)**

For each of the 64 criteria across 8 dimensions, assess maturity level:
- **0**: Non-existent - No evidence of capability
- **1**: Initial - Ad-hoc, reactive, inconsistent
- **2**: Developing - Basic capability, manual processes
- **3**: Defined - Standardized, documented, trained
- **4**: Managed - Metrics-driven, integrated, automated
- **5**: Optimizing - Continuous improvement, predictive, industry-leading

**Step 2: Calculate Dimension Scores**

For each dimension, calculate weighted average:

```
Dimension Score = Σ (Criterion Score × Criterion Weight) / Σ Criterion Weights
```

**Step 3: Calculate Overall CM Maturity Score**

```
Overall CM Maturity = Σ (Dimension Score × Dimension Weight) / 100%

Where Dimension Weights are:
- Governance: 15%
- Process: 20%
- Tool & Data: 20%
- Measurement: 10%
- People: 10%
- Improvement: 10%
- Integration: 10%
- Compliance: 15%
```

### Maturity Level Interpretation

| Overall Score | Maturity Level | Risk Level | Interpretation |
|---------------|----------------|------------|----------------|
| **0.0-1.4** | Non-existent to Initial | Critical Risk | No formal CM capability; critical regulatory and operational risks |
| **1.5-2.4** | Initial to Developing | High Risk | Ad-hoc CM practices; significant gaps; not audit-ready |
| **2.5-3.4** | Developing to Defined | Medium Risk | Basic CM capability; documented processes; some automation; audit preparation needed |
| **3.5-4.2** | Defined to Managed | Low-Medium Risk | Strong CM capability; metrics-driven; automated; audit-ready |
| **4.3-5.0** | Managed to Optimizing | Low Risk | Industry-leading CM; continuous improvement; predictive analytics |

### Fintech Industry Benchmarks

| Organization Stage | Typical Maturity | CMDB Accuracy | Target Maturity | Investment Required |
|--------------------|------------------|---------------|-----------------|---------------------|
| **Early Stage (<2 years, <50 staff)** | 1.0-2.0 | 50-70% | 2.5-3.0 | $30K-$80K |
| **Growth Stage (2-5 years, 50-200 staff)** | 2.0-3.0 | 70-80% | 3.0-3.5 | $80K-$200K |
| **Scale Stage (5-10 years, 200-500 staff)** | 2.5-3.5 | 75-85% | 3.5-4.0 | $150K-$400K |
| **Mature (>10 years, >500 staff)** | 3.0-4.0 | 80-90% | 4.0-4.5 | $200K-$600K |

**Note**: Investment includes ITSM tools, discovery tools, implementation services, and training over 12-18 months.

### Critical Success Factors for Fintech

Regardless of maturity score, fintech organizations must achieve **minimum thresholds**:

| Critical Factor | Minimum Threshold | Rationale |
|-----------------|-------------------|-----------|
| **CMDB Accuracy** | ≥85% | Regulatory requirement, incident response effectiveness |
| **CI-Change Linkage** | ≥90% | Change management control, audit evidence |
| **Access Control** | Role-based with quarterly reviews | Security compliance, SOD |
| **Audit Trail** | 100% of CMDB changes logged | Regulatory requirement, forensics |
| **Compliance Mapping** | Documented for all regulations | Audit readiness, regulatory reporting |
| **Data Retention** | ≥2 years (per Decree 85/2019) | Legal requirement |

If any critical factor is below threshold, **overall risk level cannot be lower than "Medium Risk"** regardless of maturity score.

---

## Interview Guide & Schedule

### Interview Approach

**Recommended Interview Structure:**
- **Duration**: 45-90 minutes per interview
- **Format**: Semi-structured with open-ended questions
- **Participants**: 1-3 interviewees per session (avoid large groups)
- **Evidence**: Request supporting documentation, screenshots, reports
- **Validation**: Cross-reference responses across multiple interviewees

### Suggested Interview Schedule (10-Day Assessment)

| Day | Time | Session | Participants | Focus Dimensions |
|-----|------|---------|--------------|------------------|
| **Day 1** | 09:00-10:30 | Executive Kickoff | CIO, CTO, IT Director | All dimensions (overview) |
| **Day 1** | 11:00-12:30 | CM Leadership | Configuration Manager, IT Service Manager | Governance, Process, People |
| **Day 1** | 14:00-15:30 | Tool & Data Deep Dive | CMDB Administrator, Configuration Analyst | Tool & Data, Measurement |
| **Day 2** | 09:00-10:30 | Process Walkthrough | Configuration Analyst, System Administrator | Process, Integration |
| **Day 2** | 11:00-12:30 | Integration Focus | Change Manager, Incident Manager | Integration, Process |
| **Day 2** | 14:00-16:00 | CMDB Demo & Analysis | Configuration Analyst, CMDB Administrator | Tool & Data (hands-on) |
| **Day 3** | 09:00-10:30 | Compliance & Audit | Compliance Officer, Internal Audit | Compliance, Governance |
| **Day 3** | 11:00-12:30 | DevOps & Automation | DevOps Engineer, Cloud Engineer | Integration, Improvement |
| **Day 3** | 14:00-15:30 | Improvement & Measurement | Configuration Manager, IT Service Manager | Improvement, Measurement |
| **Day 4** | 09:00-10:30 | Frontline Operations | Service Desk Team, Configuration Analyst | All dimensions (operational view) |
| **Day 4** | 11:00-12:30 | Security & Access Control | Security Manager, CMDB Administrator | Compliance, Governance |
| **Day 4** | 14:00-16:00 | Document Review | (Independent work) | All dimensions |
| **Day 5** | 09:00-12:00 | Data Analysis & Validation | Configuration Manager (validation) | All dimensions |
| **Day 5** | 14:00-17:00 | Gap Analysis Workshop | CM Team, IT Service Manager | All dimensions |
| **Days 6-8** | - | Analysis & Report Writing | (Assessor independent work) | - |
| **Day 9** | 09:00-10:30 | Findings Validation | Configuration Manager, IT Director | All dimensions |
| **Day 9** | 14:00-16:00 | Roadmap Workshop | CM Team, IT Leadership | All dimensions |
| **Day 10** | 09:00-11:00 | Executive Presentation | CIO, CTO, Leadership Team | All dimensions (summary) |
| **Day 10** | 11:00-12:00 | Q&A & Next Steps | All stakeholders | - |

### Interviewee Role Summary

| Role | Sessions | Key Questions | Why Critical |
|------|----------|---------------|--------------|
| **CIO/CTO** | 2 | GOV-Q08, GOV-Q10, COMP-Q07 | Strategic alignment, investment, executive sponsorship |
| **IT Director** | 3 | GOV-Q02, PPL-Q01, IMP-Q12 | Governance, resource allocation, improvement oversight |
| **Configuration Manager** | 8 | All dimensions (primary stakeholder) | Process ownership, performance, roadmap |
| **Configuration Analyst** | 6 | PROC (all), TOOL (all), MEAS (most) | Operational details, data quality, day-to-day execution |
| **CMDB Administrator** | 4 | TOOL (all), COMP-Q04 | Technical platform, data model, security |
| **IT Service Manager** | 4 | GOV-Q09, INT (all), IMP-Q02 | Process integration, service mapping, improvement |
| **Change Manager** | 2 | INT-Q03, INT-Q04, GOV-Q05 | Change-CM integration, impact analysis |
| **Incident Manager** | 1 | INT-Q01, INT-Q02 | Incident-CM integration, operational usage |
| **Problem Manager** | 1 | INT-Q05, IMP-Q03 | Problem-CM integration, root cause analysis |
| **Release Manager** | 1 | INT-Q06, PROC-Q07 | Release baseline management |
| **Service Manager** | 1 | INT-Q07, INT-Q08 | Service mapping, SLA integration |
| **Compliance Officer** | 2 | COMP-Q01, COMP-Q05, COMP-Q11 | Regulatory mapping, audit evidence |
| **Internal Audit** | 1 | COMP-Q02, COMP-Q09 | Control testing, audit findings |
| **Security Manager** | 2 | GOV-Q06, COMP-Q03, COMP-Q12 | Access control, security integration |
| **DevOps Engineer** | 1 | INT-Q12, IMP-Q06 | CI/CD integration, automation |
| **Cloud Engineer** | 1 | TOOL-Q12 | Cloud discovery, multi-cloud support |
| **System Administrator** | 1 | PROC-Q02, TOOL-Q06 | Infrastructure management, discovery tools |
| **Service Desk Team** | 1 | INT-Q01, operational usage | End-user perspective, practical usage |

---

## Appendix: Quick Reference

### Top 10 Quick Win Recommendations (by Maturity Level)

**For Level 1-2 Organizations (Initial to Developing):**
1. Implement basic ITSM tool with CMDB module (Jira Service Management, Freshservice)
2. Define CI types and naming conventions
3. Populate CMDB with critical infrastructure (top 50-100 CIs)
4. Assign CI owners for all critical CIs
5. Establish monthly CM review meetings
6. Document CM policy and procedures (10-15 pages)
7. Make CIs mandatory for change requests
8. Conduct first CMDB accuracy audit (sample-based)
9. Integrate monitoring alerts with CMDB (manual matching)
10. Create compliance mapping document for SBV Circular 41/2018

**For Level 2-3 Organizations (Developing to Defined):**
1. Implement automated discovery for infrastructure (weekly scans)
2. Establish CI relationship mapping for critical services
3. Achieve 80% CMDB accuracy through quarterly audits
4. Integrate CMDB with Change Management (mandatory CI, basic impact analysis)
5. Create configuration baselines for major releases
6. Implement role-based access control for CMDB
7. Establish Configuration Control Board (CCB) with monthly meetings
8. Train team on ITIL Configuration Management (Foundation level)
9. Set up basic CM dashboards (CI count, accuracy, ownership)
10. Collect audit evidence for compliance (quarterly reports)

**For Level 3-4 Organizations (Defined to Managed):**
1. Implement real-time auto-discovery for cloud and on-prem
2. Achieve 90% CMDB accuracy through continuous verification
3. Automate change impact analysis using dependency maps
4. Integrate CI/CD pipelines with CMDB (webhook updates)
5. Implement service mapping with full dependency chains
6. Set up real-time CM dashboards with KPI tracking
7. Establish predictive analytics for CM (incident trends by CI)
8. Achieve SOC 2 or ISO 20000 certification readiness
9. Implement continuous compliance monitoring
10. Build CM center of excellence with specialized roles

### Common Pitfalls to Avoid

1. **Boiling the Ocean**: Don't try to populate CMDB with all assets on day one. Start with critical CIs.
2. **Spreadsheet Trap**: Don't use Excel as CMDB for >100 CIs. Invest in proper tooling.
3. **Set-and-Forget**: Don't assume CMDB accuracy will maintain itself. Continuous verification required.
4. **No Ownership**: Don't leave CIs without owners. Data quality depends on accountability.
5. **Tool Over Process**: Don't buy expensive tools without defined processes. Process first, tool second.
6. **Isolated CMDB**: Don't manage CMDB in isolation. Integration with ITSM processes is critical.
7. **No Executive Sponsorship**: Don't start CM initiative without executive buy-in. Requires investment and change.
8. **Ignoring Compliance**: Don't overlook regulatory requirements. Fintech = highly regulated industry.
9. **Manual Forever**: Don't rely on manual processes indefinitely. Automate to scale.
10. **No Continuous Improvement**: Don't treat CM as "done." It's a continuous journey.

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2025-10-30 | ITSM Audit Specialist | Initial framework creation |

---

**End of Configuration Management Performance Assessment Framework**

For questions or support, contact your ITSM assessment team.
