import os

class Config:
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    PROJECT_MANAGER_MODEL = "llama-3.3-70b-versatile"
    PROJECT_MANAGER_PROMPT_PATH = "utils/prompts/project_manager_prompt.txt"
    CONVERSATION_HISTORY_PATH = "generated_files/conversation_history.json"
    REQUIREMENTS_PROMPT_PATH = "utils/prompts/requirements_prompt.txt"
    REQUIREMENTS_PATH = "generated_files/requirements.json"
    TASK_LIST_PROMPT_PATH = "utils/prompts/task_list_prompt.txt"
    TASK_LIST_PATH = "generated_files/task_list.json"
    PROJECT_METADATA_PATH = "generated_files/project_metadata.json"
    PROJECT_METADATA_PROMPT_PATH = "utils/prompts/project_metadata_prompt.txt"
    PROJECT_METADATA_UPDATE_PROMPT_PATH = "utils/prompts/metadata_update_prompt.txt"
    RELATED_FILES_PROMPT_PATH = "utils/prompts/metadata_filter_prompt.txt"
    DEVELOPER_PROMPT_PATH = "utils/prompts/developer_prompt.txt"