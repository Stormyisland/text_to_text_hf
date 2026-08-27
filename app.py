
import os
from openai import OpenAI

client = OpenAI(
  base_url="https://router.huggingface.co/v1",
  api_key=os.environ[HF_TOKEN"],
)
