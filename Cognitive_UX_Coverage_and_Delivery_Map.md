# Cognitive UX coverage and delivery map

**Double FW Ltd · Draft 1.0 · 5 November 2026**

This is the authoritative mapping register for the six extensions in this pack. It preserves CP-01–10, M-01–08 and E1–E9 from the source review. Existing CUX/CTL/MW/ACT IDs remain owned by their original documents. `COG-*` IDs identify new recommended design patterns; `MEM-*` identify supplementary evaluations. No ID here is a new statutory or canonical QA requirement.

## Status, ownership and interpretation

**Documentation:** all six guides and shared records are drafted and structurally checked in this package; independent subject-matter review and publication are pending. **Product delivery:** Not assessed; all MEM results are Not tested. Completing a document is not passing a product test. Named owners must be assigned by the maintainer; role ownership below is a handoff recommendation.

Supporting CUX links indicate relevant sub-behaviours, not complete test equivalence. Follow the existing QA matrix for exact source tests and applicability. Extend its principle/gap outcome evidence with MEM observations; do not replace an existing CUX result, change its identity or infer a WCAG mapping from similar language.

## Eight gap actions and document locations

| Gap | Document / operative section | Pattern and supplementary evaluations | Owner role / priority | Documentation / outcome |
| --- | --- | --- | --- | --- |
| M-01 | [Prospective memory and reliable memory aids](Prospective_Memory_and_Reliable_Memory_Aids.md) — implementation contract and evaluation procedures | COG-PM-01 / MEM-PM-01 | Design + engineering; named owner pending; P1 | Drafted / Not assessed |
| M-02 | [Interruption recovery and task continuity](Interruption_Recovery_and_Task_Continuity.md) — implementation contract and evaluation procedures | COG-RC-01 / MEM-RC-01, COG-RC-02 / MEM-RC-02 | Design + engineering; named owner pending; P1 | Drafted / Not assessed |
| M-03 | [Interference, source memory and current context](Interference_Source_Memory_and_Current_Context.md) — implementation contract and evaluation procedures | COG-CT-01 / MEM-CT-01, COG-CT-02 / MEM-CT-02 | Design + engineering; named owner pending; P1 | Drafted / Not assessed |
| M-04 | [Familiarity, comprehension and confidence](Familiarity_Comprehension_and_Confidence.md) — implementation contract and evaluation procedures | COG-CF-01 / MEM-CF-01, COG-CF-02 / MEM-CF-02 | Design + research; named owner pending; P1 | Drafted / Not assessed |
| M-05 | [Learning, redesign and returning users](Learning_Redesign_and_Returning_Users.md) — implementation contract and evaluation procedures | COG-LR-01 / MEM-LR-01 | Design + research; named owner pending; P1 | Drafted / Not assessed |
| M-06 | [Learning, redesign and returning users](Learning_Redesign_and_Returning_Users.md) — implementation contract and evaluation procedures | COG-LR-02 / MEM-LR-02 | Design + research; named owner pending; P2 | Drafted / Not assessed |
| M-07 | [Warnings, habituation and notification management](Warnings_Habituation_and_Notification_Management.md) — implementation contract and evaluation procedures | COG-NT-01 / MEM-NT-01, COG-NT-02 / MEM-NT-02 | Design + research; named owner pending; P1 | Drafted / Not assessed |
| M-08 | [Prospective memory and reliable memory aids](Prospective_Memory_and_Reliable_Memory_Aids.md) — implementation contract and evaluation procedures | COG-PM-02 / MEM-PM-02 | Design + engineering; named owner pending; P2 | Drafted / Not assessed |

## Pattern-to-principle-to-evidence mapping

