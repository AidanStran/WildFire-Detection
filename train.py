import os

from ultralytics import YOLOv10

config_path = './config.yaml'

#load model
model = YOLOv10(".yaml")

#use model
model.train(data = config_path, epochs = 20, batch = 32)