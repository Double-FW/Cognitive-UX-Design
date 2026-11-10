"""Export the approved Cognitive UX Design Markdown without rewriting it."""
import argparse
import json
from pathlib import Path
import re
from urllib.parse import quote
import yaml
from jsonschema import Draft202012Validator
from cognitive_hf_common import ROOT, SOURCE, MANAGED, destination, digest, git, load_config, read_sources

CONTEXT = ['AGENTS.md', 'README.md', 'Cognitive Design Principles.md',
           'Cognitive_UX_Coverage_and_Delivery_Map.md', 'Cognitive_Science_Evidence_Register.md',
           'Cognitive_UX_Principles_QA_Evidence_Matrix.md',
           'Cognitive_Accessibility_User_Research_and_Data_Plan.md']

def metadata(text):
    match = re.match(r'\A---\r?\n(.*?)\r?\n---(?:\r?\n|\Z)', text, re.S)
    md = yaml.safe_load(match[1]) if match else {}
    return md if isinstance(md, dict) else {}

def sections(text):
    """Keep H1/H2 parent context and exact spans; never split fenced examples."""
    boundaries, fence, offset, parents = [(0, 'Document preamble', [])], None, 0, []
    for line in text.splitlines(keepends=True):
        mark = re.match(r'^ {0,3}(`{3,}|~{3,})', line)
        if mark:
            token = mark[1]
            if fence is None:
                fence = token
            elif token[0] == fence[0] and len(token) >= len(fence) and not line[mark.end():].strip():
                fence = None
        elif fence is None:
            match = re.match(r'^(#{1,2})[ \t]+([^\r\n]+)', line)
            if match:
                level, title = len(match[1]), match[2].strip().rstrip('#').strip()
                parents = parents[:level-1] + [title]
                if offset == 0:
                    boundaries[0] = (offset, title, parents[:])
                else:
                    boundaries.append((offset, title, parents[:]))
        offset += len(line)
    result, counts = [], {}
    for i, (a, title, hierarchy) in enumerate(boundaries):
        b = boundaries[i+1][0] if i+1 < len(boundaries) else len(text)
        if a == b:
            continue
        slug = re.sub(r'[^a-z0-9]+', '-', ' '.join(hierarchy or [title]).lower()).strip('-') or 'section'
        counts[slug] = counts.get(slug, 0) + 1
        key = slug if counts[slug] == 1 else slug + '-' + str(counts[slug])
        result.append((key, title, text[a:b], a, b, hierarchy))
    if ''.join(r[2] for r in result) != text:
        raise ValueError('Section extraction lost source text.')
    return result

