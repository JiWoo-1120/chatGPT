from openai import OpenAI
from dotenv import load_dotenv
import os
# load .env
load_dotenv()
client = OpenAI(
 api_key=os.environ.get("API_KEY")
)