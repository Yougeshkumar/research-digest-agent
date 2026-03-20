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

The Research Digest Agent follows a multi-stage AI pipeline:

### 1️⃣ Data Collection
- Scrapes and aggregates content from multiple sources (articles, web pages)
- Ensures diverse and relevant input data

### 2️⃣ Claim Extraction
- Uses NLP techniques to extract meaningful insights from raw text
- Converts unstructured text into structured claims

### 3️⃣ Semantic Clustering
- Applies ML techniques (TF-IDF / embeddings) to group similar claims
- Reduces redundancy and organizes related ideas

### 4️⃣ Digest Generation
- Uses AI models to generate a concise, structured summary
- Outputs key insights, summaries, and source references

### 5️⃣ Interactive Visualization
- Displays results in a user-friendly dashboard
- Enables easy exploration of insights 

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