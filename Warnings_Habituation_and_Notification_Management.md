# Warnings, habituation and notification management

**Double FW Ltd · Draft 1.0 · 5 November 2026**

**Scope:** M-07. **Principles:** CP-05, CP-08, CP-09, CP-10.

## User need and design purpose

Notice a meaningful consequential change, understand its action and return to the ongoing task without being overwhelmed by repetitive or competing messages.

This guide supplies practical design patterns and evaluations. Its recommendations are not quotations from legislation or a guarantee of WCAG/EAA conformity. All worked scenarios are fictitious; no user evaluations have been executed. Confirm applicability, risk and acceptance criteria for the product before treating a recommendation as a project requirement.

## Scientific basis and boundaries

Repeated computer-warning images have shown neural/behavioural habituation. This does not directly establish spoken-alert outcomes or justify random novelty. Interruption research motivates preserving the active goal while prioritising genuinely important feedback.

See [E6](Cognitive_Science_Evidence_Register.md#e6), [E7](Cognitive_Science_Evidence_Register.md#e7) in the shared evidence register. The research-to-UX application remains a hypothesis to validate; no clinical memory assessment, brain scan or universal capacity threshold is proposed.

## Design approaches

### Inventory before adding

Classify each message by consequence, action, urgency, source and expiry. Remove avoidable repeat messages and fix recurrent errors rather than making warnings ever louder.

### Separate priority from modality

Choose whether to interrupt based on urgency, not a channel preference. Offer equivalent perceivable routes and user-controlled channels where supported; do not force simultaneous sound, speech and vibration.

### Keep stable meaning

Preserve predictable control locations, labels and priority cues. A changed consequence needs distinguishing content, not an arbitrary new colour or animation.

### Retain and recover

Store actionable information where it can be revisited. Coalesce routine updates, deduplicate events and restore context after justified interruptions.

## Worked task and state record

A customer reading a comparison receives routine stock refreshes and then a change to the selected item’s collection availability. Routine updates are coalesced without stealing focus. The changed selection gets a clear, retrievable message and correction route. The customer can revisit it without replaying all stock notifications.

| Trigger/state | Information available to the customer | Interaction and screen-reader intent |
| --- | --- | --- |
| Routine update | Meaningful summary if needed; details available | Preserve focus and reading; do not announce every changed cell. |
| Action needed | What changed, impact and remedy | Choose documented status or contextual error treatment. |
| Justified urgent event | Consequence and immediate action | Use interruption only when justified; provide a recovery path. |
| Revisit/dismiss | Current message state and pending action | Do not equate dismissing a message with completing the action. |

The table is an implementation-facing script of meaning, not an exact speech transcript. Specify actual names, roles, relationships and states in HTML; check browser/AT output. Support heading/control navigation and braille as well as sequential speech. Keep essential information available visually and programmatically.

## Implementation contract

| Contract field | Required decision |
| --- | --- |
| Message identity | Stable event/message ID, originating task, priority, essential content, required action and expiry. |
| Policy | Routine = non-interrupting/retrievable; action-needed = persistent enough for the task with clear remedy; urgent = interruption only with a documented harm/urgency rationale. |
| Channels | Specify supported visual/AT/audio/haptic routes, user settings and any safety restriction. Screen-reader speech and application audio must not compete unnecessarily. |
| Ordering | Deduplicate retries and group related updates; avoid announcing both a focused error summary and an identical live alert. |
| Lifecycle | Created → queued → presented → acknowledged/acted-on/dismissed/expired; acknowledgement is not comprehension or completion. |

## Evaluation procedures

New `MEM-*` identifiers below are local supplementary outcome evaluations, not canonical QA test IDs. Existing CUX assertions are supporting checks and do not establish the whole outcome. **A** means bounded script/agent checks; **M** means expert/content/actual-AT review; **U** means intended-user evidence. Each evaluation requires the relevant combination, not an automatic whole-test pass.

### MEM-NT-01 — Manage competing channels and messages

**Pattern:** `COG-NT-01`. **Status:** Not tested. **Methods:** A + M + U.

**Applicability and preparation:** Apply when the described feature/context exists. Use a controlled fixture for failures, fictitious task data and an agreed outcome rubric. Include relevant vision/cognitive intersections and actual preferred modes without imposing diagnoses or withholding support.

**Procedure:** Generate concurrent routine/action-needed events, duplicate retries and platform-channel failures in fixtures. Test chosen preference combinations and actual supported AT/devices.

**Expected result:** Priority/order follow the policy; messages remain perceivable/retrievable without duplicate forced output or routine focus theft.

**Retain:** Event/announcement/focus traces, settings matrix and participant task recovery; log unsupported tactile/audio routes.

**Boundaries:** An agent can exercise states and check saved values, relationships or events. A reviewer checks meaning and real AT behaviour; participants establish understanding and usable task outcomes. Record blocked/cannot-tell cases, environment and scope.

### MEM-NT-02 — Evaluate repeated exposure and meaningful change

**Pattern:** `COG-NT-02`. **Status:** Not tested. **Methods:** A + M + U.

**Applicability and preparation:** Apply when the described feature/context exists. Use a controlled fixture for failures, fictitious task data and an agreed outcome rubric. Include relevant vision/cognitive intersections and actual preferred modes without imposing diagnoses or withholding support.

**Procedure:** Use a proportionate repeated-use study with baseline messages and a genuinely changed consequential message. Predefine notice, understanding and action outcomes; avoid coaching participants to hunt for a warning.

**Expected result:** Intended users can identify and act on material changes without undue disruption; failure and uncertainty remain visible rather than replaced by a novelty claim.

**Retain:** Exposure history, comprehension/action, misses, interruption recovery and comparison method; a one-off scan cannot satisfy this evaluation.

**Boundaries:** An agent can exercise states and check saved values, relationships or events. A reviewer checks meaning and real AT behaviour; participants establish understanding and usable task outcomes. Record blocked/cannot-tell cases, environment and scope.

## Inclusive research and privacy

Habituation, fatigue and distraction are not interchangeable diagnoses. Do not induce fear or desensitise participants to real safety warnings. Test consequential scenarios with fictitious outcomes and approved safeguarding boundaries.

Use the [research/data plan](Cognitive_Accessibility_User_Research_and_Data_Plan.md) for lawful processing, optional functional segmentation, accessible participation, compensation and safe stopping. Energy, stress and sight history are context, not proxies for legal capacity. Do not ask people to become fatigued, intoxicated or distressed; do not alter medication. Treat participant-linked support/context data under the approved sensitive-data assessment.

## Delivery, ownership and links

Design owns the task/interaction contract, content owns meaningful wording, engineering owns state/data integrity, QA owns reproducible checks, and research owns outcome interpretation. The product owner accepts scope and resolves remaining barriers. Named maintainers and independent review are pending.

Use the [delivery template](Cognitive_UX_Design_and_Evidence_Template.md) to record expected and actual results separately. Link evidence rather than copying identifiable participant records into public documentation. Report each applicable satisfaction domain separately alongside comprehension, action and recovery. A faster task or confident answer alone is not success.

Supporting QA assertions: CUX-26, CUX-27, CUX-28, CUX-29, CUX-30, CUX-31, CUX-32 in the [existing matrix](Cognitive_UX_Principles_QA_Evidence_Matrix.md). Full mappings, cross-repository sources and document status live in the [coverage register](Cognitive_UX_Coverage_and_Delivery_Map.md).
