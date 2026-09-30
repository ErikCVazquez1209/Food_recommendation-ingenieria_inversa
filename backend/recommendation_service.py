from models import RecommendationRequest, Recipe
from recipes import RECIPES


def find_best_recipe(
    preferences: RecommendationRequest,
) -> Recipe | None:
    """Return the highest-scoring recipe that satisfies all limits."""

    matching_recipes = [
        recipe
        for recipe in RECIPES
        if recipe.food_type == preferences.food_type
        and recipe.minutes <= preferences.max_minutes
        and len(recipe.steps) <= preferences.max_steps
        and len(recipe.ingredients) <= preferences.max_ingredients
    ]

    if not matching_recipes:
        return None

    return max(
        matching_recipes,
        key=lambda recipe: recipe.score,
    )