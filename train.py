from ultralytics import YOLO

#training on last from now one
#model = YOLO('yolo11n-seg.pt')  # Model is previously used, faster + less accurate

model = YOLO('yolo11m-seg.pt')  # Model is new, Slow + more accurate

#model = YOLO('D:/dev/WildFire-Detection/yolo11n')

#mask_ratio is 1/6, shrinks our mask by the same factor the img is being resized to
#batch increased from 16 -> 32
#optimizer SGD = Stochastic Gradient Descent (mini batch)
results = model.train(data="config.yaml", epochs=5, imgsz=(640, 360), mask_ratio=6, batch=32, optimizers='SGD') 