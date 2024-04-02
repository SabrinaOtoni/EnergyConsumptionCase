'''
Python script for automated creation of the project's folder structure
--------------------------------------
By Sabrina Otoni da Silva - 2024/04
'''
# Importing the necessary libraries
import os

# Dictionary defining the desired folder structure
folders_structure = {
    'automations' : [], # Folder for Python scripts
    'data': {  # Main folder 'data' containing subfolders
        'd01_raw': [],  # Subfolder for raw data
        'd02_intermediate': [],  # Subfolder for intermediate data
        'd03_processed': [],  # Subfolder for processed data
        'd04_models': [] # Subfolder for processed data
    },
    'documentation': [],  # Folder for documentation
    'model': [],  # Folder for models
    'notebooks': [],  # Folder for Jupyter notebooks
    'preprocessing': [],  # Folder for preprocessing scripts
    'presentation': [] # Folder for presentations
}

# Base path where the folders will be created (current directory)
base_path = os.getcwd()

def create_folders(base, structure):
    """
    Creates a folder structure based on the provided dictionary

    Parameters:
    base: str
        Base path where the folders will be created
    structure: dict
        Dictionary representing the desired folder structure
    """
    # Iterates over each item (folder and its contents) in the structure dictionary
    for folder, content in structure.items():

        # Checks if the content is a dictionary (indicating subfolders)
        if isinstance(content, dict):
            # Builds the folder path and creates it if it doesn't exist
            folder_path = os.path.join(base, folder)
            os.makedirs(folder_path, exist_ok=True)
            # Recursive call to create subfolders
            create_folders(folder_path, content)

        else:
            # If it's not a dictionary, creates the folder
            folder_path = os.path.join(base, folder)
            os.makedirs(folder_path, exist_ok=True)
            
            # Iterates over each subfolder in the 'content' list
            for subfolder in content:
                # Builds the subfolder path and creates it if it doesn't exist
                subfolder_path = os.path.join(folder_path, subfolder)
                os.makedirs(subfolder_path, exist_ok=True)
                # Creates a .gitkeep file in each subfolder to ensure they are included in Git
                with open(os.path.join(subfolder_path, '.gitkeep'), 'w') as f:
                    pass

# Calling the function to create the folder structure at the base path
create_folders(base_path, folders_structure)
