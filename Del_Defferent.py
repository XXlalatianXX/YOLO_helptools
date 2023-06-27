import os

#dataset_path = "C:/Yolo_v4/Dataset/Person"
#dataset_path = "C:/Yolo_v4/Dataset/From_UAV/images/Person_SmallCar_BigCar"
dataset_path = 'F:/Darknet_Using/darknet/build/darknet/x64/data/obj'

for filename in os.listdir(dataset_path):
    if filename.endswith(".txt"):
        with open(os.path.join(dataset_path, filename), "r") as f:
            if f.read().strip() == "":
                f.close()
                os.remove(os.path.join(dataset_path, filename))
                os.remove(os.path.join(dataset_path, filename[:-4] + ".jpg"))
