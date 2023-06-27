import os

#folder_path = "D:/Pom_All"
folder_path = "D:/Dataset_UAV/images/val"

# Iterate over the files in the folder
for filename in os.listdir(folder_path):
    # Check if the file is a text file
    if filename.endswith('.txt'):
        # Construct the full file path
        file_path = os.path.join(folder_path, filename)

        # Open the annotation file for reading
        with open(file_path, 'r') as file:
            lines = file.readlines()

        # Open the annotation file for writing
        with open(file_path, 'w') as file:
            for line in lines:
                # Split the line by spaces
                parts = line.strip().split(' ')

                # Check if the first number is 2
                if len(parts) > 0 and parts[0] == '2':
                    # Change the first number to 1
                    parts[0] = '1'

                # Join the numbers back together with spaces
                modified_line = ' '.join(parts)

                # Write the modified line to the annotation file
                file.write(modified_line + '\n')

print("Annotation modification complete!")