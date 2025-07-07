from dotenv import load_dotenv

from app.config import Config
from app.assistant import SmartResearchAssistant

# Load environment variables
load_dotenv()

# Initialize config and assistant
config = Config()
assistant = SmartResearchAssistant(config)

document_paths = [
    "./data/docs/article1.pdf",
    "./data/docs/article2.pdf",
]

try:
    # Setup assistant with documents
    assistant.setup(document_paths)

    # Ask questions interactively
    while True:
        question = input("\nAsk a question (or type 'exit'): ")
        if question.lower() in ["exit", "quit"]:
            break

        try:
            answer = assistant.ask_question(question)
            print(f"\nAnswer:\n{answer}\n")
        except Exception as qe:
            print(f"Error: {qe}")

except Exception as e:
    print(f"Setup failed: {e}")
