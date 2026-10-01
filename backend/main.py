from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from models import RecommendationRequest, Recipe
from recommendation_service import find_best_recipe


app = FastAPI(
    title="Food Recommendation API",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=False,
    allow_methods=[
        "GET",
        "POST",
    ],
    allow_headers=[
        "Content-Type",
    ],
)


@app.get("/api/test")
def test_api():
    """Confirm that the API is available."""

    return {
        "test": "GET success",
    }


@app.post(
    "/api/recommendations",
    response_model=Recipe,
)
def recommend_recipe(
    preferences: RecommendationRequest,
) -> Recipe:
    """Return the best recipe that satisfies the supplied preferences."""

    recipe = find_best_recipe(preferences)

    if recipe is None:
        raise HTTPException(
            status_code=404,
            detail="No matching recipe found",
        )

    return recipe