import os
from autogen import AssistantAgent, UserProxyAgent
from tools import search_recipes, get_nutrition, get_recipe_steps

# Tool schemas tell the LLM exactly how to call each tool
# Necessary when using a non-OpenAI model
TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "search_recipes",
            "description": "Search for recipes based on available ingredients.",
            "parameters": {
                "type": "object",
                "properties": {
                    "ingredients": {
                        "type": "string",
                        "description": "Comma-separated list of ingredients, e.g. 'chicken, lemon, garlic'",
                    }
                },
                "required": ["ingredients"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "get_nutrition",
            "description": "Fetch nutrition data for a recipe by its Spoonacular ID.",
            "parameters": {
                "type": "object",
                "properties": {
                    "recipe_id": {
                        "type": "integer",
                        "description": "The Spoonacular recipe ID.",
                    }
                },
                "required": ["recipe_id"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "get_recipe_steps",
            "description": "Fetch step-by-step cooking instructions for a recipe by its Spoonacular ID.",
            "parameters": {
                "type": "object",
                "properties": {
                    "recipe_id": {
                        "type": "integer",
                        "description": "The Spoonacular recipe ID.",
                    }
                },
                "required": ["recipe_id"],
            },
        },
    },
]


LLM_CONFIG = {
    "model": "mistral-small-latest",
    "api_key": os.getenv("MISTRAL_API_KEY"),
    "api_type": "mistral",
    "temperature": 0,     # No creativity, we want consistent, predictable answers
    "native_tool_calls": False,  # Forces AutoGen to handle tool calls itself
    "tools": TOOLS,
}

# System prompt: tells the LLM who it is and how to behave
SYSTEM_PROMPT = """
You are a helpful Recipe & Nutrition Agent.

Your job is to:
1. Receive a list of ingredients from the user (and optionally a nutrition goal).
2. Call search_recipes to find matching recipes.
3. Pick the most relevant recipe and call get_nutrition to retrieve its nutrition data.
4. Evaluate whether the recipe meets the user's goal (e.g. low calorie, high protein).
5. Call get_recipe_steps to fetch the cooking instructions for the chosen recipe.
6. Present the final result using EXACTLY this format:

---
### Recipe: <recipe title>

**Ingredients used:** <comma-separated list of used ingredients>
**Missing ingredients:** <comma-separated list or "None">

**Nutrition Facts (per serving):**
- Calories: <value>
- Protein: <value>
- Fat: <value>
- Carbs: <value>

**Evaluation:** <one sentence on whether the recipe meets the goal>

**How to cook it:**
<numbered list of steps from get_recipe_steps>

**Recommendation:** <one clear sentence> TERMINATE
---

Rules:
- Always respond in English regardless of the language of the user's input.
- Always translate ingredients to English before calling search_recipes.
- Always call search_recipes before get_nutrition and get_recipe_steps.
- Never guess nutrition values or cooking steps - always use the tools.
- If the user provides no ingredients, state that you need at least one ingredient and end with TERMINATE.
- If the user states a contradictory goal (e.g. both high and low calorie), explain that the goal is contradictory and end with TERMINATE.
- If the user's calorie goal is impossible to meet (e.g. under 50 calories), state clearly that no real meal can meet this goal and end with TERMINATE.
- If no recipes are found or an error occurs, explain this clearly and end with TERMINATE.
- If the ingredients are clearly not real food items, state that the ingredients are not recognizable and end with TERMINATE.
- If no nutrition goal is stated, default to checking whether the meal is under 600 calories.
- Never ask follow-up questions.
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
        is_termination_msg=lambda msg: "TERMINATE" in msg.get("content", ""),
        function_map={
            "search_recipes": search_recipes,
            "get_nutrition": get_nutrition,
            "get_recipe_steps": get_recipe_steps,
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

















