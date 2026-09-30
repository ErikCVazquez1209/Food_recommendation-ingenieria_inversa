from models import FoodType, Recipe


RECIPES = [
    Recipe(
        name="Quick Oat Bowl",
        food_type=FoodType.HEALTHY,
        minutes=10,
        steps=[
            "Place the oats in a bowl",
            "Add milk and fruit",
            "Mix and serve",
        ],
        ingredients=[
            "oats",
            "milk",
            "banana",
            "strawberries",
            "cinnamon",
        ],
        score=4.3,
    ),
    Recipe(
        name="Vegetable Pasta",
        food_type=FoodType.HEALTHY,
        minutes=25,
        steps=[
            "Boil the pasta",
            "Cut the vegetables",
            "Cook the vegetables",
            "Combine all ingredients",
            "Serve the pasta",
        ],
        ingredients=[
            "pasta",
            "tomato",
            "spinach",
            "bell pepper",
            "olive oil",
            "garlic",
        ],
        score=4.8,
    ),
    Recipe(
        name="Grilled Vegetable Wrap",
        food_type=FoodType.VEG,
        minutes=20,
        steps=[
            "Cut the vegetables",
            "Grill the vegetables",
            "Warm the tortilla",
            "Assemble the wrap",
        ],
        ingredients=[
            "tortilla",
            "zucchini",
            "bell pepper",
            "onion",
            "cheese",
        ],
        score=4.6,
    ),
    Recipe(
        name="Herb Chicken",
        food_type=FoodType.NON_VEG,
        minutes=35,
        steps=[
            "Season the chicken",
            "Heat the pan",
            "Cook the chicken",
            "Prepare the vegetables",
            "Serve the dish",
        ],
        ingredients=[
            "chicken",
            "rosemary",
            "garlic",
            "olive oil",
            "carrot",
            "broccoli",
        ],
        score=4.7,
    ),
]