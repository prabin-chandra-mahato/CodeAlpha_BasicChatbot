# CodeAlpha Basic AI Chatbot

A simple console-based AI chatbot built with Python and enhanced with the Google Gemini API.

I built this project as part of my CodeAlpha Python Programming Internship. I started with a basic chatbot structure and then connected it to Gemini so that the chatbot could respond to a wider range of questions instead of relying only on fixed replies.

## About the Project

The chatbot runs directly in the terminal and communicates with the user through text input.

It can maintain context during a conversation, answer general questions, explain topics, perform simple reasoning and calculations, and respond naturally to different messages.

The chatbot also handles basic commands such as `bye`, `goodbye`, and `exit` to end the conversation.

## What the Chatbot Can Do

- Accepts natural-language questions
- Generates responses using Google Gemini
- Maintains conversation context
- Handles empty input
- Supports `bye`, `goodbye`, and `exit`
- Handles temporary API failures
- Keeps the API key outside the source code
- Uses environment variables for API configuration

## Example Conversation

```text
Welcome to the Basic AI Chatbot!
==================================================
              BASIC AI CHATBOT
==================================================
Powered by Google Gemini
Type 'bye' to end the conversation.

You: hi
Bot: Hello! How can I help you today?

You: my name is ace
Bot: Nice to meet you, Ace! How can I help you today?

You: what is my name?
Bot: Your name is Ace!

You: who invented the light bulb?
Bot: [Gemini-generated response]

You: bye
Bot: Goodbye! Have a great day.

Thanks for chatting!

    "Installation:"

Make sure Python 3 is installed.

Install the required packages using:

pip install -r requirements.txt

API Key Setup:

This project uses a Google Gemini API key.

Create a .env file in the project folder:

GEMINI_API_KEY=your_api_key_here

Replace your_api_key_here with your own Gemini API key. 


How to Run

After installing the dependencies and configuring the API key, run:

python chatbot.py

in terminal

Important

Notice that the README **does not contain your actual API key**.

Your local folder can have:

```text
.env

"""WHILE USING OR RUNNING IT ERRORS MAY COME

BUT NO NEED TO REPLACE API KEY

INSTEAD CHECK THAT WHAT IS THE API KEY VERSION."""

THIS CHATBOT WILL NOT WORK UNLESS YOU GIVE YOUR API FROM GOOGLE AI STUDIO.