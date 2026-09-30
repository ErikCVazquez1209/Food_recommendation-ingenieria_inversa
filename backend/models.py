from enum import Enum

from pydantic import BaseModel, Field


class FoodType(str, Enum):
    """Food categories accepted by the recommendation API."""

    HEALTHY = "Healthy"
    VEG = "Veg"
    NON_VEG = "Non-Veg"
    VEG_DESSERT = "Veg_Dessert"
    NON_VEG_DESSERT = "Non-Veg_Dessert"


class RecommendationRequest(BaseModel):
    """User preferences used to find a recipe."""

    food_type: FoodType
    max_minutes: int = Field(gt=0)
    max_steps: int = Field(gt=0)
    max_ingredients: int = Field(gt=0)


class Recipe(BaseModel):
    """Recipe returned by the recommendation API."""

    name: str
    food_type: FoodType
    minutes: int
    steps: list[str]
    ingredients: list[str]
    score: float