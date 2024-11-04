from ultralytics import YOLO

#training on last from now one
#model = YOLO('yolo11n-seg.pt')  # load a pretrained model (recommended for training)

model = YOLO('D:/dev/WildFire-Detection/10_epoch_weights/last.pt')

results = model.train(data="config.yaml", epochs=30, imgsz=(640, 360))