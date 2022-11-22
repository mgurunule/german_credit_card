import os
from pathlib import Path
import logging

logging.basicConfig(
    level   = logging.INFO,
    format  = "[%(asctime)s: %(levelname)s]: %(message)s" 
)

'''
        Accept the project name from Author 
'''
while True:
    project_name = input("Enter project name ")
    if project_name != '':
        break

logging.info(f"Creating project by name : {project_name}")  # Information logger 

list_of_file = [
        ".github/workflows/.gitkeep",
        ".github/workflows/ci.yaml",
        f"src/{project_name}/__init__.py",
        f"test/__init__.py",
        f"test/unit/__init__.py",
        f"configs/config.yaml",
        f"docs/index.md",
        "init_setup.sh",
        "requirements.txt",
        "setup.py",
        "setup.cfg",
        "tox.ini",
        "main.py",
        "mkdocs.yaml"
    ]

for filepath in list_of_file:
    
    filepath = Path(filepath) 
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating a new directory at : {filedir} for file : {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath,"w") as f:
            pass
            logging.info(f"Creating new file : {filename} at path : {filedir}")
    else:
        logging.info(f" File is already present at {filepath}")


