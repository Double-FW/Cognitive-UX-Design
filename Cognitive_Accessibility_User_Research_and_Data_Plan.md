# Cognitive accessibility: user research and data plan

**Prepared for Double FW Ltd · Extension draft 1.1 · 5 November 2026**

## 1. Purpose and intended decisions

This plan combines qualitative research that explains barriers with quantitative measures that show how customer experience changes across tasks, designs, support needs and circumstances. It covers Navigation, Task Completion, Task Time Expectation, Content Consumption and User Preference Support. Its goal is independent, informed and satisfactory customer outcomes, including when someone has less energy, attention or available time.

The plan is ready to adapt to a service; it is not a record of completed research or a guarantee of GDPR compliance. Before collecting data, the controller must complete the service-specific decisions in section 12. Proposed questions, samples, time bands, retention periods and thresholds below are research design choices, not statutory requirements or validated clinical measures.

Use this alongside [Cognitive_UX_Principles_QA_Evidence_Matrix.md](Cognitive_UX_Principles_QA_Evidence_Matrix.md). CP, CUX and G identifiers refer to that companion document. Technical accessibility testing should remove known barriers before evaluative user sessions, while disabled people should also influence discovery and design. Participants should not spend research sessions rediscovering avoidable technical defects.

**Design decisions this evidence must support:** what to simplify; which instructions, alternatives and preferences to provide; how to preserve progress; where to offer human assistance; which barriers have disproportionate effects; and whether a change improves satisfaction without reducing comprehension, control, privacy or safe completion.

## 2. EAA basis and limits

Annex I, Section VII(j) of the European Accessibility Act addresses usage with limited cognition through an easier, simpler mode of operation. Section VII(k) concerns privacy when using accessibility features. Section VII explains when functional performance criteria apply; they are not a general permission to replace specific technical requirements. These are functional expectations, not diagnostic categories or a prescribed survey. Confirm the product/service scope and applicable national implementation separately. [S1]

This plan operationalises those outcomes through the research dimensions below. **Memory, attention, comprehension, planning, confidence and fluctuation are research constructs proposed here, not an EAA classification of people.** A support-need tag must never become a judgement of intelligence, legal capacity or eligibility for service.

| Outcome to investigate | Qualitative question / observation | Quantitative evidence | Companion evidence links |
| --- | --- | --- | --- |
| Simpler operation | Where does the person hesitate, backtrack, seek help or make an avoidable decision? | Independent completion; errors; navigation satisfaction; task-time expectation | CP-03; CUX-07–09; G-01 |
| Understanding and recognition | Can the person explain the choice and find information without remembering an absent instruction? | Content satisfaction; comprehension rubric; recovery; help findability | CP-04/07; CUX-11–13, 22–25; G-02/03 |
| Predictable structure and action | Does the action match expectations and is progress apparent? | Navigation satisfaction; wrong turns; recovery; completion confidence | CP-01/02/06/09; CUX-01–06, 18–21, 29–30 |
| Choice and support | Can the person find and use a useful mode, format, pace or human route? | Preference support satisfaction; preference activation and task parity | CP-05/10; CUX-14–17, 33–36; G-06 |
| Privacy while obtaining support | Can a person access help/preferences without revealing an unnecessary diagnosis or private information? | Optional privacy/control feedback; disclosure burden; support-route parity | CP-09/10; CUX-31–35; G-05/06 |

These measures can support evidence of delivery in tested scope; satisfaction alone cannot establish EAA conformity. Keep applicable legal requirements, source QA results, user outcomes and organisational design ambitions as separate evidence layers. Consumer-banking information has a sector-specific B2 complexity provision in Annex I Section IV(e); do not apply it as a universal website readability rule. [S1]

## 3. Research architecture and recruitment

### Two linked research streams

| Stream | Method and cadence | Output for designers | Limits |
| --- | --- | --- | --- |
| Qualitative discovery | Interviews, co-design and contextual walkthroughs before solution selection | Context, language, unmet needs, preferred support and risky assumptions | Explains possible mechanisms, not prevalence |
| Formative evaluation | Small moderated rounds on prototypes and complete journeys; retest after change | Observed barrier → design change → rationale → expected outcome | Repeated observations are not population estimates |
| Context diary | Optional short entries over 7–14 days at participant-chosen moments | Fluctuations, interruptions, safe return/resume, support sought | Burden and diary completion bias must be reported |
| Quantitative benchmark | Task-based testing plus the five-domain survey before/after meaningful releases | Comparable task outcomes and satisfaction by agreed segments | Needs comparable tasks, sampling and sufficient independent users |
| Live experience pulse | Short, optional surveys sampled across success, failure and abandonment where feasible | Trends and emerging barriers across lifecycle stages | Self-selection, coverage and non-response bias; service access must continue without research |

Start formative work with **12–18 participants across 2–3 rounds** as a planning budget, adjusting recruitment to the variety of tasks and needs. This is not a saturation guarantee. Recruit further where important needs or contexts are absent. Quantitative sample size follows the precision or effect-size question, not the qualitative recruitment budget.