| Pattern / gap | Principles | Guide / observable design outcome | Existing supporting QA | New evaluation / science |
| --- | --- | --- | --- | --- |
| COG-PM-01; M-01 | CP-07, CP-09, CP-10 | [Create, find and act on a cue](Prospective_Memory_and_Reliable_Memory_Aids.md) — The intended action and relevant context can be found and performed; preferences are respected. No success claim is based only on dispatch. | CUX-22, CUX-23, CUX-24, CUX-25, CUX-31, CUX-32, CUX-33 (partial support) | MEM-PM-01; E2 |
| COG-PM-02; M-08 | CP-07, CP-09, CP-10 | [Survive memory-aid failure and deletion](Prospective_Memory_and_Reliable_Memory_Aids.md) — The system reports actual state, avoids duplicate/obsolete cues, protects account boundaries and honours the specified deletion/retention contract. | CUX-22, CUX-23, CUX-24, CUX-25, CUX-31, CUX-32, CUX-33 (partial support) | MEM-PM-02; E2 |
| COG-RC-01; M-02 | CP-03, CP-06, CP-07, CP-09, CP-10 | [Resume a paused task](Interruption_Recovery_and_Task_Continuity.md) — Valid answers survive; the customer can identify the task and next action and resume without moderator reconstruction. | CUX-12, CUX-23, CUX-24, CUX-29, CUX-33 (partial support) | MEM-RC-01; E3, E7 |
| COG-RC-02; M-02 | CP-03, CP-06, CP-07, CP-09, CP-10 | [Recover stale or expired state](Interruption_Recovery_and_Task_Continuity.md) — No silent overwrite, cross-account disclosure or false restore success. Explain loss/changes and provide a safe next action while retaining still-valid work. | CUX-12, CUX-23, CUX-24, CUX-29, CUX-33 (partial support) | MEM-RC-02; E3, E7 |
| COG-CT-01; M-03 | CP-02, CP-03, CP-04, CP-07, CP-09 | [Distinguish similar current contexts](Interference_Source_Memory_and_Current_Context.md) — The current entity and consequence can be distinguished without recalling a hidden previous screen. Wrong carryover is detectable and correctable. | CUX-05, CUX-06, CUX-11, CUX-12, CUX-13, CUX-21, CUX-24, CUX-29 (partial support) | MEM-CT-01; E4 |
| COG-CT-02; M-03 | CP-02, CP-03, CP-04, CP-07, CP-09 | [Detect stale or superseded information](Interference_Source_Memory_and_Current_Context.md) — History and current state are distinguishable; material changes are exposed before commitment and the action uses the reviewed version. | CUX-05, CUX-06, CUX-11, CUX-12, CUX-13, CUX-21, CUX-24, CUX-29 (partial support) | MEM-CT-02; E4 |
| COG-CF-01; M-04 | CP-02, CP-04, CP-07, CP-10 | [Compare expectation and consequence](Familiarity_Comprehension_and_Confidence.md) — Intended users can access and explain material consequences or obtain useful clarification before deciding. Correct cancellation is a valid outcome. | CUX-04, CUX-11, CUX-12, CUX-13, CUX-25, CUX-35 (partial support) | MEM-CF-01; E2, E4 |
| COG-CF-02; M-04 | CP-02, CP-04, CP-07, CP-10 | [Verify and correct a result](Familiarity_Comprehension_and_Confidence.md) — People can distinguish outcome states and access an appropriate correction/support path. Reassuring wording never masks uncertainty. | CUX-04, CUX-11, CUX-12, CUX-13, CUX-25, CUX-35 (partial support) | MEM-CF-02; E2, E4 |
| COG-LR-01; M-05 | CP-01, CP-02, CP-06, CP-07, CP-10 | [Transfer safely across redesign](Learning_Redesign_and_Returning_Users.md) — Changes do not hide consequential new behaviour behind a misleading old contract. Customers can discover the current action and recover safely. | CUX-01, CUX-02, CUX-03, CUX-22, CUX-24, CUX-25, CUX-33, CUX-36 (partial support) | MEM-LR-01; E5, E8 |
| COG-LR-02; M-06 | CP-01, CP-02, CP-06, CP-07, CP-10 | [Return and relearn after delay](Learning_Redesign_and_Returning_Users.md) — Customers can regain task competence through available cues/help; avoidable navigation memorisation is not required. | CUX-01, CUX-02, CUX-03, CUX-22, CUX-24, CUX-25, CUX-33, CUX-36 (partial support) | MEM-LR-02; E5, E8 |
| COG-NT-01; M-07 | CP-05, CP-08, CP-09, CP-10 | [Manage competing channels and messages](Warnings_Habituation_and_Notification_Management.md) — Priority/order follow the policy; messages remain perceivable/retrievable without duplicate forced output or routine focus theft. | CUX-26, CUX-27, CUX-28, CUX-29, CUX-30, CUX-31, CUX-32 (partial support) | MEM-NT-01; E6, E7 |
| COG-NT-02; M-07 | CP-05, CP-08, CP-09, CP-10 | [Evaluate repeated exposure and meaningful change](Warnings_Habituation_and_Notification_Management.md) — Intended users can identify and act on material changes without undue disruption; failure and uncertainty remain visible rather than replaced by a novelty claim. | CUX-26, CUX-27, CUX-28, CUX-29, CUX-30, CUX-31, CUX-32 (partial support) | MEM-NT-02; E6, E7 |

## All ten principles: reverse map

