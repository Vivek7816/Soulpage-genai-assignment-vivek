# Conersational Knowledge Bot (Langchain + Memory + Wikipidea)

# Overview of the project
1. Answer factual questions using an external knowledge source
2. Maintain coversational context across multiple turns
3. Handle follow-up questions based on previous conversations

The bot is built using "Python" and "Langchain", with "Wikipedia" as a free external knowledge source.
This approach avoids paid LLM APIs while still demonstrating tool integration, memory, and conversational flow.

# Features
1. External knowledge lookup via Wikipidea API
2. No API keys or paid services requires as I used Wikipedia API
3. Runs locally via a command-line interface
4. Follows contextual handling such as pronouns like "he/she"

# Tech Stack
1. Python 3.10
2. LangChain (memory abstraction)
3. Wikipedia API (Data source)

# Structure of the Project
1. main.py (python)
2. README.md (documentation)
3. requirements.txt 
4. venv/ (local)