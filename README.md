# 🧠 Study Tutor Agent

A modern AI-powered **Study Tutor Agent** built with **Streamlit, CrewAI, and Groq**.

The Study Tutor Agent helps students understand academic topics, get simple explanations, create study plans, perform calculations, and practice concepts. It uses **CrewAI tools and memory** to make the learning experience more interactive and personalized.

---

## ✨ Features

### 🤖 AI Study Tutor

A single CrewAI agent called **Study Tutor Agent** acts as an academic tutor.

It can:

* Explain difficult concepts in simple language
* Adapt explanations to the student's level
* Provide examples
* Highlight key points
* Generate practice questions
* Help with calculations
* Create simple study plans
* Use relevant previous learning context through memory

---

### 🛠️ Agent Tools

The Study Tutor Agent currently has two custom tools:

#### 🧮 Calculator Tool

The agent can use the calculator when a mathematical calculation is required.

Example:

> Calculate 25 × 48

The agent can use the Calculator Tool instead of trying to calculate the result itself.

#### 📅 Study Plan Tool

The agent can create simple study plans.

Example:

> Create a 7-day study plan for Machine Learning.

---

### 🧠 Agent Memory

The application uses **CrewAI Memory**.

Memory allows the Study Tutor Agent to use relevant information from previous interactions to provide a more personalized learning experience.

The project uses:

* CrewAI Memory
* Hugging Face Sentence Transformers
* `all-MiniLM-L6-v2` embeddings

---

### 🎨 Modern UI

The frontend is built with **Streamlit** and includes:

* Modern AI-inspired design
* Neon blue/cyan theme
* Dark interface
* Glassmorphism-style cards
* Responsive layout
* Subject selection
* Learning-level selection
* Large question input
* AI tutor response section
* Agent/tool/memory status indicators

---

## 🏗️ Architecture

```text
                    Student
                       │
                       ▼
                ┌─────────────┐
                │  Streamlit  │
                │   Frontend  │
                └──────┬──────┘
                       │
                       ▼
              ┌──────────────────┐
              │  Study Tutor     │
              │      Agent       │
              └────────┬─────────┘
                       │
              ┌────────┴─────────┐
              │                  │
              ▼                  ▼
        ┌───────────┐       ┌──────────┐
        │   Tools   │       │  Memory  │
        └─────┬─────┘       └────┬─────┘
              │                  │
       ┌──────┴──────┐      Previous
       │             │      learning
       ▼             ▼      context
  Calculator    Study Plan
       │             │
       └──────┬──────┘
              │
              ▼
       ┌───────────────┐
       │     Groq      │
       │ GPT-OSS 120B  │
       └───────────────┘
```

---

## 🧰 Technologies Used

| Technology                | Purpose                      |
| ------------------------- | ---------------------------- |
| Python                    | Application development      |
| Streamlit                 | Frontend and web application |
| CrewAI                    | AI agent framework           |
| Groq                      | LLM provider                 |
| GPT-OSS 120B              | Large Language Model         |
| Sentence Transformers     | Memory embeddings            |
| GitHub                    | Source code repository       |
| Streamlit Community Cloud | Deployment                   |

---

## 📁 Project Structure

```text
study-tutor-agent/
│
├── app.py
├── agent.py
├── tools.py
├── config.py
├── requirements.txt
├── .python-version
├── .gitignore
└── README.md
```

### `app.py`

Contains the Streamlit frontend and user interface.

### `agent.py`

Contains:

* Study Tutor Agent
* CrewAI Memory
* Study Task
* Crew configuration

### `tools.py`

Contains the custom tools used by the agent:

* Calculator Tool
* Study Plan Tool

### `config.py`

Contains the Groq/CrewAI LLM configuration.

### `requirements.txt`

Contains the Python dependencies required by the application.

### `.python-version`

Specifies the Python version used by the deployment environment.

### `.gitignore`

Prevents files such as API keys, virtual environments, and temporary files from being uploaded to GitHub.

---

# 🔑 Environment Variable

The application requires a Groq API key.

The environment variable name is:

```text
GROQ_API_KEY
```

The application reads the key using:

```python
os.environ.get("GROQ_API_KEY")
```

### Important

Never put your actual API key directly inside:

* `app.py`
* `agent.py`
* `config.py`
* GitHub repository
* `README.md`

