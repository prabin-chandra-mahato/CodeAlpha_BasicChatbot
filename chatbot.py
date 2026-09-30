import os
import time

from dotenv import load_dotenv
from google import genai


load_dotenv()


MODEL_NAME = "gemini-3.6-flash"


def create_client():
    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        print("Gemini API key was not found.")
        print("Please add GEMINI_API_KEY to the .env file.")
        return None

    try:
        return genai.Client(api_key=api_key)

    except Exception as error:
        print("Could not create the Gemini client.")
        print(f"Error: {error}")
        return None


def get_response(client, user_input, previous_interaction_id=None):
    max_attempts = 3

    for attempt in range(1, max_attempts + 1):
        try:
            request_data = {
                "model": MODEL_NAME,
                "input": user_input
            }

            if previous_interaction_id:
                request_data["previous_interaction_id"] = (
                    previous_interaction_id
                )

            interaction = client.interactions.create(**request_data)

            if interaction.output_text:
                return interaction.output_text.strip(), interaction.id

            return "I couldn't generate a response.", interaction.id

        except Exception as error:
            error_message = str(error)

            if (
                "503" in error_message
                or "UNAVAILABLE" in error_message
            ):
                if attempt < max_attempts:
                    wait_time = 2 ** attempt

                    print(
                        f"Gemini is temporarily busy. "
                        f"Retrying in {wait_time} seconds..."
                    )

                    time.sleep(wait_time)
                    continue

                return (
                    "Gemini is currently busy. "
                    "Please try again in a moment.",
                    previous_interaction_id
                )

            print(f"API error: {error}")

            return (
                "Sorry, I couldn't process your request right now.",
                previous_interaction_id
            )

    return (
        "Sorry, I couldn't process your request right now.",
        previous_interaction_id
    )


def run_chatbot():
    print("=" * 50)
    print("              BASIC AI CHATBOT")
    print("=" * 50)
    print("Powered by Google Gemini")
    print("Type 'bye' to end the conversation.\n")

    client = create_client()

    if client is None:
        return

    previous_interaction_id = None

    while True:
        user_input = input("You: ").strip()

        if not user_input:
            print("Bot: Please type something.\n")
            continue

        if user_input.lower() in ["bye", "goodbye", "exit"]:
            print("Bot: Goodbye! Have a great day.")
            break

        response, previous_interaction_id = get_response(
            client,
            user_input,
            previous_interaction_id
        )

        print("Bot:", response)
        print()


print("Welcome to the Basic AI Chatbot!")
run_chatbot()
print("\nThanks for chatting!")