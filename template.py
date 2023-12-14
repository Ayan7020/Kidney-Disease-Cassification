import os
from pathlib import Path
import logging

# For printing string in terminal
logging.basicConfig(level=logging.INFO, format="[%(asctime)s]: %(message)s")

project_name = "CNN-Classifier"

list_of_files = [
    ".github/workflows/.gitkeep",  # If your folder is empty it won't be uploaded to github
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/enitity/__init__.py",
    f"src/{project_name}/constants/__init__.py" "config/config.yaml" "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html",
]


for filepath in list_of_files:
    filepath = Path(filepath)  # for managing slash
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating Directory: {filedir} for the file:{filename}")
    # for taking the  os.path.getsize(filepath) == 0 if we re run the code it will ignore the file for recreating if they have code intit
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"creating empty file : {filepath}")
    else:
        logging.info(f"{filename} is already exist!")
