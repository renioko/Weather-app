import os
from dotenv import load_dotenv

import openai

def load_api_key() -> str:
    """loads api key"""
    load_dotenv()
    try:
        openai.api_key = os.getenv('OPEN_API_KEY')
    except ValueError:
        print('problem with OPEN_API_KEY')
    return openai.api_key

if __name__ == '__main__':
    load_api_key()

