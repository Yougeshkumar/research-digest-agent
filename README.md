# 🧠 Research Digest Agent

<p align="center">
  <b>AI-powered system to extract, cluster, and summarize insights from multiple sources</b><br>
  <i>Turning raw information into structured knowledge</i>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10-blue?logo=python">
  <img src="https://img.shields.io/badge/ML-TF--IDF-orange">
  <img src="https://img.shields.io/badge/Status-Active-success">
  <img src="https://img.shields.io/badge/License-MIT-green">
</p>

---

## 🚀 Overview

The **Research Digest Agent** is an autonomous AI system that:

- 🌐 Collects data from multiple sources  
- 🧠 Extracts meaningful insights  
- 🔄 Removes redundancy  
- 📊 Produces structured, evidence-backed summaries  

👉 Designed to simulate an AI research assistant.

---

## ✨ Features

- 🔍 Web Scraping  
- 🧠 Claim Extraction  
- 🧩 TF-IDF Clustering  
- 📊 Structured Output  
- 🎨 Interactive Dashboard  
- 🌙 Dark / ☀️ Light Mode  
- 🔎 Search Functionality  
- 🎯 Theme Filtering  

---

## 🏗️ Tech Stack

| Category | Technology |
|----------|-----------|
| Language | Python |
| Scraping | BeautifulSoup |
| ML | Scikit-learn |
| UI | HTML, CSS, JavaScript |

---

## 📂 Project Structure

```
research-digest-agent/
│
├── src/
│   ├── main.py
│   ├── fetch.py
│   ├── extract.py
│   ├── cluster.py
│   └── generate.py
│
├── outputs/
│   ├── digest.html
│   ├── digest.md
│   └── sources.json
│
├── requirements.txt
└── README.md
```

## ▶️ Run Locally

```bash
git clone https://github.com/Yougeshkumar/research-digest-agent.git
cd research-digest-agent

pip install -r requirements.txt
python src/main.py

👉 Then open: 
outputs/digest.html
```

---

## ⚙️ How It Works

1. **Data Collection**  
   Scrapes content from multiple sources  

2. **Claim Extraction**  
   Breaks text into meaningful insights  

3. **Clustering**  
   Groups similar claims using ML  

4. **Digest Generation**  
   Outputs structured summary + interactive UI  

---

## ⚠️ Limitations

- Heuristic-based extraction (not LLM-level)  
- Limited semantic understanding  

---

## 🔮 Future Improvements

- 🤖 LLM integration (GPT / Gemini)  
- 🧠 Vector database (FAISS)  
- 🌐 Real-time APIs  
- 📊 Analytics dashboard  