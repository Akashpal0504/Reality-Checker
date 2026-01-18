# 🕵️ Reality Checker – AI Fact-Checking Web App

## 📌 Overview
Reality Checker is a web-based AI application that automatically verifies factual claims from PDF documents using live web data.  
It is designed to act as a **fact-checking layer** between content creation and publishing, helping identify **false, outdated, or misleading information**.

This project was built as part of the **Founder's Office – AI Intern Assignment**.

---

## The Deployed App URL:

Link = https://reality-checker.streamlit.app/



## Table of Contents

🚀 What This App Does

⚙️ Quick Start

📄 Reference Example File

📂 Example Use Case

🖼️ Example Output

🧠 How It Works

🛠 Tech Stack

🌟 Project Structure


🌟 Features

⚙️ Quick Start

📁 Folder Structure

🖼️ Example Output

🧾 Sample JSONL Entry

🧠 Key Highlights

📄 File includes

## 🚀 What This App Does

1. **Accepts a PDF document** via a simple drag-and-drop interface  
2. **Extracts factual claims** such as:
   - Statistics  
   - Dates  
   - Prices  
   - Economic figures  
   - Technical or event-based statements  
3. **Cross-checks each claim against live web data**
4. **Classifies every claim** into one of the following:
   - ✅ **Verified** – Claim matches real-time information  
   - ⚠️ **Inaccurate** – Claim is outdated or partially incorrect  
   - ❌ **False** – No credible evidence found  

---

## ⚙️ Quick Start

### 1️⃣ Clone the Repository
```bash
git clone <your-github-repo-url>
cd reality-checker
```

2️⃣ Create Virtual Environment
```
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

3️⃣ Install Dependencies
```
pip install -r requirements.txt
```

4️⃣ Add API Keys

Create a .env file:
```
OPENAI_API_KEY=your_openai_api_key
TAVILY_API_KEY=your_tavily_api_key
```

▶️ Run the App Locally
```
streamlit run app.py
```
Then open the browser URL shown in the terminal.


## 📄 Reference Example File





## 📂 Example Use Case

When a market or technology report contains claims like:
- Bitcoin price figures  
- GDP growth rates  
- AI model release timelines  
- Aerospace mission outcomes  

The app automatically flags which claims are **reliable** and which are **incorrect or misleading**.

---

## 🖼️ Example Output

Below is an example of the deployed Reality Checker application, demonstrating successful PDF upload, automated claim extraction, live web verification, and accurate classification of claims as Verified, Inaccurate, or False.

![](https://github.com/Akashpal0504/Reality-Checker/blob/main/Example%201.png)

![](https://github.com/Akashpal0504/Reality-Checker/blob/main/Example%202.png)

![](https://github.com/Akashpal0504/Reality-Checker/blob/main/Example%204.png)

![](https://github.com/Akashpal0504/Reality-Checker/blob/main/Example%206.png)

![](https://github.com/Akashpal0504/Reality-Checker/blob/main/Example%207.png)

![](https://github.com/Akashpal0504/Reality-Checker/blob/main/Example%208.png)

![](https://github.com/Akashpal0504/Reality-Checker/blob/main/Example%209.png)


## 🧠 How It Works (High-Level Flow)

```
PDF Upload
↓
Text Extraction (PyPDF)
↓
Claim Detection (LLM)
↓
Live Web Search (Tavily)
↓
AI-Based Comparison
↓
Verification Status + Evidence
```



---

## 🛠 Tech Stack

| Component | Technology |
|--------|-----------|
| Frontend | Streamlit |
| Backend | Python |
| PDF Parsing | PyPDF |
| LLM | OpenAI (GPT-4o-mini) |
| Claim Logic | LangChain |
| Web Search | Tavily API |
| Deployment | Streamlit Cloud |

---


## 📁 Project Structure

```
├── app.py # Main Streamlit application
├── requirements.txt # Python dependencies
├── .env.example # Environment variable template
├── README.md # Project documentation
└── Assessment Reference_Market_Report.pdf

```






