# Evaluation Results

All 10 test cases were run against the Recipe & Nutrition Agent using Mistral (`mistral-small-latest`) and the Spoonacular API.

---

## Summary

| ID | Category | Description | Status |
|---|---|---|---|
| 1 | Success | Common ingredients with a low calorie goal | ✅ Pass |
| 2 | Success | Vegetarian ingredients with high protein goal | ✅ Pass |
| 3 | Success | Valid ingredients with no explicit nutrition goal | ✅ Pass |
| 4 | Success | Valid ingredients with low carb goal | ✅ Pass |
| 5 | Failure | Nonsense ingredients that yield no recipes | ✅ Pass |
| 6 | Failure | Contradictory nutrition goal | ✅ Pass |
| 7 | Failure | Impossible calorie goal no recipe can meet | ✅ Pass |
| 8 | Edge | Empty input - no ingredients provided | ✅ Pass |
| 9 | Edge | Single uncommon ingredient | ✅ Pass |
| 10 | Edge | Input in Danish - tests language robustness | ✅ Pass |

---

## Test 1 - Success: Common ingredients with a low calorie goal

**Input:** I have chicken, lemon and garlic. I want a low calorie meal.

**Output:**

### Recipe: Lemon and Garlic Slow Roasted Chicken

**Ingredients used:** chicken, garlic, lemons
**Missing ingredients:** None

**Nutrition Facts (per serving):**
- Calories: 346
- Protein: 24g
- Fat: 26g
- Carbs: 3g

**Evaluation:** This recipe meets your low-calorie goal as it contains 346 calories per serving.

**How to cook it:**
1. Trim the leg tips and wing tips from the chicken and remove any excess fat from the neck of the bird. Season the chicken inside and out. Separate the garlic into cloves but do not bother to peel them.
2. Place about two-thirds of the garlic cloves inside the chicken and the rest in the bottom of the roasting tin, sitting the chicken on top of them.
3. Pare the zest from the lemons and cover it in plastic wrap for later use as a garnish. Rub the juice into the chicken inside and out, then rub the olive oil over the breast.
4. Roast the chicken quickly for 30 minutes, then transfer it to the simmering oven and cook for at least 4 hours. Stand for 10 to 15 minutes before carving or pulling the joints apart for serving.
5. Heat a wok or large frying pan for 5 minutes on the floor of the roasting oven while the chicken is standing.
6. Transfer the wok to the boiling plate and add the sunflower oil. Stir fry the vegetables in the oil for 3 to 4 minutes then serve the chicken on the vegetables or mixed in with them if the meat has fallen off the bone.

**Recommendation:** This simple and flavorful slow-roasted chicken is perfect for a low-calorie meal.

---

## Test 2 - Success: Vegetarian ingredients with high protein goal

**Input:** I have eggs, spinach and feta cheese. I want a high protein meal.

**Output:**

### Recipe: Mini Spinach and Feta Quiches

**Ingredients used:** eggs, spinach, feta cheese
**Missing ingredients:** half-and-half, garlic, onion, basil, cheddar cheese

**Nutrition Facts (per serving):**
- Calories: 38
- Protein: 3g
- Fat: 2g
- Carbs: 1g

**Evaluation:** This recipe does not meet the high protein goal as it only provides 3g of protein per serving.

**How to cook it:**
1. Preheat oven to 375 degrees.
2. Set a large skillet over medium heat and spray with a generous amount of olive oil. When the oil is hot, add the garlic and stir around for about 30 seconds.
3. Add the chopped onion, some salt and pepper, and turn up the heat to medium-high. Stirring frequently, cook until the onion is lightly browned.
4. Add the spinach, chopped basil, some more salt and pepper, and lower the heat to medium. Cook for about 10 to 15 minutes.
5. Combine the eggs, cheese, half-and-half, salt, pepper, and beat until well blended.
6. Distribute the spinach mixture evenly between the muffin cups, about 1 tablespoonful. Then spoon about 1 tablespoonful of egg batter into each muffin cup.
7. Bake about 15 minutes.
8. Remove the muffin pan from the oven and sprinkle the top of each muffin cup with reserved shredded cheddar cheese.
9. Bake for another 5 minutes or until the cheese has formed a golden brown crust on top.
10. Cool the quiches and serve warm or at room temperature.

**Recommendation:** Consider adding a protein-rich ingredient like chicken or turkey to boost the protein content.

---

## Test 3 - Success: Valid ingredients with no explicit nutrition goal

**Input:** I have salmon, broccoli and olive oil. What can I make?

**Output:**

### Recipe: Oven Baked Salmon with Broccoli (Sheet Pan)

**Ingredients used:** salmon steaks, broccoli
**Missing ingredients:** mayonnaise, soy sauce, lemon juice, breadcrumbs, parmesan, lemon zest, garlic, pepper flakes

**Nutrition Facts (per serving):**
- Calories: 439
- Protein: 29g
- Fat: 28g
- Carbs: 16g

**Evaluation:** This recipe does not meet the goal of being under 600 calories.

