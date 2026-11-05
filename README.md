# Cognitive UX Design

Practical guidance from Double FW Ltd for understandable, controllable and inclusive experiences, including people with intersecting vision, cognitive, learning and attention-related needs.

**Document pack: draft 1.0, 5 November 2026.** Guidance has been authored and structurally checked; independent review, repository publication and product/user evaluations are not implied. All supplementary evaluation results start as Not tested.

## Start here

1. Read the [ten principles](Cognitive%20Design%20Principles.md).
2. Use the [coverage and delivery map](Cognitive_UX_Coverage_and_Delivery_Map.md) to select a task, gap and guide.
3. Specify the design using the [delivery template](Cognitive_UX_Design_and_Evidence_Template.md).
4. Combine [existing QA](Cognitive_UX_Principles_QA_Evidence_Matrix.md), new MEM evaluations and [user research](Cognitive_Accessibility_User_Research_and_Data_Plan.md).
5. Record actual outcomes, limitations, owner and retest; do not infer cognitive delivery from a clean automated scan.

## Practical guides

| Customer/design problem | Guide | Local patterns / evaluations |
| --- | --- | --- |
| Remember to act later; rely on an aid safely | [Prospective memory and reliable memory aids](Prospective_Memory_and_Reliable_Memory_Aids.md) | COG-PM-01/02; MEM-PM-01/02 |
| Resume after interruption, sign-in or handoff | [Task continuity](Interruption_Recovery_and_Task_Continuity.md) | COG-RC-01/02; MEM-RC-01/02 |
| Distinguish current from similar previous information | [Interference and current context](Interference_Source_Memory_and_Current_Context.md) | COG-CT-01/02; MEM-CT-01/02 |
| Understand a familiar action and verify the result | [Comprehension and confidence](Familiarity_Comprehension_and_Confidence.md) | COG-CF-01/02; MEM-CF-01/02 |
| Adapt to redesign or return after an absence | [Learning and returning users](Learning_Redesign_and_Returning_Users.md) | COG-LR-01/02; MEM-LR-01/02 |
| Notice important changes without competing alerts | [Warning and notification management](Warnings_Habituation_and_Notification_Management.md) | COG-NT-01/02; MEM-NT-01/02 |

## Routes by role

- **Design/content:** principles, relevant practical guide, [screen-reader script/structure guide](Vision_Memory_and_Cognitive_Screen_Reader_UX.md), template and task-specific consequences.
- **Engineering/QA:** guide implementation contracts, existing QA and MEM procedures; inspect real state, data, focus and supported AT behaviour.
- **Research/data:** the research plan, module extensions and [science register](Cognitive_Science_Evidence_Register.md); distinguish observation, hypothesis, confidence and actual understanding.
- **Product/maintainers:** coverage, named ownership, outstanding evidence, [changelog](CHANGELOG.md) and [package notes](PACKAGE_NOTES.md).
- **Authorised agents:** retrieve the owning guide and source before acting; retain IDs/revisions, run bounded checks, record tool errors and route meaning/user outcomes to humans. Do not fabricate participants or infer diagnosis from behaviour.

## Evidence and identity

CP identifies the ten principles; M identifies the review’s eight gap actions; E identifies science groups; CUX/G retain the existing QA matrix meanings. New COG patterns and MEM supplementary evaluations are local additions. See the coverage register for exact relationships. This repository does not create new legal criteria or declare every pattern equivalent to a WCAG success criterion.

The [gap review](Cognitive_UX_Ten_Principles_Memory_and_Evidence_Gap_Review.md) is historical rationale, not the current delivery-status register. It remains unchanged. The coverage register records the new documents and outstanding review; the science register owns bounded research claims.

Publication of guidance closes an editorial action only. It cannot supply missing evidence for a real service. Keep participant-level data outside this public repository and follow the research plan’s jurisdiction-specific governance before collection.

## Maintenance

Use stable IDs, source revisions and human review. Update the owner document first, then its mappings and dependent examples. Reassess affected cases after a component, policy, paper or source change. Assign named maintainers before publishing an approved release; record the actual published commit and date.

The existing [licence](LICENSE) is retained unchanged in this pack. See package notes for installation and baseline information.
