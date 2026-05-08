import sys
import os

# Allow imports from the root directory
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from main import run_agent

# --- 10 test cases covering success, failures, and edge cases ---
TEST_CASES = [
    # SUCCESS CASES - normal use with valid ingredients and clear goals
    {
        "id": 1,
        "category": "success",
        "description": "Common ingredients with a low calorie goal",
        "input": "I have chicken, lemon and garlic. I want a low calorie meal.",
    },
    {
        "id": 2,
        "category": "success",
        "description": "Vegetarian ingredients with high protein goal",
        "input": "I have eggs, spinach and feta cheese. I want a high protein meal.",
    },
    {
        "id": 3,
        "category": "success",
        "description": "Valid ingredients with no explicit nutrition goal",
        "input": "I have salmon, broccoli and olive oil. What can I make?",
    },
    {
        "id": 4,
        "category": "success",
        "description": "Valid ingredients with low carb goal",
        "input": "I have ground beef and zucchini. I want a low carb meal.",
    },

    # FAILURE CASES - inputs the agent should handle gracefully
    {
        "id": 5,
        "category": "failure",
        "description": "Nonsense ingredients that yield no recipes",
        "input": "I have xkqzj and blorfp. What can I make?",
    },
    {
        "id": 6,
        "category": "failure",
        "description": "Contradictory nutrition goal",
        "input": "I have pasta and butter. I want a meal that is both high calorie and low calorie.",
    },
    {
        "id": 7,
        "category": "failure",
        "description": "Impossible calorie goal no recipe can meet",
        "input": "I have chicken and rice. I want a meal with less than 10 calories.",
    },

    # EDGE CASES - unusual or boundary inputs
    {
        "id": 8,
        "category": "edge",
        "description": "Empty input - no ingredients provided",
        "input": "",
    },
    {
        "id": 9,
        "category": "edge",
        "description": "Single uncommon ingredient",
        "input": "I only have durian. Find me something to make.",
    },
    {
        "id": 10,
        "category": "edge",
        "description": "Input in Danish - tests language robustness",
        "input": "Jeg har kylling, citron og hvidløg. Jeg vil gerne have en ret med få kalorier.",
    },
]


def run_all_tests():
    print(f"\n{'='*60}")
    print(f"Running {len(TEST_CASES)} test cases")
    print(f"{'='*60}\n")

    for test in TEST_CASES:
        print(f"\n[Test {test['id']}] [{test['category'].upper()}] {test['description']}")
        print(f"{'-'*60}")
        run_agent(test["input"])
        print(f"\n{'='*60}")


if __name__ == "__main__":
    # Run a single test by index (0 = test 1, 1 = test 2, etc.)
    test = TEST_CASES[7]
    print(f"\n[Test {test['id']}] [{test['category'].upper()}] {test['description']}")
    run_agent(test["input"])
    # run_all_tests()