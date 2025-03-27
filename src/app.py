from agents.developer import DeveloperAgent
from agents.project_manager import ProjectManagerAgent
from agents.task_list_generator import TaskListGenerator
from services.metadata_service import create_initial_metadata
import logging
from logger import setup_logging

# Set up the logging system
setup_logging()

logger = logging.getLogger(__name__)

def gather_requirements():
    """
    Gather project requirements using the Project Manager Agent.
    """
    logger.info("Gathering project requirements")
    pm_agent = ProjectManagerAgent()
    pm_agent.collect_requirements()
    logger.info("Project requirements gathered successfully and saved to file.")

def generate_task_list():
    """
    Generate the task list using the Task List Generator Agent.
    """

    # Create initial metadata for the project
    logger.info("Creating initial metadata for the project.")
    create_initial_metadata()
    logger.info("Initial metadata created successfully and saved to file.")
    logger.info("Generating task list based on project requirements and metadata.")
    task_generator = TaskListGenerator()
    task_generator.generate_and_save_task_list()
    logger.info("Task list generated successfully and saved to file.")


def process_tasks():
    """
    Process tasks sequentially using the Developer Agent.
    """
    logger.info("Processing tasks sequentially.")
    agent = DeveloperAgent()
    agent.process_tasks()
    logger.info("All tasks processed successfully.")


def main():
    """
    Main function to orchestrate the workflow across all agents.
    """
    try:
        gather_requirements()
        generate_task_list()
        process_tasks()
    except Exception as e:
        logger.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()