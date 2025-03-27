import os
from services.metadata_service import update_metadata
from utils.file_utils import write_file

def create_files_from_json(json_data):
    """
    Create or update files from the given JSON object and update metadata.

    Args:
        json_data (dict): JSON object where each key represents a file's details.
        metadata_file (str): Path to the metadata JSON file.
    """
    changes = []
    
    for key, value in json_data.items():
        file_path = value['path']
        code_content = value['code']
        operation = "create" if not os.path.exists(file_path) else "update"
        
        write_file(file_path, code_content)
        
        changes.append({
            "path": file_path,
            "type": "file",
            "operation": operation
        })
    
    # Update metadata after all changes
    update_metadata(changes)