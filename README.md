# 🔴 Vyrex — AI Research & Productivity Agent

**A tool-using AI agent that turns natural-language requests into actionable results.**

Vyrex is an AI-powered research and productivity application built with Python, Streamlit, and Groq. Unlike a traditional chatbot, Vyrex can select and execute external tools, retrieve current information from the web, perform calculations, and generate structured responses.

The project demonstrates practical AI agent engineering through custom function calling, tool orchestration, execution control, and an interactive agent workspace.

## ✨ Features

- **AI Tool Calling** — Automatically selects tools based on the user's request.
- **Web Research** — Searches the internet for information using DuckDuckGo-compatible search.
- **Smart Calculations** — Performs arithmetic using executable Python functions.
- **Agent Execution Loop** — Processes tool calls and returns results to the language model.
- **Research Summaries** — Produces structured responses with source URLs.
- **Agent Activity Tracking** — Displays real execution events in the interface.
- **Interactive Chat** — Chat-based interface with session history.
- **Report Export** — Downloads conversations as Markdown reports.
- **Execution Controls** — Configurable maximum agent steps.
- **Error Handling** — Handles search failures and certain Groq tool-parsing errors.
- **Premium Dark UI** — Minimal Streamlit interface with crimson accents.

## 🧠 How Vyrex Works

Vyrex implements a custom tool-calling workflow without relying on a high-level agent framework.

```text
User Request
     |
     v
Groq LLM — GPT-OSS 20B
     |
     v
Tool Selection
     |
     +----> Web Search
     |
     +----> Calculator
     |
     v
Python Tool Execution
     |
     v
Tool Results
     |
     v
Agent Processing
     |
     v
Final Response + Source URLs
```

The agent can retry tool selection when a search fails and uses a separate final-answer step after successful web research.

## 🛠️ Technology Stack

| Component | Technology |
|---|---|
| Programming Language | Python |
| Frontend | Streamlit |
| LLM Inference | Groq API |
| Language Model | GPT-OSS 20B |
| Web Search | DDGS |
| Function Calling | Groq Tool Calling |
| Agent Orchestration | Custom Python Agent Loop |
| Environment Configuration | Python Dotenv |
| Report Export | Markdown |

## 📁 Project Structure

```text
Vyrex/
├── app.py
├── agent.py
├── tools.py
├── requirements.txt
├── README.md
├── .gitignore
└── .env                  # Local only — not committed
```

### Core Components

- **`app.py`** — Streamlit chat interface, session history, activity tracking, example prompts, settings, and report export.
- **`agent.py`** — LLM integration, tool schemas, execution loop, error handling, and activity callbacks.
- **`tools.py`** — Calculator and web search implementations.
- **`requirements.txt`** — Python dependencies.

## 🚀 Getting Started

### Prerequisites

- Python 3.11
- Groq API key
- Internet connection for Groq inference and web research

### 1. Clone the Repository

```bash
git clone https://github.com/Tarikh792/Vyrex.git
cd Vyrex
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

Activate the environment.

**Windows PowerShell:**

```powershell
.\.venv\Scripts\Activate.ps1
```

**macOS / Linux:**

```bash
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Configure Your Groq API Key

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key
```

The `.env` file is excluded from version control.

For Streamlit Cloud deployment, configure the key using the application's Secrets settings and expose it as an environment variable or update the backend to read `st.secrets`.

### 5. Run Vyrex

```bash
python -m streamlit run app.py
```

Open the URL shown in the terminal, usually `http://localhost:8501`.

## 💬 Example Tasks

**Web Research**

> Research three emerging AI engineering trends and provide source URLs.

**Calculations**

> Calculate 249 multiplied by 36.

**Research Summaries**

> Find recent developments in AI agents and summarize the key themes.

**Tool-Based Assistance**

> Compare recent AI agent trends and explain their practical implications.

## 🛡️ Engineering Decisions

Vyrex uses a deliberately limited tool set instead of unrestricted system access.

- **Tool Allowlisting:** Only registered Python functions can be called.
- **Argument Validation:** Tool inputs are checked before execution.
- **Execution Limits:** The agent has a maximum number of tool-calling rounds.
- **Source Awareness:** Research outputs include retrieved URLs.
- **Failure Recovery:** Search failures can trigger additional attempts, and certain Groq parsing errors fall back to final-answer generation.
- **Secret Management:** API credentials are kept outside committed source files.

## ⚠️ Current Limitations

Vyrex is a Version 1 application.

- Web research is based on search-result snippets rather than full article extraction.
- Search availability depends on external providers and network conditions.
- Source references are not independently verified against complete webpages.
- The model can occasionally produce inaccurate or unsupported claims.
- Conversation history is displayed in the interface but is not yet passed into the agent as conversational memory.
- Successful web searches typically trigger final-answer generation, limiting deeper multi-stage research.
- The calculator currently supports basic arithmetic operations.
- Public use is subject to Groq API limits.

## 🗺️ Future Improvements

- Full webpage content retrieval
- Source verification and citation checking
- Persistent conversational memory
- Multi-step research planning
- More specialized productivity tools
- Tool execution evaluation
- Improved retry and rate-limit handling
- Research report formats and export options

## 👨‍💻 Author

**Syed Ali Tarikh**

AI Engineering | Generative AI | Agentic Systems

GitHub: [@Tarikh792](https://github.com/Tarikh792)

---

**Vyrex — Research. Reason. Execute.**

Built to explore real-world AI agent engineering through custom tool calling, tool execution, and agent orchestration.