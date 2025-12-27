import os
from pathlib import Path
from dotenv import load_dotenv

# Path to the .env file in the same directory as this file
# env_path = Path(__file__).parent / ".env"
env_path = os.path.join(os.path.dirname(__file__), ".env")
load_dotenv(dotenv_path=env_path)

COLLEGIATE_DICTIONARY_KEY = os.environ.get("COLLEGIATE_DICTIONARY_KEY")
LEARNER_DICTIONARY_KEY = os.environ.get("LEARNER_DICTIONARY_KEY")
