# AI Engineering "Shared Brain" Vault

Welcome to the collaborative knowledge base for AI Engineers. This vault uses the **CAST** (Concepts, Applied, Sources, Tools) abstraction to turn raw information into reusable technical intelligence.

## 🧠 The Architecture: Shared Core vs. Private Layer

To enable collaboration on GitHub while protecting proprietary project logic, we split the vault into two layers:

### 1. The Shared Core (Contribute via PR)
These folders contain the "Physics" of AI Engineering. We build these together.
- **`/Concepts`**: The theoretical paradigms (e.g., RAG, Agentic Workflows, LoRA).
- **`/Tools`**: The technical primitives (e.g., LangChain, ChromaDB, Llama-3).
- **`/Hubs`**: Maps of Content (MOCs) that link concepts and tools together.
- **`/Assets`**: Shared templates, CLI playbooks, and reference architectures.

### 2. The Private Layer (Ignored by Git)
These folders are for your local execution. They are listed in `.gitignore`.
- **`/Applied`**: Your specific system designs, proprietary prompts, and active projects.
- **`/Sources`**: Your personal library of ingested transcripts, papers, and raw data.
- **`/Daily_Notes`**: Your personal workspace and log.

---

## 🚀 Getting Started

1. **Clone the Repo:** `git clone <repo-url>`
2. **Setup Folders:** Ensure you have local `/Applied` and `/Sources` folders (Git will ignore these).
3. **Use the Agent:** Feed the `AGENTS.md` prompt to your LLM of choice to start ingesting new knowledge.
4. **Contribute:** If you learn a new concept or find a better way to use a tool, submit a Pull Request to the `/Concepts` or `/Tools` folders.

---

## 🤖 The Agent Prompt
The master ingestion logic is located in `AGENTS.md`. Use this to process URLs, YouTube videos, and research papers directly into this vault.

> Core Node: [[Applied/AI_Native_Engineer]]
