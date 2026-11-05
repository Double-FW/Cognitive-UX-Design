# Prospective memory and reliable memory aids

**Double FW Ltd · Draft 1.0 · 5 November 2026**

**Scope:** M-01, M-08. **Principles:** CP-07, CP-09, CP-10.

## User need and design purpose

Remember an intended future action without having to keep rehearsing it, and trust the aid enough to use it safely.

This guide supplies practical design patterns and evaluations. Its recommendations are not quotations from legislation or a guarantee of WCAG/EAA conformity. All worked scenarios are fictitious; no user evaluations have been executed. Confirm applicability, risk and acceptance criteria for the product before treating a recommendation as a project requirement.

## Scientific basis and boundaries

Prospective-memory and offloading experiments examine delayed intentions, external cues, effort and confidence; neural work examines storage of delayed intentions. These findings motivate support for future actions, but do not prescribe reminder frequency or prove that a product reminder will be noticed or acted upon.

See [E2](Cognitive_Science_Evidence_Register.md#e2) in the shared evidence register. The research-to-UX application remains a hypothesis to validate; no clinical memory assessment, brain scan or universal capacity threshold is proposed.

## Design approaches

### Create a useful cue

Attach the reminder to an understandable goal and a genuine event or time. Offer a clear default with editable timing and delivery route. Do not make a person configure a complex reminder engine to save one task.

### Keep the action available

Provide a stable in-service saved-task route as well as any external reminder. Keep the goal, next action and meaningful deadline together; distinguish an advisory reminder from a real expiry.

### Make the dependency honest

Explain whether saving succeeded and what is retained. A message being queued or delivered is not the same as the user seeing it or completing the task.

### Give control

Allow edit, snooze, cancel and deletion through accessible controls. Avoid pressure, repeated marketing reminders or requiring disability disclosure to unlock the aid.

## Worked task and state record

A customer saves an unfinished collection booking. The service says “Booking saved. Next: choose a collection time,” offers a reminder tomorrow and keeps a “Saved bookings” route. If reminder delivery fails, the saved booking is still available. A generic notification says “You have a saved task” rather than exposing the collection contents.

| Trigger/state | Information available to the customer | Interaction and screen-reader intent |
| --- | --- | --- |
| Save | Booking saved; next action and expiry available | Keep focus on the initiating action or move only as documented; expose one concise result. |
| Delivery failure | Reminder could not be sent; booking is still saved | Provide a retry/alternative and do not imply task loss. |
| Resume | Saved booking; current details; choose a collection time | Use the recovery guide to verify context before restoring. |
| Complete/delete | Booking completed or removed; obsolete reminder cancelled | Preserve a suitable outcome record; explain limits of external copies. |

The table is an implementation-facing script of meaning, not an exact speech transcript. Specify actual names, roles, relationships and states in HTML; check browser/AT output. Support heading/control navigation and braille as well as sequential speech. Keep essential information available visually and programmatically.

## Implementation contract

| Contract field | Required decision |
| --- | --- |
| Identity | Stable task ID, account/context binding and reminder ID; never put private identifiers in a lock-screen message. |
| State | Draft → saved → reminder scheduled → delivered/failed → resumed → completed/cancelled/expired. Completion cancels obsolete cues. |
| Timing | Time zone, daylight-saving handling, event trigger, real expiry and retry policy are explicit; deduplicate retries. |
| Reliability | Confirm durable save separately from reminder scheduling. Handle offline and failed sync without false success. |
| Access and deletion | Define retention, shared-device visibility, authentication, deletion propagation and what an external calendar copy can retain. |

## Evaluation procedures

New `MEM-*` identifiers below are local supplementary outcome evaluations, not canonical QA test IDs. Existing CUX assertions are supporting checks and do not establish the whole outcome. **A** means bounded script/agent checks; **M** means expert/content/actual-AT review; **U** means intended-user evidence. Each evaluation requires the relevant combination, not an automatic whole-test pass.

### MEM-PM-01 — Create, find and act on a cue

**Pattern:** `COG-PM-01`. **Status:** Not tested. **Methods:** A + M + U.

**Applicability and preparation:** Apply when the described feature/context exists. Use a controlled fixture for failures, fictitious task data and an agreed outcome rubric. Include relevant vision/cognitive intersections and actual preferred modes without imposing diagnoses or withholding support.

**Procedure:** Use a fictitious task with a genuine deferred next step. Create a reminder through each supported route; revisit it after an agreed delay and locate the saved task without the reminder. Include a skipped reminder and a changed deadline.

**Expected result:** The intended action and relevant context can be found and performed; preferences are respected. No success claim is based only on dispatch.

**Retain:** Task/action trace, setup effort, comprehension and outcome; record failures, non-response and completion separately.

**Boundaries:** An agent can exercise states and check saved values, relationships or events. A reviewer checks meaning and real AT behaviour; participants establish understanding and usable task outcomes. Record blocked/cannot-tell cases, environment and scope.

### MEM-PM-02 — Survive memory-aid failure and deletion

**Pattern:** `COG-PM-02`. **Status:** Not tested. **Methods:** A + M + U.

**Applicability and preparation:** Apply when the described feature/context exists. Use a controlled fixture for failures, fictitious task data and an agreed outcome rubric. Include relevant vision/cognitive intersections and actual preferred modes without imposing diagnoses or withholding support.

**Procedure:** In fixtures, fail durable save, scheduling and delivery separately; retry a queued event, change account, complete the task elsewhere and delete it.

**Expected result:** The system reports actual state, avoids duplicate/obsolete cues, protects account boundaries and honours the specified deletion/retention contract.

**Retain:** State/event logs and accessible outputs; human review of wording and privacy; participant evaluation of recovery in safe scenarios.

**Boundaries:** An agent can exercise states and check saved values, relationships or events. A reviewer checks meaning and real AT behaviour; participants establish understanding and usable task outcomes. Record blocked/cannot-tell cases, environment and scope.

## Inclusive research and privacy

External calendars, email and operating systems may retain copies or suppress delivery. Specify the boundary and provide a retrievable in-service route. Do not promise recall, delivery or deletion beyond what the integration can establish.

Use the [research/data plan](Cognitive_Accessibility_User_Research_and_Data_Plan.md) for lawful processing, optional functional segmentation, accessible participation, compensation and safe stopping. Energy, stress and sight history are context, not proxies for legal capacity. Do not ask people to become fatigued, intoxicated or distressed; do not alter medication. Treat participant-linked support/context data under the approved sensitive-data assessment.

## Delivery, ownership and links

Design owns the task/interaction contract, content owns meaningful wording, engineering owns state/data integrity, QA owns reproducible checks, and research owns outcome interpretation. The product owner accepts scope and resolves remaining barriers. Named maintainers and independent review are pending.

Use the [delivery template](Cognitive_UX_Design_and_Evidence_Template.md) to record expected and actual results separately. Link evidence rather than copying identifiable participant records into public documentation. Report each applicable satisfaction domain separately alongside comprehension, action and recovery. A faster task or confident answer alone is not success.

Supporting QA assertions: CUX-22, CUX-23, CUX-24, CUX-25, CUX-31, CUX-32, CUX-33 in the [existing matrix](Cognitive_UX_Principles_QA_Evidence_Matrix.md). Full mappings, cross-repository sources and document status live in the [coverage register](Cognitive_UX_Coverage_and_Delivery_Map.md).