| Principle | Guides / patterns | Existing QA range |
| --- | --- | --- |
| CP-01 — Standard Elements | [LR](Learning_Redesign_and_Returning_Users.md) (COG-LR-01/02) | CUX-01–03 in existing matrix |
| CP-02 — Affordances and Signifiers | [CT](Interference_Source_Memory_and_Current_Context.md) (COG-CT-01/02); [CF](Familiarity_Comprehension_and_Confidence.md) (COG-CF-01/02); [LR](Learning_Redesign_and_Returning_Users.md) (COG-LR-01/02) | CUX-04–06 in existing matrix |
| CP-03 — Simplicity | [RC](Interruption_Recovery_and_Task_Continuity.md) (COG-RC-01/02); [CT](Interference_Source_Memory_and_Current_Context.md) (COG-CT-01/02) | CUX-07–09 in existing matrix |
| CP-04 — Clear Communication | [CT](Interference_Source_Memory_and_Current_Context.md) (COG-CT-01/02); [CF](Familiarity_Comprehension_and_Confidence.md) (COG-CF-01/02) | CUX-10–13 in existing matrix |
| CP-05 — Redundancies | [NT](Warnings_Habituation_and_Notification_Management.md) (COG-NT-01/02) | CUX-14–17 in existing matrix |
| CP-06 — Patterns | [RC](Interruption_Recovery_and_Task_Continuity.md) (COG-RC-01/02); [LR](Learning_Redesign_and_Returning_Users.md) (COG-LR-01/02) | CUX-18–21 in existing matrix |
| CP-07 — Recognition Rather than Recall | [PM](Prospective_Memory_and_Reliable_Memory_Aids.md) (COG-PM-01/02); [RC](Interruption_Recovery_and_Task_Continuity.md) (COG-RC-01/02); [CT](Interference_Source_Memory_and_Current_Context.md) (COG-CT-01/02); [CF](Familiarity_Comprehension_and_Confidence.md) (COG-CF-01/02); [LR](Learning_Redesign_and_Returning_Users.md) (COG-LR-01/02) | CUX-22–25 in existing matrix |
| CP-08 — Variable Stimuli and the Pop-Out Effect | [NT](Warnings_Habituation_and_Notification_Management.md) (COG-NT-01/02) | CUX-26–28 in existing matrix |
| CP-09 — Feedback and Notification | [PM](Prospective_Memory_and_Reliable_Memory_Aids.md) (COG-PM-01/02); [RC](Interruption_Recovery_and_Task_Continuity.md) (COG-RC-01/02); [CT](Interference_Source_Memory_and_Current_Context.md) (COG-CT-01/02); [NT](Warnings_Habituation_and_Notification_Management.md) (COG-NT-01/02) | CUX-29–32 in existing matrix |
| CP-10 — User Control and Choice | [PM](Prospective_Memory_and_Reliable_Memory_Aids.md) (COG-PM-01/02); [RC](Interruption_Recovery_and_Task_Continuity.md) (COG-RC-01/02); [CF](Familiarity_Comprehension_and_Confidence.md) (COG-CF-01/02); [LR](Learning_Redesign_and_Returning_Users.md) (COG-LR-01/02); [NT](Warnings_Habituation_and_Notification_Management.md) (COG-NT-01/02) | CUX-33–36 in existing matrix |

## Supporting documentation by guide

| Guide | Relevant existing Double FW documents | Relation |
| --- | --- | --- |
| [PM](Prospective_Memory_and_Reliable_Memory_Aids.md) | D2, D4, D5, D12 | Supporting methods/context; not evidence that the new outcome has been evaluated |
| [RC](Interruption_Recovery_and_Task_Continuity.md) | D2, D4, D5, D7, D10, D11 | Supporting methods/context; not evidence that the new outcome has been evaluated |
| [CT](Interference_Source_Memory_and_Current_Context.md) | D2, D5, D7, D11 | Supporting methods/context; not evidence that the new outcome has been evaluated |
| [CF](Familiarity_Comprehension_and_Confidence.md) | D2, D4, D5, D8, D9 | Supporting methods/context; not evidence that the new outcome has been evaluated |
| [LR](Learning_Redesign_and_Returning_Users.md) | D1, D6, D10, D12 | Supporting methods/context; not evidence that the new outcome has been evaluated |
| [NT](Warnings_Habituation_and_Notification_Management.md) | D1, D3, D4, D5, D6, D7 | Supporting methods/context; not evidence that the new outcome has been evaluated |

## Existing-source register

D1–D12 retain the source review’s local meanings. Specialised sources remain the owners of their technical/domain-specific content. Re-read the current target section before implementing or changing a project requirement.

