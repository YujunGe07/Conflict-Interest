# Conflict Interest Detector

<div align="left">

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=flat&logo=jupyter&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=flat&logo=scikit-learn&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat&logo=pandas&logoColor=white)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=flat)

</div>

> **Automated conflict-of-interest detection for academic conference peer review.**
> Scans co-authorship history, institutional affiliations, and financial ties to flag potential conflicts — replacing a manual, error-prone process with a weighted scoring pipeline.

---

## The Problem

Academic peer review depends on unbiased assignment of reviewers to submissions. Manually checking for conflicts across hundreds of participants is slow, inconsistent, and easy to miss. This system automates it.

---

## How It Works

```
Input: List of conference participants
         │
         ▼
┌─────────────────────┐
│   Data Collection   │
│  • Google Scholar   │  ──▶  Co-authorship (past 2 years)
│  • LinkedIn / inst. │  ──▶  Current & past affiliations
│  • Public disclos.  │  ──▶  Financial ties
└─────────────────────┘
         │
         ▼
┌─────────────────────────┐
│  Conflict Detection     │
│  • Shared institution   │
│  • Co-authored papers   │
│  • Advisor–advisee      │
│  • Financial overlap    │
└─────────────────────────┘
         │
         ▼
┌──────────────────────┐
│  Weighted Conflict   │
│  Score per pair      │
└──────────────────────┘
         │
         ▼
   Dashboard output
```

---

## Features

| Feature | Description |
|---------|-------------|
| **Co-Authorship Detection** | Flags shared publications within the past 2 years using Google Scholar |
| **Affiliation Matching** | Identifies current and past institutional overlaps |
| **Financial Conflict Detection** | Links individuals to financial ties via public disclosure data |
| **Conflict Scoring** | Weighted algorithm assigns a conflict score per participant pair |
| **Explainability** | Each flagged conflict includes a human-readable reason |

---

## Tech Stack

- **Language**: Python, JavaScript
- **Data / NLP**: Pandas, Scikit-learn, Requests, `scholarly`
- **Notebook**: Jupyter (`updatedScholarly.ipynb`)
- **Frontend**: HTML, CSS, JavaScript (Chrome Extension interface)

---

## Repo Structure

```
Conflict-Interest/
├── updatedScholarly.ipynb      # Main detection notebook
├── updatedScholarlyFile.py     # Python script version
├── test_file.py                # Unit tests
└── README.md
```

---

## Quickstart

```bash
git clone https://github.com/YujunGe07/Conflict-Interest.git
cd Conflict-Interest
pip install pandas scikit-learn requests scholarly
jupyter notebook updatedScholarly.ipynb
```

---

## Who It's For

- Academic conference organizers
- Program committee chairs managing reviewer assignments
- Journal editors ensuring unbiased review
- Anyone vetting professional conflicts at scale

---

## Roadmap

- [x] Co-authorship detection via Google Scholar
- [x] Affiliation matching
- [x] Weighted conflict scoring
- [ ] Advisor–advisee relationship detection
- [ ] Financial disclosure integration
- [ ] Web dashboard for bulk input + export
- [ ] REST API endpoint for integration with conference management systems

---

## Author

**Yujun Ge** · [GitHub](https://github.com/YujunGe07) · [Email](mailto:geyujunamy@gmail.com)
