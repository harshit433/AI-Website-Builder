import logging

def setup_logging(log_file='project.log'):
    """
    Set up logging configuration.
    
    Args:
        log_file (str): The log file where logs will be saved.
    """
    logging.basicConfig(
        level=logging.DEBUG,  # You can change this to any level you want to track.
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.StreamHandler(),  # Logs will be output to the console.
            logging.FileHandler(log_file)  # Logs will also be saved to a file.
        ]
    )