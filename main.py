from ultralytics import YOLO

model = YOLO("yolo11n-cls.pt")
results = model.train(data="config.yaml", epochs=1, imgsz=64)

print("hello")
