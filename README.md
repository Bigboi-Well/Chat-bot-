# 🤖 Python Chatbot (CLI + GUI)

This is a **self-learning chatbot** built in Python that uses a JSON knowledge base.  
It can answer questions, learn new ones from the user, and has both:

- **Command-line interface** (chatbot.py)
- **Graphical user interface (GUI)** with Tkinter (chatbot1.py)

---

## ✨ Features
- 📂 Stores Q&A pairs in `knowledge_base.json`
- 🔎 Uses fuzzy matching (`difflib.get_close_matches`) to find best question
- 🧠 Learns new answers interactively if it doesn’t know something
- 💻 Two versions available:
  - `chatbot.py` → Command-line chatbot
  - `chatbot1.py` → GUI chatbot with Tkinter

---

## 🛠️ Tech Stack
- **Python 3**
- **Tkinter** (GUI)
- **JSON** (database)
- **difflib** (fuzzy matching)

---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/<your-username>/chatbot.git
cd chatbot
