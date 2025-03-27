import os
import json
import subprocess
import time
from groq import Groq
from config import Config
from services.file_service import create_files_from_json
from utils.file_utils import read_file, read_json, write_file
from agents.debugger import DebuggerAgent
from services.llm_service import interact


class DeveloperAgent:
    """
    Developer Agent responsible for creating project structures, processing tasks, 
    generating code, and debugging using LLMs.
    """

    def __init__(self):
        """
        Initializes the Developer Agent.

        Args:
            project_name (str): Name of the project.
            task_list_file (str): Path to the task list JSON file.
        """
        self.project_name = read_json(Config.REQUIREMENTS_PATH)["project_name"]
        self.project_path = os.path.join("outputs", self.project_name)
        self.backend_file_path = os.path.join("outputs", "backend.py")
        self.task_list = read_json(Config.TASK_LIST_PATH)
        self.llm_client = Groq(api_key=Config.GROQ_API_KEY)
        self.debugger = DebuggerAgent()
        self.related_files_prompt = read_file(Config.RELATED_FILES_PROMPT_PATH)
        self.developer_prompt = read_file(Config.DEVELOPER_PROMPT_PATH)
        self.metadata = read_json(Config.PROJECT_METADATA_PATH)
        self.requirements = read_json(Config.REQUIREMENTS_PATH)

    def setup_project_structure(self):
        """
        Initializes a Node.js project structure and sets up the backend.
        """
        try:
            subprocess.run(
                ["npx", "create-react-app", str.lower(self.project_path)], check=True, text=True, shell=True
            )
            self.setup_backend()
        except Exception as e:
            print(f"Error setting up project structure: {e}")

    def setup_backend(self):
        """
        Sets up a basic FastAPI backend by creating a backend.py file in the project directory.
        """
        backend_code = (
            "from fastapi import FastAPI\n"
            "app = FastAPI()\n"
            "\n"
            "@app.get('/')\n"
            "def read_root():\n"
            '    return {"message": "Welcome to the backend API"}\n'
            "\n"
            "@app.get('/health')\n"
            "def health_check():\n"
            '    return {"status": "ok"}'
        )
        write_file(self.backend_file_path, backend_code)

    def process_task(self, task: dict):
        """
        Processes individual tasks based on their name.

        Args:
            task (dict): Task details from the task list.
        """
        if task["name"].lower() == "setup project structure":
            self.setup_project_structure()
        else:
            self.handle_task_with_llm(task)

    def handle_task_with_llm(self, task: dict):
        """
        Handles tasks using the LLM to generate code and process related files.

        Args:
            task (dict): Task details.
        """

        # Step 1: Fetch related files using the LLM

        messages=[
                {"role": "system", "content": self.related_files_prompt},
                {
                    "role": "user",
                    "content": f"The task is {task} \n"
                               f"The metadata of the project structure is: {self.metadata}",
                },
            ]

        response_files = self.debugger.extract_top_level_json(interact(messages, Config.PROJECT_MANAGER_MODEL))

        important_files = response_files.get("important_files", [])

        # Step 2: Fetch content of identified files
        files_content = {}
        for file_path in important_files:
            files_content[file_path] = read_file(file_path)

        # Step 3: Generate code using the LLM
        messages=[
                {"role": "system", "content": self.developer_prompt},
                {
                    "role": "user",
                    "content": f"The task is {task} \n"
                               f"Related files are: {files_content} \n"
                               f"The metadata of the project structure is: {self.metadata} \n"
                               f"The requirements of the project are: {self.requirements}. \n"
                               "Now you can generate the code in the specified format.",
                },
            ]

        code = self.debugger.extract_top_level_json(interact(messages, Config.PROJECT_MANAGER_MODEL))
        create_files_from_json(code)

    def process_tasks(self):
        """
        Processes all tasks sequentially from the task list.
        """
        for task in self.task_list["tasks"]:
            print("Waiting for 2 minutes before processing the task...")
            time.sleep(120)
            self.process_task(task)