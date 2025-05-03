# 🔗 LinkLens 

> **Graph-Augmented GenAI for Personalized Suggestions and Smart QA**

**LinkLens** is a GenAI system that models user-entity interactions as a graph, enabling intelligent suggestions and natural language question answering using LLMs.  
Built with Django, Neo4j, and LangChain, it turns raw interaction events (like, hate, follow, etc.) into meaningful knowledge and context-aware recommendations.

---

[![Postman Collection](https://img.shields.io/badge/Postman-Collection-a)](https://www.postman.com/blue-station-79898/workspace/linklens)
For an easier experience with the API, you can explore my Postman collection.

---

### 📌 Key Features

- 🧠 **Graph-Powered AI Reasoning** — Every user interaction is stored as a relationship in Neo4j.
- 💬 **Smart Chat API** — Ask natural language questions like _"What movie does John like?"_
- 🎯 **Suggestion Engine** — Recommend relevant entities for a user using real-time graph traversal + LLMs.
- 👤 **Full CRUD APIs** — Create, update, and delete users, entities, and their interaction events.
- 📊 **Real-Time Logging** — Integrated with Logstash, Elasticsearch, and Kibana.
- 🐳 **Containerized** — Easily deployable with Docker Compose.

---

### 🧠 How It Works

```plaintext
Users + Entities + Events → Neo4j Graph → LangChain → LLM Response
```

---

## 🔧 Tech Stack

| Layer           | Stack                                  |
|-----------------|----------------------------------------|
| Backend         | Django, Django REST Framework (DRF)    |
| GenAI           | Langchain + OpenAI/AI21                |
| Graph DB        | Neo4j                                  |
| Logging         | Logstash, Kibana (ELK Stack)           |
| Deployment      |	Docker + Docker Compose                |

---

## 📁 Project Structure

```
QueryBaseAI/
├── Backend/           # Django logic (views, serializers, APIs)
├── Core/              # Core database logics
├── LLM/               # LLM providers (OpenAI & AI21 logic)
├── GraphDB /          # Neo4J logics aand connector
├── Constants/         # LinkLens project constants
├── Models/            # All django models like user, entity, event
└── README.md          # Project documentation
```

---

## 💻 Getting Started

1. Clone the repository from GitHub to your local machine
```bash
git clone https://github.com/GoodGuyAdy/LinkLens.git
```
2. Change the current directory to the cloned project folder
```bash
cd LinkLens
```
3. Install the Python dependencies listed in the requirements.txt file
```bash
pip install -r requirements.txt
```
4. Build and starts the Docker containers defined in the docker-compose.yml file
```bash
docker-compose up --build
```
5. Run the Django development server for the project
```bash
python manage.py runserver
```

---

## 🧑🏻‍🔧 Troubleshooting :-
 
 - Ensure that your .env file contains a valid OPENAI_API_KEY or AI21_API_KEY.
 - Make sure you have an active internet connection.

---