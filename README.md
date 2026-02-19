                      AI Chatbot
Rule-Based Conversational System | Python | Tkinter | JSON
===========================================================
A desktop-based AI chatbot built using Python that demonstrates structured problem-solving, modular architecture, and foundational Natural Language Processing (NLP) concepts.
This project was developed to explore how conversational systems work at a fundamental level — without relying on external machine learning libraries.

Project Objective:
------------------
The goal of this project is to:
-> Design a modular conversational system
-> Implement deterministic intent recognition
-> Build a scalable knowledge-base structure
-> Develop a GUI-based user interaction system
-> Apply clean code principles and separation of concerns
-> This chatbot simulates intelligent conversation using keyword scoring and regex-based intent classification.

Technical Highlights:
---------------------

1. Knowledge Base Engine:
.........................
> External JSON-driven knowledge storage
> Keyword-based scoring using set intersection
> Minimum threshold matching (≥ 2 keywords)
> Supports both single and multiple response formats
> Prevents repeated responses using tracking logic

2. Intent Recognition System:
............................
> Regex-powered intent detection
> Handles:
(i) Greetings
(ii) Help requests
(iii)Small talk
(iv) Exit commands
(v) Fallback mechanism for unmatched queries

3. Response Optimization:
.........................
> Best-match selection algorithm
> Randomized non-repeating responses
> Clean fallback hierarchy:
> Knowledge base
> Intent rules
> Default response

4. Logging & Traceability:
.........................
> Persistent logging to chat_log.txt
> Timestamped entries
> Useful for debugging and analytics

5. GUI Implementation:
......................
> Built using Tkinter (standard Python library)
> Scrollable chat interface
> eyboard event binding (Enter key support)
> Graceful exit handling
> Cross-platform compatibility

System Architecture Overview:
-----------------------------
User Input:
→ Text Normalization
→ Keyword Matching (Knowledge Base)
→ Intent Pattern Matching (Regex)
→ Response Selection
→ Logging
→ GUI Display

How to Run:
-----------
Requirements:
-> Python 3.8+
-> No external dependencies

Setup:
git clone https://github.com/Fazlul03/AIChatbot.git
cd AIChatbot
python chatbot.py

Design Decisions:
-----------------
> Rule-Based System: Chosen for interpretability and deterministic behavior.
> JSON Knowledge Base: Enables easy extension without modifying application logic.
> Regex Intent Detection: Lightweight alternative to ML-based classifiers.
> Response Randomization: Improves conversational variability while maintaining control.
> Tkinter GUI: Provides cross-platform desktop support without third-party libraries.

Use Cases:
----------
-> Academic demonstration of rule-based NLP systems
-> Beginner AI/NLP portfolio project
-> Prototype conversational logic testing
-> GUI application architecture practice

Limitations:
------------
-> No contextual memory beyond single query
-> No NLP preprocessing (stemming, lemmatization, stopword removal)
-> Keyword matching is surface-level
-> No machine learning integration