Recruit through accessible customer invitations, disabled-person organisations, community partners and appropriate panels. Include people who abandon tasks, use assisted channels or cannot use the current design; recruiting only successful digital customers hides exclusion. Partners should distribute invitations rather than disclose member health information. Pay fairly for time, access costs and support; stopping or skipping questions must not reduce the promised session payment.

Include different levels of digital familiarity, literacy/language confidence, communication preferences, assistive technology and relevant intersecting sensory/motor access needs. Avoid collecting ethnicity, diagnosis or other sensitive attributes simply to fill a dashboard. Justify each attribute before collection and document its legal treatment.

### Optional functional segmentation

Ask participants to select what would help, with multiple selections, “something else” and “prefer not to say.” Do not require a diagnosis or medical evidence. Examples:

- “It helps when instructions stay visible.”
- “I prefer short steps and a clear next action.”
- “I need more time or the option to pause and return.”
- “I find it easier to use plain words or an example.”
- “I need fewer distractions or notifications.”
- “I prefer another way to read, listen, enter information or get help.”

Treat participant-linked answers as potentially revealing health/access needs and apply the sensitive-data assessment in section 8. Optional wording does not make the answers anonymous or non-sensitive. Tags may overlap: report each group’s denominator and never add overlapping groups as if they were distinct populations. The comparison group is “no listed support need reported,” not “normal” or “unimpaired.” Non-disclosure is a separate state, not absence of need.

Keep longer-term preferences separate from **session context**, which can change. Do not infer diagnosis, trauma, intoxication or cognitive impairment from clicks, typing, purchase history, voice, facial expression or time of day.

## 4. Qualitative protocol

Use realistic but fictitious data and sandbox transactions. Example tasks span discovery, understanding an offer, choosing/comparing, identification, purchase/booking/application, confirmation, support, cancellation and returning later. Include consequential choices and errors without real financial, legal or clinical consequences.

A typical session is 30–45 minutes with flexible duration, breaks and alternatives. Low-energy sessions may be 15–25 minutes. These are scheduling proposals; participants determine a workable arrangement.

1. **Before:** provide accessible information and separate choices about participation, recording, sensitive answers and recontact. Explain that the design is being tested, not the participant. Offer a supporter, preferred communication mode, captions and a non-recorded route.
2. **Check in:** confirm willingness, access settings, available time and optional energy/context answers. Say that they can skip, pause, stop or reschedule without explanation.
3. **Set the task:** establish what successful completion means and ask the optional time-expectation question before exposure. Do not coach the route.
4. **Observe:** record decisions, wrong turns, uncertainty, lost context, help requests, workarounds and whether consequences are understood. Use neutral prompts such as “What would you do next?”
5. **Probe meaning:** ask “What do you think this means?” or “What do you expect will happen?” Avoid asking the participant to repeat sensitive real-life events. Check essential understanding using a pre-agreed rubric, not a memory examination.
6. **Recover and resume:** include an agreed error, a pause or a return visit where relevant. Give assistance when requested; record it rather than withholding support to obtain a failure.
7. **Rate and reflect:** collect only applicable domain scores and an optional explanation. Ask what would have helped and which preferred mode was unavailable.
8. **Close:** confirm what may be retained, explain withdrawal and contact routes, pay as agreed and offer a neutral debrief. Do not promise clinical support or confidentiality beyond the stated safeguarding limits.

Think-aloud can increase task load and change timing. Offer silent observation or retrospective discussion. Do not combine think-aloud time with silent benchmark time without labelling the difference. A supporter’s responses must be distinguished from the participant’s own account; supported communication is not automatically a failure of independence.

### Designer insight record

| Field | Required content |
| --- | --- |
| Insight ID / evidence | Pseudonymous session/task IDs; controlled evidence references; source/build/date |
| Observed barrier | What happened, step/state and consequence; distinguish observation from interpretation |
| Context / need | Only agreed, relevant functional needs and session context; no diagnostic inference |
| Participant account | Redacted quotation with quotation/publication permission, or clearly marked paraphrase |
| Outcome affected | Navigation, completion, time expectation, consumption, preference support; CP/CUX/G links |
| Design hypothesis | Proposed change and mechanism, including trauma-informed considerations |
| Priority / owner | Severity, reach, confidence, reversibility and owner; a rare serious exclusion can outrank a frequent minor annoyance |
| Validation | Acceptance criteria, follow-up method, result and remaining uncertainty |

## 5. Quantitative scorecard

### Five satisfaction measures

Use a consistent **five-point satisfaction scale**: 1 Very dissatisfied; 2 Dissatisfied; 3 Neither satisfied nor dissatisfied; 4 Satisfied; 5 Very satisfied. Also offer **Not applicable / did not experience** and **Prefer not to answer** outside the numeric scale. Provide visible labels and accessible controls; do not require an answer. This is a bespoke instrument to pilot, not a validated psychometric scale or medical assessment.