| ID | Inspected Double FW documentation | Relevant existing coverage |
| --- | --- | --- |
| D1 | [Cognitive Design Principles](Cognitive%20Design%20Principles.md) | Ten-principle foundation |
| D2 | [Vision, Memory and Cognitive Screen Reader UX](Vision_Memory_and_Cognitive_Screen_Reader_UX.md) | Memory demands, semantic structure, script/state records, comparisons and interruption/recovery |
| D3 | [Cognitive QA Evidence Matrix](Cognitive_UX_Principles_QA_Evidence_Matrix.md) | Existing QA links, 36 assertions and G-01–G-06 outcome gaps |
| D4 | [User Research and Data Plan](Cognitive_Accessibility_User_Research_and_Data_Plan.md) | Qualitative research, five satisfaction domains, variable contexts, trauma-informed methods and data governance |
| D5 | [Inclusive Chatbot Interface Reference](https://github.com/Double-FW/Accessible-Chatbots/blob/main/Inclusive_Chatbot_Interface_Reference.md) and [Testing Brief](https://github.com/Double-FW/Accessible-Chatbots/blob/main/Accessible_Chatbot_Testing_Brief.md) | Transcript navigation, controlled announcements, streaming, drafts, expiry and recovery |
| D6 | [Accessible Games and Other Dynamic Content](https://github.com/Double-FW/Inclusive-Games-Design/blob/main/Accessible%20Games%20and%20other%20Dynamic%20Content.md) | Practice modes, repeatable instructions, pacing, remapping, motion and dynamic feedback |
| D7 | [Charts, Maps and Complex Graphics](https://github.com/Double-FW/Accessible_Charts_Graphs_and_Maps/blob/main/Inclusive_Design_Charts_Maps_and_Complex_Graphics.md) | Layers, explicit relationships, comparison, shared state, persistent details and recovery |
| D8 | [Accessible Typography for UX and Brand Systems](https://github.com/Double-FW/Accessible-Typography-for-UX-and-Brand-Systems/blob/main/Accessible_Typography_for_UX_and_Brand_Systems.md) | Legibility, readability, comprehension and preference distinguished; contextual evaluation |
| D9 | [POUR through emotional brand/CX outcomes](https://github.com/Double-FW/POUR-for-Branding-Systems-and-CX/blob/main/The%20WCAG%20POUR%20principles%20reframed%20through%20emotional%20outcomes%20for%20branding%20systems.md) | Clarity, confidence, dignity and trust as experience outcomes |
| D10 | [Task Analysis Methodology](https://github.com/Double-FW/Task-Analysis-for-Comparative-Accessibility-Evaluation-of-Internal-Systems/blob/main/TA%20Methodology.md) | Goals, subtask structure, frequency, complexity and comparative cognitive burden |
| D11 | [Canonical QA Test Library](https://github.com/Double-FW/QA_Accessibility_Testing/blob/main/Canonical%20Test%20Library.md) | Structure, labels, errors, input retention, dynamic states, controls and timing; technical results do not establish all cognitive outcomes |
| D12 | [Ethical and Inclusive Data Use](https://github.com/Double-FW/Data_Ethics_and_Disability/blob/main/Ethical%20and%20Inclusive%20Use%20of%20Data%20Relating%20to%20Disabled%20People.md) and [Customer Research Framework](https://github.com/Double-FW/Data_Ethics_and_Disability/blob/main/CUSTOMER%20RESEARCH%20FRAMEWORK.md) | Usability versus learnability, customer context, evidence groups, sensitive data and comparable experience |


## Project delivery record

Copy the [delivery template](Cognitive_UX_Design_and_Evidence_Template.md) for each scoped task/pattern. Record named owner, task/build, feature applicability, supported device/AT/modes, acceptance rubric, source revisions, implementation status, MEM/CUX results, evidence links, unresolved barriers, review and retest. The public register must not contain participant identities or row-level research data.

Allowed execution results: Pass, Fail, Not tested, Blocked, Cannot tell, Not applicable with reason, Tool error. Principle judgements remain Supported in tested scope, Partially supported, Not supported or Insufficient evidence, with human review. No average pass percentage represents cognitive delivery.

## Maintenance and publication actions

1. Maintainer appoints named design/content/engineering/research/QA owners and reviews the original-to-revised principle changes in the changelog.
2. Review new guides and evidence transfer limits. Resolve contradictions in the owning document, then update every dependent reference.
3. Keep CUX assertions at their original IDs. Add MEM results as supplementary evidence and retain the original QA source revisions.
4. Publish the reviewed files together so local links resolve. Record actual commit/release and dates; do not mark these drafts published in advance.
5. On changes to principles, paper conclusions, component behaviour or data policy, identify affected mappings and repeat proportionate review/testing.
6. Reassess the eight documentation actions against the published content. User-outcome gaps remain open until a real product has suitable evidence.