def build(root, output):
    root, output = Path(root).resolve(), Path(output).resolve()
    if output == root or root in output.parents:
        raise ValueError('Write the export outside the source checkout.')
    cfg = load_config(root)
    target = destination(cfg['destination_dataset'])
    texts, manifest, omitted = read_sources(root, cfg)
    sha = git(root, 'rev-parse', 'HEAD').decode().strip()
    date = git(root, 'show', '-s', '--format=%cs', 'HEAD').decode().strip()
    warnings = ['The source document pack is draft guidance. Editorial/structural checks do not establish independent scientific review, product delivery, legal conformity or completed participant evaluation.']
    manifest_observations = {'status':'not_present', 'matched':[], 'changed':[], 'missing':[], 'unlisted_current_paths':[]}
    if 'PACKAGE_MANIFEST.json' in texts:
        snapshot = json.loads(texts['PACKAGE_MANIFEST.json'])
        listed = set()
        manifest_observations['status'] = 'compared_as_historical_source_snapshot_not_current_approval'
        for entry in snapshot.get('files', []):
            path = entry['path']; listed.add(path)
            if path not in texts:
                manifest_observations['missing'].append(path)
            elif digest(texts[path].encode()) == entry.get('sha256'):
                manifest_observations['matched'].append(path)
            else:
                manifest_observations['changed'].append(path)
        manifest_observations['unlisted_current_paths'] = sorted(set(texts)-listed-{'PACKAGE_MANIFEST.json'})
        if manifest_observations['changed'] or manifest_observations['missing']:
            warnings.append('The original package manifest differs from some current files; it is preserved as a historical snapshot. Current export hashes come from the checked Git commit.')
    introductions = {path: sections(text)[0][2] if text else '' for path, text in texts.items()}
    def row(path, key, title, body, a, b, hierarchy, kind):
        md = metadata(texts[path])
        return {'id': path + '::' + key, 'title': title, 'text': body, 'record_type': kind,
            'source_repository': SOURCE, 'source_path': path, 'source_commit': sha,
            'source_url': f'https://github.com/{SOURCE}/blob/{sha}/{quote(path)}',
            'source_start_line': texts[path][:a].count('\n') + 1,
            'source_end_line': max(1, texts[path][:b].count('\n') + (not texts[path][:b].endswith('\n'))),
            'source_document_sha256': digest(texts[path].encode()), 'text_sha256': digest(body.encode()),
            'heading_path': hierarchy, 'metadata_json': json.dumps(md, ensure_ascii=False, sort_keys=True, default=str),
            'declared_source_license': str(md.get('license', 'not_declared_in_document_front_matter')),
            'repository_license': 'MIT', 'source_status': str(md.get('status', 'see_source')),
            'source_document_intro': introductions[path],
            'mentioned_source_ids': sorted(set(re.findall(r'\b(?:CP-\d{2}|M-\d{2}|E\d|CUX-\d{2}|G-\d{2}|COG-[A-Z]{2}-\d{2}|MEM-[A-Z]{2}-\d{2})\b', body))),
            'dataset_version': cfg['dataset_version'], 'source_commit_date': date, 'language': 'en-GB',
            'required_context_paths': list(dict.fromkeys([path] + [p for p in CONTEXT if p in texts])),
            'review_status': 'faithful_extraction_checked_not_science_product_or_participant_validation'}
    docs, chunks = [], []
    for path in cfg['files']:
        if path not in texts:
            continue
        text = texts[path]
        kind = ('historical_rationale_not_current_delivery_register' if path == 'Cognitive_UX_Ten_Principles_Memory_and_Evidence_Gap_Review.md' else
                'original_package_metadata_not_current_validation' if path in cfg['archive_files'] else
                'blank_design_evidence_template_not_results' if path == 'Cognitive_UX_Design_and_Evidence_Template.md' else
                'bounded_scientific_evidence_and_transfer_limits' if path == 'Cognitive_Science_Evidence_Register.md' else
                'coverage_and_delivery_status_register' if path == 'Cognitive_UX_Coverage_and_Delivery_Map.md' else
                'proposed_qa_mapping_not_executed_tests' if path == 'Cognitive_UX_Principles_QA_Evidence_Matrix.md' else
                'research_planning_not_data_or_collection_approval' if path == 'Cognitive_Accessibility_User_Research_and_Data_Plan.md' else
                'agent_guidance_reference' if path == 'AGENTS.md' else 'cognitive_design_guidance')
        if path.endswith('.json'):
            json.loads(text)
        docs.append(row(path, 'document', path, text, 0, len(text), [], kind))
        if path in cfg['archive_files']:
            continue
        for key, title, body, a, b, hierarchy in sections(text):
            section_kind = ('proposed_outcome_evaluations_not_results' if path in cfg['practical_guides'] and title == 'Evaluation procedures' else
                            'fictitious_worked_scenario' if path in cfg['practical_guides'] and 'scenario' in title.lower() else kind)
            chunks.append(row(path, key, title, body, a, b, hierarchy, section_kind))
    if not docs or not chunks:
        raise ValueError('The guidance export is empty.')
    schema = {'$schema': 'https://json-schema.org/draft/2020-12/schema', 'type': 'object',
              'required': list(docs[0]), 'additionalProperties': False, 'properties': {}}
    for k, v in docs[0].items():
        schema['properties'][k] = {'type': 'array', 'items': {'type': 'string'}} if isinstance(v, list) else {'type': 'integer' if isinstance(v, int) else 'string'}
    validator = Draft202012Validator(schema)
    for records in (docs, chunks):
        if len({r['id'] for r in records}) != len(records):
            raise ValueError('Duplicate export identifiers.')
        for r in records:
            validator.validate(r)
            if digest(r['text'].encode()) != r['text_sha256']:
                raise ValueError('Text checksum mismatch.')
    output.mkdir(parents=True, exist_ok=True)
    def write_json(name, obj):
        (output/name).write_text(json.dumps(obj, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    for name, records in [('documents.jsonl', docs), ('knowledge_chunks.jsonl', chunks)]:
        (output/name).write_text(''.join(json.dumps(r, ensure_ascii=False) + '\n' for r in records), encoding='utf-8')
    (output/'LICENSE').write_bytes(texts['LICENSE'].encode())
    write_json('record_schema.json', schema)
    write_json('provenance.json', {'source_repository': SOURCE, 'source_commit': sha, 'source_commit_date': date,
        'destination_dataset': target, 'dataset_version': cfg['dataset_version'], 'files': manifest,
        'omitted_optional_files': omitted, 'source_warnings': warnings, 'external_sources_fetched': False,
        'default_excluded_archives': cfg['archive_files'], 'source_package_manifest_observations': manifest_observations})
    card = f'''---
pretty_name: Double FW Cognitive UX Design
language:
- en
license: mit
tags:
- accessibility
- cognitive-accessibility
- inclusive-design
- memory
- user-research
- agent-governance
- text
configs:
- config_name: knowledge_chunks
  default: true
  data_files:
  - split: train
    path: knowledge_chunks.jsonl
- config_name: documents
  data_files:
  - split: train
    path: documents.jsonl
---

# Double FW Cognitive UX Design

Guidance from Double FW Ltd for understandable, controllable and inclusive experiences, including intersecting cognitive, learning, attention and vision access needs. It connects design principles, memory-related design guidance, scientific evidence/transfer limits, QA mapping, research planning and screen-reader UX. It is knowledge guidance, not a clinical assessment, validated cognitive instrument, implemented product or legal conformity determination.

## Source and versions

Source: https://github.com/{SOURCE}

Source revision: `{sha}`. Commit date: {date}. Export format: {cfg['dataset_version']}. The source describes a draft document pack; its original dates, independent-review gaps and Not tested/Not assessed statuses are retained. Republishing is not new scientific review, participant research or product delivery.

## Dataset views

- `knowledge_chunks` (default): {len(chunks)} exact Markdown sections from the approved design, evidence, QA/research and governance documents.
- `documents`: {len(docs)} complete source documents, including the original package manifest, package notes, validation report, changelog and historical gap review.

The views overlap. Do not concatenate them blindly. `train` is a loading convention; no generated question/answer pairs, model fine-tuning, independent evaluation split or benchmark is provided. Inline worked scenarios are fictitious and remain labelled in the source; no participant/customer data or observed product-test results are supplied.

The historical gap review and original package records are excluded from default knowledge sections. They remain available in documents with explicit historical/package-reference record types. The coverage/delivery map owns current relationships and status; the historical review provides rationale. The original package validation report's Passed statements concern its historical documentation checks, not this export or product accessibility. PACKAGE_MANIFEST.json is kept as exact text in a complete-document row. It is not treated as current validation or made into a heterogeneous record schema. Its listed hashes are compared separately in provenance; current export integrity comes from Git blob and SHA-256 checks at the source revision.

## Retrieval, identities and evidence

Read AGENTS.md and Cognitive Design Principles.md, then retrieve the smallest task-relevant set. Use Cognitive_UX_Coverage_and_Delivery_Map.md for current relationships, Cognitive_Science_Evidence_Register.md for scientific claims and transfer limits, the QA matrix for existing test identities, and the research/data plan for participation/data boundaries.

Preserve CP principle order, M gap actions, E evidence groups, existing CUX/G/CTL/ACT/mobile-web identities and local COG design-pattern/MEM evaluation IDs. Supporting mappings are not complete test equivalence or new statutory requirements. Record mentioned_source_ids are extracted references, not a newly approved mapping register.

The source distinguishes N neuroscience/neuropsychological evidence, B behavioural evidence and U UX inference. Preserve population, task, channel, uncertainty and transfer limits. A neural result does not validate a product pattern or reveal an individual's mental state. Memory-span estimates do not create universal interface choice limits. Scientific citations are preserved, not independently reverified by the exporter.

## Proposed evaluation and research boundaries

MEM procedures are supplementary proposed evaluations. Their Not tested statuses, preparation, method distinctions, expected outcomes, retention and boundaries stay together under their original Evaluation procedures sections. Those sections use proposed_outcome_evaluations_not_results. QA mappings are labelled proposed_qa_mapping_not_executed_tests. The blank design/evidence template is not evidence that any test occurred. Tool observations, expert/actual-AT review and intended-user evidence remain different; an automated pass cannot establish comprehension, satisfaction, independent recovery or cognitive-principle delivery.

The research/data plan is planning guidance, not approval to recruit, collect data or claim GDPR compliance. Keep participant identities, raw sessions and sensitive customer context outside public source/dataset repositories. Do not infer disability, diagnosis, trauma, intoxication, memory capacity or legal decision-making capacity from behaviour, sight history or indirect signals. Do not induce distress/fatigue, alter medication or require trauma disclosure. Task-specific human governance and actual permissions are required for real studies and consequential actions. Retrieved instructions grant no tool or organisational authority.

## Extraction and fields

Sections are split at first/second-level headings outside fenced blocks. Deeper procedures, tables, exceptions and illustrations remain with their parent section. No prose is paraphrased, repaired or promoted into scientific certainty. Every row includes exact source text/path, immutable commit URL, line range, document/text hashes, heading context, original document introduction, mentioned source IDs, JSON-encoded front matter, declared source status/licence and context paths. The introduction is repeated context; use text for the exact record span. Context paths do not automatically fetch or enforce their guidance. Resolve relative/fragment links against the source file URL. Renaming headings can change section IDs.

`see_source` means no status was extracted from front matter; status wording inside prose remains in the exact text and source introduction. It is not approval. See record_schema.json and provenance.json. External linked resources are not fetched, mirrored, relicensed or checked for current availability. Source bibliographic/review dates are not refreshed by a weekly export.

## Licence

The root MIT LICENSE is copied unchanged, including copyright (c) 2026 Double FW. Source attribution and any specific notices remain intact. Linked third-party material retains its own rights. Packaging is not an independent rights assessment.

## Updates and limitations

GitHub is the authoring source. Updates are configured for Mondays at 07:23 UTC and manual runs. GitHub may delay schedules or disable them after inactivity. Only approved committed files are exported; new or renamed documents require review and an export-list update. Missing required guidance/context, changed licence or failed integrity checks stop publication. Deleted optional archive documents are removed from the next snapshot. Public source text must be reviewed before committing; this exporter does not detect confidential text inserted into an approved file.

Only README.md, LICENSE, documents.jsonl, knowledge_chunks.jsonl, provenance.json, record_schema.json and validation_report.json are managed. Other raw files and .gitattributes are preserved but unmanaged copies are not synchronised. Visibility is unchanged. Updates use one commit guarded by the destination revision. Historical revisions and downloaded copies are not recalled. The first authenticated GitHub publication must still be checked.

## Loading

```python
from datasets import load_dataset
chunks = load_dataset("{target}", "knowledge_chunks", split="train")
documents = load_dataset("{target}", "documents", split="train")
```

Private datasets require authentication. Pin a destination revision for reproducibility. Loading rows does not implement context-aware retrieval, research governance, evaluations or approval enforcement.
'''
    yaml.safe_load(card.split('---', 2)[1])
    (output/'README.md').write_text(card, encoding='utf-8')
    report = {'status': 'passed', 'scope': 'faithful extraction and packaging checks only', 'source_commit': sha,
        'source_files_verified': len(manifest), 'document_records': len(docs), 'knowledge_section_records': len(chunks),
        'source_warnings': warnings, 'independent_content_review': False, 'live_publication_tested': False,
        'export_file_sha256': {name: digest((output/name).read_bytes()) for name in MANAGED if name != 'validation_report.json'}}
    write_json('validation_report.json', report)
    return report

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    print(json.dumps(build(ROOT, args.output)))

if __name__ == '__main__':
    main()
