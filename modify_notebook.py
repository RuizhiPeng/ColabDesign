#!/usr/bin/env python3
"""
Script to modify Jupyter notebook to hide code cells by default.
This adds "cellView": "form" to all code cells' metadata.
"""

import json
import sys

def modify_notebook(notebook_path):
    """Modify notebook to hide code cells by default"""

    # Read the notebook
    with open(notebook_path, 'r', encoding='utf-8') as f:
        notebook = json.load(f)

    # Count modifications
    modified_count = 0

    # Process each cell
    for cell in notebook.get('cells', []):
        if cell.get('cell_type') == 'code':
            # Initialize metadata if it doesn't exist
            if 'metadata' not in cell:
                cell['metadata'] = {}

            # Add cellView: form if not already present
            if 'cellView' not in cell['metadata']:
                cell['metadata']['cellView'] = 'form'
                modified_count += 1
                print(f"Added cellView to code cell")
            elif cell['metadata']['cellView'] != 'form':
                cell['metadata']['cellView'] = 'form'
                modified_count += 1
                print(f"Updated cellView to form")

    # Write back the modified notebook
    with open(notebook_path, 'w', encoding='utf-8') as f:
        json.dump(notebook, f, indent=1, ensure_ascii=False)

    print(f"Modified {modified_count} cells in {notebook_path}")
    return modified_count

if __name__ == '__main__':
    notebook_path = r"C:\Users\kfzr5\OneDrive\research\colabdesign\ColabDesign\rf\examples\diffusion.ipynb"
    modify_notebook(notebook_path)