
import os
from openai import OpenAI

client = OpenAI(
  base_url="https://router.huggingface.co/v1",
  api_key=os.environ[HF_TOKEN"],
)

completion = client.chat.completions.create(
  model="meta-models/Muse-Glimmer-30B:together",
  messages=[
    {
      "role": "user",
      "content":[
        {
          "type":"text",
          "text":"discribe this image in one sentence.
          {
