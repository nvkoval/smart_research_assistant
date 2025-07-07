import shutil
from fastapi import FastAPI, UploadFile, File, Form
from typing import List
from pathlib import Path
from dotenv import load_dotenv

from app.config import Config
from app.assistant import SmartResearchAssistant

load_dotenv()
app = FastAPI()

config = Config()

assistant = SmartResearchAssistant(config)

UPLOAD_DIR = "./data/temp_docs"
Path(UPLOAD_DIR).mkdir(parents=True, exist_ok=True)


@app.post("/setup")
async def setup(documents: List[UploadFile] = File(...)):
    saved_path = []
    for doc in documents:
        dest = Path(UPLOAD_DIR) / doc.filename
        with open(dest, "wb") as f:
            shutil.copyfileobj(doc.file, f)
        saved_path.append(dest)

    try:
        assistant.setup(saved_path)
        return {"status": "ready",
                "documents": [Path(p).name for p in saved_path]}
    except Exception as e:
        return {"status": "error", "message": str(e)}


@app.post("/ask")
async def ask(question: str = Form(...)):
    try:
        answer = assistant.ask_question(question)
        return {"question": question, "answer": answer}
    except Exception as e:
        return {"error": str(e)}


@app.post("/clear")
async def clear():
    assistant.clear_history()
    return {"status": "chat history cleared"}


@app.get("/status")
async def status():
    """Check if assistant is initialized and ready"""
    is_ready = assistant.qa_chain is not None
    return {"ready": is_ready}
