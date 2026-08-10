# Classical Data Analytics

A curated collection of student-facing materials for the classical data analytics learning track.

## Repository Principles

- The structure is topic-based rather than date-based.
- Repository navigation and technical file names are in English.
- Educational content may remain in Russian because it was prepared for Russian-speaking learners.
- Teacher solutions, instructor scripts, QA internals, generated outputs, and redundant nested archives are excluded.
- Large multi-topic cases are stored once and linked from related topic folders.
- Relative links are used for repository-internal navigation.

## Learning Path

1. [Foundations and Data Collection](./01_foundations/)
2. [Data Processing](./02_processing/)
3. [Analysis and Modeling](./03_analysis/)
4. [Visualization, Interpretation, and Reporting](./04_reporting/)
5. [Supplementary Materials](./supplementary/)

See [TOPIC_MAP.md](./TOPIC_MAP.md) for the complete topic-to-folder mapping.

## Shared End-to-End Cases

Some projects cover several curriculum topics. To avoid duplicate datasets and notebooks, they are stored once under [`shared/`](./shared/) and linked from the relevant topic folders.

## Quick Start

1. Choose a topic from the learning path.
2. Open the topic `README.md`.
3. If the topic contains a project-specific `requirements.txt`, create a virtual environment and install those dependencies.
4. Run notebooks from the project root as instructed in the local README.
5. Keep raw datasets unchanged and write generated artifacts only to the designated output folders.

## Source and Curation

The source archive contained webinar and in-person seminar materials, including multiple revisions, teacher packages, student packages, generated outputs, and exact duplicates. This repository contains a curated student-facing view organized by curriculum topic.

For traceability, see [`SOURCE_MANIFEST.csv`](./SOURCE_MANIFEST.csv) and [`QA_REPORT.md`](./QA_REPORT.md).

## Windows path compatibility

Physical directory names are intentionally compact. Full topic names are kept in the navigation and topic documentation, while short folder names reduce the risk of Windows path-length extraction and checkout issues.

