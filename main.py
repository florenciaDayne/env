from dotenv import load_dotenv
import os
from typing import List, Dict, Optional

def load_env_variables():
    load_dotenv()
    api_key = os.getenv('API_KEY')
    print(api_key)
    

def main():
    vars=load_env_variables()
   

if __name__ == "__main__":
    main()
