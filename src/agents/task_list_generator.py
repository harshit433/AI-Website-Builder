import json
from config import Config
from utils.file_utils import read_file, read_json, write_json
from services.llm_service import interact
from agents.debugger import DebuggerAgent
from Schemas import task_schema

class TaskListGenerator:
    """
    An agent responsible for generating and managing task lists based on project requirements.
    """

    def __init__(self):
        """
        Initializes the Task List Generator agent with necessary configurations.
        """
        self.debugger = DebuggerAgent()
        self.system_prompt = read_file(Config.TASK_LIST_PROMPT_PATH)
        self.metadata = read_json(Config.PROJECT_METADATA_PATH)
        self.requirements = read_json(Config.REQUIREMENTS_PATH)

    def generate_and_save_task_list(self):
        """
        Generates a task list based on the gathered requirements and project metadata.

        Args:
            requirements (str): The project's requirements as input.

        Returns:
            str: The generated task list as a JSON string.
        """
        messages = [
            {"role": "system", "content": self.system_prompt},
            {"role": "user", "content": f"The project requirements are as follows: {self.requirements} \nThe current status of the project is: {self.metadata}"},
        ]
         #self.debugger.extract_top_level_json
        task_list_json = (interact(messages, Config.PROJECT_MANAGER_MODEL, task_schema.TaskList))  # Ensure it's valid JSON
        write_json(Config.TASK_LIST_PATH, task_list_json)