import os
import requests
from logger import log_tool_call

SPOONACULAR_API_KEY = os.getenv("SPOONACULAR_API_KEY")
BASE_URL = "https://api.spoonacular.com"

# Searches Spoonacular for matching recipes
def search_recipes(ingredients: str) -> dict:
    """Find recipes based on a comma-separated list of ingredients."""

    # Guard against empty input to return early with a clear error
    if not ingredients or not ingredients.strip():
        result = {"error": "No ingredients provided. Please provide at least one ingredient."}
        log_tool_call("search_recipes", {"ingredients": ingredients}, result)
        return result

    url = f"{BASE_URL}/recipes/findByIngredients"
    params = {
        "apiKey": SPOONACULAR_API_KEY,
        "ingredients": ingredients,
        "number": 5,          # Return top 5 matches
        "ranking": 1,         # Prioritize recipes that use the most provided ingredients
        "ignorePantry": True, # Ignore common pantry items like water and salt
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()     # Raises an error for 4xx/5xx responses
        data = response.json()

        if not data:
            result = {"error": f"No recipes found for ingredients: {ingredients}"}
            log_tool_call("search_recipes", {"ingredients": ingredients}, result)
            return result

        # Extract only what the agent needs to keep it lean
        recipes = [
            {
                "id": r["id"],
                "title": r["title"],
                "used_ingredients": [i["name"] for i in r["usedIngredients"]],
                "missing_ingredients": [i["name"] for i in r["missedIngredients"]],
            }
            for r in data
        ]

        result = {"recipes": recipes}
        log_tool_call("search_recipes", {"ingredients": ingredients}, result)
        return result

    except requests.exceptions.Timeout:
        result = {"error": "Request timed out. Please try again."}
        log_tool_call("search_recipes", {"ingredients": ingredients}, result)
        return result
    except requests.exceptions.RequestException as e:
        result = {"error": f"API request failed: {str(e)}"}
        log_tool_call("search_recipes", {"ingredients": ingredients}, result)
        return result

# Gets nutritional facts about a recipe
def get_nutrition(recipe_id: int) -> dict:
    """
    nutrition data for a specific recipe by its Spoonacular ID.
    This is the deterministic step - numbers come directly from the API, no LLM guessing.
    """
    # Guard against missing recipe ID
    if not recipe_id:
        result = {"error": "No recipe ID provided."}
        log_tool_call("get_nutrition", {"recipe_id": recipe_id}, result)
        return result

    url = f"{BASE_URL}/recipes/{recipe_id}/nutritionWidget.json"
    params = { "apiKey": SPOONACULAR_API_KEY }

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()

        # Pull out the foru key nutrition values
        result = {
            "recipe_id": recipe_id,
            "calories": data.get("calories", "N/A"),
            "protein": data.get("protein", "N/A"),
            "fat": data.get("fat", "N/A"),
            "carbs": data.get("carbs", "N/A"),
        }
        log_tool_call("get_nutrition", {"recipe_id": recipe_id}, result)
        return result

    except requests.exceptions.Timeout:
        result = {"error": "Request timed out. Please try again."}
        log_tool_call("get_nutrition", {"recipe_id": recipe_id}, result)
        return result
    except requests.exceptions.RequestException as e:
        result = {"error": f"API request failed: {str(e)}"}
        log_tool_call("get_nutrition", {"recipe_id": recipe_id}, result)
        return result


# Gets recipe preparation steps
def get_recipe_steps(recipe_id: int) -> dict:
    """
        Fetch step-by-step cooking instructions for a recipe by its Spoonacular ID.
        Returns a list of steps with instructions.
        """
    if not recipe_id:
        result = {"error": "No recipe ID provided."}
        log_tool_call("get_recipe_steps", {"recipe_id": recipe_id}, result)
        return result

    url = f"{BASE_URL}/recipes/{recipe_id}/analyzedInstructions"
    params = {"apiKey": SPOONACULAR_API_KEY}

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()

        if not data or not data[0].get("steps"):
            result = {"error": f"No instructions found for recipe ID: {recipe_id}"}
            log_tool_call("get_recipe_steps", {"recipe_id": recipe_id}, result)
            return result
        # Extract step number and instruction text only
        steps = [
            {"step": s["number"], "instruction": s["step"]}
            for s in data[0]["steps"]
        ]

        result = {"recipe_id": recipe_id, "steps": steps}
        log_tool_call("get_recipe_steps", {"recipe_id": recipe_id}, result)
        return result

    except requests.exceptions.Timeout:
        result = {"error": "Request timed out. Please try again."}
        log_tool_call("get_recipe_steps", {"recipe_id": recipe_id}, result)
        return result
    except requests.exceptions.RequestException as e:
        result = {"error": f"API request failed: {str(e)}"}
        return result








