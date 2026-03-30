import os
from groq import Groq
client = Groq(api_key="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")

def get_ai_response(user_input, chat_history=None):
    """
    This is the function app.py is trying to import.
    It takes user input and optional history, then returns the AI's string response.
    """
    if chat_history is None:
        chat_history = []
    messages = [{"role": "system", "content": "You are a helpful student assistant."}]
    
    for entry in chat_history:
        messages.append(entry)
    messages.append({"role": "user", "content": user_input})

    try:
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=messages,
            temperature=0.7,
            max_tokens=1024,
        )
        return completion.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"
if __name__ == "__main__":
    print("Testing chatbot.py...")
    print(get_ai_response("Hello!"))