| ID / aspect | Exact proposed question | When / applicability | Behavioural evidence beside the score |
| --- | --- | --- | --- |
| SAT-NAV / Navigation | “How satisfied were you with finding where to go and what to do next?” | After a navigation task or meaningful journey step, including unsuccessful attempts | Correct first destination, wrong turns, backtracking, help required |
| SAT-COMP / Task Completion | “How satisfied were you with what you were able to achieve?” | After every attempted task, including partial completion, failure or stopping | Verified outcome and critical errors; confidence that the result is correct |
| SAT-TIME / Task Time Expectation | “How satisfied were you with the time this task took compared with what you expected?” | After every attempted task; incomplete tasks remain eligible | Pre-task expectation, elapsed time, pauses, system waiting and whether completion occurred |
| SAT-CONT / Content Consumption | “How satisfied were you with understanding and using the information?” | After meaningful content use, in the participant’s chosen format | Essential comprehension, consequences understood, re-reading, format barriers |
| SAT-PREF / User Preference Support | “How satisfied were you with using this service in the way that works for you?” | After an opportunity to use or seek a preference/support route | Preference found, applied and effective; keyboard/voice/AT/format/pace parity; inability to find support is eligible dissatisfaction, not N/A |

After each sampled question, optionally ask: “What most affected your answer?” Limit invitations to avoid fatigue. For long journeys, sample one or two domains per step and offer the complete set at a suitable endpoint; record which questions were offered. A customer who stops must have an accessible route to give feedback without finishing the task.

For each domain report: full 1–5 distribution; valid response count; missing, skipped and N/A counts separately; satisfied share = ratings 4 or 5 divided by valid ratings; and, optionally, mean and median. A display score on 0–100 is **25 × (mean rating − 1)**. Label it as a transformed satisfaction mean, not percent successful or percent compliant. Do not average the five domains into a release decision; report them separately so gains cannot hide a deterioration in another aspect.

### Objective outcomes and task-time expectations

| Measure | Definition / calculation | Interpretation safeguard |
| --- | --- | --- |
| Task outcome | Independent success; success with assistance; partial; failed; participant stopped; research stopped. Define success and assistance before the task. | Normal assistive technology and chosen access preferences are not assistance. Human prompting/agent intervention is recorded by type; a legitimate assisted service route is also reported on its own terms. |
| Independent completion rate | Primary: independent successes / all task attempts, including research-stopped cases; also show a labelled sensitivity result excluding research-stopped cases | A task attempt starts when the participant accepts the task and can begin; record people unable to start separately. Never exclude customer failures or stops merely to improve the rate. |
| Expectation | Before the task: “How long would you expect this to take?” Offer numeric minutes, an agreed range or “not sure.” | Do not supply a reassuring estimate that primes the answer. Record whether an on-screen promise was visible. |
| Time | Elapsed start-to-result/stop, plus active time, system wait and participant-requested pauses where measurable | Report completion and stopped/failed durations separately. Keep raw timestamps restricted; do not invent active time where it cannot be observed. |
| Expectation gap | For completed tasks with numeric expectation > 0: actual elapsed minutes − expected minutes; optionally actual / expected | Report paired count and distribution. Range expectations are categorised below/within/above range; “not sure,” zero and missing are not imputed. An incomplete task is not “within expectation” because it ended quickly. |
| Comprehension | Correctly understood essential items / applicable essential items, using a task-specific rubric | Distinguish guessing and misunderstandings with consequences. Test use of available information, not unaided recall. |
| Preference effectiveness | Among those seeking a mode/preference, report found, applied and usable, with each denominator | Keep no need, not sought, unavailable, not found and not tested distinct. Do not treat a detected browser setting as proof a need was met. |
| Return/recovery | Successful resume/correction among applicable attempts; repeated entry and support needed | A pause may be a healthy choice. Resuming safely can be more valuable than immediate conversion. |

A fast but misunderstood purchase is not a good result. A longer task may reflect informed choice, accessible interaction or deliberate checking. Use time satisfaction, understanding, outcome and observed effort together. Never rank participants’ capability by speed.

### Sampling and analysis

Define primary tasks, domains, comparison groups, minimum meaningful differences and analysis before recruitment. Pilot the questions with people who use different communication/support approaches; check interpretation and whether response formats are accessible. If substantially different versions of a question are needed, label and assess comparability.

For a simple random sample of independent respondents, approximately **100 valid responses** gives a worst-case 95% margin of roughly ±10 percentage points for a proportion; approximately **385** gives about ±5 points. These are planning calculations, not guarantees for convenience panels, opt-in surveys, weighted data or repeated tasks. Each important group/comparison needs its own precision plan; the overall sample cannot supply it automatically. Use power analysis for A/B differences rather than borrowing these sample sizes.

