import json5
from config import Config
from utils.file_utils import read_file
from services.llm_service import interact

class DebuggerAgent:
    """
    An agent for debugging and validating code by analyzing JSON objects and 
    identifying potential errors.
    """

    def __init__(self):
        """
        Initializes the Debugger Agent with prompts and LLM configurations.
        """

    def check_code(self, code: str) -> dict:
        """
        Checks the provided code for errors using the LLM client.

        Args:
            code (str): The code to analyze for errors.

        Returns:
            dict: The extracted and parsed JSON object with debugging insights.
        """
        messages=[
                {"role": "system", "content": "Check the provided code for errors and return the corrected code in the same format as input"},
                {"role": "user", "content": f"The code JSON object is: {code}"},
            ]
        return self.extract_top_level_json(interact(messages=messages, model=Config.PROJECT_MANAGER_MODEL))

    @staticmethod
    def extract_top_level_json(response_text: str) -> dict:
        """
        Extracts the top-level JSON object from a text string by identifying 
        the outermost braces.

        Args:
            response_text (str): Text containing additional text and a JSON object.

        Returns:
            dict: Parsed JSON object if found.

        Raises:
            ValueError: If no valid JSON object is found in the input.
        """
        start_idx = -1
        brace_count = 0

        # Identify the top-level JSON object by tracking braces
        for idx, char in enumerate(response_text):
            if char == '{':
                if brace_count == 0:
                    start_idx = idx  # Start of the JSON
                brace_count += 1
            elif char == '}':
                brace_count -= 1
                if brace_count == 0 and start_idx != -1:
                    json_str = response_text[start_idx:idx + 1]
                    return json5.loads(json_str)  # Parse JSON

        raise ValueError("No valid JSON object found in the input.")
