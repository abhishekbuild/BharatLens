# 🌏 BharatLens

**BharatLens** is a AI-powered multimodal RAG platform designed to explore and understand global geopolitics through **India’s perspective**.  
It provides clear, insightful responses that help users grasp the **strategic, economic, and cultural dimensions** of international affairs.  

Whether it’s analyzing global events, interpreting diplomatic trends, or contextualizing policies, BharatLens offers an **India-centered lens** to view the world.

---

## 🚀 Project Overview

- **Frontend**: Built in **React.js** (designed using [Lovable](https://lovable.app)) and deployed separately (link will be added soon).  
- **Backend**: FastAPI server with:
  - Async support (async SQLAlchemy, asyncpg, etc.)
  - JWT Authentication
  - Session & Conversation management
  - Integration with **OpenAI LLM**
  - Implemented **RAG (Retrieval-Augmented Generation)**  
- **Database**: PostgreSQL (hosted on [Neon](https://neon.tech))  
- **Deployment**: Deployed on [Render.com](https://render.com) using Docker + GitHub Actions CI/CD.  
- **Try Out Live API**: [https://bharatlens.onrender.com/docs](https://bharatlens.onrender.com/docs)  

---

## 📂 Features

- 🔐 **User Authentication** (Register, Login, Profile Management)  
- 💬 **Chat Sessions**: Create sessions, store conversation history  
- 🤖 **LLM Integration**: Powered by OpenAI GPT  
- 📜 **Conversation History**: Retrieve past chats, with pagination support  
- 🗑️ **Delete Sessions**: Cascade delete messages when a session is removed  
- 🧩 **Modular Architecture**: Easily extendable

---

## ⚡ API Endpoints

### Authentication
- `POST /auth/register` → Register new user  
- `POST /auth/login` → Login and get JWT token  

### Chat
- `POST /api/v1/chat/sessions` → Create new chat session  
- `GET /api/v1/chat/sessions` → Get all user sessions with messages  
- `DELETE /api/v1/chat/sessions/{session_id}` → Delete session + messages  
- `POST /api/v1/chat/sessions/{session_id}/messages` → Send message & get LLM response  
- `GET /api/v1/chat/sessions/{session_id}/messages` → Get messages (paginated)  

---

## 🛠️ Running Locally

### 1. Clone the Repository
```bash
git clone https://github.com/1abhi6/BharatLens
cd BharatLens
````

### 2. Setup Environment

Copy `.env.example` to `.env` and fill in your secrets:

```bash
cp .env.example .env
```

Required values:

* `DATABASE_URL` → Neon Postgres connection string
* `JWT_SECRET_KEY` → Any secure random string
* `OPENAI_API_KEY` → Your OpenAI API key

### 3. Create & Activate Virtual Environment
I recommend [`uv`](https://github.com/astral-sh/uv) as a package manager for speed and reproducibility:

```bash
uv venv
```

```bash
.\.venv\Scripts\activate
```

### 3. Install Dependencies (using `uv`)

```bash
uv pip install -r pyproject.toml
```

### 4. Run the App

```bash
uvicorn app.main:app --reload
```

Backend will be available at `http://localhost:8000`

API docs are available at `http://localhost:8000/docs`

---

## 🐳 Docker Support

You can also run the backend inside a container:

```bash
docker build -t bharatlens-backend .
docker run --env-file .env -p 8000:8000 bharatlens-backend
```

---

## 🔗 Frontend

The **frontend UI** is built separately in React (repo link will be added here).
Once deployed, the UI connects to this backend at [https://bharatlens.onrender.com](https://bharatlens.onrender.com).

---

## 🤝 Contributing

Pull requests are welcome! Please open an issue first to discuss changes.
Make sure to update tests as appropriate.

---

## 📜 License

This project is licensed under the MIT License.

---

## 👨‍💻 About the Developer  

Developed with ❤️ by **Abhishek Gupta**  

🌐 [LinkedIn](https://www.linkedin.com/in/iautomates)  

---
