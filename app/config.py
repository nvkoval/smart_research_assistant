import os
from dotenv import load_dotenv


class Config:
    """Configuration management for the Smart Research Assistant."""

    def __init__(self):
        self._setup_environment()

    def _setup_environment(self):
        """Set up environment variables for LangChain and OpenAI."""

        load_dotenv()
        # Verify required keys
        missing_keys = []
        for key in ["OPENAI_API_KEY", "LANGSMITH_API_KEY"]:
            if not os.getenv(key):
                missing_keys.append(key)

        if missing_keys:
            raise EnvironmentError(f"Missing required environment variables: {', '.join(missing_keys)}")

        print("Environment successfully configured from .env")
