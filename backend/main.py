import os
import requests
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get API key for IO Intelligence
IO_INTEL_API_KEY = os.getenv("IO_INTEL_API_KEY")

# IO Intelligence API Endpoint
IO_INTEL_ENDPOINT = "https://api.intelligence.io.solutions/api/v1/workflows/run"

# Initialize FastAPI
app = FastAPI()

# CORS 設定
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request model for API
class RecipeRequest(BaseModel):
    ingredients: list

# Function to generate a recipe based on ingredients
def generate_recipe(ingredients):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {IO_INTEL_API_KEY}"
    }

    data = {
        "text": f"Generate a recipe using the given ingredients along with additional suitable ingredients. \n\n"
                "Ensure the output follows this structured format:\n\n"
                "【Recipe Name】\n"
                "Provide a creative and relevant name for the dish.\n\n"
                "■ Ingredients\n"
                "List all necessary ingredients including additional ones to complete the recipe, formatted as bullet points starting with ・\n\n"
                "■ Instructions\n"
                "Provide step-by-step cooking instructions, numbering each step (1., 2., 3., etc.)\n\n"
                "■ Tips\n"
                "Include cooking tips, alternatives, or additional suggestions to enhance the dish.\n\n"
                f"Primary Ingredients: {', '.join(ingredients)}",
        "agent_names": ["custom_agent"],
        "model": "deepseek-ai/DeepSeek-R1",
        "args": {
            "type": "custom",
            "name": "Recipe Generation",
            "objective": "Generate a well-structured recipe with a proper title, additional ingredients, and a clear format.",
            "instructions": "Ensure that all recipes follow the exact format provided, including a dish name, expanded ingredient list, numbered instructions, and a tips section.",
            "temperature": 0.7,
            "top_p": 0.9
        }
    }

    response = requests.post(IO_INTEL_ENDPOINT, headers=headers, json=data)

    try:
        result = response.json()
        return result.get("result", "Recipe generation failed.")
    except Exception as e:
        print("🔴 Recipe generation error:", e)
        return "Recipe generation failed."

# API endpoint to receive ingredient list and return a recipe
@app.post("/generate-recipe/")
def generate_recipe_endpoint(request: RecipeRequest):
    return {"recipe": generate_recipe(request.ingredients)}
