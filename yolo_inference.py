from ultralytics import YOLO 

model = YOLO('models/yolo_best.pt')

model.predict('data/input/football_video.mp4', save=True)