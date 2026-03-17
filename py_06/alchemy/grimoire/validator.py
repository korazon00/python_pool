

def validate_ingredients(ingredients: str) -> str:
    ingredients_spl = ingredients.split()
    ingredients_list = ["fire", "water", "earth", "air"]
    
    for ingred in ingredients_spl:
        if ingred not in ingredients_list:
            return f"{ingredients} - INVALID"

    return f"{ingredients} - VALID"
