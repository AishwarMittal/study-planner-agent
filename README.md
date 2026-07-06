# Study Planner Agent

An AI-powered study planning agent built using Google's Agent Development Kit (ADK) and Gemini, created as a capstone for the Google & Kaggle AI Agents Intensive 2026.

## The Problem

Students often don't know how to organize their study time before exams, leading to last-minute cramming and poor performance.

## The Solution

This agent takes a subject and exam date from the student and generates a personalized, day-by-day study plan. Students can then have a conversation with the agent to adjust or improve the plan.

## Architecture

- **Framework:** Google Agent Development Kit (ADK)
- **Model:** Gemini 2.5 Flash via Google AI Studio
- **Session:** InMemorySessionService (maintains conversation history)
- **Interface:** Command-line chat
- **Security:** API key stored in `.env` file, not in code

## How to Run

1. Clone this repository
2. Install packages: `pip install google-adk google-genai python-dotenv`
3. Create a `.env` file with: `GOOGLE_API_KEY=your_key_here`
4. Run: `python main.py`
5. Type your subject and exam date when prompted

## Deployability

This agent can be containerized with Docker and deployed on Google Cloud Run as a REST API endpoint. A web frontend or WhatsApp bot could connect to it, making it accessible to students anywhere without needing to run code locally.

## Google Concepts Demonstrated

- **Agent/Multi-agent system** using Google ADK
- **Security:** API key management via environment variables
- **Deployability:** architecture designed for Cloud Run deployment