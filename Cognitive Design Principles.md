# 10 Cognitive Design Principles

**Double FW Ltd · Revised draft 2.0 · 5 November 2026**

Cognitive UX design helps people understand, navigate and control an experience without unnecessary demands on attention, memory, language or interpretation. These ten principles organise that work. Their application should account for neurodivergent people, cognitive/learning disabilities, vision and other access needs, familiarity, fatigue and the circumstances of use. No diagnosis or sight history determines one fixed capability profile.

Use these as design guidance alongside technical accessibility requirements and intended-user evidence. Historical origins alone do not establish whose needs a heuristic serves; evaluate the actual barriers and outcomes. Laboratory memory estimates do not set a universal choice count. Research, UX inference and product evidence are kept separate in the [science register](Cognitive_Science_Evidence_Register.md).

The CP-01–CP-10 references match this document’s unchanged source order and the existing QA matrix. This revised draft clarifies substantive points; see the [changelog](CHANGELOG.md). No independent review, publication or product conformity is implied.


## 1. Standard Elements

Use familiar components, terminology and interaction contracts consistently so that users can apply what they already know. Equivalent controls should retain equivalent meaning, keyboard behaviour and state across visual, speech and other supported presentations.

Consistency includes the transition from an earlier version of the service. Identify where a remembered action could cause an unintended consequence after redesign. Keep stable conventions where useful; explain and test justified changes. A familiar appearance is not proof that the user understands a new action.

Apply [learning and redesign guidance](Learning_Redesign_and_Returning_Users.md); existing QA CUX-01–03 supports limited observable behaviours.

## 2. Affordances and Signifiers

Make the perceived action agree with the actual action. Visible styling, labels, icons and non-visual name/role/state relationships should help users predict what will happen and distinguish choices. Do not rely on position or colour alone.

Use descriptive actions that remain understandable when encountered through a screen reader’s links or controls navigation. Prefer coherent visible and accessible wording. Before consequential actions, make the current entity, cost and commitment available; recognition of the control is not sufficient evidence of comprehension.

Apply [current-context guidance](Interference_Source_Memory_and_Current_Context.md) and [comprehension guidance](Familiarity_Comprehension_and_Confidence.md); see CUX-04–06.

## 3. Simplicity

Reduce unnecessary processing, retained comparisons, navigation, repetition and decisions while preserving meaningful choice. Information volume, clutter, ambiguity and complex language can increase effort; fewer items or fewer screens do not automatically make a task easier.

Group familiar concepts meaningfully and keep relevant reference information available. A well-indexed list can be easier than a short but opaque hierarchy. Test the complete task, including interruptions and recovery, rather than scoring simplicity by element count or an arbitrary memory limit.

Apply the [screen-reader UX guide](Vision_Memory_and_Cognitive_Screen_Reader_UX.md) and [continuity guide](Interruption_Recovery_and_Task_Continuity.md); see CUX-07–09 and G-01.

## 4. Clear Communication

Make important information noticeable, distinguishable and interpretable. Use legible text, meaningful structure, appropriate contrast and clear relationships. Choose wording, examples and representations that support the intended decision, and keep essential instructions retrievable.

Errors should identify the issue and a practical remedy without blame or loss of valid work. Separate reading accuracy, understanding, confidence and preference. Explain whether information is current, estimated, pending or superseded where that distinction affects the task.

Apply [comprehension/confidence guidance](Familiarity_Comprehension_and_Confidence.md) and [source/context guidance](Interference_Source_Memory_and_Current_Context.md); see CUX-10–13.

## 5. Redundancies

Provide equivalent cues and interaction routes so that missing one cue does not remove meaning or control. Useful redundancy may include text for audio, labels for icons, non-colour state cues, alternative formats and alternative input methods.

Balance reinforcement against duplicated effort and competing output. Providing accessible channels does not mean forcing every channel to operate simultaneously. Keep the relevant meaning consistent, offer user control and avoid repeated announcements of the same event. Support both unfamiliar and experienced users without assigning fixed learning styles.

