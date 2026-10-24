import argparse
import os
import sys

import dotenv
from openai import OpenAI

CEFR_LEVELS = ["A1", "A2", "B1", "B2", "C1", "C2"]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Text tutor to practice a language.")
    parser.add_argument("level", choices=CEFR_LEVELS, help="your CEFR level")
    return parser.parse_args()


def build_system_prompt(level: str, language: str) -> str:
    """Build the tutor's system prompt for a learner's CEFR level and language."""
    return (
        f"You are a friendly {language} tutor having a conversation with a learner "
        f"at CEFR level {level}. Always reply in {language}, using vocabulary and "
        f"grammar suited to {level}. Keep replies short (2-3 sentences), as in a "
        "spoken conversation, and end with a question to keep it going. If the "
        "learner makes a mistake, gently repeat the correct form, then continue."
    )


def chat(client: OpenAI, model: str, messages: list[dict]) -> str:
    response = client.chat.completions.create(model=model, messages=messages)
    return response.choices[0].message.content or ""


def run() -> None:
    args = parse_args()
    dotenv.load_dotenv()
    client = OpenAI(
        api_key=os.getenv("LLM_API_KEY"), base_url=os.getenv("LLM_BASE_URL")
    )
    model = os.getenv("LLM_MODEL")

    if not model:
        print("Error: LLM_MODEL is not set.")
        sys.exit(1)

    messages = [
        {"role": "system", "content": build_system_prompt(args.level, "Italian")}
    ]
    print("Type 'exit' to quit.")

    try:
        while True:
            text = input("You: ").strip()
            if not text:
                continue
            if text.lower() == "exit":
                break
            messages.append({"role": "user", "content": text})
            reply = chat(client, model, messages)
            print(f"Tutor: {reply}")
            messages.append({"role": "assistant", "content": reply})
    except (KeyboardInterrupt, EOFError):
        print()
    print("Ciao!")
