This project implements an AI conversational assistant with multiple services. (url http://127.0.0.1:7860)

Service 1 — API Weather Service

This service retrieves real-time weather information using an external API backend. The system sends a request to wttr.in and receives structured weather data for a specified city.

The response is processed and reformatted into a natural language summary rather than returning raw API output. This service demonstrates external API integration, response transformation, and conversational delivery through the chat interface.


Service 2 — Semantic Search

This service answers conceptual questions using semantic similarity instead of keyword matching.

A local dataset (data/knowledge.txt) contains short AI and machine learning concepts. Each line is converted into a vector embedding using the SentenceTransformer model all-MiniLM-L6-v2.

Embeddings are generated once using build_db.py and stored in a persistent ChromaDB database (chroma_db). This allows the system to reuse embeddings without recomputation.

When a user asks a knowledge question, the query is embedded and compared with stored vectors. The most relevant results are retrieved and returned as a natural language response.


Service 3: Study Plan Generation Tool
This service generates a structured study plan based on a user’s requested topic and duration. It is implemented as a function-based tool that produces organized learning steps rather than retrieving external data.

The system analyzes the requested topic and selects appropriate learning modules (e.g., fundamentals, practice exercises, and project work). It then builds a multi-day schedule with specific tasks for each day.

The service is integrated into the chat interface through routing logic in app.py. When a user requests a study plan, the tool is executed and the generated plan is returned in natural language form.
