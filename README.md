# 🔍 Conflict Interest – Automatic Conflict of Interest Detector

**Conflict Interest** is a smart system that helps detect academic or financial conflicts of interest among conference participants. It scans institutional affiliations, co-authorship history, and financial ties to flag potential conflicts automatically—streamlining a process that’s often manual and tedious.

---

## 📘 What It Does

🧑‍🤝‍🧑 **Co-Authorship Detection** – Identifies shared publications within the past 2 years using Google Scholar data.  
🏢 **Affiliation Matching** – Flags current or past institutional overlaps using public and scraped data.  
💸 **Financial Conflict Detection** – Connects individuals to potential financial ties where disclosure data is available.  
📊 **Conflict Scoring** – Uses a weighted algorithm to assign a conflict score to each pair of individuals.  
🖥️ **User-Friendly Interface** – View detected conflicts and their explanations in an intuitive UI.

---

## 🧩 How It Works

The system operates through three primary phases:

### 📥 Data Collection
- Scrapes or integrates data from:
  - Google Scholar (publication + co-authorship)
  - LinkedIn or institutional pages (affiliations)
  - Public financial disclosures (if available)

### 🧪 Conflict Detection Algorithm
- Extracts features like:
  - Past or current shared institutions  
  - Co-authorship in the past 2 years  
  - Advisor–advisee relationships  
  - Financial ties from disclosures
- Computes a **conflict score** based on these features

### 🖼️ User Interface
- Input names of conference participants
- Display conflict results in a simple dashboard
- Explain reasoning behind each detected conflict

---

## 🛠 Tech Stack

- **Languages**: Python, JavaScript  
- **Data/NLP**: Pandas, Scikit-learn, Requests  
- **Frontend**: HTML, CSS, JavaScript (Chrome Extension)  
- **APIs**: Google Scholar (scraped or unofficial API), LinkedIn, public data sources

---

## 🎯 Who It's For

- Academic conference organizers  
- Peer review managers  
- Journal editors ensuring unbiased review  
- Anyone vetting professional conflicts at scale

---

## 👤 Author

Built by **Yujun Ge**  
