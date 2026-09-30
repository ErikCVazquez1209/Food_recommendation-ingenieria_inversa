import pytest
from fastapi.testclient import TestClient

from main import app


client = TestClient(app)


def create_valid_request(**changes):
    """Create a valid request and optionally replace selected values."""

    request_data = {
        "food_type": "Healthy",
        "max_minutes": 30,
        "max_steps": 6,
        "max_ingredients": 8,
    }

    request_data.update(changes)

    return request_data


def test_api_is_available():
    """The test route must confirm that the API is available."""

    response = client.get("/api/test")

    assert response.status_code == 200
    assert response.json() == {
        "test": "GET success",
    }


def test_returns_best_matching_recipe():
    """The API must return the highest-scoring matching recipe."""

    response = client.post(
        "/api/recommendations",
        json=create_valid_request(),
    )

    assert response.status_code == 200

    recipe = response.json()

    assert recipe["name"] == "Vegetable Pasta"
    assert recipe["food_type"] == "Healthy"
    assert recipe["minutes"] <= 30
    assert len(recipe["steps"]) <= 6
    assert len(recipe["ingredients"]) <= 8


@pytest.mark.parametrize(
    ("field_name", "requested_limit"),
    [
        ("max_minutes", 20),
        ("max_steps", 4),
        ("max_ingredients", 5),
    ],
)
def test_respects_each_requested_limit(
    field_name,
    requested_limit,
):
    """Each maximum limit must independently exclude recipes above it."""

    request_data = create_valid_request()
    request_data[field_name] = requested_limit

    response = client.post(
        "/api/recommendations",
        json=request_data,
    )

    assert response.status_code == 200

    recipe = response.json()

    assert recipe["name"] == "Quick Oat Bowl"
    assert recipe["minutes"] <= request_data["max_minutes"]
    assert len(recipe["steps"]) <= request_data["max_steps"]
    assert (
        len(recipe["ingredients"])
        <= request_data["max_ingredients"]
    )


def test_rejects_unknown_food_type():
    """An unsupported food category must be rejected."""

    response = client.post(
        "/api/recommendations",
        json=create_valid_request(
            food_type="Unknown",
        ),
    )

    assert response.status_code == 422


def test_rejects_non_positive_limit():
    """Maximum limits must be greater than zero."""

    response = client.post(
        "/api/recommendations",
        json=create_valid_request(
            max_minutes=0,
        ),
    )

    assert response.status_code == 422


def test_returns_not_found_when_no_recipe_matches():
    """The API must return 404 when no recipe satisfies the filters."""

    response = client.post(
        "/api/recommendations",
        json=create_valid_request(
            food_type="Veg",
            max_minutes=10,
            max_steps=4,
            max_ingredients=5,
        ),
    )

    assert response.status_code == 404
    assert response.json() == {
        "detail": "No matching recipe found",
    }