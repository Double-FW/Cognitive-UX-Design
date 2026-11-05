# Package notes and repository handoff

**Double FW Ltd · 5 November 2026 · Draft document pack 1.0**

## Contents and status

This is a complete repository document pack: six new practical guides, two shared registers, a reusable delivery template, revised principles/README and extended versions of the QA matrix, research plan and screen-reader guide. The historical gap review, existing licence, changelog, validation report and checksum manifest are included.

The files are prepared as replacement/addition candidates at the repository root. Nothing has been committed or pushed to GitHub by this work. Previous standalone Library documents are not silently overwritten; this archive is a separate, reviewable package.

## Source baseline

Repository: [Double-FW/Cognitive-UX-Design](https://github.com/Double-FW/Cognitive-UX-Design).

Baseline commit: `f3432fce3b1f4dba15c8453621f67b4e75c5c619`. The root tree was checked; no AGENTS.md was present at that revision. Baseline files were retrieved at this commit and their Git blob identities checked before editing. The unchanged source review supplies D/M/E mapping rationale and the related-repository source register; its status language describes the earlier review, not this new pack’s completion.

The package manifest records baseline blob identities for replaced/preserved source files and SHA-256 hashes of packaged files. Manifest hashes exclude the manifest itself. These hashes help detect file drift; they do not establish correctness or product conformity.

## Add the documents

1. Work on a branch or separate checkout of Cognitive-UX-Design. Compare its current HEAD with the baseline above; if it changed, review each affected file before replacing it.
2. Copy the archive’s root files into the repository root, preserving filenames. New guides and registers are additions. Principles, README and the three existing guides are revised copies; do not erase unrelated files that appeared after the baseline.
3. Review substantive principle changes in CHANGELOG.md and the original/revised diff. Confirm the channel/persistence, simplicity and memory wording with the responsible maintainers.
4. Assign named owners, complete independent subject-matter review and record actual review decisions. The draft status is intentional; do not change it to “validated” on the basis of structural checks.
5. Verify relative links and source revisions in the repository context. All existing IDs should remain stable. The supplementary MEM tests have Not tested status until a scoped product evaluation is executed.
6. Publish the reviewed files together, recording the actual commit/release and date in the coverage/change records. Any later changes to requirements must identify affected mappings and tests.

## Priority for use

Start with prospective-memory aids, interruption recovery and similar-current-context tasks. Use the template to agree a task/build, supported modes, source revisions, expected outcomes and people responsible. Then combine existing QA, bounded agent checks, actual AT review and intended-user evidence. The other guides are fully authored in this package; priority is a deployment choice, not unfinished drafting.

## Evaluation and privacy boundary

No product or participant tests were run. Use the research plan for controller-specific lawful basis, sensitive data, processors, participation, retention and safeguarding decisions before collection. Do not store participant identities, raw sessions or sensitive customer contexts in this public repository. Existing legal references are carried forward; this document pack does not constitute a fresh legal compliance audit.