Report counts and uncertainty intervals, recruitment source, task/build/method, survey invitation coverage and response rates. Compare like tasks and contexts. Repeated tasks from one person are correlated: use person-level summaries or an appropriate clustered/repeated-measures analysis. Counterbalance design order and use equivalent task variants where learning could bias comparisons. Treat exploratory multiple comparisons as exploratory.

Analyse the five domains by optional support need, energy/context, device/AT, customer lifecycle step and design version only where justified. Keep an unsegmented view for non-disclosers. Intersections can reveal barriers but sharply raise re-identification and small-sample risks. Qualitative findings from a few people can be actionable without pretending to be prevalence estimates.

## 6. Time, energy, stress and substance-related contexts

**Energy** here means self-reported resources; **functional capacity** means what the person can manage in this situation; **capability** concerns the task demands and available means of interaction. These are context descriptions, not assessments of legal decision-making capacity. Early morning and evening are hypotheses to investigate: some people function best then, and shift workers may have different patterns.

Ask, optionally and briefly: “How much energy do you have for this task right now?” (Very low / Low / Moderate / High / Very high); “Do you feel under pressure right now?” (Not at all / A little / Moderately / A lot / Prefer not to say); and “Would anything make this task easier today?” Make “prefer not to say” available for every context question. Do not ask why energy is low unless a necessary, separately approved study requires it.

| Context | Research approach | Design hypotheses / evidence sought |
| --- | --- | --- |
| Early morning / evening | Offer voluntary sessions at participant-chosen times. Illustrative local bands: 05:00–09:00 and 18:00–23:00; agree relevant bands and time zone before collection. Include other times for comparison. | Visible instructions, lower distraction, easy orientation, readable content, pause/resume; compare actual reported energy rather than assigning low capacity from the clock. |
| Fatigue / limited energy | Optional diary or paired sessions at naturally occurring higher/lower energy, only if the person wishes; never induce sleep loss or require endurance. | Short steps, preserved work, flexible timing, fewer repeated decisions and effective assistance; compare within-person patterns while acknowledging learning and context differences. |
| Stress, urgency or consequential choices | Use neutral fictional scenarios and retrospective interviews. Do not manufacture panic or involve live emergencies. Let people skip consequential topics. | Clear consequences, reversible choices, reassurance grounded in fact, timely help and no false scarcity; assess understanding, control and safe completion. |
| Trauma-related circumstances | Co-design with appropriately supported participants/representatives and use the protocol in section 7. No personal trauma history is required. | Predictability, choice, reduced forced disclosure, safe exits, non-blaming errors and participant-defined comfort. |
| Alcohol or recreational-drug effects | Default to retrospective accounts after the person is able and willing to consent, expert review and testing design features in safe, non-impaired sessions. Do not administer, encourage or require consumption. | Prevent accidental commitment; clear totals/consequences, confirmation, undo/cancellation where appropriate and safe return later. Generic fatigue tests cannot establish substance-specific effects. |
| Prescription medication effects | Participants may describe relevant functional effects voluntarily; do not ask for medicine, dose, diagnosis or medication changes. Study a reported support need, not presumed impairment. | Flexible timing, memory support, alternative modes and recovery; distinguish self-report from clinical causation. |

The default protocol **does not recruit people to attend while intoxicated**. If a participant appears unable to understand the study or distressed, stop collection, offer a paid reschedule and use the agreed safeguarding route. Do not label them as intoxicated or incapable without basis. Existing consent does not remove the need to check ongoing willingness and safe participation. Disability, low energy or taking medication is not itself evidence that someone cannot consent.

A specialist study involving people who are currently impaired or in acute crisis would need a separate protocol, competent ethical/safeguarding oversight and a specific legal assessment; it is outside this plan. The practical need to design for those customers can still be addressed now through safer methods above. No research invitation or survey should obstruct access to urgent support.

## 7. Trauma-informed research and design

The following applies the UK government’s trauma-informed practice principles to UX research and service design; it is an adaptation, not a claim that the guidance is a website standard or a trauma treatment. [S2]

| Principle | Research delivery | Design checks |
| --- | --- | --- |
| Safety | Preview topics; participant-selected setting; accessible stop/break route; clear safeguarding limits | Avoid surprise sensitive content, forced recounting and aggressive error messages; protect private content on shared screens |
| Trust | Explain purpose, recording, observers, retention and what happens next; no hidden observation | Honest progress, charges and consequences; clear data-use explanations and reliable confirmations |
| Choice | Skip, reschedule, use a supporter, decline recording or choose communication mode | Alternatives, reversible decisions, adjustable pace, human help and clear cancellation |
| Collaboration | Paid co-design and participant review of interpretations where agreed | Validate language, support and recovery patterns with relevant customers |
| Empowerment | Reinforce that the service is being tested; preserve pay when stopping | Explain options without blame or coercion; give users control of preferences and next steps |
| Cultural consideration | Avoid assuming one response to trauma; use suitable language/community expertise | Respect different communication and privacy needs without inferring sensitive identity |

