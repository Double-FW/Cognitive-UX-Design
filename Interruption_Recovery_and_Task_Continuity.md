# Interruption recovery and task continuity

**Double FW Ltd · Draft 1.0 · 5 November 2026**

**Scope:** M-02. **Principles:** CP-03, CP-06, CP-07, CP-09, CP-10.

## User need and design purpose

Recover the goal, current context and next action after a pause, interruption, reauthentication or handoff without reconstructing the whole journey.

This guide supplies practical design patterns and evaluations. Its recommendations are not quotations from legislation or a guarantee of WCAG/EAA conformity. All worked scenarios are fictitious; no user evaluations have been executed. Confirm applicability, risk and acceptance criteria for the product before treating a recommendation as a project requirement.

## Scientific basis and boundaries

Interrupted-task experiments concern goal preparation and resumption; event-segmentation research concerns organisation of experience. A change of webpage is not automatically a neural event boundary, and these studies do not establish a universal restoration target.

See [E3](Cognitive_Science_Evidence_Register.md#e3), [E7](Cognitive_Science_Evidence_Register.md#e7) in the shared evidence register. The research-to-UX application remains a hypothesis to validate; no clinical memory assessment, brain scan or universal capacity threshold is proposed.

## Design approaches

### Save meaningful progress

Persist completed answers and the current step where justified. Distinguish unsaved typing, locally stored draft and server-confirmed state.

### Orient before asking

On return, expose the task, completed work, remaining action and significant changes. Make a concise summary available instead of forcing the whole journey to be heard again.

### Restore predictably

Choose a useful location based on whether this is a small in-page update, a route transition or full navigation. Preserve reading position where possible; do not steal focus for background saves.

### Reconcile rather than overwrite

If another device or agent changed the task, explain which state is current and ask only for the decision necessary to resolve the conflict. Preserve a recoverable copy where safe.

## Worked task and state record

A person pauses an application at the address step. On return after authentication, the service presents “Continue your application” with saved answers and “Next: check your address.” A previously selected appointment is no longer available, so it is marked as needing a new choice rather than silently substituted.

| Trigger/state | Information available to the customer | Interaction and screen-reader intent |
| --- | --- | --- |
| Pause/save | Progress saved; distinguish any unsaved work | No routine focus movement; one appropriate save acknowledgement. |
| Reauthenticate | Explain why sign-in is needed and which progress is retained | Return to a coherent task context after successful authentication. |
| Resume changed data | Saved answers plus the changed appointment condition | Orient at a meaningful heading; provide direct correction. |
| Handoff | Summary of what will be shared; retain route back | Support explicit consent/permission where applicable under the research/service policy. |

The table is an implementation-facing script of meaning, not an exact speech transcript. Specify actual names, roles, relationships and states in HTML; check browser/AT output. Support heading/control navigation and braille as well as sequential speech. Keep essential information available visually and programmatically.

## Implementation contract

| Contract field | Required decision |
| --- | --- |
| Continuity record | Task/account identity, step, completed values, save acknowledgement, schema/version, timestamp and required next action. |
| Restore policy | Define focus target, reading context, expanded state and selected values for each transition; DOM focus does not equal a screen-reader reading cursor. |
| Expiry | Specify what expires and why, what survives and how to recover. Security limits must not be concealed behind a generic timeout message. |
| Handoff | Carry only authorised task context into a human/agent channel; show what is shared and avoid requiring repeated sensitive disclosure. |
| Conflict | Version changes, stale tabs, concurrent writes and invalidated choices have explicit reconciliation and rollback behaviour. |

## Evaluation procedures

New `MEM-*` identifiers below are local supplementary outcome evaluations, not canonical QA test IDs. Existing CUX assertions are supporting checks and do not establish the whole outcome. **A** means bounded script/agent checks; **M** means expert/content/actual-AT review; **U** means intended-user evidence. Each evaluation requires the relevant combination, not an automatic whole-test pass.

### MEM-RC-01 — Resume a paused task

**Pattern:** `COG-RC-01`. **Status:** Not tested. **Methods:** A + M + U.

**Applicability and preparation:** Apply when the described feature/context exists. Use a controlled fixture for failures, fictitious task data and an agreed outcome rubric. Include relevant vision/cognitive intersections and actual preferred modes without imposing diagnoses or withholding support.

**Procedure:** Complete several meaningful steps, pause voluntarily, then return using in-service navigation and a supported alternate device. Include reauthentication. Ask the person to continue using all available summaries.

**Expected result:** Valid answers survive; the customer can identify the task and next action and resume without moderator reconstruction.

**Retain:** Restored state, meaningful navigation/focus trace, assistance and comprehension; measure resumption time alongside understanding.

**Boundaries:** An agent can exercise states and check saved values, relationships or events. A reviewer checks meaning and real AT behaviour; participants establish understanding and usable task outcomes. Record blocked/cannot-tell cases, environment and scope.

### MEM-RC-02 — Recover stale or expired state

**Pattern:** `COG-RC-02`. **Status:** Not tested. **Methods:** A + M + U.

**Applicability and preparation:** Apply when the described feature/context exists. Use a controlled fixture for failures, fictitious task data and an agreed outcome rubric. Include relevant vision/cognitive intersections and actual preferred modes without imposing diagnoses or withholding support.

**Procedure:** Use fixtures for expired authentication, removed options, concurrent updates, interrupted network and schema change. Attempt safe restoration and cancellation.

**Expected result:** No silent overwrite, cross-account disclosure or false restore success. Explain loss/changes and provide a safe next action while retaining still-valid work.

**Retain:** Version/save logs, conflict outputs and manual AT traces; record unsupported handoffs as limitations.

**Boundaries:** An agent can exercise states and check saved values, relationships or events. A reviewer checks meaning and real AT behaviour; participants establish understanding and usable task outcomes. Record blocked/cannot-tell cases, environment and scope.

## Inclusive research and privacy

Save/resume is not permission to retain everything indefinitely. Shared devices, sensitive answers and emergency contexts can require a different persistence policy. Do not induce stress or interrupt participants unexpectedly for realism.

Use the [research/data plan](Cognitive_Accessibility_User_Research_and_Data_Plan.md) for lawful processing, optional functional segmentation, accessible participation, compensation and safe stopping. Energy, stress and sight history are context, not proxies for legal capacity. Do not ask people to become fatigued, intoxicated or distressed; do not alter medication. Treat participant-linked support/context data under the approved sensitive-data assessment.

## Delivery, ownership and links

Design owns the task/interaction contract, content owns meaningful wording, engineering owns state/data integrity, QA owns reproducible checks, and research owns outcome interpretation. The product owner accepts scope and resolves remaining barriers. Named maintainers and independent review are pending.

Use the [delivery template](Cognitive_UX_Design_and_Evidence_Template.md) to record expected and actual results separately. Link evidence rather than copying identifiable participant records into public documentation. Report each applicable satisfaction domain separately alongside comprehension, action and recovery. A faster task or confident answer alone is not success.

Supporting QA assertions: CUX-12, CUX-23, CUX-24, CUX-29, CUX-33 in the [existing matrix](Cognitive_UX_Principles_QA_Evidence_Matrix.md). Full mappings, cross-repository sources and document status live in the [coverage register](Cognitive_UX_Coverage_and_Delivery_Map.md).
