# QA Report

**Status:** READY

## Summary

- Final files: 313
- Total size: 103.65 MiB
- Notebooks structurally checked: 39
- Notebook parse errors: 0
- Notebook syntax errors: 0
- Local Markdown links checked: 484
- Broken local Markdown links: 0
- Non-ASCII repository paths: 0
- Nested archives: 0
- Files over 50 MiB: 0
- Files over 100 MiB: 0
- Windows paths >= 260 characters for the tested user checkout prefix: 0
- Maximum tested Windows path length: 239 characters
- Detailed Russian root navigation: added
- Complete physical file index: `FILE_INDEX.md`
- Topic map: bilingual Russian/English

## Validation Scope

- Notebook checks cover notebook JSON parsing and Python code-cell syntax; this does not claim full execution of every notebook.
- Markdown relative links were rechecked after the navigation README update.
- Technical paths remain English/ASCII; Russian topic names and explanations are provided in README navigation.
- Teacher-only solutions, instructor scripts, internal QA source materials, generated outputs, and redundant nested archives remain excluded from the student-facing set.
- Compact technical directory names are preserved for Windows path compatibility.

## Navigation QA

The root `README.md` now explains:

- all 22 curriculum topics;
- Russian topic name -> English technical folder mapping;
- what each standard folder means (`materials`, `notebooks`, `data/raw`, etc.);
- which file to open first for every topic;
- which topics are navigation-only and where their physical materials are stored;
- the shared Support Analytics case;
- supplementary Prompting, AI Workflows, and Final Project materials;
- Python/R launch conventions;
- rules for raw/processed/BI data.

`FILE_INDEX.md` lists every physical file in the curated package.

## Largest Files

| Size (MiB) | Path |
|---:|---|
| 33.5 | `02_processing/06_big_data/big_data_student_kit/data/raw/events_lite.csv` |
| 18.9 | `shared/cases/support_analytics/data/raw/ticket_events.csv` |
| 14.4 | `04_reporting/05_results_presentation/final_consultation_case/data/processed/ecommerce_datamart.csv` |
| 14.0 | `supplementary/final_project/data/raw/orders_big.csv` |
| 6.7 | `shared/cases/support_analytics/data/raw/tickets.csv` |
| 3.5 | `04_reporting/05_results_presentation/final_consultation_case/data/raw/orders.csv` |

## Intentional Duplicate Raw Data

Some standalone cases intentionally keep their own copies of small source tables so the exercise can be run independently. This is not treated as accidental duplication.
