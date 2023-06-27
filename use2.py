import os

# This use with select just first of .txt have 0 and 1

# Set the folder path where the text files are located
#folder_path = 'C:/Users/gmupo/Downloads/labels/train'
#folder_path = 'C:/Users/gmupo/Downloads/labels/test'
#folder_path = 'C:/Users/gmupo/Downloads/labels/val'
#folder_path = 'C:/Yolo_v4/Dataset/Dummy'
#folder_path = 'C:/Yolo_v4/Dataset/From_UAV/labels/val'
folder_path = "D:/Dataset_UAV/images/val"

# Loop through every file in the folder
for filename in os.listdir(folder_path):
    # Check if the file is a text file
    if filename.endswith('.txt'):
        # Open the input file
        with open(os.path.join(folder_path, filename), 'r') as f:
            # Read the contents of the file
            contents = f.read()

        # Split the contents of the file into lines
        lines = contents.split('\n')

        # Create a list to store the filtered lines
        filtered_lines = []

        # Loop through each line of the file
        for line in lines:
            # Skip blank lines
            if not line:
                continue

            # Split the line into separate values using whitespace as the delimiter
            values = line.split()

            # Check the length of the values list. If it is less than 1, skip the line.
            if len(values) < 1:
                continue

            # Check the first value in the list. If it is not equal to 0 or 1, skip the line.
            # select just 0,2 => person & Car
            if values[0] not in ['0', '2']:    
                continue

            # Otherwise, keep the line.
            # Add the line to the filtered lines list.
            filtered_lines.append(line)

        # Join the filtered lines into a single string
        filtered_contents = '\n'.join(filtered_lines)

        # Overwrite the original file with the filtered data
        with open(os.path.join(folder_path, filename), 'w') as f:
            f.write(filtered_contents)

        # Close the file
        f.close()
