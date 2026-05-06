from dotenv import load_dotenv
from agents import create_agents

load_dotenv()  # Load API keys from .env


def run_agent(user_message: str) -> None:
    """Run the Recipe & Nutrition Agent with a given user message."""
    assistant, user_proxy = create_agents()

    user_proxy.initiate_chat(
        assistant,
        message=user_message,
    )


if __name__ == "__main__":
    run_agent("I have chicken, lemon and garlic. I want a low calorie meal.")