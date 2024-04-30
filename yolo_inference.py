from ultralytics import YOLO 

model = YOLO('models/yolov8x.pt')

model.predict('data/')