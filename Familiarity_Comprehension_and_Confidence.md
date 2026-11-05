# Familiarity, comprehension and confidence

**Double FW Ltd · Draft 1.0 · 5 November 2026**

**Scope:** M-04. **Principles:** CP-02, CP-04, CP-07, CP-10.

## User need and design purpose

Understand the actual consequence of a familiar-looking action and verify a result without being pressured to trust memory, confidence or a fluent answer.

This guide supplies practical design patterns and evaluations. Its recommendations are not quotations from legislation or a guarantee of WCAG/EAA conformity. All worked scenarios are fictitious; no user evaluations have been executed. Confirm applicability, risk and acceptance criteria for the product before treating a recommendation as a project requirement.

## Scientific basis and boundaries

Recognition and reminder studies distinguish relevant aspects of familiarity, association, confidence and strategy. They motivate examining confidence alongside correctness; they do not validate a new psychometric confidence score or prove that more explanation always improves comprehension.

See [E2](Cognitive_Science_Evidence_Register.md#e2), [E4](Cognitive_Science_Evidence_Register.md#e4) in the shared evidence register. The research-to-UX application remains a hypothesis to validate; no clinical memory assessment, brain scan or universal capacity threshold is proposed.

## Design approaches

### Make consequences available

State what the action does, material cost/commitment and reversibility at the decision. A familiar label such as Continue is insufficient when it commits a payment.

### Layer explanations

Offer a short summary, examples and fuller detail with meaningful labels. Let users revisit information rather than testing unaided recall.

### Explain uncertainty honestly

Distinguish confirmed result, pending state, estimate and unverified AI suggestion. Provide an appropriate route to correct or check information.

### Test understanding safely

In research, ask neutral questions about expected consequence before activation and verify outcome afterwards. Do not add a comprehension quiz as a universal service gate.

## Worked task and state record

A trial enrolment uses a button labelled “Start paid subscription — £12 per month” with cancellation terms available before activation. A participant may recognise the button style but still misunderstand the trial end. The design is evaluated on informed choice and correction, not on whether the person says they feel confident.

| Trigger/state | Information available to the customer | Interaction and screen-reader intent |
| --- | --- | --- |
| Before action | Task and material consequence; optional detail | Information is available in normal reading and relevant control context. |
| Ask for help | Relevant explanation and a route back | Keep current choices; avoid a forced long announcement. |
| After action | Confirmed, pending or failed result with next action | Use accurate state and appropriate focus/status behaviour. |
| Correction | Specific change, cancellation or support route | Explain what remains reversible; do not promise undo when unavailable. |

The table is an implementation-facing script of meaning, not an exact speech transcript. Specify actual names, roles, relationships and states in HTML; check browser/AT output. Support heading/control navigation and braille as well as sequential speech. Keep essential information available visually and programmatically.

## Implementation contract

| Contract field | Required decision |
| --- | --- |
| Action identity | Name, role, state and context match actual behaviour; visible and accessible names remain coherent. |
| Decision information | Identify essential consequences and their source of truth; specify where they can be retrieved. |
| Result | Separate success, partial, pending and failure. A spinner disappearing is not a sufficient result record. |
| Assistance | Clarification/help remains available without forcing a diagnosis or loss of progress. |
| Research coding | Pre-agreed rubric distinguishes understood, partial, misunderstood and cannot tell; record prompted versus spontaneous explanation. |

## Evaluation procedures

New `MEM-*` identifiers below are local supplementary outcome evaluations, not canonical QA test IDs. Existing CUX assertions are supporting checks and do not establish the whole outcome. **A** means bounded script/agent checks; **M** means expert/content/actual-AT review; **U** means intended-user evidence. Each evaluation requires the relevant combination, not an automatic whole-test pass.

### MEM-CF-01 — Compare expectation and consequence

**Pattern:** `COG-CF-01`. **Status:** Not tested. **Methods:** A + M + U.

**Applicability and preparation:** Apply when the described feature/context exists. Use a controlled fixture for failures, fictitious task data and an agreed outcome rubric. Include relevant vision/cognitive intersections and actual preferred modes without imposing diagnoses or withholding support.

**Procedure:** For a safe fictitious consequential action, define essential understanding points. Ask “What do you expect this action to do?” without suggesting an answer; allow all normal information and help. Then observe activation or cancellation.

**Expected result:** Intended users can access and explain material consequences or obtain useful clarification before deciding. Correct cancellation is a valid outcome.

**Retain:** Rubric-coded explanation, confidence where voluntarily rated, information consulted and decision; not a memory quiz.

**Boundaries:** An agent can exercise states and check saved values, relationships or events. A reviewer checks meaning and real AT behaviour; participants establish understanding and usable task outcomes. Record blocked/cannot-tell cases, environment and scope.

### MEM-CF-02 — Verify and correct a result

**Pattern:** `COG-CF-02`. **Status:** Not tested. **Methods:** A + M + U.

**Applicability and preparation:** Apply when the described feature/context exists. Use a controlled fixture for failures, fictitious task data and an agreed outcome rubric. Include relevant vision/cognitive intersections and actual preferred modes without imposing diagnoses or withholding support.

**Procedure:** Present success, pending and recoverable failure fixtures. Ask the user to establish what happened and how to correct an unwanted outcome.

**Expected result:** People can distinguish outcome states and access an appropriate correction/support path. Reassuring wording never masks uncertainty.

**Retain:** System state versus participant interpretation, assistance and correction outcome; use the five satisfaction domains separately.

**Boundaries:** An agent can exercise states and check saved values, relationships or events. A reviewer checks meaning and real AT behaviour; participants establish understanding and usable task outcomes. Record blocked/cannot-tell cases, environment and scope.

## Inclusive research and privacy

Confidence is self-report, not correctness or clinical capacity. Do not treat a hesitant but correct customer as incompetent, or use comprehension evidence for sales pressure. Allow supported communication and an unpressured choice to stop.

Use the [research/data plan](Cognitive_Accessibility_User_Research_and_Data_Plan.md) for lawful processing, optional functional segmentation, accessible participation, compensation and safe stopping. Energy, stress and sight history are context, not proxies for legal capacity. Do not ask people to become fatigued, intoxicated or distressed; do not alter medication. Treat participant-linked support/context data under the approved sensitive-data assessment.

## Delivery, ownership and links

Design owns the task/interaction contract, content owns meaningful wording, engineering owns state/data integrity, QA owns reproducible checks, and research owns outcome interpretation. The product owner accepts scope and resolves remaining barriers. Named maintainers and independent review are pending.

Use the [delivery template](Cognitive_UX_Design_and_Evidence_Template.md) to record expected and actual results separately. Link evidence rather than copying identifiable participant records into public documentation. Report each applicable satisfaction domain separately alongside comprehension, action and recovery. A faster task or confident answer alone is not success.

Supporting QA assertions: CUX-04, CUX-11, CUX-12, CUX-13, CUX-25, CUX-35 in the [existing matrix](Cognitive_UX_Principles_QA_Evidence_Matrix.md). Full mappings, cross-repository sources and document status live in the [coverage register](Cognitive_UX_Coverage_and_Delivery_Map.md).