Ask “Did you feel able to pause, change your mind or ask for help?” rather than requesting traumatic details. Offer an optional comfort/control rating; do not market it as a clinical trauma score. A visibly accessible “quick exit” requires threat-model review: it cannot promise to erase browsing history, logs or evidence on a monitored device. Safe exit, progress saving and screen privacy can conflict; research the context rather than applying one pattern universally.

## 8. GDPR-conscious identification and governance

### Legal decisions before collection

Distinguish EU GDPR and relevant Member State rules from UK GDPR, DPA 2018 and applicable UK amendments. A UK organisation serving EU customers may need both regimes considered. EAA alignment is not a lawful basis for unrestricted research profiling.

Document purpose, necessity and Article 6 basis for each processing activity. For this **voluntary recruited study**, consent is a proposed basis only where there is genuine choice, clear information and easy withdrawal. Participation agreement and GDPR consent are different decisions. Health/access-need disclosures may require an additional Article 9 condition; explicit consent is a candidate where valid, not an automatic solution. Do not assume commercial UX work qualifies for a research exemption. [S3–S5]

Information about illegal drug activity may also engage criminal-offence data rules depending on what is recorded and the jurisdiction; Article 9 explicit consent alone does not settle Article 10. Avoid collecting substance details or allegations in the standard study. Restrict and redact incidental disclosures, escalating genuinely necessary retention to the privacy lead. [S6]

Complete DPIA screening for the whole programme, including profiling, potentially vulnerable people, sensitive data, recordings, datasets combined and AI processing. A DPIA is required where processing is likely to present high risk; record the assessment and mitigate risks before launch. [S7]

### Identification model

1. Generate a random **study participant ID** and a separate random session ID. Do not embed email, initials, date of birth, diagnosis or customer account number; hashing an email is not sufficient anonymisation.
2. Keep contact details, scheduling, payment details and consent records in a restricted recruitment store. Store the participant-ID lookup separately with coordinator-only access.
3. Keep optional functional-need/context records in a restricted research dataset. Designers receive redacted observations, task outcomes and only the necessary group summaries; they do not receive recruitment identities.
4. For live feedback, default to a session-scoped identifier or no persistent identifier. Do not join feedback to customer accounts or marketing systems unless the specific purpose, basis, transparency and safeguards have been approved.
5. For optional longitudinal research, use a study-limited ID and explicit recontact choice. Supply a participant-held withdrawal token so records can be located without circulating a name. Never put the token in public reports.
6. Treat linked or linkable research records as personal data. Pseudonymisation reduces risk; it does not turn them into anonymous data. Assess residual linkability before claiming anonymisation. [S8]

### Privacy notice and choices

Provide accessible, layered information before collection: controller and privacy contact; specific purposes and bases; requested data and optional fields; recordings and observers; recipients/processors; overseas processing and safeguards; retention; applicable rights and complaint routes; withdrawal; and any automated processing. Explain that declining does not affect service or payment. Use short explanations, read-aloud/accessible formats and a chance to ask questions. [S9]

Separate choices for participation, recording, sensitive answers, publication of quotations and future recontact. A participant can do a non-recorded session. Check understanding using a respectful explanation in their own words; do not turn consent into an exclusionary memory test. Provide support without assuming a supporter has legal authority to consent on another adult’s behalf.

### Access, collection and lifecycle controls — proposed implementation

| Data / purpose | Collection and access | Proposed retention / disposal |
| --- | --- | --- |
| Contact and recruitment linkage | Coordinator only; minimum contact and scheduling fields; encrypted separate store | Delete 90 days after study closure unless separately opted-in panel membership justifies retention |
| Consent / permissions / payment | Restricted accountable owner; payment details outside research analysis | Set a documented accountability/statutory retention schedule before launch; no blanket indefinite retention |
| Audio/video/screens | Separate opt-in; mask real data; avoid faces/private rooms unless necessary; no default full-screen replay | Delete within 90 days of the session after validated redaction/coding; earlier if no longer needed |
| Pseudonymous task records, optional needs/context and survey | Approved research team; least privilege; encrypted transfer/storage; export logging | Review and erase or effectively anonymise within 6 months of study closure unless a justified, notified extension applies |
| Aggregate trends and redacted insight reports | Designers/product/QA; assess unique quotations and small-cell risks | Review after 12 months; retain only justified records; an “aggregate” label alone does not prove anonymity |

These periods are proposed caps, not GDPR rules. Confirm necessity, rights handling, legal holds and backup expiry before launch; keep the shortest justified period. GDPR does not prescribe one universal retention period. [S10]

Maintain a withdrawal/deletion workflow that reaches processors, working copies and linked datasets, with documented exceptions and backup expiry. Explain that genuine anonymisation removes the ability to locate a person’s contribution, and that already-issued aggregate findings may not be retractable; do not claim all data are anonymous while retaining a key.

