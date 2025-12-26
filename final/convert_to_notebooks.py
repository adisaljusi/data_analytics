#!/usr/bin/env python3
"""
Convert create_notebook_XX.py scripts to actual Jupyter notebooks
"""

import json
import re

def parse_script_to_notebook(script_path):
    """Parse Python script and extract cells"""
    with open(script_path, 'r') as f:
        content = f.read()

    cells = []

    # Find all cell markers
    cell_pattern = r'# =+\n# CELL \d+: (MARKDOWN|CODE).*?\n# =+\n(.*?)(?=# =+\n# CELL|$)'
    matches = re.findall(cell_pattern, content, re.DOTALL)

    for cell_type, cell_content in matches:
        cell_content = cell_content.strip()

        if not cell_content:
            continue

        if cell_type == 'MARKDOWN':
            # Remove triple quotes
            cell_content = cell_content.strip('"""').strip("'''").strip()
            if cell_content:
                cells.append({
                    "cell_type": "markdown",
                    "metadata": {},
                    "source": [line + "\n" for line in cell_content.split('\n')]
                })
        else:  # CODE
            if cell_content:
                cells.append({
                    "cell_type": "code",
                    "execution_count": None,
                    "metadata": {},
                    "outputs": [],
                    "source": [line + "\n" for line in cell_content.split('\n')]
                })

    return cells

def create_notebook(cells, output_path):
    """Create Jupyter notebook from cells"""
    notebook = {
        "cells": cells,
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3"
            },
            "language_info": {
                "codemirror_mode": {"name": "ipython", "version": 3},
                "file_extension": ".py",
                "mimetype": "text/x-python",
                "name": "python",
                "nbconvert_exporter": "python",
                "pygments_lexer": "ipython3",
                "version": "3.11.0"
            }
        },
        "nbformat": 4,
        "nbformat_minor": 4
    }

    with open(output_path, 'w') as f:
        json.dump(notebook, f, indent=1)

    print(f"✓ Created: {output_path}")
    print(f"  Cells: {len(cells)}")

if __name__ == "__main__":
    print("Converting Python scripts to Jupyter notebooks...\n")

    # Convert Notebook 03
    print("Processing create_notebook_03.py...")
    try:
        cells_03 = parse_script_to_notebook('create_notebook_03.py')
        create_notebook(cells_03, '03_exploratory_analysis.ipynb')
    except Exception as e:
        print(f"✗ Error creating notebook 03: {e}")

    print()

    # Convert Notebook 06
    print("Processing create_notebook_06.py...")
    try:
        cells_06 = parse_script_to_notebook('create_notebook_06.py')
        create_notebook(cells_06, '06_clustering_analysis.ipynb')
    except Exception as e:
        print(f"✗ Error creating notebook 06: {e}")

    print("\n" + "="*70)
    print("DONE! Notebooks created successfully.")
    print("="*70)
    print("\nNext steps:")
    print("1. Open Jupyter: jupyter notebook")
    print("2. Open 03_exploratory_analysis.ipynb")
    print("3. Run all cells (Cell → Run All)")
    print("4. Repeat for 06_clustering_analysis.ipynb")