**How to cook it:**
1. In a bowl, combine minced garlic with extra virgin olive oil, hot pepper flakes, kosher sea salt, and freshly cracked pepper.
2. Add broccoli and toss.
3. Line a baking sheet with heavy-duty aluminum foil and place the vegetables around the perimeter of the sheet pan, leaving room for the fish in the middle.
4. In a small mixing bowl, combine mayonnaise with soy sauce, lemon juice, and salt.
5. Place the fish in the middle of the sheet pan and coat it with the sauce.
6. Combine breadcrumbs, Parmesan, and lemon zest and apply generously on top of the salmon steaks.
7. Bake for 15 minutes at 400°F until the salmon flakes easily and the vegetables have a nice al dente bite.
8. Serve with a glass of Chardonnay.

**Recommendation:** Use only olive oil, salt, and pepper to keep the dish simple and under 600 calories.

---

## Test 4 - Success: Valid ingredients with low carb goal

**Input:** I have ground beef and zucchini. I want a low carb meal.

**Output:**

### Recipe: Hidden Veggie Chipotle Taco Meat

**Ingredients used:** ground beef, zucchini
**Missing ingredients:** bell pepper, onion, tomato sauce, chipotle chile powder, chiles, black beans, corn, cilantro

**Nutrition Facts (per serving):**
- Calories: 312
- Protein: 19g
- Fat: 15g
- Carbs: 24g

**Evaluation:** This recipe does not meet the low-carb goal due to its 24g of carbs per serving.

**How to cook it:**
1. Brown ground beef in a large skillet over medium-high heat.
2. Mince vegetables and add the minced pepper and zucchini when the beef is almost cooked through. Cook for 3-4 more minutes.
3. Add diced onion, tomato sauce, chipotle powder, diced green chiles, salt, pepper, beans, corn, and 1/2 cup water. Cook another 4-5 minutes until saucy.
4. Stir in cilantro and keep warm until ready to serve.

**Recommendation:** Try a stuffed zucchini recipe with ground beef and minimal added carbs for a better low-carb option.

---

## Test 5 - Failure: Nonsense ingredients that yield no recipes

**Input:** I have xkqzj and blorfp. What can I make?

**Output:** The ingredients you provided are not recognizable as real food items. TERMINATE

---

## Test 6 - Failure: Contradictory nutrition goal

**Input:** I have pasta and butter. I want a meal that is both high calorie and low calorie.

**Output:** The goal you provided is contradictory (both high calorie and low calorie). TERMINATE

---

## Test 7 - Failure: Impossible calorie goal no recipe can meet

**Input:** I have chicken and rice. I want a meal with less than 10 calories.

**Output:** No real meal can meet a goal of under 10 calories. TERMINATE

---

## Test 8 - Edge: Empty input - no ingredients provided

**Input:** (empty)

**Output:** Please provide at least one ingredient to get started. TERMINATE

---

## Test 9 - Edge: Single uncommon ingredient

**Input:** I only have durian. Find me something to make.

**Output:**

### Recipe: Durian Panna Cotta

**Ingredients used:** durian puree
**Missing ingredients:** gelatine powder, milk, whipping cream

**Nutrition Facts (per serving):**
- Calories: 156
- Protein: 3g
- Fat: 5g
- Carbs: 23g

**Evaluation:** This recipe meets the goal of being under 600 calories.

**How to cook it:**
1. Add gelatine to water to soak for 5 minutes.
2. Combine fresh milk, whipping cream and sugar in a pot over medium heat and stir until sugar is dissolved. Bring to a light boil. Add soaked gelatine and stir until dissolved. Add durian puree and mix well. Keep stirring for 5-8 minutes at low heat. Strain and pour into cups or moulds.
3. Refrigerate for at least 2 hours and serve.

**Recommendation:** Use canned durian puree for convenience, but ensure other ingredients are fresh.

---

## Test 10 - Edge: Input in Danish - tests language robustness

**Input:** Jeg har kylling, citron og hvidløg. Jeg vil gerne have en ret med få kalorier.

**Output:**

### Recipe: Lemon and Garlic Slow Roasted Chicken

**Ingredients used:** chicken, garlic, lemons
**Missing ingredients:** None

**Nutrition Facts (per serving):**
- Calories: 346
- Protein: 24g
- Fat: 26g
- Carbs: 3g

**Evaluation:** This recipe meets your goal of a low-calorie meal (under 600 calories).

**How to cook it:**
1. Trim the leg tips and wing tips from the chicken and remove any excess fat from the neck of the bird. Season the chicken inside and out. Separate the garlic into cloves but do not bother to peel them.
2. Place about two-thirds of the garlic cloves inside the chicken and the rest in the bottom of the roasting tin, sitting the chicken on top of them.
3. Pare the zest from the lemons and cover it in plastic wrap for later use as a garnish. Rub the juice into the chicken inside and out, then rub the olive oil over the breast.
4. Roast the chicken quickly for 30 minutes, then transfer it to the simmering oven and cook for at least 4 hours. Stand for 10 to 15 minutes before carving or pulling the joints apart for serving.
5. Serve the chicken as desired.

**Recommendation:** This simple and flavorful slow-roasted chicken is perfect for a light yet satisfying meal.