---

# 🚀 Getting a Groq API Key

1. Create/login to your Groq account.
2. Open the Groq Console.
3. Create an API key.
4. Copy the key.
5. Add it to Streamlit Secrets.

The application uses:

```text
openai/gpt-oss-120b
```

through Groq.

---

# ☁️ Deploying on Streamlit Community Cloud

This project is designed to be deployed directly from GitHub using **Streamlit Community Cloud**.

## Step 1 — Upload the project to GitHub

Create a GitHub repository.

For example:

```text
study-tutor-agent
```

Upload these files:

```text
app.py
agent.py
tools.py
config.py
requirements.txt
.python-version
.gitignore
README.md
```

---

## Step 2 — Open Streamlit Community Cloud

Go to Streamlit Community Cloud and sign in using your GitHub account.

Create a new application.

Select:

```text
Deploy an app
```

Then select your GitHub repository.

---

## Step 3 — Select the main file

For the main file, select:

```text
app.py
```

Your structure should be:

```text
study-tutor-agent/
│
├── app.py
├── agent.py
├── tools.py
├── config.py
└── requirements.txt
```

---

# 🔐 Step 4 — Add the Groq API Key

Before deploying, open the application's **Advanced Settings / Secrets** section.

Add:

```toml
GROQ_API_KEY = "your_groq_api_key_here"
```

Replace:

```text
your_groq_api_key_here
```

with your actual Groq API key.

Do not add the API key to GitHub.

---

# ▶️ Step 5 — Deploy

Click:

```text
Deploy
```

Streamlit will:

```text
GitHub
   ↓
Read requirements.txt
   ↓
Install dependencies
   ↓
Read Streamlit Secrets
   ↓
Start app.py
   ↓
Launch Study Tutor Agent
```

After deployment, Streamlit will provide a public application URL.

---

# 📦 Requirements

The project uses the following main packages:

```text
streamlit
crewai
sentence-transformers
groq
```

The exact dependency versions can be pinned in `requirements.txt` if needed for a reproducible deployment.

---

# 🔒 Security

Never commit your Groq API key to GitHub.

Use Streamlit Secrets:

```toml
GROQ_API_KEY = "your_api_key"
```

The Python application accesses it through the environment:

```python
os.environ.get("GROQ_API_KEY")
```

If an API key is accidentally exposed publicly, revoke it and generate a new one.

---

# 🎯 Example Questions

You can ask the Study Tutor Agent questions such as:

### Computer Science

```text
Explain recursion in Python like I am a beginner.
```

### Artificial Intelligence

```text
What is a neural network? Give me a simple example.
```

### Mathematics

```text
Calculate 125 * 48 and explain the calculation.
```

### Study Planning

```text
Create a 7-day study plan for learning machine learning.
```

### Science

```text
Explain photosynthesis in simple words.
```

### Law

```text
Explain the difference between civil law and criminal law.
```

---

# 🧠 How the Agent Works

The application follows this process:

```text
1. Student enters a question
             ↓
2. Streamlit sends the request
             ↓
3. CrewAI Study Tutor Agent receives it
             ↓
4. Agent checks the student's subject and level
             ↓
5. Agent uses memory when relevant
             ↓
6. Agent decides whether a tool is needed
             ↓
7. Calculator / Study Plan Tool is used if required
             ↓
8. Groq GPT-OSS 120B generates the response
             ↓
9. Response is displayed in Streamlit
```

---

# 🎓 Project Goal

The goal of this project is to demonstrate how a **single AI agent** can combine:

* Large Language Models
* Agent frameworks
* Custom tools
* Memory
* Interactive UI
* Cloud deployment

to create a practical AI-powered learning assistant.

---

# 🔮 Future Improvements

Possible future features include:

* 📄 PDF/document learning
* 📚 RAG-based study material
* 📝 Automatic quizzes
* 🗂️ Flashcard generation
* 📊 Student progress tracking
* 👤 User accounts
* 💾 Persistent external memory
* 🎤 Voice interaction
* 🔎 Web research tool
* 📅 Advanced personalized study schedules

These features are intentionally outside the initial MVP to keep the application simple and easy to maintain.

---

## 👩‍💻 Built With

**Streamlit + CrewAI + Groq + GPT-OSS 120B**

### Learn • Practice • Improve 🧠

