# Learning, redesign and returning users

**Double FW Ltd · Draft 1.0 · 5 November 2026**

**Scope:** M-05, M-06. **Principles:** CP-01, CP-02, CP-06, CP-07, CP-10.

## User need and design purpose

Reuse familiar skills, recover competence after absence and adapt safely when a service changes, without compulsory memorisation or repeated onboarding.

This guide supplies practical design patterns and evaluations. Its recommendations are not quotations from legislation or a guarantee of WCAG/EAA conformity. All worked scenarios are fictitious; no user evaluations have been executed. Confirm applicability, risk and acceptance criteria for the product before treating a recommendation as a project requirement.

## Scientific basis and boundaries

Neuroscience distinguishes declarative and nondeclarative learning/memory; learning experiments examine benefits of retrieval practice in educational tasks. Neither establishes a particular migration design. Retrieval practice belongs to genuine learning, not an obligation to memorise ordinary service navigation.

See [E5](Cognitive_Science_Evidence_Register.md#e5), [E8](Cognitive_Science_Evidence_Register.md#e8) in the shared evidence register. The research-to-UX application remains a hypothesis to validate; no clinical memory assessment, brain scan or universal capacity threshold is proposed.

## Design approaches

### Inventory learned contracts

Before change, list labels, locations, keyboard behaviour, shortcuts, sequence and consequences people may have learned. Identify harmful old actions on the proposed design.

### Preserve useful continuity

Retain stable terminology and interaction contracts when feasible. Explain meaningful changes at the relevant task rather than forcing a tour of all new features.

### Offer safe practice

Provide optional reversible exploration, repeatable instructions and help. A returning user can skip explanations or return to them later.

### Evaluate after delay

Test first use, repeated use and a task-relevant return interval. Include infrequent customers and actual returning users; distinguish learning from selection and novelty effects.

## Worked task and state record

A repeat booking service changes its final step. The old primary action saved a draft; the new action pays immediately. The team avoids reusing an indistinguishable “Continue” contract, preserves a separate save route and tests whether returning customers predict the changed consequence. At a later visit, current instructions remain available.

| Trigger/state | Information available to the customer | Interaction and screen-reader intent |
| --- | --- | --- |
| Before rollout | Explain a material task change where it matters | Preserve normal navigation; avoid unsolicited repeated tours. |
| During use | Distinct consequence and optional assistance | Retain keyboard and semantic patterns or document justified changes. |
| Return after absence | Current task context, choices and retrievable help | Do not assume the person remembers prior training. |
| Rollback | State compatibility and any consequences explained | Prevent silent data loss or replay of completed actions. |

The table is an implementation-facing script of meaning, not an exact speech transcript. Specify actual names, roles, relationships and states in HTML; check browser/AT output. Support heading/control navigation and braille as well as sequential speech. Keep essential information available visually and programmatically.

## Implementation contract

| Contract field | Required decision |
| --- | --- |
| Change record | Old/new behaviour, reason, affected tasks and risk of an old action causing an unintended consequence. |
| Migration | Saved tasks/preferences, schema changes, fallback and rollback boundaries are explicit; preserve only appropriate data. |
| Onboarding | Entry, skip, replay, dismissal and help routes; never trap an experienced user in an introductory modal. |
| Compatibility | Keyboard/AT contracts and responsive states are tested across change. A familiar visual with a new action needs particular review. |
| Longitudinal design | Define interval, attrition handling, task variants, exposure history, compensation and participant data retention before recruitment. |

## Evaluation procedures

New `MEM-*` identifiers below are local supplementary outcome evaluations, not canonical QA test IDs. Existing CUX assertions are supporting checks and do not establish the whole outcome. **A** means bounded script/agent checks; **M** means expert/content/actual-AT review; **U** means intended-user evidence. Each evaluation requires the relevant combination, not an automatic whole-test pass.

### MEM-LR-01 — Transfer safely across redesign

**Pattern:** `COG-LR-01`. **Status:** Not tested. **Methods:** A + M + U.

**Applicability and preparation:** Apply when the described feature/context exists. Use a controlled fixture for failures, fictitious task data and an agreed outcome rubric. Include relevant vision/cognitive intersections and actual preferred modes without imposing diagnoses or withholding support.

**Procedure:** Recruit relevant new and returning users, record old-system exposure and use comparable tasks. Observe predictions, old-habit errors, help and outcomes on the revised design.

**Expected result:** Changes do not hide consequential new behaviour behind a misleading old contract. Customers can discover the current action and recover safely.

**Retain:** Old/new contract record, expectation and task traces, AT regression evidence; do not attribute all differences to memory.

**Boundaries:** An agent can exercise states and check saved values, relationships or events. A reviewer checks meaning and real AT behaviour; participants establish understanding and usable task outcomes. Record blocked/cannot-tell cases, environment and scope.

### MEM-LR-02 — Return and relearn after delay

**Pattern:** `COG-LR-02`. **Status:** Not tested. **Methods:** A + M + U.

**Applicability and preparation:** Apply when the described feature/context exists. Use a controlled fixture for failures, fictitious task data and an agreed outcome rubric. Include relevant vision/cognitive intersections and actual preferred modes without imposing diagnoses or withholding support.

**Procedure:** Agree a task-relevant interval and equivalent task variants. Invite participants back without forced revision, leave normal references available and report attrition.

**Expected result:** Customers can regain task competence through available cues/help; avoidable navigation memorisation is not required.

**Retain:** Retained/recovered competence, assistance, reorientation and satisfaction; analyse repeated measures and report missing follow-up.

**Boundaries:** An agent can exercise states and check saved values, relationships or events. A reviewer checks meaning and real AT behaviour; participants establish understanding and usable task outcomes. Record blocked/cannot-tell cases, environment and scope.

## Inclusive research and privacy

A short study cannot establish annual-task retention. Do not require real customers to practise payments or high-stakes commitments. Delayed-return data need purpose-specific consent/basis and retention decisions under the research plan.

Use the [research/data plan](Cognitive_Accessibility_User_Research_and_Data_Plan.md) for lawful processing, optional functional segmentation, accessible participation, compensation and safe stopping. Energy, stress and sight history are context, not proxies for legal capacity. Do not ask people to become fatigued, intoxicated or distressed; do not alter medication. Treat participant-linked support/context data under the approved sensitive-data assessment.

## Delivery, ownership and links

Design owns the task/interaction contract, content owns meaningful wording, engineering owns state/data integrity, QA owns reproducible checks, and research owns outcome interpretation. The product owner accepts scope and resolves remaining barriers. Named maintainers and independent review are pending.

Use the [delivery template](Cognitive_UX_Design_and_Evidence_Template.md) to record expected and actual results separately. Link evidence rather than copying identifiable participant records into public documentation. Report each applicable satisfaction domain separately alongside comprehension, action and recovery. A faster task or confident answer alone is not success.

Supporting QA assertions: CUX-01, CUX-02, CUX-03, CUX-22, CUX-24, CUX-25, CUX-33, CUX-36 in the [existing matrix](Cognitive_UX_Principles_QA_Evidence_Matrix.md). Full mappings, cross-repository sources and document status live in the [coverage register](Cognitive_UX_Coverage_and_Delivery_Map.md).
