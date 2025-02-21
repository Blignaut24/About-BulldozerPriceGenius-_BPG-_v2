import os
import nbformat
import re

def find_file_references(notebook_path):
    with open(notebook_path) as f:
        nb = nbformat.read(f, as_version=4)
    
    references = []
    for cell in nb.cells:
        if cell.cell_type == 'code':
            # Look for file operations
            file_ops = re.findall(r'open\([\'"](.+?)[\'"]\)', cell.source)
            pd_reads = re.findall(r'pd\.read_\w+\([\'"](.+?)[\'"]\)', cell.source)
            references.extend(file_ops + pd_reads)
    
    return references

def scan_project():
    notebooks = []
    for root, dirs, files in os.walk('.'):
        for file in files:
            if file.endswith('.ipynb'):
                notebooks.append(os.path.join(root, file))
    
    all_references = []
    for nb in notebooks:
        refs = find_file_references(nb)
        all_references.extend(refs)
    
    # Extract and print only the file names
    file_names = [os.path.basename(ref) for ref in all_references]
    print(file_names)
    return file_names

# Run the scan_project function
scan_project()