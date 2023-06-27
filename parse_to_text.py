import os
import xml.etree.ElementTree as ET

folder_path = 'D:/tocrop'

# Iterate through the files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.xml'):
        # Remove the ".xml" extension from the annotation filename
        new_filename = filename.replace('.xml', '')
        
        # Get the full file paths
        old_path = os.path.join(folder_path, filename)
        new_path = os.path.join(folder_path, new_filename)
        
        # Rename the file
        os.rename(old_path, new_path)