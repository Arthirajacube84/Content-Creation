import os
from dotenv import load_dotenv

# Load environment variables from .env file if present
load_dotenv()

# API Keys
# SECURITY WARNING: For production, set these as environment variables
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY") # This will be None if not found
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY", "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")

# Debug: Verify key is set (safe version)
if OPENAI_API_KEY:
    print(f"[DEBUG] OPENAI_API_KEY is found (Prefix: {OPENAI_API_KEY[:5]}...)")
else:
    print("[DEBUG] OPENAI_API_KEY IS MISSING!")

# Configuration
MODEL_NAME = os.getenv("MODEL_NAME", "gpt-4o-mini")
TEMPERATURE = float(os.getenv("TEMPERATURE", "0.8"))
MAX_OUTPUT_TOKENS = int(os.getenv("MAX_OUTPUT_TOKENS", "2000"))