Approve processor terms, subprocessors, security and international-transfer arrangements before using survey, transcription, hosting or AI vendors. EU transfers may require a valid transfer mechanism and assessment; UK transfers need their own applicable assessment. Use approved workspaces, no model training/secondary reuse, role access, bounded retention and incident response. [S11]

Do not collect raw form text, payment fields, session replay, IP/device fingerprints or full browsing history for routine metrics. Assess device storage/access separately from GDPR lawful basis. This plan defaults to consent-controlled optional research tracking; it does not assume every analytics technology is exempt. UK PECR now has conditional statistical/appearance exceptions with information and objection requirements; do not apply those exceptions automatically to sensitive study profiling or EU visitors. [S12]

### Publication and re-identification

Proposed reporting floor: suppress quantitative subgroup cells with **fewer than 10 distinct people**, plus complementary cells where subtraction would reveal them. This is a cautious starting control, not a guarantee of anonymity or a legal threshold. Review rare combinations, exact timings, AT/device combinations, unique stories and quotations; restrict further where needed. Use a minimum-precision rule as well as a disclosure rule: a cell can be safe to disclose yet too small for an inference. Preserve small-sample qualitative barriers in controlled, de-identified findings rather than discarding them.

Do not publish individual participant rows. Do not link research vulnerability/support tags to pricing, advertising, eligibility, fraud screening or individual sales pressure. Offer useful accessibility preferences to everyone rather than requiring sensitive profiling to unlock them.

## 9. Minimum data dictionary

Optional sensitive fields remain restricted even when attached to pseudonyms. Store precise timing only if needed for measurement; use derived broad local time bands in analysis exports. Do not collect location to calculate a time band: use an agreed study zone or an optional local band selected by the participant.

| Dataset / fields | Rule |
| --- | --- |
| Study: study_id, protocol_version, notice_version, applicable_jurisdictions, controller, approved_purposes | Define once; retain source revisions and approval references |
| Recruitment: participant_id, contact_ref, permission_records, recontact_choice | Separate identity store; no diagnosis required |
| Session: session_id, participant_id, task_id, design_version, method, device/AT category, chosen_mode | Do not collect exact device details unless needed for reproducibility |
| Optional needs: support_tags[], disclosure_status | Multi-select; record not asked / declined / none selected separately |
| Optional context: local_time_band, energy_band, pressure_band, interruptions, preferred_support | Do not store inferred impairment, medication name, drug type, dose or trauma history |
| Task: attempted, outcome, assistance_type, critical_error_count, expected_minutes_or_range, elapsed_seconds, pause_seconds, system_wait_seconds | Preserve provenance and missingness; no synthetic success values |
| Survey: aspect_id, question_version, offered, response_status, rating_1_5, redacted_comment_ref | response_status distinguishes answered / skipped / declined / N/A / not offered; no zero-score substitutions |
| Insight: insight_id, redacted_evidence_ref, observation, interpretation, CP/CUX/G links, design_hypothesis, owner, retest | Separate observed data from AI/human interpretation |
| Governance: collection_basis_ref, Article9_assessment_ref, permitted_uses, retention_due, access_class | Inherit restrictions into exports; log deletion/review without retaining erased sensitive content |

Use CSV/JSON exports with documented field definitions and score formulas; never embed contact data or raw consent text in analytical exports. Keep row-level data controlled. The public deliverable is an insight/score summary with disclosure review, not the research database.

## 10. Reporting and design decisions

Produce one report per key journey/task and design version. Show who was reached and who was missing, each satisfaction domain, objective outcomes, time expectation, relevant context comparisons, qualitative explanations and design actions. Separate moderated studies from live telemetry and convenience panels from representative sampling. State where results cannot support a conclusion.

| Report field | Example of what to record — not an observed result |
| --- | --- |
| Question | Can customers understand and safely complete cancellation with their preferred support? |
| Coverage | Recruitment source, functional-need mix, non-disclosure, contexts, supported modes and missing groups |
| Scorecard | Five satisfaction distributions/counts; independent and assisted outcomes; expectation-gap distribution; comprehension |
| Context | Energy/pressure and local time comparisons; no causal claim that evening caused a barrier |
| Insight | Where progress or consequences were unclear, with redacted evidence |
| Change | Persistent summary, clearer next action, safe return and human alternative |
| Decision | Named owner, priority, acceptance criteria and planned retest |
| Limitations | Missing groups, imprecision, repeat-exposure effects, survey non-response and residual privacy risks |

Before release, agree task-specific quality and equity targets using baseline evidence. Review high-impact comprehension/control failures even if overall satisfaction is high. Assess whether a proposed change benefits one group while making another route worse. Set confidence/precision rules and meaningful differences before comparisons; do not treat a small p-value as proof of useful improvement.

For paired A/B work, predefine primary outcomes and counterbalance/assign designs appropriately. Keep critical content, prices and consequences equivalent; avoid experimental pressure on customers in vulnerable circumstances. Improved conversion is secondary to informed, safe and satisfactory outcomes. Conversion should never replace cancellation success or effective help as the target for those tasks.