Apply [notification management](Warnings_Habituation_and_Notification_Management.md) and the screen-reader guide; see CUX-14–17.

## 6. Patterns

Organise information and controls into understandable relationships, groups and hierarchies. Use meaningful headings, lists, labels and other semantics so that structure can be navigated and retrieved through different presentation modes.

A chunk must make sense to the user; a box or category name does not create understanding by itself. Preserve useful context across steps and changes. Let people revisit their current choices and related information instead of memorising a sequence.

Apply the [screen-reader guide](Vision_Memory_and_Cognitive_Screen_Reader_UX.md) and [continuity guide](Interruption_Recovery_and_Task_Continuity.md); see CUX-18–21.

## 7. Recognition Rather than Recall

Make objects, actions, choices, instructions and help identifiable and retrievable so people do not need to remember information that the service could keep available. Preserve appropriate input and expose current selections, progress and next actions.

Memory support also concerns future intentions, recovery after interruption and distinguishing current information from similar earlier encounters. Familiarity can be misleading; retain the associations needed to verify an action. Offer relevant help after difficulties without intrusive diagnosis, blame or automatic advancement that removes user control.

Apply [prospective memory](Prospective_Memory_and_Reliable_Memory_Aids.md), [continuity](Interruption_Recovery_and_Task_Continuity.md), [context](Interference_Source_Memory_and_Current_Context.md) and [comprehension](Familiarity_Comprehension_and_Confidence.md); see CUX-22–25 and G-02/03.

## 8. Variable Stimuli and the Pop-Out Effect

Make a genuinely important change distinguishable without destabilising the interface. Repeated low-value warnings can lose attention; novelty can also distract, obscure meaning or disrupt a task. Treat salience, habituation and harmful interruption as different issues.

Keep familiar controls and meaningful priority cues stable. Reduce unnecessary warnings, identify changed consequences and provide a clear remedy. Evaluate repeated exposure and actual understanding/action; do not prescribe random layout, colour, animation or sound changes to attract attention. Useful new features should be discoverable without repeated coercive promotion.

Apply [warnings and notification management](Warnings_Habituation_and_Notification_Management.md); see CUX-26–28 and G-04.

## 9. Feedback and Notification

Give timely, clear feedback about actions, state changes, errors and outcomes. Distinguish success, pending, partial and failure. Keep consequential information available long enough to act and, where appropriate, retrievable afterwards.

Provide equivalent perceivable feedback and suitable user-controlled channel options on supported platforms. Do not require visual, audible and haptic output to run simultaneously. Define priority, interruption, persistence and channel behaviour; avoid competing application audio and AT speech, duplicated alerts and routine focus theft. Record unsupported channels and product scope explicitly.

This qualifies the earlier unconditional all-channel wording; it does not excuse inaccessible feedback or remove applicable legal/technical requirements. Apply [notification management](Warnings_Habituation_and_Notification_Management.md) and [continuity](Interruption_Recovery_and_Task_Continuity.md); see CUX-29–32 and G-05.

## 10. User Control and Choice

Enable people to choose effective interaction, presentation, pace and support routes. Support applicable keyboard, pointer, touch, voice and other access modes without forcing unnecessary disclosure. Preserve equivalent task outcomes across supported routes and document unsupported combinations.

Make text available to supported text-to-speech/assistive technology, dialogue available in readable form and complex interactions configurable where needed. This does not require a separately recorded audio track for every paragraph. Consider braille, magnification, media controls and format choices in their real contexts.

Include low-effort reminders, retrievable summaries, saved state and reliable memory aids. Explain persistence, privacy, correction and deletion; allow users to change their choices. Apply [memory-aid guidance](Prospective_Memory_and_Reliable_Memory_Aids.md); see CUX-33–36 and G-06.
