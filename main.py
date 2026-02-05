import wikipedia
from langchain.memory import ConversationBufferMemory

memory = ConversationBufferMemory()


last_entity = {"person": None}

def search_wikipedia(query):
    try:
        summary = wikipedia.summary(query, sentences=3)
        return summary
    except wikipedia.exceptions.DisambiguationError as e:
        return f"Your query is ambiguous. Possible options: {e.options[:5]}"
    except Exception:
        return "I could not find information on that topic."


print("Wikipedia Conversational Knowledge Bot (type 'exit' to quit)\n")

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break

   
    memory.save_context({"input": user_input}, {"output": ""})

    
    if user_input.lower().startswith("who is"):
        entity = user_input.replace("who is", "").strip()
        last_entity["person"] = entity
        answer = search_wikipedia(entity)

    
    elif "he" in user_input.lower() or "she" in user_input.lower():
        if last_entity["person"]:
            query = f"{last_entity['person']} {user_input}"
            answer = search_wikipedia(query)
        else:
            answer = "I am not sure who you are referring to."

    
    else:
        answer = search_wikipedia(user_input)

    print("Bot:", answer, "\n")
