# gemini_test.py
from google import genai
from dotenv import load_dotenv

load_dotenv()
# The client gets the API key from the environment variable `GEMINI_API_KEY`.
client = genai.Client()
use_model = "gemini-2.5-flash" #"gemini-2.5-pro"
response = client.models.generate_content(
    model=use_model, contents="How recent is your training data?"
)
print(response.text)

    
