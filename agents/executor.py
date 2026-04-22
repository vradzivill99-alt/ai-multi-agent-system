import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def execute_task(plan, data):
    prompt = f"""
You are an AI executor.

Plan:
{plan}

Data:
{data}

Execute the task and provide a final answer.
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content
