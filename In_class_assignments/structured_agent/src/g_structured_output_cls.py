from pydantic import BaseModel, Field
from typing import List, Optional
from google import genai
from dotenv import load_dotenv
import os
 
class Ingredient(BaseModel):
    name: str = Field(description="Name of the ingredient.")
    quantity: str = Field(description="Quantity including units.")
 
class Recipe(BaseModel):
    recipe_name: str = Field(description="The name of the recipe.")
    prep_time_minutes: Optional[int] = Field(
        description="Optional prep time in minutes."
    )
    ingredients: List[Ingredient]
    instructions: List[str]

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
client = genai.Client(api_key=api_key)

def extract_recipe(text: str) -> Recipe:
    response = client.models.generate_content(
        model="gemini-2.5-flash-lite",
        contents=f"Extract the recipe from this text.\n{text}",
        config={
            "response_mime_type": "application/json",
            "response_json_schema": Recipe.model_json_schema(),
        },
    )
    return Recipe.model_validate_json(response.text)


if __name__ == "__main__":
    sample = "Make scrambled eggs with 3 eggs, 1 tbsp butter, and salt..."
    recipe = extract_recipe(sample)
    print(recipe)