## 11. Agent and human responsibilities

| Work | Agent contribution | Accountable human |
| --- | --- | --- |
| Scope and mapping | Draft task/CP/CUX/G coverage and identify missing evidence | Research lead and product/design owner confirm scope and claims |
| Recruitment and consent | Assemble accessible materials from approved templates; support scheduling without exposing needs | Coordinator checks accessibility and consent process; privacy lead approves basis |
| Moderation / safeguarding | Approved assistance only; no automated diagnosis, capacity assessment or distress classification | Trained researcher conducts sessions and applies stop/escalation protocol |
| Coding | Redact, suggest themes and link evidence with confidence flags | Researcher validates interpretation, quotations and cultural/contextual meaning |
| Metrics | Calculate predefined denominators, missingness, intervals and disclosure suppression | Analyst validates calculations, dependence and sampling limitations |
| Reporting | Draft scorecards, gap findings and traceable design tickets | Designer/research lead reviews evidence; product owner decides priorities |
| Governance | Enforce permissions, retention reminders and export rules; flag exceptions | Controller/privacy lead owns lawful processing and rights response; security owner manages controls |

An agent must not invent participant testimony, fill missing scores, simulate a disabled-user sample or label inferred intoxication/trauma. AI-generated hypotheses remain hypotheses. No participant-level data should be sent to an unapproved model or used to train a general model. Human review remains necessary for consequential interpretation and safeguarding.

## 12. Implementation sequence and launch record

1. **Scope:** choose priority lifecycle tasks, jurisdictions, builds, CP/CUX/G links, relevant contexts and supported modes. Agree design decisions the evidence will inform.
2. **Governance:** name controller, research lead, privacy/security owners and processors. Approve purpose/basis assessment, sensitive-data treatment, DPIA screening/assessment, notice, rights process, transfer/security controls and retention.
3. **Protocol:** co-design accessible recruitment/materials, compensation and safe participation rules. Pilot the five questions, task-success rubric, expectation capture and optional support/context tags.
4. **Qualitative rounds:** investigate barriers and iterate before larger measurement. Include safe return/error recovery and participant-chosen energy/time contexts.
5. **Benchmark:** calculate the needed independent sample, predefine comparisons, recruit beyond successful digital users, execute and report missingness/uncertainty.
6. **Design/retest:** link each priority finding to a design change, owner and acceptance evidence. Check for new barriers in other routes/groups.
7. **Operate:** run proportionate optional pulses, periodic qualitative follow-up and source/protocol review; honour objections/withdrawals and erase data on schedule.

| Launch decision | Required record |
| --- | --- |
| Product/task and legal scope | Applicable EU/UK regimes and EAA service/product relevance; scope owner |
| Lawful processing | Purpose-by-purpose Article 6 basis; Article 9/10 treatment where relevant; necessity and alternatives |
| Consent and access | Tested accessible materials; separate permissions; refusal/withdrawal and safe-stop process |
| Safeguarding | Trained moderator, distress response, emergency-service boundaries and no induced impairment |
| Measurement | Question versions, denominators, sampling/power, context bands and pre-agreed decision criteria |
| Security/privacy | DPIA outcome, access map, processors/transfers, retention/backup deletion and disclosure review |
| Evidence traceability | Task/build/method, matrix revision and insight-to-change-to-retest records |

Until these service-specific records are complete, use this document for planning and synthetic-data rehearsal rather than participant data collection.

## 13. Sources and interpretation notes

Sources checked 5 November 2026. Regulatory guidance can change; check the applicable jurisdiction and current implementation before launch. The sources ground the legal/practice boundaries; the survey, tagging model and operational research design are Double FW planning proposals in this document.

