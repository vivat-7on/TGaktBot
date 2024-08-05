from ultralytics import YOLO

model = YOLO('runs/detect/yolov8s_custom/weights/last.pt')

results = model('my_dataset_yolo/images/test/act_17.jpg', save=True, conf=0.2)

for result in results:
    boxes = result.boxes  # Получаем объект Boxes

    # Извлекаем координаты прямоугольников, классы и вероятности
    coordinates = boxes.xyxy  # Координаты прямоугольников
    classes = boxes.cls  # Классы объектов
    scores = boxes.conf  # Вероятности классов

    for box, cls, score in zip(coordinates, classes, scores):
        print(f"Box: {box}, Class: {cls}, Score: {score}")