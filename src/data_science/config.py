import os
from pathlib import Path
from dotenv import load_dotenv

# Always resolve from the known project root
env_path = Path(__file__).resolve().parents[2] / ".env.local" 
load_dotenv(env_path)

