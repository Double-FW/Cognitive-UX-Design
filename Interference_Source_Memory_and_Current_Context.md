# Interference, source memory and current context

**Double FW Ltd · Draft 1.0 · 5 November 2026**

**Scope:** M-03. **Principles:** CP-02, CP-03, CP-04, CP-07, CP-09.

## User need and design purpose

Distinguish the current recipient, account, selection or answer from a similar earlier one, without trusting familiarity as proof of correctness.

This guide supplies practical design patterns and evaluations. Its recommendations are not quotations from legislation or a guarantee of WCAG/EAA conformity. All worked scenarios are fictitious; no user evaluations have been executed. Confirm applicability, risk and acceptance criteria for the product before treating a recommendation as a project requirement.

## Scientific basis and boundaries

Interference experiments study competition from earlier information; recognition experiments distinguish remembering an item from its associations. Findings support investigating analogous confusion, not predicting a customer error rate or diagnosing memory ability.

See [E4](Cognitive_Science_Evidence_Register.md#e4) in the shared evidence register. The research-to-UX application remains a hypothesis to validate; no clinical memory assessment, brain scan or universal capacity threshold is proposed.

## Design approaches

### Expose the binding

Keep a value attached to the entity and task it belongs to: recipient/account, price/currency, address/purpose or answer/source. Do not require comparison across isolated pages.

### Mark meaningful changes

Show which selected values changed, when relevant and why. A regenerated answer should not silently replace earlier guidance while preserving an apparently unchanged confirmation.

### Review before consequence

Provide a clear current summary with specific change actions. Include the consequence of confirmation and a safe cancellation/undo route where appropriate.

### Use provenance selectively

Dates, source and version help when they distinguish validity; avoid appending long technical IDs to every spoken label. Important current context must also be visually available.

## Worked task and state record

A customer has two recipients with similar names. The review shows the intended name and a meaningful distinguishing detail, available visually and through the control/reading routes. An old saved recipient is not preselected merely because it was used last time. If the destination changes after review, the service requests a fresh review.

| Trigger/state | Information available to the customer | Interaction and screen-reader intent |
| --- | --- | --- |
| Select | Specific entity and its distinguishing context | Choice state available without a long hidden-only name. |
| Refresh | Explain a meaningful changed price or recipient detail | Do not steal focus for incidental updates; retain the current comparison. |
| Review | Current values, destination and consequence together | Provide direct, descriptive change actions. |
| Version mismatch | Details changed since review; identify affected values | Prevent unintended commitment and provide a new review. |

The table is an implementation-facing script of meaning, not an exact speech transcript. Specify actual names, roles, relationships and states in HTML; check browser/AT output. Support heading/control navigation and braille as well as sequential speech. Keep essential information available visually and programmatically.

## Implementation contract

| Contract field | Required decision |
| --- | --- |
| Entity and scope | Canonical entity ID plus a meaningful user-facing label; separate billing/delivery or personal/business contexts explicitly. |
| Freshness | Valid-at time/version, invalidation triggers and refresh behaviour are defined; do not imply a cached value is current. |
| History | Retain or disclose relevant changes according to an approved policy. Clearly distinguish history from the current committed state. |
| AI outputs | Identify draft, regenerated, verified and superseded content; do not let fluent familiarity stand in for provenance. |
| Commit | Bind submitted action to the reviewed current version. Detect relevant changes between review and commit and require a comprehensible re-review. |

## Evaluation procedures

New `MEM-*` identifiers below are local supplementary outcome evaluations, not canonical QA test IDs. Existing CUX assertions are supporting checks and do not establish the whole outcome. **A** means bounded script/agent checks; **M** means expert/content/actual-AT review; **U** means intended-user evidence. Each evaluation requires the relevant combination, not an automatic whole-test pass.

### MEM-CT-01 — Distinguish similar current contexts

**Pattern:** `COG-CT-01`. **Status:** Not tested. **Methods:** A + M + U.

**Applicability and preparation:** Apply when the described feature/context exists. Use a controlled fixture for failures, fictitious task data and an agreed outcome rubric. Include relevant vision/cognitive intersections and actual preferred modes without imposing diagnoses or withholding support.

**Procedure:** Prepare two similar fictitious recipients/accounts or repeated orders. Change context and ask the participant to verify the intended current action using available information.

**Expected result:** The current entity and consequence can be distinguished without recalling a hidden previous screen. Wrong carryover is detectable and correctable.

**Retain:** Observed selection, confidence/understanding and carryover errors; no clinical interpretation.

**Boundaries:** An agent can exercise states and check saved values, relationships or events. A reviewer checks meaning and real AT behaviour; participants establish understanding and usable task outcomes. Record blocked/cannot-tell cases, environment and scope.

### MEM-CT-02 — Detect stale or superseded information

**Pattern:** `COG-CT-02`. **Status:** Not tested. **Methods:** A + M + U.

**Applicability and preparation:** Apply when the described feature/context exists. Use a controlled fixture for failures, fictitious task data and an agreed outcome rubric. Include relevant vision/cognitive intersections and actual preferred modes without imposing diagnoses or withholding support.

**Procedure:** In fixtures change a material value after review, regenerate an answer, and reopen an old result. Attempt commitment from stale state.

**Expected result:** History and current state are distinguishable; material changes are exposed before commitment and the action uses the reviewed version.

**Retain:** Data/version trace, review and update output, human judgement of meaningful change; AT navigation where relevant.

**Boundaries:** An agent can exercise states and check saved values, relationships or events. A reviewer checks meaning and real AT behaviour; participants establish understanding and usable task outcomes. Record blocked/cannot-tell cases, environment and scope.

## Inclusive research and privacy

Do not reveal excessive private details to distinguish accounts or recipients. Use the minimum effective context and test masked values. A timestamp is not proof of accuracy, and source labels do not prove a source is trustworthy.

Use the [research/data plan](Cognitive_Accessibility_User_Research_and_Data_Plan.md) for lawful processing, optional functional segmentation, accessible participation, compensation and safe stopping. Energy, stress and sight history are context, not proxies for legal capacity. Do not ask people to become fatigued, intoxicated or distressed; do not alter medication. Treat participant-linked support/context data under the approved sensitive-data assessment.

## Delivery, ownership and links

Design owns the task/interaction contract, content owns meaningful wording, engineering owns state/data integrity, QA owns reproducible checks, and research owns outcome interpretation. The product owner accepts scope and resolves remaining barriers. Named maintainers and independent review are pending.

Use the [delivery template](Cognitive_UX_Design_and_Evidence_Template.md) to record expected and actual results separately. Link evidence rather than copying identifiable participant records into public documentation. Report each applicable satisfaction domain separately alongside comprehension, action and recovery. A faster task or confident answer alone is not success.

Supporting QA assertions: CUX-05, CUX-06, CUX-11, CUX-12, CUX-13, CUX-21, CUX-24, CUX-29 in the [existing matrix](Cognitive_UX_Principles_QA_Evidence_Matrix.md). Full mappings, cross-repository sources and document status live in the [coverage register](Cognitive_UX_Coverage_and_Delivery_Map.md).
