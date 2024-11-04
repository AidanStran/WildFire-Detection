from ultralytics import YOLO
import os
import cv2

model_path = 'D:/dev/WildFire-Detection/10_epoch_weights/last.pt'
image_path = 'D:/dev/WildFire-Detection/TrainANDTest/images/test/image_1845.jpg'


img = cv2.imread(image_path)
H, W, _ = img.shape

model = YOLO(model_path)

results = model(img)

for result in results:
    for j, mask in enumerate(result.masks.data):

        mask = mask.numpy() * 255

        mask = cv2.resize(mask, (W, H))

        cv2.imwrite('D:/dev/WildFire-Detection/TrainANDTest/testingMasks/output.png', mask)