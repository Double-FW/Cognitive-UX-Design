# Cognitive UX principles: QA delivery and evidence matrix

**Prepared for Double FW Ltd · 5 November 2026 · Extension draft 1.1**

This matrix maps existing tests in the Double FW QA repository to all ten Cognitive UX Design principles. It provides 36 scoped evidence assertions, a reverse test index and six supplementary evaluations for outcomes the selected tests cannot establish. **This is a mapping and execution template; no product tests have been run. Twelve MEM supplementary evaluations are added in section 7; the original 36 CUX assertions retain their IDs.**

A technically accessible interface can still demand too much memory, present too much information or leave users unsure what happened. A QA pass supports the particular behaviour tested; it does not, by itself, establish delivery of a cognitive principle. Use the technical results alongside expert review and evidence from relevant users.

## 1. Source baseline and interpretation

- [Cognitive Design Principles.md](https://github.com/Double-FW/Cognitive-UX-Design/blob/a6d0f2751bdc67a19e7d3f9c9645a7a93303a6e4/Cognitive%20Design%20Principles.md), commit `a6d0f2751bdc67a19e7d3f9c9645a7a93303a6e4`. Principle names are reproduced unchanged; descriptions below are operational interpretations.
- [Canonical Test Library.md](https://github.com/Double-FW/QA_Accessibility_Testing/blob/c0450cdcb89484248ca4a15355ea5d71a58af043/Canonical%20Test%20Library.md), [ACT-style test system](https://github.com/Double-FW/QA_Accessibility_Testing/blob/c0450cdcb89484248ca4a15355ea5d71a58af043/Accessibility_ACT-Style_Test_System.md) and [mobile/application/website test library](https://github.com/Double-FW/QA_Accessibility_Testing/blob/c0450cdcb89484248ca4a15355ea5d71a58af043/Mobile_Application_and_Website_Test_Library.md), QA commit `c0450cdcb89484248ca4a15355ea5d71a58af043`.
- [QA testing approach](https://github.com/Double-FW/QA_Accessibility_Testing/blob/c0450cdcb89484248ca4a15355ea5d71a58af043/Testing_Approach.md) and [canonical WCAG relationship register](https://github.com/Double-FW/QA_Accessibility_Testing/blob/c0450cdcb89484248ca4a15355ea5d71a58af043/Canonical_WCAG_AA_Relationship_Register.md) inform evidence boundaries. The QA library distinguishes repository requirements, recommended practices and WCAG relationships. This document makes **no new WCAG or statutory mappings**.

The pinned source above is the original mapping baseline. The bundled [revised principles](Cognitive%20Design%20Principles.md) qualify feedback/channel wording; section 7 and G-05 use that clarified intent. Reconfirm project acceptance criteria against the chosen revision and record any substantive difference.

Pin these revisions in each execution record. Recheck mappings after either repository changes. The linked source contains the full test requirement/procedure; the matrix supplies its cognitive purpose and evidence expectations rather than replacing that procedure.

### Identifiers and evidence labels

| Label | Meaning |
| --- | --- |
| CP-01–CP-10 | Local principle references assigned here in source order; not source repository IDs. |
| CUX-01–CUX-36 | Local evidence assertions created for this matrix; not new QA repository tests. |
| CTL-nnn | Existing canonical test identifiers, retained as used in the QA relationship register. |
| ACT ID | Existing identifier in the ACT-style test system. |
| MW #n | Local citation to numbered item n in the mobile/web library, not a source-issued test ID. |
| D | Direct evidence for the **limited observable behaviour in the row**. It does not mean full principle coverage. |
| P | Partial/supporting evidence. A material part of the broader outcome remains outside the cited tests. |
| A | Some objective checks can be automated or agent-assisted: state, structure, keyboard scripts, timing or measurements. This does not mean the complete row is automatable or that axe covers it. |
| M | Expert manual review, content/design evaluation or actual assistive-technology/device testing. Required where indicated. |
| U | Evaluation with relevant users to establish comprehension, discoverability, memory burden, control or task outcomes. An agent cannot impersonate this evidence. |

For each A-labelled row, specify the actual tool and version at execution. axe may contribute only its applicable rules; do not translate a clean scan into a pass for these rows. Browser agents can collect repeatable observations and draft interpretation, while unresolved meaning and user outcomes remain for human review.

## 2. Principle-level coverage

| Local ID / source principle | Evidence assertions | What existing QA can help demonstrate | Additional outcome evidence needed |
| --- | --- | --- | --- |
| CP-01 — Standard Elements | CUX-01, CUX-02, CUX-03 | Consistent naming, control behaviour and component conventions. | Familiarity across the complete service, including visual/audio consistency; novice and experienced user expectations. |
| CP-02 — Affordances and Signifiers | CUX-04, CUX-05, CUX-06 | Purpose, roles, labels, state and action align. | Whether the intended users recognise cues and correctly predict actions. |
| CP-03 — Simplicity | CUX-07, CUX-08, CUX-09 | Focused promos, reduced duplicate effort, readable structure and layout. | G-01: task-level information volume, complexity, clutter and effort; current checks are partial. |
| CP-04 — Clear Communication | CUX-10, CUX-11, CUX-12, CUX-13 | Perceivable messages, explicit instructions, useful errors and visual equivalents. | Interpretation, readable character forms and successful error recovery with relevant users. |
| CP-05 — Redundancies | CUX-14, CUX-15, CUX-16, CUX-17 | Multiple cues, media alternatives and interaction routes. | Whether redundancy improves access without repetitive consumption; novice/expert flexibility. |
| CP-06 — Patterns | CUX-18, CUX-19, CUX-20, CUX-21 | Meaningful hierarchy, groups, component relationships and data structure. | Whether users understand the grouping and can locate the information or action. |
| CP-07 — Recognition Rather than Recall | CUX-22, CUX-23, CUX-24, CUX-25 | Persistent cues, retained input, orientation and available help. | G-02 memory burden; G-03 appropriate support after persistent errors. |
| CP-08 — Variable Stimuli and the Pop-Out Effect | CUX-26, CUX-27, CUX-28 | Salience, warning timing and bounds on disruptive attention cues. | G-04 repeated exposure, consequential-warning recognition and useful feature discovery; current checks are partial. |
| CP-09 — Feedback and Notification | CUX-29, CUX-30, CUX-31, CUX-32 | Status, error and multimodal feedback; non-disruption and timing. | G-05 distinct channel identities, visual/audio/haptic provision and independent persistence controls. |
| CP-10 — User Control and Choice | CUX-33, CUX-34, CUX-35, CUX-36 | Input alternatives, preferences, playback control and adjustable interaction. | Actual preferred-mode task completion, output equivalence and G-06 complex interaction/game configuration. |

## 3. Delivery evidence matrix

Apply each row only to relevant components, content, platforms and journey states. A justified N/A requires an applicability reason and reviewer, not an empty result. The acceptance wording below supplements the cited source tests. Set task-specific measures before execution; do not invent universal time, complexity or satisfaction thresholds.

### CP-01 — Standard Elements

| Evidence ID and observable outcome | Existing QA references | Relationship / methods | Procedure, expected result and evidence |
| --- | --- | --- | --- |
| **CUX-01** — Repeated controls keep the same meaning and interaction across the journey. | CTL-093; CTL-200; MW #121; MW #122; MW #155; MW #156 | D; A+M | Compare repeated controls across screens and success/error states. Record labels, actions and any visual/audio cues; equivalent controls behave consistently. Semantic comparison can flag differences; a reviewer judges meaning and familiarity. |
| **CUX-02** — Familiar component conventions are preserved. | CTL-093; CTL-165; CTL-167; CTL-176; CTL-177; CTA-01; ACC-01; NAV-01 | D; A+M | For each applicable component, record role, keyboard contract and observed activation. Expected behaviour follows its selected pattern. These component-specific tests do not establish familiarity for the whole product. |
| **CUX-03** — Interaction remains consistent across input methods. | CTL-107; MW #66; MW #137; PRACTICE-MULTI-01 | P; A+M+U | Complete the same task by supported input routes. Retain action/result traces and differences; meaning and outcome remain equivalent. Validate voice/touch on actual supported devices; include experienced and new users for learnability. |

### CP-02 — Affordances and Signifiers

| Evidence ID and observable outcome | Existing QA references | Relationship / methods | Procedure, expected result and evidence |
| --- | --- | --- | --- |
| **CUX-04** — Visible controls and semantic cues predict the action. | CTL-011; CTL-071; CTL-073; CTL-081; CTL-082; MW #55; MW #56; MW #58; MW #123; PRACTICE-AFF-01 | D; A+M+U | Capture visual appearance, accessible name/role/state and action result. Cues match the actual action. A reviewer checks misleading affordances; users explain expected action before activation. |
| **CUX-05** — Links and functional icons communicate their purpose. | CTL-035; CTL-136; CTL-137; CTL-140; LINK-01; PRACTICE-ICON-01 | D; A+M | Inspect labels/icons in context and accessibility output, then follow destinations. Record the expected and actual action, including downloads. Name presence is automatable; meaningful wording and recognised icon meaning need review. |
| **CUX-06** — Selected, focused and expanded states remain distinguishable. | CTL-004; CTL-005; CTL-095; CTL-144; CTL-157; CTL-161 | D; A+M | Capture before/after visual and accessibility states for each control. State is correctly exposed, focus is locatable, and colour is supplemented. Verify styling in relevant preference modes. |

### CP-03 — Simplicity

| Evidence ID and observable outcome | Existing QA references | Relationship / methods | Procedure, expected result and evidence |
| --- | --- | --- | --- |
| **CUX-07** — Promotional content presents one clear primary action. | CTL-185; CTL-186; PROMO-01 | P; A+M+U | Inventory promo links and compare headline with destination. One clear primary action is identifiable. Limit this result to promos; it does not prove that a form or whole journey is simple. Use G-01 for the complete task. |
| **CUX-08** — Avoidable repetition and competing interruptions are reduced. | CTL-033; CTL-083; CTL-138; CTL-153; CTL-179 | P; A+M+U | Record repeated names/links, decorative announcements, notifications and carousel behaviour. No unnecessary duplicate effort or competing interruptions in the sampled task. Measure comprehension and task burden through G-01 rather than inferring it from element counts. |
| **CUX-09** — Presentation supports reading without avoidable layout burden. | CTL-016; CTL-019; CTL-060; CTL-063; MW #36; MW #176; PRACTICE-TYPE-02 | P; A+M+U | Save reflow/text-spacing views and reading order. Content remains usable and groups coherent. Judge language complexity, information volume and progressive disclosure separately through G-01; responsive layout alone is insufficient. |

### CP-04 — Clear Communication

| Evidence ID and observable outcome | Existing QA references | Relationship / methods | Procedure, expected result and evidence |
| --- | --- | --- | --- |
| **CUX-10** — Text and important controls can be distinguished visually. | CTL-008; CTL-009; CTL-011; CTL-012; PRACTICE-CONTRAST-01; PRACTICE-TYPE-01 | D; A+M | Retain measured colour pairs, font settings and representative strings such as 1/l/I and 0/O. Contrast meets the applicable source test and characters are distinguishable in context. Review typeface suitability; contrast cannot establish interpretation. |
| **CUX-11** — Labels and instructions explain what is required. | CTL-072; CTL-075; CTL-078; CTL-113; CTL-114; CTL-116; MW #16; MW #17 | D; A+M+U | Record field labels, associated instructions, required/optional and format cues before and during entry. Instructions remain available and users can explain the requested input. Automation checks association/persistence; people judge clarity. |
| **CUX-12** — Errors explain the problem and a usable remedy. | CTL-122; CTL-124; CTL-125; CTL-126; CTL-127; CTL-128; CTL-129; MW #244; PRACTICE-FORM-02 | D; A+M+U | Trigger representative errors. Retain message, field association, summary navigation and preserved values. Messages identify the issue and actionable non-technical correction; users recover without guessing. |
| **CUX-13** — Meaningful visuals have interpretable equivalents. | CTL-034; CTL-035; CTL-036; CTL-039; PRACTICE-ALT-01 | D; A+M+U | Compare the image/chart purpose with its text/summary. Retain both and essential information checklist. Presence checks can be automated; a person verifies equivalence and users interpret essential messages. |

### CP-05 — Redundancies

| Evidence ID and observable outcome | Existing QA references | Relationship / methods | Procedure, expected result and evidence |
| --- | --- | --- | --- |
| **CUX-14** — Meaning survives loss of colour cues. | CTL-001; CTL-002; CTL-003; CTL-004; CTL-007; PRACTICE-COLOUR-01 | D; A+M | Review errors, required fields, states and charts without colour. Retain text/shape/pattern cues plus AT output; meaning remains recoverable. Do not rely on a colour simulation alone. |
| **CUX-15** — Spoken and essential visual media information has suitable alternatives. | CTL-183; CTL-184; MW #67; MW #69; PRACTICE-CAPTION-01; PRACTICE-BIMEDIA-01 | D; A+M+U | Record media, caption synchronisation/accuracy and essential visual information covered by description or equivalent. People judge completeness and tone; track detection is partial. Scope alternatives to the actual content and target use. |
| **CUX-16** — Users can select an equivalent interaction route. | CTL-091; CTL-092; CTL-107; CTL-108; MW #78; MW #79; MW #80; PRACTICE-MULTI-01 | D; A+M+U | Complete the task using keyboard, pointer, touch and voice where supported/applicable, including gesture alternatives. Record device/AT and parity of outcomes; DOM simulation alone does not verify real voice or touch operation. |
| **CUX-17** — Redundancy helps without making users consume duplicated information. | CTL-083; CTL-138; CTL-153; CTL-159; MW #338; MW #339; MW #340 | P; A+M+U | Record accessibility speech output, tooltips and repeated controls. Supplementary help adds value without repeating names or being the only source of essential information. Compare novice/expert burden through G-01/G-02. |

### CP-06 — Patterns

| Evidence ID and observable outcome | Existing QA references | Relationship / methods | Procedure, expected result and evidence |
| --- | --- | --- | --- |
| **CUX-18** — Hierarchy, reading order and groups express meaningful structure. | CTL-054; CTL-056; CTL-057; CTL-058; CTL-060; CTL-063; PRACTICE-HEAD-01; PRACTICE-ORDER-01 | D; A+M+U | Save heading outline, source order and screen-reader navigation trace. Structure matches visible hierarchy and intended meaning. A reviewer checks grouping logic; users locate related content using the structure. |
| **CUX-19** — Related questions and controls share an understandable group context. | CTL-080; CTL-119; CTL-120; CTL-121; MW #258; MW #260; MW #290; MW #291; PRACTICE-FORM-01 | D; A+M | Capture group labels, relationships and announced context. Each choice belongs to the correct question and the shared context is available visually and through AT. Semantic presence alone does not prove a meaningful group label. |
| **CUX-20** — Disclosure and tab patterns maintain context. | CTL-161; CTL-162; CTL-163; CTL-164; CTL-165; CTL-167; CTL-169; ACC-01; ACC-02; DISC-01 | D; A+M | Retain toggle/tabpanel states, focus order and hidden-content checks. Controls expose relationships and state; only intended content is presented, with predictable navigation. Apply only to the pattern actually used. |
| **CUX-21** — Tables retain their information relationships. | CTL-066; CTL-067; CTL-068; CTL-069; CTL-070 | D; A+M | Record caption/header associations and representative cell announcements at narrow layouts. Users can relate data to headers without losing structure. Human review establishes whether the chosen table structure conveys the data relationships. |

### CP-07 — Recognition Rather than Recall

| Evidence ID and observable outcome | Existing QA references | Relationship / methods | Procedure, expected result and evidence |
| --- | --- | --- | --- |
| **CUX-22** — Labels, instructions and help are persistent or easily retrievable. | CTL-072; CTL-075; CTL-076; CTL-078; CTL-083; MW #254; MW #275; MW #277 | D; A+M+U | Capture before/during entry and after a pause. Users can identify controls and recover instructions without remembering placeholder text or a prior screen. G-02 evaluates the residual memory burden across the whole task. |
| **CUX-23** — Validation and time pressure do not impose avoidable re-entry or recall. | CTL-129; CTL-134; CTL-197; CTL-198; CTL-199; MW #248; MW #257; MW #302 | P; A+M+U | Cause errors, revisit a step and exercise an allowed timeout. Record retained values, autofill/support, warnings and consequences. Confirm recovery within security/privacy constraints; document justified intentional expiry rather than assuming indefinite retention. |
| **CUX-24** — Current location and return context are apparent. | CTL-045; CTL-046; CTL-047; CTL-086; CTL-087; CTL-100; CTL-101; CTL-148; CTL-149; PRACTICE-ROUTE-01; PANEL-01 | D; A+M+U | Traverse routes, open/close a panel and use back navigation. Capture title, current item, focus destination/return and history. Users can identify location and next action without reconstructing prior navigation. |
| **CUX-25** — Help is discoverable, contextual and perceivable. | CTL-083; CTL-171; MW #275; MW #276; MW #277; MW #278 | P; A+M+U | Request help at a difficult step; retain location, content and AT presentation. Help relates to the current task and is retrievable. Existing tests do not establish detection of persistent errors or appropriate adaptive advancement: add G-03. |

### CP-08 — Variable Stimuli and the Pop-Out Effect

| Evidence ID and observable outcome | Existing QA references | Relationship / methods | Procedure, expected result and evidence |
| --- | --- | --- | --- |
| **CUX-26** — Important messages stand out from surrounding information. | CTL-008; CTL-011; CTL-095; CTL-152; MW #245; MW #268; PRACTICE-CONTRAST-01; PRACTICE-FOCUS-01 | P; A+M+U | Capture realistic crowded/error states. Record visual contrast, placement and accessible delivery. Users notice and interpret the important message. These checks support salience but do not test habituation after repeated exposure: G-04. |
| **CUX-27** — Attention cues respect motion preferences and avoid competing disruption. | CTL-022; CTL-023; CTL-024; CTL-026; CTL-153; CTL-156; CTL-179; PRACTICE-MOTION-01; CAR-01 | P; A+M | Exercise attention cues with reduced motion and ongoing tasks. Record controls, focus and notification ordering. Meet source motion/flashing conditions and preserve task continuity. Adding animation is not evidence of this principle. |
| **CUX-28** — Consequential warnings are timely and available long enough to act. | CTL-131; CTL-160; CTL-198; CTL-199; MW #279; MW #301 | P; A+M+U | Trigger timeout or consequential warnings. Capture timestamps, consequence text and recovery action. Users have usable notice and response opportunities. Repeated-warning recognition and discovery of beneficial new features require G-04. |

### CP-09 — Feedback and Notification

| Evidence ID and observable outcome | Existing QA references | Relationship / methods | Procedure, expected result and evidence |
| --- | --- | --- | --- |
| **CUX-29** — Actions, loading and changes receive appropriate status feedback. | CTL-146; CTL-150; CTL-151; CTL-155; CTL-157; CTL-158; CTL-159; PRACTICE-DYNAMIC-01; COMMENTS-01 | D; A+M+U | Capture action-to-feedback timing, accessibility events and focus. The relevant result is perceivable without an unnecessary focus move; state matches the actual outcome. Review whether users understand that the action succeeded. |
| **CUX-30** — Validation feedback supports correction without repeated interruption. | CTL-122; CTL-123; CTL-124; CTL-125; CTL-126; CTL-130; CTL-131; MW #249; MW #267; PRACTICE-FORM-02 | D; A+M+U | Enter invalid data at realistic speed and submit. Record announcement timing, message persistence and correction. Users identify and fix the problem; feedback does not inappropriately interrupt each keystroke. |
| **CUX-31** — Notifications use perceivable channels without competition. | CTL-032; CTL-152; CTL-153; CTL-154; MW #293; MW #294; MW #295; MW #296 | P; A+M+U | Generate concurrent critical/non-critical notifications. Record visual/audio/tactile delivery where supported, identity, announcement order and focus. Existing tests support multimodality but do not prove every channel or independent persistence controls: G-05. |
| **CUX-32** — Feedback remains usable for its task and urgency. | CTL-131; CTL-153; CTL-160; MW #28; MW #267; MW #279 | P; A+M+U | Retain display duration, dismissal/retrieval options and response trace. Users can perceive and act on feedback without overload. Set acceptance by task risk and user evidence; an arbitrary universal duration is insufficient. See G-05 for individual channel settings. |

### CP-10 — User Control and Choice

| Evidence ID and observable outcome | Existing QA references | Relationship / methods | Procedure, expected result and evidence |
| --- | --- | --- | --- |
| **CUX-33** — Users can operate tasks through supported input modes. | CTL-091; CTL-092; CTL-094; CTL-107; CTL-108; CTL-109; CTL-110; CTL-133; MW #63; MW #64; MW #65; MW #78; MW #79; MW #80; PRACTICE-KEY-01; PRACTICE-MULTI-01 | D; A+M+U | Complete end-to-end tasks on supported devices/AT using the chosen modes. Record reachability, activation, traps, target/gesture alternatives and equivalent result. Keep real device evidence separate from synthetic events. |
| **CUX-34** — Presentation respects user preferences. | CTL-014; CTL-016; CTL-019; CTL-020; CTL-022; PRACTICE-DISPLAY-01; THEME-01; PRACTICE-ZOOM-01 | D; A+M | Retain zoom/reflow, spacing, contrast/theme and reduced-motion views with OS/browser settings. Content and controls remain usable under the applicable source tests. Record unsupported platform preferences explicitly. |
| **CUX-35** — Users control media and can use appropriate output alternatives. | CTL-028; CTL-029; CTL-031; CTL-181; CTL-182; CTL-183; CTL-184; VIDEO-01; VIDEO-02 | P; A+M+U | Record playback/audio controls, captions, descriptions and actual AT reading. Check dialogue can be read and text heard through supported AT; test braille output where in scope. This is partial evidence of broad output choice, not proof of every format or braille combination. |
| **CUX-36** — Interaction precision, complexity and pace can be adjusted where needed. | CTL-197; CTL-198; CTL-199; MW #59; MW #60; MW #61; MW #62 | P; A+M+U | Record available settings and complete the same task before/after adjustment. Adjustment has a usable effect and does not remove core outcomes. Game/control remapping and unrepresented configurations need G-06. |

## 4. Supplementary outcome evaluations

These are **proposed additions**, not existing QA tests. They close specific gaps in the mapping and should have their own approved procedure and evidence record before use. Recruitment should reflect relevant cognitive needs, communication preferences and intersecting access needs; avoid treating diagnosis alone as a proxy for ability or collecting unnecessary health data.

| Local gap ID | Related principles / assertions | Proposed evaluation and acceptance basis | Evidence / responsibility |
| --- | --- | --- | --- |
| G-01 — Whole-task simplicity | CP-03; CUX-07–09; CP-05 CUX-17 | Give representative users a complete realistic task. Examine competing actions, unnecessary decisions, information volume, language complexity and repeated consumption. Agree essential information and success/assistance/error measures beforehand; consider a comparative design where useful. | Task trace, observed hesitation/rework, assistance, outcome and participant feedback. Researcher and designer judge whether avoidable burden has been reduced; no universal element-count rule. |
| G-02 — Recognition and memory | CP-07 CUX-22–24; CP-05 CUX-17 | Include a pause/interruption and return to the task. Check whether users can locate current state, instructions, choices and saved progress without recalling absent information. Include novice/experienced use and preferences. | Record where recall was required, help retrieval and independent completion; researcher validates. Agree acceptable independence and recovery for the task. |
| G-03 — Persistent-error support | CP-07 CUX-25; CP-04 CUX-12 | Repeat a realistic error or stalled step. Check that appropriate help, an alternative route or human support becomes available without blame, trapping or unwanted data collection. Do not assume intrusive monitoring or automatic advancement is the right design. | Trigger/support sequence, relevance of help, consent/privacy decisions and user recovery. Product owner defines support policy; researcher verifies that it helps. |
| G-04 — Habituation and useful novelty | CP-08 CUX-26–28 | Evaluate important warnings over representative repeated exposures, including a changed consequential warning. Separately check discovery of a useful new feature. Test recognition and understanding, without coaching participants to look for a warning; plan a suitable longitudinal/comparative study. | Exposure history, notice/comprehension/action, missed warnings and benefit discovery. Researcher determines an ethical protocol; safety-critical outcomes need stronger evidence than a single-session scan. |
| G-05 — Channel identity and control | CP-09 CUX-31–32 | Inventory visual, audible and haptic notification channels, concurrent sources and independent persistence controls. Check distinguishing identity, preference changes, timing, dismissal and retrieval on actual supported platforms. | Channel/settings matrix, device evidence and user response. The revised principle calls for equivalent perceivable feedback and suitable user-controlled channels, with priority and persistence specified. QA multimodality alone does not establish this. Record supported/unsupported channels and unresolved access needs for product-owner review. |
| G-06 — Complete control/output choice | CP-10 CUX-33–36 | Agree required input/output modes by context, then test full-task equivalence. For games/complex controls, test remapping, precision/complexity/pace settings and persistence. Check text can be heard through actual AT, dialogue read and braille output where in scope. | Supported-mode/configuration matrix, device/AT traces and user outcomes. Clearly separate tested, unsupported and untested combinations. An arbitrary format inventory does not demonstrate equivalent task completion. |

Principle scope decisions must remain visible. The original source’s ambitions for all input/output modes and notification channels were broader than many web products provide. The revised notification principle qualifies simultaneous channel delivery; broad input/output choice still needs explicit scope and evidence. Record the original expectation, agreed context, delivered capability, unsupported aspects and approving owner. An agreed scope limit is not evidence that the entire original principle has been fulfilled.

## 5. Evidence records and delivery decisions

### Scope and execution plan

Before testing, record product/build and environment, target tasks and critical outcomes, supported browsers/devices/AT, input/output modes, preference settings, component inventory, content states, sampling rationale and exclusions. Include default, loading, success, error, empty, expanded, modal, timeout and return/resume states where applicable. List expected observations and human acceptance criteria before reviewing results.

Use one result per source test, scoped target and environment. Reuse its evidence across linked principles, with the relevant interpretation attached; do not count the same observation as multiple independent successes. A principle can have many tests and a test can support several principles.

### Execution ledger template

Copy this row for each applicable source test/target. Keep lengthy traces and personal data outside public reports; link controlled evidence rather than embedding identifiable participant details.

| Run ID | Assertion / principle | Source test / revision | Target / state / build | Environment / method | Expected result | Actual result | Status | Evidence link | Defect / owner | Reviewer / date / retest |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Pending | Select CUX / CP IDs | Exact QA ID or MW number + pinned commit | Pending | Tool/version or human reviewer; device/AT/settings | Source requirement + scoped acceptance | Not executed | Not tested | Pending | Pending | Pending |

Use explicit statuses: **Pass**, **Fail**, **Not tested**, **Blocked**, **Cannot tell**, **Not applicable**, **Tool error**. These are reporting labels proposed here, not claimed source test-system enums. Preserve original tool outcomes as well. A script error is not a product pass or failure; insufficient evidence remains Cannot tell. Review N/A decisions and retests.

### Principle delivery record

| Principle | Applicable assertions / gap checks | Technical/manual results | User-outcome evidence | Remaining barriers / unsupported scope | Owner / decision / date | Delivery judgement |
| --- | --- | --- | --- | --- | --- | --- |
| CP-01 | Select applicable CUX and G IDs | Not tested | Pending | Pending scope assessment | Pending | Not assessed |
| CP-02 | Select applicable CUX and G IDs | Not tested | Pending | Pending scope assessment | Pending | Not assessed |
| CP-03 | Select applicable CUX and G IDs | Not tested | Pending | Pending scope assessment | Pending | Not assessed |
| CP-04 | Select applicable CUX and G IDs | Not tested | Pending | Pending scope assessment | Pending | Not assessed |
| CP-05 | Select applicable CUX and G IDs | Not tested | Pending | Pending scope assessment | Pending | Not assessed |
| CP-06 | Select applicable CUX and G IDs | Not tested | Pending | Pending scope assessment | Pending | Not assessed |
| CP-07 | Select applicable CUX and G IDs | Not tested | Pending | Pending scope assessment | Pending | Not assessed |
| CP-08 | Select applicable CUX and G IDs | Not tested | Pending | Pending scope assessment | Pending | Not assessed |
| CP-09 | Select applicable CUX and G IDs | Not tested | Pending | Pending scope assessment | Pending | Not assessed |
| CP-10 | Select applicable CUX and G IDs | Not tested | Pending | Pending scope assessment | Pending | Not assessed |

Judge delivery as **Supported in tested scope**, **Partially supported**, **Not supported**, or **Insufficient evidence**. These are evidence judgements, not certifications. To support a principle in a stated scope, resolve applicable failures, complete required expert/user evaluations, explain exclusions and record residual limitations. A passed subset with untested material outcomes remains partial or insufficient. Do not average technical passes into a cognitive delivery percentage.

### Agent-managed workflow

1. Read the pinned principle and QA sources; build the component/task inventory and draft applicability decisions. A human confirms task risks, supported modes and meaningful acceptance criteria.
2. Select existing QA tests and relevant ACT procedures from this matrix. Generate a run plan, specifying which checks use axe, browser scripts, actual-device testing, expert review or user research. Do not invent an axe rule for a conceptual outcome.
3. Execute authorised repeatable checks, retain actual observations and label tool errors. Capture screenshots, DOM/accessibility state, event logs and timing as appropriate; record scope and environment for every artefact.
4. Route semantics, clarity, perception, physical-device/AT checks and user-outcome evaluations to the right humans. An AI review or simulated persona may suggest issues but cannot stand in for participation by relevant users.
5. Assemble results into the execution ledger, link shared evidence, create actionable findings and retest changed behaviour. Keep source-test results separate from the broader principle judgement.
6. Produce a delivery summary with the principle records, unresolved gaps, unsupported capabilities and named human review. On source or product change, identify affected assertions and schedule proportionate re-evaluation.

## 6. Exact QA test index and reverse mapping

Every source test selected above is listed below with its exact source title. The final column provides reverse traceability to local evidence assertions; each assertion belongs to the principle shown in section 3. The use of a source test here does not extend its original scope.

### Canonical tests

[Open pinned source](https://github.com/Double-FW/QA_Accessibility_Testing/blob/c0450cdcb89484248ca4a15355ea5d71a58af043/Canonical%20Test%20Library.md)

| Source reference | Exact source title | Evidence assertions |
| --- | --- | --- |
| CTL-001 | Information Not Conveyed by Colour Alone | CUX-14 |
| CTL-002 | Error States Not Conveyed by Colour Alone | CUX-14 |
| CTL-003 | Required States Not Conveyed by Colour Alone | CUX-14 |
| CTL-004 | Selection State Not Conveyed by Colour Alone | CUX-06, CUX-14 |
| CTL-005 | Focus State Not Conveyed by Colour Alone | CUX-06 |
| CTL-007 | Data Series Not Differentiated Only by Colour | CUX-14 |
| CTL-008 | Text Contrast Minimum | CUX-10, CUX-26 |
| CTL-009 | Large Text Contrast Minimum | CUX-10 |
| CTL-011 | Control Boundary Contrast | CUX-04, CUX-10, CUX-26 |
| CTL-012 | Placeholder Contrast Adequacy | CUX-10 |
| CTL-014 | Text Resizes to 200 Percent | CUX-34 |
| CTL-016 | Layout Reflows Without Horizontal Dependency | CUX-09, CUX-34 |
| CTL-019 | Text Spacing Override Support | CUX-09, CUX-34 |
| CTL-020 | Zoom Capability Preserved | CUX-34 |
| CTL-022 | Motion Respects Reduced Motion Preference | CUX-27, CUX-34 |
| CTL-023 | Auto-Moving Content Can Be Paused | CUX-27 |
| CTL-024 | Auto-Moving Content Can Be Stopped or Hidden | CUX-27 |
| CTL-026 | Flashing Content Frequency Safety | CUX-27 |
| CTL-028 | Autoplay Audio Control | CUX-35 |
| CTL-029 | Autoplay Video Control | CUX-35 |
| CTL-031 | Separate Audio Streams Adjustable | CUX-35 |
| CTL-032 | Notification Sound Supplemented by Another Modality | CUX-31 |
| CTL-033 | Decorative Images Ignored by Assistive Technology | CUX-08 |
| CTL-034 | Informative Images Have Equivalent Text | CUX-13 |
| CTL-035 | Functional Images Describe Action | CUX-05, CUX-13 |
| CTL-036 | Complex Visuals Have Summary | CUX-13 |
| CTL-039 | Visible Rating or Graphic Indicators Have Text Equivalent | CUX-13 |
| CTL-045 | Page Title Describes Primary Content | CUX-24 |
| CTL-046 | Page Title Is Unique Within Context | CUX-24 |
| CTL-047 | SPA Title Updates on Route Change | CUX-24 |
| CTL-054 | Heading Structure Present | CUX-18 |
| CTL-056 | Heading Levels Follow Logical Hierarchy | CUX-18 |
| CTL-057 | Heading Text Is Descriptive | CUX-18 |
| CTL-058 | Visual Headings Match Semantic Headings | CUX-18 |
| CTL-060 | Source Order Matches Intended Reading Order | CUX-09, CUX-18 |
| CTL-063 | Related Thematic Items Use List Semantics | CUX-09, CUX-18 |
| CTL-066 | Data Tables Include Header Cells | CUX-21 |
| CTL-067 | Data Table Header Scope Defined | CUX-21 |
| CTL-068 | Data Tables Include Caption | CUX-21 |
| CTL-069 | Table Remains Structurally Intact on Small Screens | CUX-21 |
| CTL-070 | Scrollable Table Container Is Accessible | CUX-21 |
| CTL-071 | Interactive Elements Have Accessible Names | CUX-04 |
| CTL-072 | Visible Labels Exist for Form Inputs | CUX-11, CUX-22 |
| CTL-073 | Accessible Name Matches Visible Label | CUX-04 |
| CTL-075 | Label Remains Available During Input | CUX-11, CUX-22 |
| CTL-076 | Placeholder Does Not Replace Label | CUX-22 |
| CTL-078 | Instructions Associated With Relevant Field | CUX-11, CUX-22 |
| CTL-080 | Group Labels for Related Controls | CUX-19 |
| CTL-081 | Control Text Describes Purpose | CUX-04 |
| CTL-082 | Icon-Only Controls Have Equivalent Text | CUX-04 |
| CTL-083 | Supplementary Help Does Not Duplicate Primary Name | CUX-08, CUX-17, CUX-22, CUX-25 |
| CTL-086 | Breadcrumb Current Item Labelled Correctly | CUX-24 |
| CTL-087 | Current Navigation Item Exposed | CUX-24 |
| CTL-091 | All Interactive Elements Reachable by Keyboard | CUX-16, CUX-33 |
| CTL-092 | All Interactive Elements Operable by Keyboard | CUX-16, CUX-33 |
| CTL-093 | Standard Keyboard Activation Preserved | CUX-01, CUX-02 |
| CTL-094 | No Keyboard Trap | CUX-33 |
| CTL-095 | Focus Indicator Always Visible | CUX-06, CUX-26 |
| CTL-100 | Focus Moves to New Context on Open | CUX-24 |
| CTL-101 | Focus Returns on Close | CUX-24 |
| CTL-107 | Alternative Input Method Support | CUX-03, CUX-16, CUX-33 |
| CTL-108 | Gesture Functions Have Non-Gesture Alternatives | CUX-16, CUX-33 |
| CTL-109 | Pointer Precision Not Required for Basic Tasks | CUX-33 |
| CTL-110 | Target Size Meets Minimum Usability Threshold | CUX-33 |
| CTL-113 | Required Fields Indicated Programmatically | CUX-11 |
| CTL-114 | Required Fields Indicated Visually | CUX-11 |
| CTL-116 | Input Format Expectations Communicated | CUX-11 |
| CTL-119 | Related Inputs Grouped Semantically | CUX-19 |
| CTL-120 | Radio Groups Operate as One Logical Question | CUX-19 |
| CTL-121 | Checkbox Sets Grouped Where They Share a Question | CUX-19 |
| CTL-122 | Error Messages Shown When Submission Fails | CUX-12, CUX-30 |
| CTL-123 | Error Messages Are Announced to Assistive Technology | CUX-30 |
| CTL-124 | Error Message Identifies the Relevant Field | CUX-12, CUX-30 |
| CTL-125 | Error Message Explains the Problem | CUX-12, CUX-30 |
| CTL-126 | Error Message Tells User How to Fix It | CUX-12, CUX-30 |
| CTL-127 | Error Summary Provided for Multiple Errors | CUX-12 |
| CTL-128 | Error Summary Supports Navigation to Fields | CUX-12 |
| CTL-129 | User Input Preserved After Validation Failure | CUX-12, CUX-23 |
| CTL-130 | Validation Does Not Interrupt Every Keystroke Inappropriately | CUX-30 |
| CTL-131 | Error Cues Persist Long Enough to Be Used | CUX-28, CUX-30, CUX-32 |
| CTL-133 | Form Completion Possible by Keyboard Only | CUX-33 |
| CTL-134 | Password and Complex Input Assistance Available | CUX-23 |
| CTL-136 | Link Purpose Understandable in Isolation | CUX-05 |
| CTL-137 | Repeated Link Text Distinguishable Where Destinations Differ | CUX-05 |
| CTL-138 | Adjacent Duplicate Links Consolidated | CUX-08, CUX-17 |
| CTL-140 | Download or Alternate Format Links Identified | CUX-05 |
| CTL-144 | Current Navigation State Programmatically Exposed | CUX-06 |
| CTL-146 | Search Suggestions Announced Accessibly | CUX-29 |
| CTL-148 | SPA Route Changes Update Focus Position | CUX-24 |
| CTL-149 | SPA Route Changes Update History | CUX-24 |
| CTL-150 | Route Change Loading State Communicated | CUX-29 |
| CTL-151 | Status Messages Announced Without Forced Focus Change | CUX-29 |
| CTL-152 | Critical Alerts Perceivable in Multiple Modalities | CUX-26, CUX-31 |
| CTL-153 | Notifications Not Overbearing | CUX-08, CUX-17, CUX-27, CUX-31, CUX-32 |
| CTL-154 | Standard OS or Platform Notifications Used When Appropriate | CUX-31 |
| CTL-155 | Dynamic Content Discoverable After Update | CUX-29 |
| CTL-156 | Focus Not Stolen by Non-Critical Updates | CUX-27 |
| CTL-157 | State Changes Reflected Programmatically | CUX-06, CUX-29 |
| CTL-158 | State Change Announced When It Matters | CUX-29 |
| CTL-159 | Live Regions Used Appropriately | CUX-17, CUX-29 |
| CTL-160 | Update Timing Allows Perception | CUX-28, CUX-32 |
| CTL-161 | Disclosure Controls Expose Expanded State | CUX-06, CUX-20 |
| CTL-162 | Disclosure Controls and Content Linked | CUX-20 |
| CTL-163 | Collapsed Disclosure Content Removed Accessibly | CUX-20 |
| CTL-164 | Revealed Content Follows Control Logically | CUX-20 |
| CTL-165 | Accordion Items Use Heading + Button Pattern | CUX-02, CUX-20 |
| CTL-167 | Tabs Use Correct Roles When Enhanced | CUX-02, CUX-20 |
| CTL-169 | Only Active Tab Panel Exposed | CUX-20 |
| CTL-171 | Information Panels Not Used for Essential-Only Content | CUX-25 |
| CTL-176 | Action Dialog Uses Buttons vs Links Appropriately | CUX-02 |
| CTL-177 | Mega Menu Trigger Uses Button Semantics | CUX-02 |
| CTL-179 | Carousel Is Entirely User Driven | CUX-08, CUX-27 |
| CTL-181 | Native Media Controls or Accessible Equivalent Present | CUX-35 |
| CTL-182 | Media Does Not Autoplay Unexpectedly | CUX-35 |
| CTL-183 | Captions Available for Spoken Video | CUX-15, CUX-35 |
| CTL-184 | Audio Description or Equivalent for Essential Visual Information | CUX-15, CUX-35 |
| CTL-185 | Promo Has One Clear Primary Action | CUX-07 |
| CTL-186 | Promo Headline Consistent With Destination | CUX-07 |
| CTL-197 | Time Limits Can Be Extended, Disabled, or Adjusted | CUX-23, CUX-36 |
| CTL-198 | Timeout Warning Issued Before Expiry | CUX-23, CUX-28, CUX-36 |
| CTL-199 | Timeout Consequences Communicated | CUX-23, CUX-28, CUX-36 |
| CTL-200 | Unexpected Context Changes Prevented | CUX-01 |

### ACT-style procedures

[Open pinned source](https://github.com/Double-FW/QA_Accessibility_Testing/blob/c0450cdcb89484248ca4a15355ea5d71a58af043/Accessibility_ACT-Style_Test_System.md)

| Source reference | Exact source title | Evidence assertions |
| --- | --- | --- |
| ACC-01 | Keyboard Navigation and Toggle | CUX-02, CUX-20 |
| ACC-02 | Screen Reader Role and State | CUX-20 |
| CAR-01 | Navigation, Announcements, and Motion Control | CUX-27 |
| COMMENTS-01 | Structure, Labels, and Live Feedback | CUX-29 |
| CTA-01 | Semantic Link Integrity | CUX-02 |
| DISC-01 | Keyboard Toggle and State | CUX-20 |
| LINK-01 | Meaningful Link Text | CUX-05 |
| NAV-01 | Toggle and Focus Behaviour | CUX-02 |
| PANEL-01 | Trigger, Focus Transfer, and Return | CUX-24 |
| PRACTICE-AFF-01 | Visual and Semantic Alignment | CUX-04 |
| PRACTICE-ALT-01 | Non-Decorative Image Meaning | CUX-13 |
| PRACTICE-BIMEDIA-01 | Scripted Accessibility by Default | CUX-15 |
| PRACTICE-CAPTION-01 | Caption Placement Safety | CUX-15 |
| PRACTICE-COLOUR-01 | Meaning Survives Without Colour | CUX-14 |
| PRACTICE-CONTRAST-01 | Foreground and Interface Contrast | CUX-10, CUX-26 |
| PRACTICE-DISPLAY-01 | Preference Mode Support | CUX-34 |
| PRACTICE-DYNAMIC-01 | Necessary Announcements | CUX-29 |
| PRACTICE-FOCUS-01 | Visibility and Robustness | CUX-26 |
| PRACTICE-FORM-01 | Label Association | CUX-19 |
| PRACTICE-FORM-02 | Validation and Recovery | CUX-12, CUX-30 |
| PRACTICE-HEAD-01 | Heading Integrity | CUX-18 |
| PRACTICE-ICON-01 | Decorative and Functional Distinction | CUX-05 |
| PRACTICE-KEY-01 | Full Keyboard Operation | CUX-33 |
| PRACTICE-MOTION-01 | Reduced Motion Response | CUX-27 |
| PRACTICE-MULTI-01 | Equivalent Interaction Paths | CUX-03, CUX-16, CUX-33 |
| PRACTICE-ORDER-01 | Source Order Integrity | CUX-18 |
| PRACTICE-ROUTE-01 | Route Change Communication | CUX-24 |
| PRACTICE-TYPE-01 | Font Suitability | CUX-10 |
| PRACTICE-TYPE-02 | Spacing, Alignment, and Reflow | CUX-09 |
| PRACTICE-ZOOM-01 | 200% Usability | CUX-34 |
| PROMO-01 | Single Primary Destination | CUX-07 |
| THEME-01 | Cross-Theme Visibility and Meaning | CUX-34 |
| VIDEO-01 | Progressive Enhancement of Controls | CUX-35 |
| VIDEO-02 | Toggle Labels and Range Control | CUX-35 |

### Mobile/web numbered tests

[Open pinned source](https://github.com/Double-FW/QA_Accessibility_Testing/blob/c0450cdcb89484248ca4a15355ea5d71a58af043/Mobile_Application_and_Website_Test_Library.md)

| Source reference | Exact source title | Evidence assertions |
| --- | --- | --- |
| MW #16 | Instruction Availability Test | CUX-11 |
| MW #17 | Instruction Clarity and Error Prevention Test | CUX-11 |
| MW #28 | Status Message Timing and Persistence Test | CUX-32 |
| MW #36 | Typography Line Length Readability Test | CUX-09 |
| MW #55 | Actionable Element Distinguishability Test | CUX-04 |
| MW #56 | Actionable Element Semantic Identification Test | CUX-04 |
| MW #58 | Actionable Element Interaction Expectation Test | CUX-04 |
| MW #59 | Adjustable Interaction Parameters Test | CUX-36 |
| MW #60 | Adjustable Control Complexity Test | CUX-36 |
| MW #61 | Adjustable Input Precision Test | CUX-36 |
| MW #62 | Adjustable Pace and Timing Test | CUX-36 |
| MW #63 | Alternative Input Navigation Test | CUX-33 |
| MW #64 | Alternative Input Activation Test | CUX-33 |
| MW #65 | Gesture Independence Test | CUX-33 |
| MW #66 | Multi-Input Interaction Consistency Test | CUX-03 |
| MW #67 | Media Caption Synchronisation Test | CUX-15 |
| MW #69 | Media Alternative Format Completeness Test | CUX-15 |
| MW #78 | Multiple Interaction Method Availability Test | CUX-16, CUX-33 |
| MW #79 | Gesture Alternative Provision Test | CUX-16, CUX-33 |
| MW #80 | Interaction Method Flexibility Test | CUX-16, CUX-33 |
| MW #121 | Interaction Consistency Test | CUX-01 |
| MW #122 | Control Meaning Consistency Test | CUX-01 |
| MW #123 | Visual-to-Function Alignment Test | CUX-04 |
| MW #137 | Input Device Parity Test | CUX-03 |
| MW #155 | Consistent Labelling Across Contexts Test | CUX-01 |
| MW #156 | Repeated Element Function Consistency Test | CUX-01 |
| MW #176 | Text Readability Baseline Test | CUX-09 |
| MW #244 | Error Message Tone and Clarity Test | CUX-12 |
| MW #245 | Error Message Visibility and Placement Test | CUX-26 |
| MW #248 | Input Preservation on Error Test | CUX-23 |
| MW #249 | Inline Validation Timing Test | CUX-30 |
| MW #254 | Label Persistence Test | CUX-22 |
| MW #257 | Autocomplete Support Test | CUX-23 |
| MW #258 | Form Group Labelling Test | CUX-19 |
| MW #260 | Group Context Communication Test | CUX-19 |
| MW #267 | Error Message Persistence Test | CUX-30, CUX-32 |
| MW #268 | Error Message Presence and Perceivability Test | CUX-26 |
| MW #275 | Assistance Availability Test | CUX-22, CUX-25 |
| MW #276 | Context-Sensitive Help Test | CUX-25 |
| MW #277 | Assistance Discoverability Test | CUX-22, CUX-25 |
| MW #278 | Assistance Modality Test | CUX-25 |
| MW #279 | Feedback Appropriateness Test | CUX-28, CUX-32 |
| MW #290 | Grouped Component Representation Test | CUX-19 |
| MW #291 | Grouping Semantic Structure Test | CUX-19 |
| MW #293 | Notification Multi-Modal Delivery Test | CUX-31 |
| MW #294 | Notification State Change Announcement Test | CUX-31 |
| MW #295 | Notification Non-Disruptive Behaviour Test | CUX-31 |
| MW #296 | Standard Notification Usage Test | CUX-31 |
| MW #301 | Timeout Warning Test | CUX-28 |
| MW #302 | Timeout Data Loss Prevention Test | CUX-23 |
| MW #338 | Tooltip Non-Duplication Test | CUX-17 |
| MW #339 | Tooltip Non-Essential Information Test | CUX-17 |
| MW #340 | Tooltip Supplementary Value Test | CUX-17 |

## 7. Memory extension evaluations

The [coverage register](Cognitive_UX_Coverage_and_Delivery_Map.md) owns complete CP/M/COG/MEM/source relationships. The six guides own detailed MEM procedures; this section supplies entry points and prevents these additions being mistaken for existing CTL/ACT/MW tests. All statuses below are Not tested. Preserve the original source-test and CUX results; additional outcome evidence supplements them.

| Evaluation | Guide-owned procedure / design pattern | Existing partial support | Required evidence | Status |
| --- | --- | --- | --- | --- |
| MEM-PM-01 | [Create, find and act on a cue](Prospective_Memory_and_Reliable_Memory_Aids.md); COG-PM-01 | CUX-22, CUX-23, CUX-24, CUX-25, CUX-31, CUX-32, CUX-33 | Bounded tool checks + expert/actual AT review + relevant-user outcomes | Not tested |
| MEM-PM-02 | [Survive memory-aid failure and deletion](Prospective_Memory_and_Reliable_Memory_Aids.md); COG-PM-02 | CUX-22, CUX-23, CUX-24, CUX-25, CUX-31, CUX-32, CUX-33 | Bounded tool checks + expert/actual AT review + relevant-user outcomes | Not tested |
| MEM-RC-01 | [Resume a paused task](Interruption_Recovery_and_Task_Continuity.md); COG-RC-01 | CUX-12, CUX-23, CUX-24, CUX-29, CUX-33 | Bounded tool checks + expert/actual AT review + relevant-user outcomes | Not tested |
| MEM-RC-02 | [Recover stale or expired state](Interruption_Recovery_and_Task_Continuity.md); COG-RC-02 | CUX-12, CUX-23, CUX-24, CUX-29, CUX-33 | Bounded tool checks + expert/actual AT review + relevant-user outcomes | Not tested |
| MEM-CT-01 | [Distinguish similar current contexts](Interference_Source_Memory_and_Current_Context.md); COG-CT-01 | CUX-05, CUX-06, CUX-11, CUX-12, CUX-13, CUX-21, CUX-24, CUX-29 | Bounded tool checks + expert/actual AT review + relevant-user outcomes | Not tested |
| MEM-CT-02 | [Detect stale or superseded information](Interference_Source_Memory_and_Current_Context.md); COG-CT-02 | CUX-05, CUX-06, CUX-11, CUX-12, CUX-13, CUX-21, CUX-24, CUX-29 | Bounded tool checks + expert/actual AT review + relevant-user outcomes | Not tested |
| MEM-CF-01 | [Compare expectation and consequence](Familiarity_Comprehension_and_Confidence.md); COG-CF-01 | CUX-04, CUX-11, CUX-12, CUX-13, CUX-25, CUX-35 | Bounded tool checks + expert/actual AT review + relevant-user outcomes | Not tested |
| MEM-CF-02 | [Verify and correct a result](Familiarity_Comprehension_and_Confidence.md); COG-CF-02 | CUX-04, CUX-11, CUX-12, CUX-13, CUX-25, CUX-35 | Bounded tool checks + expert/actual AT review + relevant-user outcomes | Not tested |
| MEM-LR-01 | [Transfer safely across redesign](Learning_Redesign_and_Returning_Users.md); COG-LR-01 | CUX-01, CUX-02, CUX-03, CUX-22, CUX-24, CUX-25, CUX-33, CUX-36 | Bounded tool checks + expert/actual AT review + relevant-user outcomes | Not tested |
| MEM-LR-02 | [Return and relearn after delay](Learning_Redesign_and_Returning_Users.md); COG-LR-02 | CUX-01, CUX-02, CUX-03, CUX-22, CUX-24, CUX-25, CUX-33, CUX-36 | Bounded tool checks + expert/actual AT review + relevant-user outcomes | Not tested |
| MEM-NT-01 | [Manage competing channels and messages](Warnings_Habituation_and_Notification_Management.md); COG-NT-01 | CUX-26, CUX-27, CUX-28, CUX-29, CUX-30, CUX-31, CUX-32 | Bounded tool checks + expert/actual AT review + relevant-user outcomes | Not tested |
| MEM-NT-02 | [Evaluate repeated exposure and meaningful change](Warnings_Habituation_and_Notification_Management.md); COG-NT-02 | CUX-26, CUX-27, CUX-28, CUX-29, CUX-30, CUX-31, CUX-32 | Bounded tool checks + expert/actual AT review + relevant-user outcomes | Not tested |

Do not rename G-01–G-06. G-01 is supported by the continuity/context/comprehension evaluations; G-02 by prospective-memory, continuity and context evaluations; G-03 by comprehension/recovery where assistance is relevant; G-04 by MEM-NT-02; G-05 by MEM-NT-01/02; G-06 by applicable mode/configuration evidence across guides. These are supporting relationships, not claims that the supplementary evaluations exhaust each G outcome.

Product evidence remains pending. A document being drafted/reviewed/published must never fill a test result with Pass. Use the shared template for actual observations, limitations and human judgement.
