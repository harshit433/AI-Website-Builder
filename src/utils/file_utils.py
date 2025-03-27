import os
import json

def read_file(file_path: str) -> str:
    """
    Reads the content of a text file.

    Args:
        file_path (str): The path to the file.

    Returns:
        str: The content of the file.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")
    except Exception as e:
        raise RuntimeError(f"Error reading file {file_path}: {e}")

def write_file(file_path: str, content: str):
    """
    Writes content to a text file.

    Args:
        file_path (str): The path to the file.
        content (str): The content to write.
    """
    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(content)
    except Exception as e:
        raise RuntimeError(f"Error writing to file {file_path}: {e}")

def read_json(file_path: str) -> dict:
    """
    Reads and parses a JSON file.

    Args:
        file_path (str): The path to the JSON file.

    Returns:
        dict: The parsed JSON content.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        raise FileNotFoundError(f"JSON file not found: {file_path}")
    except json.JSONDecodeError:
        raise ValueError(f"Invalid JSON format in file: {file_path}")
    except Exception as e:
        raise RuntimeError(f"Error reading JSON file {file_path}: {e}")

def write_json(file_path: str, data: dict):
    """
    Writes a dictionary as a JSON file.

    Args:
        file_path (str): The path to the JSON file.
        data (dict): The dictionary to write.
    """
    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, default=str)
    except Exception as e:
        raise RuntimeError(f"Error writing JSON file {file_path}: {e}")
