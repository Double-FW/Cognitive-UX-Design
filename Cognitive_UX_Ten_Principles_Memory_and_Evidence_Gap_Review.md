# Cognitive UX: ten-principle review, memory and evidence gaps

**Double FW Ltd · 5 November 2026 · Version 1.0**

## 1. Findings and scope

There are useful memory dimensions beyond span and ordered recall: **remembering future intentions; recovering a goal after interruption; distinguishing current information from an earlier encounter; retaining learned interaction skills; retrieving context; and judging whether a remembered or familiar answer is trustworthy**. These change what an interface should preserve, explain, repeat or make easy to retrieve.

The ten Double FW principles remain a useful organising framework. The largest need is more operational guidance and evidence under them, rather than a growing list of loosely overlapping principles. Memory is relevant across all ten, not only “Recognition Rather than Recall.”

This review checked the current public Cognitive-UX-Design files and selected related documentation in eight other Double FW repositories. The three recent guides are now present in the public cognitive repository. Their coverage is credited below, rather than described as missing. The public repository search returned 30 repositories; this is a targeted content review, not a line-by-line audit of every public file. “Gap” means no sufficient operational treatment was found in the inspected material, not proof that no sentence elsewhere mentions it.

No files in GitHub have been changed. Proposed additions, tests and wording below are recommendations. Existing repository guidance, research findings and UX inferences are distinguished throughout.

## 2. Evidence interpretation

- **N — Neuroscience evidence:** neural, neuropsychological or patient evidence concerning a mechanism. It does not establish that a proposed interface change works.
- **B — Behavioural evidence:** experiments concerning memory, attention, action or learning. This is often closer to the practical UX question than a brain-imaging result.
- **U — UX inference to validate:** an application proposed here, requiring task-appropriate evaluation with intended users.

A mechanism can be well established while an interface recommendation remains untested. Avoid reverse inference: observed activity in a brain area does not prove a user is overloaded, confused or remembering successfully. Neither a scanner nor a webpage word count supplies a universal cognitive-load threshold.

The earlier guide already corrects the historical reference to Miller’s **seven ± two** and explains Cowan’s smaller capacity estimates under particular conditions. Neither gives a maximum menu size. Retain that framing; do not replace one magic number with another. [E1]

## 3. Existing Double FW documentation register

The IDs below are local references for this review. Links point to actual inspected files; section names in the matrix identify the relevant treatment. Source blob identifiers are recorded in the appendix so later changes can be identified.

