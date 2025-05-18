import requests
import json
import api_key

prompts:list = [
    {
            "role": "system",
            "content": "Your name is r_ducky and you are a \"rubber duck\" debugging assistant. Your job is to help encourage users to walk through their code/thought processes thoroughly, step by step. Do not debug for the user; instead, continue to ask questions about how they believe their code/algorithm works. If you believe they make a mistake in their logic, then ask them if they are sure; you may also point out (minimal but necessary) information to steer them in the right direction. Make sure to question why they make specific decisions, especially when they are wrong."
        }
]

def debug(question: str) -> str:
    prompts.append({
        "role": "user",
        "content": question
    })

    response = requests.post(
    url="https://openrouter.ai/api/v1/chat/completions",
    headers={
        "Authorization": "Bearer " + api_key.OPENROUTER_API_KEY,
        "Content-Type": "application/json",
    },
    data=json.dumps({
        "model": "meta-llama/llama-3.3-8b-instruct:free",
        "messages": prompts,
    })
    )

    m: dict = response.json()["choices"][0]["message"]

    prompts.append({
        "role": m["role"],
        "content": m["content"]
    })

    return m["content"]

while True:
    print(debug(input()))