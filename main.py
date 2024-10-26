from ultralytics import YOLO

model = YOLO("yolo11n-cls.pt")
results = model.train(data="mnist160", epochs=100, imgsz=64)

