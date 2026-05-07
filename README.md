# Recipe & Nutrition Agent

An AI-powered agent that recommends recipes based on available ingredients and evaluates whether they meet a given nutrition goal. Built with AutoGen and the Spoonacular API.

---

## Agent Architecture

The agent consists of two AutoGen components:

- **RecipeAssistantAgent** - the "brain". An LLM-powered agent (Mistral) that decides which tools to call and in what order, and formats the final response.
- **UserProxyAgent** - the "hands". Executes tool calls autonomously and returns results to the assistant.

### Tools

| Tool | Description |
|---|---|
| `search_recipes(ingredients)` | Searches Spoonacular for recipes matching a comma-separated list of ingredients |
| `get_nutrition(recipe_id)` | Fetches precise nutrition facts for a recipe - the deterministic step |
| `get_recipe_steps(recipe_id)` | Fetches step-by-step cooking instructions for a recipe |

---

## Dependencies

- Python 3.12
- pyautogen 0.2.35
- mistralai 0.4.2
- requests
- python-dotenv

---

## Setup

**1. Clone the repository**

```bash
git clone https://github.com/Tobbekjaer/recipe-nutrition-agent.git
cd recipe-nutrition-agent
```

**2. Create and activate a virtual environment**

```bash
python -m venv .venv
source .venv/bin/activate
```

On Windows:

```bash
.venv\Scripts\activate
```

**3. Install dependencies**

```bash
pip install -r requirements.txt
```

**4. Configure API keys**

Copy `.env.example` to `.env`:

```bash
cp .env.example .env
```

Then fill in your keys in `.env`:

```
MISTRAL_API_KEY=your_mistral_key_here
SPOONACULAR_API_KEY=your_spoonacular_key_here
```

- Get your Mistral API key at: https://console.mistral.ai
- Get your Spoonacular API key at: https://spoonacular.com/food-api

---

## How to Run

**Run the agent with a single query:**

```bash
python main.py
```

**Run all 10 test cases:**

```bash
python evaluation/test_cases.py
```

**Run a single test case** by editing the bottom of `evaluation/test_cases.py`:

```python
if __name__ == "__main__":
    test = TEST_CASES[0]  # Change index to run a different test
    run_agent(test["input"])
```

**Evaluation results** from all 10 test cases are documented in `evaluation/results.md`.

---

## Project Structure

```
recipe-nutrition-agent/
├── main.py              # Entry point
├── agents.py            # AssistantAgent + UserProxyAgent setup
├── tools.py             # search_recipes, get_nutrition, get_recipe_steps
├── logger.py            # Logs all tool calls to tool_calls.log
├── evaluation/
│   ├── test_cases.py    # 10 test cases covering success, failures and edge cases
│   └── results.md       # Documented output from all test cases
├── .env.example         # API key template
├── requirements.txt
└── README.md
```

---

## Logging

Every tool call is automatically logged to `tool_calls.log` with timestamp, inputs and output:

```json
{
  "timestamp": "2026-05-06T12:00:00",
  "tool": "get_nutrition",
  "inputs": {"recipe_id": 649495},
  "output": {"calories": "346", "protein": "24g", "fat": "26g", "carbs": "3g"}
}
```

The log file is committed to the repository as documentation of the evaluation runs.
