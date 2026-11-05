# Cognitive UX design and evidence template

**Double FW Ltd · Draft 1.0 · 5 November 2026**

Copy this document per scoped task or linked pattern. Replace Pending with actual decisions; the template is not evidence that testing happened. Do not upload identifiable research data or private task content to the public repository.

## 1. Identity and scope

| Field | Project record |
| --- | --- |
| Project / record ID / revision | Pending |
| Named owner / reviewer / date | Pending |
| User task and successful outcome | Pending; include informed cancellation/support where legitimate |
| Principles / gap / pattern | CP-xx; M-xx; COG-xx-xx from coverage map |
| Product / build / environment | Pending; retain exact device, browser, OS, AT, mode and settings |
| Applicable users and contexts | Pending; functional needs, relevant intersections and support preferences |
| Exclusions / unsupported modes | Pending with reason and owner |
| Source revisions | Principles, guide, QA matrix/canonical source and science register |

## 2. Evidence chain

| Step | Record |
| --- | --- |
| Scientific observation | E ID and bounded claim; distinguish primary result, review and UX inference |
| Plausible user risk | Specific failure of comprehension, action, context or control |
| Design hypothesis | Proposed mechanism and alternatives considered |
| Observable acceptance | Task-specific result and rubric agreed before collection |
| Contrary evidence | What would show the design did not help or created a new barrier? |

## 3. Design and implementation contract

Record the task flow and decision branches, information available before each consequence, native HTML relationships, visible/accessible names, relevant state, focus/reading strategy, routine and urgent feedback, persistence, cancellation, timeout and error recovery. Link the visual annotations and accessible text equivalent. Do not specify one mandatory speech sentence for every screen reader.

| Trigger / current state | Required information and action | Next state / source of truth | Focus and feedback | Recovery / invalidation |
| --- | --- | --- | --- | --- |
| Pending | Pending | Pending | Pending | Pending |

### Memory demand review

For every decision, identify what must be retained, retrieved, compared or done later. State what the interface keeps available and how someone finds it again. Include interference from similar prior tasks and recovery after a pause. Do not assign a numerical cognitive-capacity score.

## 4. Evaluation plan

Select existing CUX assertions and their applicable source tests without renaming them. Add the relevant MEM evaluations. Define fixtures, real-integration checks and human/user activities separately; an agent must not fill the user-outcome column with simulated personas.

| Evaluation ID / source | Preconditions and task | Expected outcome / rubric | Method and required reviewer | Applicability |
| --- | --- | --- | --- | --- |
| Pending | Pending | Pending | A: bounded tools; M: expert/AT; U: real users | Pending |

Use fictitious transactions for consequences. Let people retain normal instructions, summaries and preferred AT. Offer safe breaks, rescheduling and assistance; record assistance rather than withholding it. Use the research/data plan for lawful processing and handling of optional sensitive fields before collecting participant data.

## 5. Execution and defects

| Run / evaluation ID | Build and environment | Actual observation | Status | Controlled evidence link | Defect / owner / retest |
| --- | --- | --- | --- | --- | --- |
| Pending | Pending | Not executed | Not tested | Pending | Pending |

Results: Pass, Fail, Not tested, Blocked, Cannot tell, Not applicable with reason, Tool error. Preserve tool-native outputs as evidence. A failed script is not a product pass/failure; an ambiguous human outcome is Cannot tell until resolved. Do not change acceptance criteria after seeing results without recording the reason and re-evaluating comparability.

## 6. User outcomes

Report Navigation, Task Completion, Task Time Expectation, Content Consumption and User Preference Support separately, with offered/applicable/responding counts. Retain task correctness, consequences understood, assistance, recovery and optional confidence. A fast/confident task can still be misunderstood; choosing not to proceed can be informed success.

Record sampling, protocol, exposure history, repeat participants, attrition, uncertainty and missing groups. Delayed-return/repeated-warning studies need their own schedule and analysis. Keep customer-level identifiers, raw recordings and sensitive context in approved controlled stores.

## 7. Decision and retest

| Field | Decision record |
| --- | --- |
| Documentation state | Drafted / Reviewed / Published; dates and commit evidence |
| Implementation state | Planned / Implemented / Changed; build |
| Delivery judgement | Insufficient evidence until assessed; then bounded judgement with rationale |
| Outstanding barriers / deviations | Pending |
| Named accountable owner and human reviewer | Pending |
| Retest trigger / due date | Pending; change, defect, unsupported context or evidence uncertainty |

Supported in tested scope requires the applicable technical, manual and user evidence—not a completed template. Preserve unresolved limitations rather than averaging them away.

## 8. Worked planning example — no execution claimed

**Task:** resume a saved application. **Mapping:** M-02, COG-RC-01; CP-03/06/07/09/10. **Scientific context:** E3/E7 motivate a continuity hypothesis. **Design:** a task heading, current-answer summary and next action, restored after authentication. **Supporting QA:** CUX-23/24/29. **Supplement:** MEM-RC-01 plus failure cases in MEM-RC-02.

**Proposed acceptance:** the customer can identify the application, verify retained answers and continue using available context without moderator reconstruction; changed/expired values are explained before commitment. **Actual observation:** Not executed. **Delivery judgement:** Insufficient evidence. Confirm applicable contexts and the project rubric before using this example as a requirement.

## Related records

- [Coverage register](Cognitive_UX_Coverage_and_Delivery_Map.md)
- [Science register](Cognitive_Science_Evidence_Register.md)
- [Existing QA matrix](Cognitive_UX_Principles_QA_Evidence_Matrix.md)
- [Research/data plan](Cognitive_Accessibility_User_Research_and_Data_Plan.md)
