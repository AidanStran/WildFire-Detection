import os
import cv2
import numpy as np

input_dir = './TrainANDTest/Masks'
output_dir = './TrainANDTest/newMasks'

for j in os.listdir(input_dir):
    image_path = os.path.join(input_dir, j)
    # Load the binary mask (already normalized to 0 and 1)
    mask = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Convert normalized mask (0 to 1) to binary (0 to 255)
    mask = (mask > 0).astype(np.uint8) * 255  # Create binary mask

    H, W = mask.shape
    contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    polygons = []
    for cnt in contours:
        if cv2.contourArea(cnt) > 200:  # Filter by contour area
            polygon = []
            for point in cnt:
                x, y = point[0]
                polygon.append(x / W)  # Normalize x
                polygon.append(y / H)  # Normalize y
            polygons.append(polygon)

    # Write polygons to text file
    with open('{}.txt'.format(os.path.join(output_dir, j)[:-4]), 'w') as f:
        for polygon in polygons:
            for p_, p in enumerate(polygon):
                if p_ == len(polygon) - 1:
                    f.write('{}\n'.format(p))
                elif p_ == 0:
                    f.write('0 {} '.format(p))
                else:
                    f.write('{} '.format(p))