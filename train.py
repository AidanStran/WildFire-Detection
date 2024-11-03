from ultralytics import YOLO

model = YOLO('yolo11n-seg.pt')  # load a pretrained model (recommended for training)

results = model.train(data="config.yaml", epochs=10, imgsz=(640, 360))