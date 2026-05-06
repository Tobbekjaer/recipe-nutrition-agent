import os
from autogen import AssistantAgent, UserProxyAgent
from tools import search_recipes, get_nutrition

LLM_CONFIG = {
    "model": "gpt-4o-mini",
    "api_key": os.getenv("OPENAI_API_KEY"),
    "temperature": 0,    # No creativity, we want consistent, predictable answers
}

# System prompt: tells the LLM who it is and how to behave
SYSTEM_PROMPT = """
You are a helpful Recipe & Nutrition Agent.

Your job is to:
1. Receive a list of ingredients from the user (and optionally a nutrition goal).
2. Call search_recipes to find matching recipes.
3. Pick the most relevant recipe and call get_nutrition to retrieve its nutrition data.
4. Evaluate whether the recipe meets the user's goal (e.g. low calorie, high protein).
5. Present the result clearly, including recipe name, nutrition facts, and your evaluation.

Rules:
- Always call search_recipes before get_nutrition.
- Never guess nutrition values - always use get_nutrition for real data.
- If no recipes are found or an error occurs, explain this clearly to the user.
- If no nutrition goal is stated, default to checking whether the meal is under 600 calories.
- Always end with a clear recommendation: does this recipe meet the goal or not?
"""


def create_agents():
    # AssistantAgent is the "brain" - it decides what to do and in what order
    assistant = AssistantAgent(
        name="RecipeAssistantAgent",
        system_message=SYSTEM_PROMPT,
        llm_config=LLM_CONFIG,
    )

    # UserProxyAgent is the "hands" - it executes the tool calls the assistant requests
    user_proxy = UserProxyAgent(
        name="UserProxyAgent",
        human_input_mode="NEVER",  # Fully autonomous - no human input during runtime
        max_consecutive_auto_reply=5,  # Safety limit to prevent infinite loops
        code_execution_config=False,  # We use registered tools, not code execution
        function_map={
            "search_recipes": search_recipes,
            "get_nutrition": get_nutrition,
        },
    )

    # Register tools on the assistant so the LLM knows they exist and how to call them
    assistant.register_function(
        function_map={
            "search_recipes": search_recipes,
            "get_nutrition": get_nutrition,
        }
    )

    return assistant, user_proxy

















