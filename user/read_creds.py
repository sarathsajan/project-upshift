import json

with open('env.json', 'r', encoding='utf-8') as file:
    env_data = json.load(file)
UPSTOX_ACCESS_TOKEN = env_data.get('UPSTOX_ACCESS_TOKEN')