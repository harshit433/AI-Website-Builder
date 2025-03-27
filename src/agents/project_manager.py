import json
from config import Config
from utils.file_utils import read_file, read_json, write_json
from services.llm_service import interact
from agents.debugger import DebuggerAgent
from Schemas import requirements_schema

class ProjectManagerAgent:
    """
    Handles project management tasks using an LLM, including requirement gathering,
    multi-turn conversations, and generating structured requirements.
    """

    def __init__(self):
        """
        Initializes the Project Manager agent with required configurations.
        """
        self.debugger = DebuggerAgent()
        self.conversation_history = [
            {"role": "system", "content": read_file(Config.PROJECT_MANAGER_PROMPT_PATH)}
        ]

    def ask_question(self, user_input: str) -> str:
        """
        Handles multi-turn conversation by maintaining history and generating responses.

        Args:
            user_input (str): The user's input message.

        Returns:
            str: The assistant's response.
        """
        self.conversation_history.append({"role": "Client", "content": user_input})

        return interact(self.conversation_history, Config.PROJECT_MANAGER_MODEL)

    def collect_requirements(self):
        """
        Interacts with the user to gather project requirements interactively.
        Saves conversation history and generates structured requirements.
        """
        print("Welcome to the Project Manager LLM! Let's gather your project requirements.")
        print("Type 'done' when you're finished providing information.")

        # while True:
        #     user_input = input("You: ")
        #     if user_input.lower() == "done":
        #         break
        #     response = self.ask_question(user_input)
        #     self.conversation_history.append({"role": "Project Manager", "content": response})
        #     print(f"Project Manager: {response}")

        # write_json(Config.CONVERSATION_HISTORY_PATH, self.conversation_history)
        self.generate_requirements()

    def generate_requirements(self):
        """
        Generates structured requirements JSON from the conversation history.
        """
        
        requirements_prompt = read_file(Config.REQUIREMENTS_PROMPT_PATH)

        combined_input = [
            {"role": "system", "content": requirements_prompt},
            {"role": "user", "content": f"The conversation history is {json.dumps(read_json(Config.CONVERSATION_HISTORY_PATH), indent=4)}"},
        ]

        response = interact(combined_input, Config.PROJECT_MANAGER_MODEL, response_model=requirements_schema.ProjectRequirements)
        write_json(Config.REQUIREMENTS_PATH, response)