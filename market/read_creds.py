import json
import os

if os.name == 'nt':
    env_path = '..\\env.json'   # Windows-style backslashes
else:
    env_path = '../env.json'    # POSIX-style forward slashes (Linux, macOS)

with open(env_path, 'r', encoding='utf-8') as file:
    env_data = json.load(file)

UPSTOX_ACCESS_TOKEN = env_data.get('UPSTOX_ACCESS_TOKEN')
UPSTOX_ACCESS_TOKEN_SANDBOX = env_data.get('UPSTOX_ACCESS_TOKEN_SANDBOX')