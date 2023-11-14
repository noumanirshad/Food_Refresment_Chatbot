import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

list_of_files = [
    ".github/workflows/.gitkeep",
    "Chatbot/__init__.py",
    "Chatbot/chatbot.py",
    "Scripts/dialogflow.py",
    "test/__init__.py",
    "Exception/exceptions.py",
    "Exception/logging.py",
    "app.py",   
    "main.py",   
    "Dockerfile",   
    "Requirements.txt",   
    "setup.py",
    "research/trials.ipynb"   
]

for file_path in list_of_files:
    file_path = Path(file_path)
    filedir, filename = os.path.split(file_path)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Created directory: {filedir} for the file {filename}")

    if (not os.path.exists(file_path)) or (os.path.getsize(file_path)== 0):
        with open(file_path, "w") as f:
            pass
            logging.info(f"Created empty file: {file_path}")

    else:
        logging.info(f"{filename} is already exists")