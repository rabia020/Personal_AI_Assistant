# 🤝 Personal AI Assistant (Agentic AI + n8n + Streamlit)
## 📌 Overview

This project is a Personal AI Assistant built using an Agentic AI architecture that connects a Streamlit frontend with an n8n workflow backend. The assistant can understand user queries and autonomously route them to different tools such as email, calendar, task management, notes, expense tracking, and web search.

It behaves like a multi-tool AI agent capable of executing real-world productivity workflows.

## 🚀 Features
💬 Conversational AI chat interface
📅 Google Calendar event management (create & fetch events)
📧 Gmail integration (read, summarize, and send emails)
📝 Notes creation and updates (Google Docs integration)
✅ Task management (create, fetch, delete tasks)
💰 Expense tracking system
🔍 Google Search integration via tool calling
🧠 Memory support for contextual conversations
⚙️ Automated workflow execution using n8n

# 🧠 Architecture

The system is built using an Agentic AI workflow:

### Streamlit Frontend
→ Sends user queries via webhook
→ Receives AI response

### n8n Workflow Engine
→ AI Agent receives input
→ Decides which tool to use
→ Executes required action (Gmail, Calendar, Tasks, etc.)
→ Returns structured response

## 🖼️ Workflow Diagram
<img width="1770" height="802" alt="image" src="https://github.com/user-attachments/assets/ac9c3968-192e-4e1e-b1bf-0749de2d1dcf" />

## 🛠️ Tech Stack
Python
Streamlit
n8n (workflow automation)
REST APIs (webhooks)
Google APIs (Gmail, Calendar, Docs)
AI Agent (LLM-based orchestration)

## 📂 Project Structure
project/
│
├── app.py                # Streamlit frontend
├── requirements.txt      # Dependencies
└── README.md

## ⚙️ How It Works
User enters a message in Streamlit chat UI
Message is sent to n8n webhook
AI Agent analyzes intent
Appropriate tool is triggered:
Gmail tool → email operations
Calendar tool → scheduling
Task tool → task management
Notes tool → documentation
Search tool → web queries
Response is returned to Streamlit UI
