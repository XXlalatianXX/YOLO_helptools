import os

folder_path = "F:/Darknet_Using/darknet/build/darknet/x64/data/obj"

files = os.listdir(folder_path)

for file in files:
    if file.endswith(".jpg"):
        annotation_file = file.replace(".jpg", ".txt")
        if annotation_file not in files:
            image_path = os.path.join(folder_path, file)
            os.remove(image_path)
            print(f"Deleted image file: {image_path}")
    elif file.endswith(".txt"):
        image_file = file.replace(".txt", ".jpg")
        if image_file not in files:
            annotation_path = os.path.join(folder_path, file)
            os.remove(annotation_path)
            print(f"Deleted annotation file: {annotation_path}")