| ID | Inspected Double FW documentation | Relevant existing coverage |
| --- | --- | --- |
| D1 | [Cognitive Design Principles](https://github.com/Double-FW/Cognitive-UX-Design/blob/main/Cognitive%20Design%20Principles.md) | Ten-principle foundation |
| D2 | [Vision, Memory and Cognitive Screen Reader UX](https://github.com/Double-FW/Cognitive-UX-Design/blob/main/Vision_Memory_and_Cognitive_Screen_Reader_UX.md) | Memory demands, semantic structure, script/state records, comparisons and interruption/recovery |
| D3 | [Cognitive QA Evidence Matrix](https://github.com/Double-FW/Cognitive-UX-Design/blob/main/Cognitive_UX_Principles_QA_Evidence_Matrix.md) | Existing QA links, 36 assertions and G-01–G-06 outcome gaps |
| D4 | [User Research and Data Plan](https://github.com/Double-FW/Cognitive-UX-Design/blob/main/Cognitive_Accessibility_User_Research_and_Data_Plan.md) | Qualitative research, five satisfaction domains, variable contexts, trauma-informed methods and data governance |
| D5 | [Inclusive Chatbot Interface Reference](https://github.com/Double-FW/Accessible-Chatbots/blob/main/Inclusive_Chatbot_Interface_Reference.md) and [Testing Brief](https://github.com/Double-FW/Accessible-Chatbots/blob/main/Accessible_Chatbot_Testing_Brief.md) | Transcript navigation, controlled announcements, streaming, drafts, expiry and recovery |
| D6 | [Accessible Games and Other Dynamic Content](https://github.com/Double-FW/Inclusive-Games-Design/blob/main/Accessible%20Games%20and%20other%20Dynamic%20Content.md) | Practice modes, repeatable instructions, pacing, remapping, motion and dynamic feedback |
| D7 | [Charts, Maps and Complex Graphics](https://github.com/Double-FW/Accessible_Charts_Graphs_and_Maps/blob/main/Inclusive_Design_Charts_Maps_and_Complex_Graphics.md) | Layers, explicit relationships, comparison, shared state, persistent details and recovery |
| D8 | [Accessible Typography for UX and Brand Systems](https://github.com/Double-FW/Accessible-Typography-for-UX-and-Brand-Systems/blob/main/Accessible_Typography_for_UX_and_Brand_Systems.md) | Legibility, readability, comprehension and preference distinguished; contextual evaluation |
| D9 | [POUR through emotional brand/CX outcomes](https://github.com/Double-FW/POUR-for-Branding-Systems-and-CX/blob/main/The%20WCAG%20POUR%20principles%20reframed%20through%20emotional%20outcomes%20for%20branding%20systems.md) | Clarity, confidence, dignity and trust as experience outcomes |
| D10 | [Task Analysis Methodology](https://github.com/Double-FW/Task-Analysis-for-Comparative-Accessibility-Evaluation-of-Internal-Systems/blob/main/TA%20Methodology.md) | Goals, subtask structure, frequency, complexity and comparative cognitive burden |
| D11 | [Canonical QA Test Library](https://github.com/Double-FW/QA_Accessibility_Testing/blob/main/Canonical%20Test%20Library.md) | Structure, labels, errors, input retention, dynamic states, controls and timing; technical results do not establish all cognitive outcomes |
| D12 | [Ethical and Inclusive Data Use](https://github.com/Double-FW/Data_Ethics_and_Disability/blob/main/Ethical%20and%20Inclusive%20Use%20of%20Data%20Relating%20to%20Disabled%20People.md) and [Customer Research Framework](https://github.com/Double-FW/Data_Ethics_and_Disability/blob/main/CUSTOMER%20RESEARCH%20FRAMEWORK.md) | Usability versus learnability, customer context, evidence groups, sensitive data and comparable experience |

## 4. Each principle in UX context

**Coverage labels:** established = substantial practical guidance exists for the stated behaviour; partial = useful guidance exists but a material operational/evidence extension is needed. These labels concern documentation, not product compliance or a systematic quality rating of whole repositories.

| Source principle | UX and memory context | Existing documentation and evidence route | Assessment / important remaining need |
| --- | --- | --- | --- |
| **1. Standard Elements** | Familiar labels and interaction contracts let people reuse learned behaviour instead of solving the interface again. A redesign can create conflict between the old habit and the new action. | D2 §§5, 8–10 documents structure and behaviour. D3 CUX-01–03; D11 canonical 93 covers standard keyboard activation. D6 §2.3 provides practice without penalty. | **Established conventions; partial change guidance.** Add migration, transfer and relearning guidance for returning users, including safe treatment of consequential old habits. Link M-05/06; E5. |
| **2. Affordances and Signifiers** | A cue helps someone predict an action. Recognising a label is insufficient if the person misunderstands its consequence. Non-visual name, role, state and group context supply signifiers too. | D2 §§5, 7–10; D3 CUX-04–06; D5 controls and panel states; D11 canonical 71–82. | **Established structural guidance.** Extend tests to expectation versus actual consequence and current versus remembered context. Do not infer understanding from recognition alone. M-03/04; E4. |
| **3. Simplicity** | Reduce unnecessary processing, retained comparisons, decisions and navigation. Choice count and page length alone are weak proxies; a short but opaque hierarchy can be harder than a well-indexed long list. | D2 §§2, 6, 10; D7 Steps 3–5; D3 CUX-07–09/G-01; D10 complexity and comparative task analysis. | **Substantial guidance; outcome evidence remains task-specific.** Add an explicit demand review for retention, interference, navigation depth and interruptions. Extend existing G-01 rather than create a universal “simple enough” score. M-02/03. |
| **4. Clear Communication** | Understandable instructions and consequences support encoding and interpretation; they should remain available when relevant. Good contrast does not prove comprehension or later retrieval. | D8 distinguishes reading measures; D2 labels and scripts; D5 input/recovery; D3 CUX-10–13. | **Established foundations.** Extend to source/version context, misleading familiarity and consequence verification, especially in repeated transactions and AI-generated answers. M-03/04; E4. |
| **5. Redundancies** | Equivalent cues and input/output routes protect against missed information. Duplication can also create competing speech or processing. Effective support is not the same as sending everything through every channel simultaneously. | D6 §7.1; D7 §4.3; D5 controlled announcements; D2 §§6–7; D3 CUX-14–17. | **Established alternatives; partial arbitration guidance.** Specify who controls channels, which message is authoritative, how duplicate output is avoided and what remains retrievable. Coordinate with principle 9; M-07. |
| **6. Patterns** | Structure and familiar categories help people organise and retrieve information. Meaningful chunks depend on prior knowledge; unfamiliar jargon does not become a chunk because it sits in a card. | D2 semantic outlines, lists, labels and state records; D7 structured detail; D3 CUX-18–21; D11 headings, groups and tables. | **Established structure guidance.** Extend to context transitions and preserving meaningful cues when reorganising content. Event-boundary neuroscience motivates investigation, not a claim that each new page causes forgetting. M-02/05; E3. |
| **7. Recognition Rather than Recall** | Support retrieval without unaided recall, but also support future intentions, association of values to choices and reorientation. Recognition itself can be mistaken or detached from source. | D2 explicitly distinguishes several memory demands; D3 CUX-22–25/G-02/03; D4 interruption and diary methods; D11 canonical 75, 78, 129, 134. | **Strongest existing memory foundation; important extensions missing.** Develop prospective-memory/offloading and interference/source-memory guidance. Broaden the explanatory text beyond a recognition-versus-recall binary. M-01–04; E2–4. |
| **8. Variable Stimuli and the Pop-Out Effect** | Distinguish useful novelty, salience, familiarity and habituation. Repeated warnings may receive less attention; constant variation can also destroy predictability and increase distraction. | D1 identifies the risk. D3 CUX-26–28/G-04 calls for repeated-exposure evaluation; D4 describes a study approach; D6 limits disruptive motion. | **Explicitly recognised but not resolved operationally.** Create a warning/attention policy and longitudinal evaluation method. Preserve stable controls and vary only justified message content or priority cues. M-07; E6. |
| **9. Feedback and Notification** | Feedback reduces uncertainty about actions and outcomes. Competing feedback can interrupt an active goal. Confirmation must remain reviewable after the sound or toast disappears. | D5 notification matrix and streaming rules; D6 §§5.1–5.4; D7 Step 8; D3 CUX-29–32/G-05. | **Substantial component guidance; source wording needs qualification.** Replace an unconditional all-channel rule with equivalent perceivable options, user-controlled output and tested urgency rules. Extend persistent action records and interruption recovery. M-02/03/07. |
| **10. User Control and Choice** | Users should be able to select a mode, pace and support route that works. External references and reminders can reduce memory demands, but excessive setup can make the support itself burdensome. | D6 remapping/pacing; D7 alternatives for everyone; D5 stop/retry and clear limitations; D3 CUX-33–36/G-06; D4 preferences. | **Established access/control coverage.** Add low-effort reminders and memory aids, reversible setup, reliable saved state and transparent retention boundaries. Offer support without diagnosis-based profiling. M-01/04/08; E2. |

## 4. Important missing or underdeveloped topics

Priority is based on likely practical value and the inspected documentation gap, not on how impressive a neural explanation sounds. **P1** = first development wave; **P2** = follow-up extension. IDs are local recommendations, not published Double FW tests or principles.

| ID / priority | Proposed topic and why it matters | Existing support; what is actually missing | Suggested deliverable and evaluation |
| --- | --- | --- | --- |
| **M-01 · P1** | **Prospective memory and accessible cognitive offloading:** remembering to act later, not merely remembering a past fact. A saved application is useful only if the person can find and resume it or remember a deadline. E2 offers both behavioural and neural evidence. | D2 names prospective memory and D4 includes diaries. No detailed end-to-end reminder design was found: creating, delivering, recognising, acting on, rescheduling, cancelling and recovering a reminder. | Guide with event/time cues, calendar/task options, minimal setup, privacy-safe messages, user choice and a reminder lifecycle. Measure intended action completed, setup burden, mistaken/duplicate reminders and missed delivery; do not count delivery as success. |
| **M-02 · P1** | **Goal recovery after interruption and context changes:** recover what was being done, what is completed and the next action. E3 and E7 motivate continuity work. | D2 already contains recovery flows; D5 preserves drafts and transcript position. The gap is a cross-service specification spanning sessions, devices, authentication, expiry and handoffs, with clear saved-state limits. | State-continuity contract: saved answers, current goal, next action, last meaningful change, restoration target and incompatible/expired state. Test safe pause/resume and handoffs without induced distress or artificial memory quizzes. |
| **M-03 · P1** | **Interference, source memory and current-state provenance:** an earlier address, recipient, price or AI answer can compete with the current one. Familiar does not mean current or correct. E4 is directly relevant. | D11 checks input preservation, labels and state; D7 uses a shared state model. These do not fully test confusion across similar transactions or stale information. | Examples for repeated orders, multiple accounts and regenerated answers: clear identity, date/version where useful, changed values, selected context, review and undo. Test mistaken carryover and source identification; never invent a clinical interference score. |
| **M-04 · P1** | **Familiarity, understanding and confidence calibration:** a user may recognise a familiar control yet misunderstand what it commits them to, or distrust correct recall. E2/E4 distinguish relevant processes. | D4 measures confidence/comprehension, D8 separates preference from performance and D5 reviews consequential actions. Missing is an explicit reusable protocol comparing expectations, confidence, actual result and corrective information. | Pre-action consequence probe and post-action verification in safe research; accessible review, uncertainty/provenance cues and human support. Measure confident misunderstandings and informed correction, not confidence alone. Avoid turning every task into a test. |
| **M-05 · P1** | **Procedural learning, transfer and redesign:** skills and habits learned over repeated use can conflict with changed controls or location. Declarative knowledge and learned routines are not identical systems. E5 provides neuroscience grounding. | D1 demands consistency and D6 permits practice. No inspected guide fully describes migration, regression testing with returning users, or safe introduction of a changed interaction contract. | Change-impact checklist with stable terminology, reversible practice, targeted explanations and preserved shortcuts where appropriate. Compare new/returning users and consequences of old actions; neuroscience does not dictate one migration pattern. |
| **M-06 · P2** | **Learning, retention and relearning across time:** first-use success does not establish competence after a month or an infrequent annual task. | D12 already distinguishes usability from learnability; D6 supports tutorials/practice. Missing is an applied longitudinal protocol for retention, infrequent use and relearning. E8 supports learning research but not compulsory training for ordinary services. | Delayed-return studies, optional practice and retrievable instructions; distinguish necessary learning from avoidable memorisation. Measure retained task competence, reorientation and support needs after a task-relevant interval. |
| **M-07 · P1** | **Habituation, warning relevance and notification arbitration:** repeated low-value alerts can compete with genuinely important changes. E6 includes neural and behavioural warning evidence. | D3 G-04/05 and D4 identify evaluation needs; D5 already gives strong chat-specific rules. Missing is a cross-product priority/channel policy plus repeated-exposure evidence criteria. | Warning inventory, urgency/interruptibility rules, deduplication, persistence, preference controls and content-change cues. Test repeated use, changed consequential messages and recovery of the interrupted task. Do not prescribe random colours, animation or new sounds. |
| **M-08 · P2** | **Memory-support reliability and control:** an aid becomes a new dependency if summaries, saved drafts or reminders are inaccurate, hidden, expired or shared unexpectedly. E2 concerns effort, confidence and offloading. | D4/D12 provide ethical-data boundaries; D5 explains expiry and recovery. Missing is an explicit memory-aid reliability contract covering persistence, access, correction, deletion, offline/error states and shared-device privacy. | Specify exactly what is retained, for how long, where it can be retrieved and how failure is explained. Test successful aid use plus failed sync, changed accounts, deletion and restoration. Preserve user control; do not conflate AI conversation “memory” with human memory. |

**Best starting package:** M-01, M-02 and M-03. Together they cover “remember to do it,” “recover what I was doing” and “distinguish this action from the previous one.” M-05 and M-07 follow closely where redesigns or notifications are substantial. M-04 can be integrated into every consequential-task evaluation rather than requiring a separate repository.

## 5. Scientific grounding and limits

The UX examples above are **inferences proposed for testing**. The research supports distinctions and mechanisms; it does not prescribe a particular heading count, reminder frequency, recovery screen or channel mix. Relevant primary experiments and neural studies are included below; foundational reviews are labelled as such.

| Evidence ID | Research / type | What it supports | Boundary on the UX inference |
| --- | --- | --- | --- |
| **E1** | [Miller, 1956](https://doi.org/10.1037/h0043158), historical synthesis; [Cowan, 2001](https://pubmed.ncbi.nlm.nih.gov/11515286/), capacity review — **B** | Limited storage and processing; estimates depend on chunking, rehearsal and task conditions | Not a maximum-choice rule or a diagnosis-specific capacity estimate |
| **E2** | [Gilbert, 2015: intention offloading](https://pubmed.ncbi.nlm.nih.gov/25404057/); [Gilbert et al., 2020: optimal reminders](https://pubmed.ncbi.nlm.nih.gov/31448938/), experiments — **B**; [Gilbert, 2011: decoding delayed intentions](https://pubmed.ncbi.nlm.nih.gov/21414910/), human fMRI — **N** | Remembering a delayed action is a distinct practical demand; external cues can support intentions; effort and confidence influence offloading. Neural work examines distributed representation/storage of delayed intentions | Not proof that more notifications help, or that a named brain area determines an interface. Validate reminder burden, reliability and actual action completion |
| **E3** | [Baldassano et al., 2017](https://pubmed.ncbi.nlm.nih.gov/28772125/), narrative perception/recall with fMRI — **N** | Event structure relates to how ongoing experience is organised and remembered | Narrative event boundaries are not automatically equivalent to web-page transitions. No claim that every new page causes forgetting |
| **E4** | [Postle and Brush, 2004](https://pmc.ncbi.nlm.nih.gov/articles/PMC1200452/), behavioural/fMRI reanalysis — **N+B**; [Hockley and Consoli, 1999](https://pubmed.ncbi.nlm.nih.gov/10479824/), item/associative recognition experiment — **B** | Earlier information can interfere with current memory; recognition of an item and remembering its associations are distinguishable questions | Does not establish error rates in banking, shopping or screen-reader use; design and test analogous context-confusion cases |
| **E5** | [Squire and Zola, 1996](https://pubmed.ncbi.nlm.nih.gov/8942965/), neuroscience review of patient and experimental evidence — **N** | Declarative and nondeclarative learning/memory are not a single interchangeable faculty | A broad systems distinction, not “one UX component equals one brain region”; redesign effects require behavioural/user evidence |
| **E6** | [Kirwan et al., 2020](https://pubmed.ncbi.nlm.nih.gov/33364992/), repeated security warnings with fMRI/behaviour — **N+B** | Repeated computer-warning exposure can show repetition suppression/habituation | Visual warning-image findings do not directly establish spoken-alert outcomes or validate a particular novelty intervention |
| **E7** | [Trafton et al., 2003](https://doi.org/10.1016/S1071-5819(03)00023-5), interrupted-task experiment — **B** | Preparation and rehearsal around interruptions can influence task resumption | Supports a recovery hypothesis; it does not imply people should bear the burden of rehearsing every interface state |
| **E8** | [Karpicke and Roediger, 2008](https://pubmed.ncbi.nlm.nih.gov/18276894/), vocabulary-learning experiment — **B** | Retrieval practice can improve later retention in a learning task | Applicable to genuine learning contexts; do not add recall tests or compulsory training to access ordinary services |
| **E9** | [Liston et al., 2009](https://pubmed.ncbi.nlm.nih.gov/19139412/), psychosocial stress, behaviour and fMRI — **N+B** | Stress can affect prefrontal processing/attentional control in the studied context | Not a diagnostic model of an individual customer; does not show all memory is impaired or justify stressful testing |

E9 reinforces D4’s existing treatment of stress and variable context. It is a reason to strengthen application and evidence, **not to claim trauma, fatigue and time of day are undocumented**. The same caution applies to neurodivergence: investigate relevant support needs and intersections without assuming every diagnosis has the same memory profile.

Likewise, sight history is not a memory-capacity classification. D2 already addresses congenital/acquired sight loss and conceptual knowledge. Extend that work through task evidence rather than introducing a “blind users have worse memory” claim.

## 6. Targeted refinements to the original ten-principle text

These are proposed editorial directions, not changes applied to D1.

| Area | Recommended clarification |
| --- | --- |
| Introduction | Historical chronology alone does not demonstrate that usability heuristics are inherently neurotypical. Explain which user needs are insufficiently represented and show how the framework addresses them |
| Standard elements / patterns | Explain both the benefit of familiarity and the risk of outdated learned behaviour after change. Familiarity is useful but does not prove correct understanding |
| Simplicity | Describe avoidable processing, retention, navigation and decision burden. Replace any implication that fewer choices always means easier use; clarify effects on time/accuracy through evidence |
| Redundancies | Distinguish equivalent access routes from simultaneous duplicate messages. Preserve comparable information without creating competing output |
| Recognition rather than recall | Explicitly include future intentions, current-state/source context and recovery. Recognition is a useful support strategy, not a complete theory of memory |
| Variable stimuli | Separate habituation, relevant salience and disruptive novelty. Stable layout/controls should not be randomised to attract attention |
| Feedback / notification | Qualify the current unconditional visual/audio/haptic wording. Define accessible alternatives, priority, user settings, persistence and suppression of duplicate announcements. Record the change openly rather than silently reinterpreting the source |
| Control / choice | Include memory aids, pacing, saved state and accessible reference information. “Text can be heard” can be delivered through supported assistive technology; it need not mean a separate audio recording for every paragraph |

Do not add unsupported fixed “learning-style” matching or diagnose memory ability from interface behaviour. Preferences and useful alternatives can be offered and evaluated directly.

## 7. What does not need a new standalone topic yet

- **Basic semantic structure and screen-reader scripts:** D2 already provides detailed guidance. Extend its recovery/state records for M-02/03.
- **Tables, maps, colour and equivalent representations:** D2 and D7 already cover meaningful relationships and alternatives. Add memory-specific task cases rather than duplicate the material.
- **General legibility/readability:** D8 already distinguishes recognition, comprehension, performance and preference. Connect it to current-task communication rather than produce another typography primer.
- **Broad stress, trauma-informed research and daily capacity:** D4/D12 already cover these. Add a focused evidence note and task-specific validation; avoid presuming early morning/evening always means lower capability.
- **General learnability as a concept:** D12 explicitly distinguishes it from usability. The missing part is the longitudinal method in M-06.

Other memory phenomena—primacy/recency, spacing, context-dependent retrieval and the distinctiveness of items—can enrich these guides. They should not become separate principles without showing a material user problem and a useful additional method. In particular, do not use a “peak-end” or “unfinished tasks” slogan to optimise remembered satisfaction while actual safety, control or completion remains poor.

## 8. Development and evidence specification

Create these as focused chapters in Cognitive-UX-Design first, linking to specialised repositories. This avoids nine versions of a reminder or recovery policy. Promote a chapter to a separate repository only if its scope and maintenance needs justify it.

For each new chapter include: mechanism and evidence type; limits and alternative explanations; functional user needs; interface examples; interactions with screen-reader/braille/magnification/voice routes; task and state flows; privacy/control boundaries; existing QA links; new user-outcome evaluations; and accountable owners.

Each finding should have an explicit chain:

**Research result → plausible user risk → design hypothesis → observable task outcome → evidence → limitation.**

Example: interference research → confusion between similar recipient records → explicit recipient/account context and review → customer identifies the intended recipient and detects a stale selection → controlled task evidence → no inference about clinical memory capacity.

Use the existing five-domain satisfaction measures alongside correct/informed task outcomes, recovery, mistaken carryover and assistance. Add delayed follow-up only where retention or relearning is the actual question. Do not hide reference information during a usability task to create an artificial recall test; a memory aid should be evaluated while available.

Agent checks can verify saved-state consistency, labels, timestamps, restoration and duplicate announcement paths. Human review and relevant-user evaluation remain necessary for understanding, relevance and misleading familiarity. No EEG, pupil measurement or brain imaging is required to evaluate normal product delivery; behavioural evidence is usually the appropriate operational measure.

## Appendix: inspected source versions

The following are **file blob SHAs**, not commit identifiers. They record the retrieved content on the review date. Public links above use main for readability; re-read and compare these identifiers before relying on this gap review after a source update.

| Repository / file | Retrieved blob SHA |
| --- | --- |
| Cognitive-UX-Design / Cognitive Design Principles.md | `f7fc0c941eee8d28741b009db9d8082e07f092e1` |
| Cognitive-UX-Design / Vision_Memory_and_Cognitive_Screen_Reader_UX.md | `ff6541b1dd3ea3d765a55270986a15c846cf150c` |
| Cognitive-UX-Design / Cognitive_UX_Principles_QA_Evidence_Matrix.md | `fd22393068792aa2b68f73864d09de9482547d3c` |
| Cognitive-UX-Design / Cognitive_Accessibility_User_Research_and_Data_Plan.md | `885fdd3ab78e899a52e8cceba5b1f31edecd9772` |
| Accessible-Chatbots / Inclusive_Chatbot_Interface_Reference.md | `cb24ef09bdfec498a06f3b6ca7747e5e97a7f92e` |
| Accessible-Chatbots / Accessible_Chatbot_Testing_Brief.md | `9077b563706d20983835891745373b7b45a4e33e` |
| Inclusive-Games-Design / Accessible Games and other Dynamic Content.md | `611b7d6dd7ee98f3cdd54658f167134a81d8fbc7` |
| Accessible_Charts_Graphs_and_Maps / Inclusive_Design_Charts_Maps_and_Complex_Graphics.md | `2d4c581eecd14abf52e618e7cb85fd341364d485` |
| Accessible-Typography-for-UX-and-Brand-Systems / Accessible_Typography_for_UX_and_Brand_Systems.md | `bf8ab7112edb18549fbaf861aa921262b3d4180a` |
| POUR-for-Branding-Systems-and-CX / The WCAG POUR principles reframed through emotional outcomes for branding systems.md | `79181b0748799d134ef1aed79f2ff97c828d6a39` |
| Task-Analysis-for-Comparative-Accessibility-Evaluation-of-Internal-Systems / README.md | `a4449c0a1c58c7a9764585daf83939233b144af2` |
| QA_Accessibility_Testing / Canonical Test Library.md | `3602b4a6d1097b73f3583cc616995db84ccdde07` |
| Task-Analysis-for-Comparative-Accessibility-Evaluation-of-Internal-Systems / TA Methodology.md | `1d9ffd7e60eca40b594a622de9679ca8e7bc296d` |
| Data_Ethics_and_Disability / CUSTOMER RESEARCH FRAMEWORK.md | `2dea42d0df12f66d15af2b9900d98178cf1ae13f` |
| Data_Ethics_and_Disability / Ethical and Inclusive Use of Data Relating to Disabled People.md | `352bf43a2d34fe620be8c2852fe6d1f128df0be7` |

