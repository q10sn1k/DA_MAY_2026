# Educational Package QA Report

## 1. Package readiness

**Status: READY for local/offline handoff.**

GitHub publication is **NOT_PERFORMED**: the connected GitHub integration returned HTTP 403 when attempting to create the working branch. This does not affect the local package contents, but the repository upload must be performed separately or after connector write permissions are enabled.

## 2. Scope

- Intended use: очное практическое занятие 05.09.2026.
- Audience: слушатели программы «Аналитик данных», начинающий/базовый уровень визуализации.
- Primary workflow: in-person practical session.
- Domain: Data Analytics / Python visualization.
- Technical artifacts: Jupyter notebooks + synthetic CSV datasets + offline instructions.
- Learner/instructor variants are separated.
- R is represented only as a short instructor overview; no R technical artifacts are included by design.

## 3. Completeness matrix

| Component | Present | Verification | Status |
|---|---:|---|---|
| Root README | yes | opened/static inspection | PASS |
| Offline preparation | yes | static inspection | PASS |
| Requirements | yes | environment imports checked | PASS |
| Environment check script | yes | executed | PASS |
| Prepared dataset | yes | loaded by all notebooks | PASS |
| Raw dataset with controlled issues | yes | file/schema inspection | PASS |
| Data dictionary | yes | cross-checked with CSV fields | PASS |
| 4 learner notebooks | yes | executed top-to-bottom as starter notebooks | PASS |
| 4 instructor notebooks | yes | executed top-to-bottom and saved | PASS |
| Learner notes DOCX | yes | rendered and visually inspected page-by-page (13/13) | PASS |
| Chart-selection handout | yes | static inspection | PASS |
| Visualization QA checklist | yes | static inspection | PASS |
| Full instructor scenario | yes | timing sum and alignment checked | PASS |
| Slide outline | yes | scope alignment checked | PASS |
| Presentation PPTX | yes | re-rendered after path edits; slide overflow test PASS; 30/30 slides visually reviewed | PASS |
| Instructor speaker notes DOCX | yes | re-rendered after path edits; 8/8 pages visually reviewed | PASS |
| Reference PNG outputs | yes | generated from executed solution notebooks | PASS |
| GitHub publication | no | branch-create attempt returned 403 | EXTERNAL BLOCKER |

## 4. Technical verification evidence

Build environment:

- Python 3.13.5
- pandas 2.2.3
- Matplotlib 3.10.8
- Seaborn 0.13.2

Checks performed:

1. `python env_check.py` — PASS.
2. All four instructor notebooks — PASS from clean kernel execution.
3. All four learner notebooks — PASS as starter notebooks; TODO cells intentionally contain comments/placeholders and do not reveal solutions.
4. Relative path discovery — PASS.
5. Scan for author-machine absolute paths — no findings.
6. Scan for `.R`, `.Rmd`, `.qmd` — none present.
7. Instructor TODO leakage — none present.
8. Learner TODO markers — present by design.
9. Expected PNG artifacts — generated and visually spot-checked.
10. Learner notes DOCX — rendered to 13 pages and every page visually inspected; no clipping, overlap or table splits found in the final render.
11. Windows path audit — PASS: longest internal archive path is 79 characters.
12. All 8 notebooks re-executed after path shortening — PASS.
13. PPTX re-rendered after path edits — 30/30 slides visually inspected; overflow test PASS.
14. Speaker notes DOCX re-rendered after path edits — 8/8 pages visually inspected.

## 5. Cross-artifact alignment

| Outcome | Taught | Practiced | Evidenced | Criteria |
|---|---|---|---|---|
| Choose a chart from an analytical question | Notebook 01 + handout | Notebooks 01–04 | Practical case | checklist |
| Prepare data at correct grain | Notebooks 01–03 | Notebooks 01–04 | Practical case | checklist |
| Build readable Matplotlib charts | Notebooks 01–02 | Notebook 02 + case | saved PNGs | checklist |
| Use Seaborn for EDA | Notebook 03 | Notebook 03 + case | case | checklist |
| Interpret without causal overclaim | Notebooks 02–03 | checkpoints + case | written conclusions | checklist |
| Work offline | README/OFFLINE | all notebooks | environment check | local run |
| Retain a reusable post-session reference | learner notes + handouts | during/after session | checklist + case workflow | learner notes/checklist |

## 6. Residual risks / external checks

- Classroom machines were not inspected; package dependencies must be installed before the session.
- Current official docs were checked during preparation, but future library updates may require re-verification before reuse in another cohort.
- GitHub repository write was not completed because branch creation through the connector was denied with HTTP 403.
- Windows Explorer copy was not executed in this Linux build environment; compatibility is supported by the shortened path structure and static path-length audit.

## 7. Final decision

- Local handoff: **allowed**.
- Offline classroom use: **allowed after pre-session environment check**.
- GitHub upload: **requires a separate write-capable GitHub action/permission**.
- Re-QA after repository upload: recommended only for path/link integrity, not for notebook logic unless files are changed.
