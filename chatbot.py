import re
import json
import datetime
import random
import tkinter as tk
from tkinter import scrolledtext

# ----------------------------
# Load Knowledge Base from JSON
# ----------------------------
def load_knowledge_base(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)

knowledge_base = load_knowledge_base("knowledge_base.json")

# ----------------------------
# Intent Patterns
# ----------------------------
intents = {
    "greeting": r"\b(hi|hello|hey|good morning|good evening)\b",
    "help": r"\b(help|support|assist)\b",
    "small_talk": r"\b(how are you|what's up|how is it going)\b",
    "exit": r"\b(bye|exit|quit|goodbye)\b"
}

# ----------------------------
# Response Rules
# ----------------------------
responses = {
    "greeting": "Hello! 👋 How can I assist you today?",
    "help": "I can answer AI-related questions. Try asking 'What is AI?'",
    "small_talk": "I'm just a bot, but I'm doing great! 😊",
    "fallback": "I'm not sure about that. Can you rephrase?"
}

# ----------------------------
# Track used answers for non-repeating responses
# ----------------------------
used_answers = {}

# ----------------------------
# Chatbot Response Function
# ----------------------------
def chatbot_response(user_input):
    global used_answers
    user_input = user_input.lower().strip()
    words = set(user_input.split())

    best_match = None
    best_keywords = None  # Initialize to avoid NameError
    max_matches = 0

    # Find best matching knowledge-base item
    for item in knowledge_base:
        keywords = set(item["keywords"])
        matches = len(keywords.intersection(words))

        if matches > max_matches:
            max_matches = matches
            best_match = item["answer"]
            best_keywords = tuple(keywords)  # use as key for used_answers

    # Knowledge-base match
    if max_matches >= 2 and best_match is not None:
        if isinstance(best_match, list):
            if best_keywords not in used_answers:
                used_answers[best_keywords] = []

            remaining = [a for a in best_match if a not in used_answers[best_keywords]]

            if not remaining:
                # All used, reset
                used_answers[best_keywords] = []
                remaining = best_match.copy()

            choice = random.choice(remaining)
            used_answers[best_keywords].append(choice)
            return choice

        return best_match

    # Check intents
    for intent, pattern in intents.items():
        if re.search(pattern, user_input):
            if intent == "exit":
                return "Goodbye! 👋 Have a nice day!"
            return responses[intent]

    return responses["fallback"]

# ----------------------------
# Logging Function
# ----------------------------
def log_conversation(user, bot):
    with open("chat_log.txt", "a", encoding="utf-8") as file:
        timestamp = datetime.datetime.now()
        file.write(f"[{timestamp}] User: {user}\n")
        file.write(f"[{timestamp}] Bot: {bot}\n")

# ----------------------------
# GUI Functions
# ----------------------------
def send_message():
    user_input = entry_box.get().strip()
    if user_input == "":
        return

    # Show user message
    chat_window.insert(tk.END, "User: " + user_input + "\n")
    
    # Get bot reply
    bot_reply = chatbot_response(user_input)
    
    # Show bot reply
    chat_window.insert(tk.END, "Bot: " + bot_reply + "\n\n")

    # Auto scroll
    chat_window.yview(tk.END)

    log_conversation(user_input, bot_reply)

    entry_box.delete(0, tk.END)

    if re.search(intents["exit"], user_input.lower()):
        root.after(1500, root.destroy)

# ----------------------------
# Create Main Window
# ----------------------------
root = tk.Tk()
root.title("AI Chatbot")
root.geometry("500x600")

# Chat window
chat_window = scrolledtext.ScrolledText(root, wrap=tk.WORD, font=("Arial", 12))
chat_window.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
chat_window.config(state=tk.NORMAL)

# Frame for entry + button
input_frame = tk.Frame(root)
input_frame.pack(padx=10, pady=5, fill=tk.X)

# Label
label = tk.Label(input_frame, text="Type your message:", font=("Arial", 12))
label.pack(side=tk.LEFT, padx=(0,5))

# Entry box
entry_box = tk.Entry(input_frame, font=("Arial", 12))
entry_box.pack(side=tk.LEFT, fill=tk.X, expand=True)
entry_box.bind("<Return>", lambda event: send_message())

# Send button
send_button = tk.Button(input_frame, text="Send", command=send_message)
send_button.pack(side=tk.RIGHT, padx=(5,0))

# ----------------------------
# Bot greets first
# ----------------------------
chat_window.insert(tk.END, "Bot: Greetings! 🤖 How can I help you today?\n\n")

# Start GUI loop
root.mainloop()