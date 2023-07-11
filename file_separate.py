import os
import random

imgspath = 'C:/Yolo_v4/Dummy/darknet/build/darknet/x64/data/obj'
path = 'data/obj/'


images = []
for i in os.listdir(imgspath):
    if i.endswith('.jpg'):
        temp = path+i
        images.append(temp)
# train and test split... adjust it if necessary
trainlen = round(len(images)*.80)
testlen = round(len(images)*.20)
#print('total, train, test dataset size -',trainlen+testlen,trainlen,testlen)
random.shuffle(images)
test = images[:testlen]
train = images[testlen:]

with open('train.txt', 'w') as f:
    for item in train:
        f.write("%s\n" % item)
with open('test.txt', 'w') as f:
    for item in test:
        f.write("%s\n" % item)