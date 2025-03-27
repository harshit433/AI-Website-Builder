from datetime import datetime
import os
from config import Config
from agents.debugger import DebuggerAgent
from services.llm_service import interact
from utils.file_utils import read_file, read_json, write_json

def create_initial_metadata():
    """
    Creates a static metadata file for the initial project structure.
    Args:
        outputs_folder (str): Path to the folder containing the project.
        project_name (str): Name of the project folder containing the React app.
    """
    project_name = read_json(Config.REQUIREMENTS_PATH)['project_name']
    outputs_folder = "outputs"
    metadata = {
        "structure": {
            "description": "Hierarchical structure of the project directory.",
            "tree": {
                f"outputs/{project_name}": {
                    "type": "directory",
                    "children": {
                        "public": {
                            "type": "directory",
                            "children": {
                                "index.html": {"type": "file"},
                                "favicon.ico": {"type": "file"},
                                "manifest.json": {"type": "file"},
                                "robots.txt": {"type": "file"}
                            }
                        },
                        "src": {
                            "type": "directory",
                            "children": {
                                "index.js": {"type": "file"},
                                "index.css": {"type": "file"},
                                "App.js": {"type": "file"},
                                "App.css": {"type": "file"},
                                "App.test.js": {"type": "file"},
                                "logo.svg": {"type": "file"},
                                "reportWebVitals.js": {"type": "file"},
                                "setupTests.js": {"type": "file"}
                            }
                        },
                        "package.json": {"type": "file"},
                        "package-lock.json": {"type": "file"},
                    }
                },
                "outputs/backend.py": {"type": "file"}
            }
        },
        f"outputs/{project_name}": {
            "name": project_name,
            "type": "directory",
            "path": f"{outputs_folder}/{project_name}",
            "description": "React frontend application generated using Create React App.",
            "last_updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        },
        f"outputs/{project_name}/public": {
            "name": "public",
            "type": "directory",
            "path": f"{outputs_folder}/{project_name}/public",
            "description": "Public assets for the React frontend application.",
            "last_updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        },
        f"outputs/{project_name}/public/index.html": {
            "name": "index.html",
            "type": "file",
            "path": f"{outputs_folder}/{project_name}/public/index.html",
            "description": "HTML template for the React application.",
            "last_updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        },
        f"outputs/{project_name}/public/favicon.ico": {
            "name": "favicon.ico",
            "type": "file",
            "path": f"{outputs_folder}/{project_name}/public/favicon.ico",
            "description": "Favicon for the React application.",
            "last_updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        },
        f"outputs/{project_name}/public/manifest.json": {
            "name": "manifest.json",
            "type": "file",
            "path": f"{outputs_folder}/{project_name}/public/manifest.json",
            "description": "Manifest file describing PWA metadata.",
            "last_updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        },
        f"outputs/{project_name}/public/robots.txt": {
            "name": "robots.txt",
            "type": "file",
            "path": f"{outputs_folder}/{project_name}/public/robots.txt",
            "description": "File specifying crawl instructions for web crawlers.",
            "last_updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        },
        f"outputs/{project_name}/src": {
            "name": "src",
            "type": "directory",
            "path": f"{outputs_folder}/{project_name}/src",
            "description": "Source code directory for the React frontend application.",
            "last_updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        },
        f"outputs/{project_name}/src/index.js": {
            "name": "index.js",
            "type": "file",
            "path": f"{outputs_folder}/{project_name}/src/index.js",
            "description": "Entry point for the React application.",
            "last_updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        },
        f"outputs/{project_name}/src/index.css": {
            "name": "index.css",
            "type": "file",
            "path": f"{outputs_folder}/{project_name}/src/index.css",
            "description": "Global CSS file for the React application.",
            "last_updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        },
        f"outputs/{project_name}/src/App.js": {
            "name": "App.js",
            "type": "file",
            "path": f"{outputs_folder}/{project_name}/src/App.js",
            "description": "Main React component for the application.",
            "last_updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        },
        "outputs/backend.py": {
            "name": "backend.py",
            "type": "file",
            "path": f"{outputs_folder}/backend.py",
            "description": "FastAPI backend with a root endpoint and health check.",
            "last_updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        },
        f"outputs/{project_name}/src/reportWebVitals.js": {
            "name": "reportWebVitals.js",
            "type": "file",
            "path": f"{outputs_folder}/{project_name}/src/reportWebVitals.js",
            "description": "File for measuring and reporting web performance metrics.",
            "last_updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        },
        f"outputs/{project_name}/src/setupTests.js": {
            "name": "setupTests.js",
            "type": "file",
            "path": f"{outputs_folder}/{project_name}/src/setupTests.js",
            "description": "Configuration for React Testing Library.",
            "last_updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        },
        f"outputs/{project_name}/src/App.css": {
            "name": "App.css",
            "type": "file",
            "path": f"{outputs_folder}/{project_name}/src/App.css",
            "description": "CSS file for styling the App component.",
            "last_updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        },
        f"outputs/{project_name}/src/logo.svg": {
            "name": "logo.svg",
            "type": "file",
            "path": f"{outputs_folder}/{project_name}/src/logo.svg",
            "description": "Default logo provided by Create React App.",
            "last_updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        },
        f"outputs/{project_name}/src/App.test.js": {
            "name": "App.test.js",
            "type": "file",
            "path": f"{outputs_folder}/{project_name}/src/App.test.js",
            "description": "Sample test file for the App component.",
            "last_updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        },
    }

    # Save the metadata as a JSON file
    write_json(Config.PROJECT_METADATA_PATH, metadata)

def update_metadata(changes):
    """
    Update the metadata JSON file based on changes in the project structure.

    Args:
        metadata_file (str): Path to the existing metadata JSON file.
        changes (list): List of changes, where each change is a dictionary
                        with details of the file/directory change.
                        Example:
                        [{"path": "outputs/new_file.js", "type": "file", "operation": "create"},
                         {"path": "outputs/old_file.js", "type": "file", "operation": "update"},
                         {"path": "outputs/old_dir", "type": "directory", "operation": "delete"}]
    """
    if not os.path.exists(Config.PROJECT_METADATA_PATH):
        raise FileNotFoundError("Metadata file not found.")

    # Load existing metadata
    metadata  = read_json(Config.PROJECT_METADATA_PATH)

    def generate_structure(directory_path, exclude_files=None, exclude_dirs=None):
        """
        Generate a hierarchical structure of the project directory.

        Args:
            directory_path (str): The root directory path.
            exclude_files (list): A list of file names to exclude.
            exclude_dirs (list): A list of directory names to exclude.

        Returns:
            dict: A JSON-like structure representing the directory.
        """
        if exclude_files is None:
            exclude_files = []
        if exclude_dirs is None:
            exclude_dirs = []

        def build_tree(path):
            tree = {}
            for item in sorted(os.listdir(path)):  # Sort items for consistent output
                item_path = os.path.join(path, item)
                if os.path.isdir(item_path):  # If it's a directory
                    if item not in exclude_dirs:
                        tree[item] = {
                            "type": "directory",
                            "children": build_tree(item_path),
                        }
                elif os.path.isfile(item_path):  # If it's a file
                    if item not in exclude_files:
                        tree[item] = {"type": "file"}
            return tree

        return {
            "description": "Hierarchical structure of the project directory.",
            "tree": {
                os.path.basename(directory_path): {
                    "type": "directory",
                    "children": build_tree(directory_path),
                }
            },
        }

    def update_metadata(metadata, change):
        """
        Update both the tree structure and top-level metadata with the given change.
        """
        path_parts = change["path"].split(os.sep)
        item_name = path_parts[-1]
        item_path = change["path"]

        if change["operation"] == "create":

            # Add to top-level metadata
            metadata[item_path] = {
                "name": item_name,
                "type": "file",
                "path": item_path,
                "description": generate(item_path)['description'],
                "last_updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }

        elif change["operation"] == "update":

            # Update top-level metadata
            if item_path in metadata:
                metadata[item_path]["last_updated"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                metadata[item_path]["description"] = generate(item_path)['description']

    # Apply changes
    for change in changes:
        update_metadata(metadata, change)
    
    metadata["structure"] = generate_structure("outputs",exclude_dirs=["__pycache__","node_modules",".git"], exclude_files=[".gitignore","README.md",])
    # Save the updated metadata
    write_json(Config.PROJECT_METADATA_PATH, metadata)

def generate(path):
    """Generate the metadata for the given path."""
    # This function should return a dictionary representing the metadata for the given path
    debugger = DebuggerAgent()

    metadata_generation_prompt = read_file(Config.PROJECT_METADATA_UPDATE_PROMPT_PATH)
    
    code = read_file(path)

    messages=[
            {"role": "system", "content": metadata_generation_prompt},
            {"role": "user", "content": f"The code is: {code}"}
        ]
    response = interact(messages, Config.PROJECT_MANAGER_MODEL)
    metadata = debugger.extract_top_level_json(response)
    return metadata