- **S1 — EAA:** [Directive (EU) 2019/882](https://eur-lex.europa.eu/eli/dir/2019/882/oj), particularly Annex I Sections IV(e) and VII. Functional criteria do not define clinical cohorts, a survey or a cognitive satisfaction threshold.
- **S2 — Trauma-informed practice:** [UK government working definition](https://www.gov.uk/government/publications/working-definition-of-trauma-informed-practice/working-definition-of-trauma-informed-practice). Adapted here from practice guidance to research/service design.
- **S3 — Consent:** [EDPB consent guidance summary](https://www.edpb.europa.eu/system/files/2026-04/edpb-summary-consent_en.pdf) and [ICO valid consent](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/lawful-basis/consent/what-is-valid-consent/). UK guidance notes ongoing legislative updates; distinguish study ethics from the processing basis.
- **S4 — Sensitive data:** [ICO special category data](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/lawful-basis/a-guide-to-lawful-basis/special-category-data/), including health-related inferences and the Article 6/9 distinction.
- **S5 — Research conditions:** [ICO principles and grounds for research processing](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/the-research-provisions/principles-and-grounds-for-processing/). Research conditions require their own necessity and safeguards assessment.
- **S6 — Offence data:** [ICO criminal offence data](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/lawful-basis/a-guide-to-lawful-basis/criminal-offence-data/) and [scope, including allegations](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/lawful-basis/criminal-offence-data/what-is-criminal-offence-data/).
- **S7 — DPIA:** [ICO when a DPIA is needed](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/accountability-and-governance/data-protection-impact-assessments-dpias/when-do-we-need-to-do-a-dpia/).
- **S8 — Pseudonymisation:** [ICO guidance](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/data-sharing/anonymisation/pseudonymisation/) and [EDPB distinction from anonymisation](https://www.edpb.europa.eu/topics/ai-and-technology/anonymisation-pseudonymisation_en).
- **S9 — Transparency and rights:** [European Commission information for individuals](https://commission.europa.eu/law/law-topic/data-protection/information-individuals_en).
- **S10 — Principles and retention:** [European Commission GDPR principles](https://commission.europa.eu/law/law-topic/data-protection/information-business-and-organisations/principles-gdpr_en) and [ICO storage limitation](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/data-protection-principles/a-guide-to-the-data-protection-principles/storage-limitation/).
- **S11 — Transfers and processing contracts:** [European Commission SCC questions and answers](https://commission.europa.eu/law/law-topic/data-protection/international-dimension-data-protection/new-standard-contractual-clauses-questions-and-answers-overview_en).
- **S12 — Device storage/access:** [ICO exceptions, including statistical purposes and appearance](https://ico.org.uk/for-organisations/direct-marketing-and-privacy-and-electronic-communications/guidance-on-the-use-of-storage-and-access-technologies/what-are-the-exceptions/). These are UK rules with conditions, not universal EU analytics exemptions.

## 14. Applied memory-study modules

This extension adds executable study modules owned by the six guides and mapped in the [coverage register](Cognitive_UX_Coverage_and_Delivery_Map.md). Use the main plan’s consent/basis, sampling, privacy, compensation, safe stopping, disclosure and retention decisions. No module authorises collection by itself. All MEM procedures are Not tested.

| Module / evaluation | Additional preparation | Outcomes and safeguards |
| --- | --- | --- |
| Reminders / MEM-PM-01/02 | Agree a useful delayed action, timing/channel, saved-task route and failure fixtures | Record setup, retrieval, intended action, missed/duplicate cues and privacy. Delivery/opening is not task success; no obligation to respond outside agreed contact windows |
| Pause/resume / MEM-RC-01/02 | Define what is saved and a voluntary pause/return/handoff; use fictitious changes/expiry | Record recovered goal, next action, retained values, correction and assistance. Do not surprise participants with distressing interruptions |
| Similar contexts / MEM-CT-01/02 | Prepare fictitious similar entities and version changes; define which values need verification | Record current-context selection and mistaken carryover. Do not interpret these as diagnosis or memory-capacity scores |
| Understanding / MEM-CF-01/02 | Predefine material consequences and a neutral explanation rubric | Compare expectation, observed decision, actual state and optional confidence. Allow references/help; cancellation can be informed success |
| Returning users / MEM-LR-01/02 | Record prior exposure, compare actual interaction contracts and agree task-relevant follow-up interval | Report learning/transfer, old-habit errors, reacquisition, attrition and exposure. Do not extrapolate a short delay to annual retention |
| Repeated messages / MEM-NT-01/02 | Define safe exposure schedule, meaningful changed consequence and channel settings | Record notice, comprehension, action and disrupted-task recovery. Do not coach warning hunting or habituate people to genuine safety threats |

### Study identity and analysis extension

Record protocol/module version, task/build, invitation/attempt/response, exposure number, prior task/design experience, reminder configuration, planned versus actual interval, assistance, interruption reason where voluntarily provided and return outcome. Collect only necessary fields. A common participant ID may link repeated observations inside the approved study; do not join it to marketing or unrelated service data.

Predefine the primary outcome, eligible denominator and stopped-task treatment for each module. For delayed intentions report separately: reminders requested, successfully scheduled, delivered if knowable, noticed if reported, tasks attempted and intended actions completed. Missing follow-up is unknown, not success or failure; disclose attrition and use sensitivity analysis where relevant. Keep source/technical failures separate from participant behaviour.

For change/relearning studies, distinguish new from experienced users and counterbalance where appropriate; exposure and task familiarity can bias later observations. Account for repeated observations within a person. A convenience panel does not supply representative rates merely because it completes many sessions.

Retain the five satisfaction domains as separate measures. Add only task-specific behavioural outcomes and a clearly labelled optional confidence question where justified; do not replace comprehension or correct current-state identification with self-report. All standard references, memory aids and preferred AT remain available during usability evaluation.

### Review and publication

The research lead approves the module, moderator and sample plan; privacy/security owners approve data/processor handling; product/design owns acceptance and follow-up changes. Use the [delivery template](Cognitive_UX_Design_and_Evidence_Template.md) for actual results. Publish controlled, redacted findings with scope and uncertainty; the public repository contains methods, not participant-level data.
