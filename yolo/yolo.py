from ultralytics import YOLO

_classes = {
    0.0: 'Печати',
    1.0: 'Подписи',
    2.0: 'Номера',
    3.0: 'Даты'
}

_model = YOLO('best.pt')


def yolo_predict(image):
    results = _model(image, save=True, conf=0.2)

    predictions = []
    for result in results:
        boxes = result.boxes  # Получаем объект Boxes

        # Извлекаем координаты прямоугольников, классы и вероятности
        coordinates = boxes.xyxy  # Координаты прямоугольников
        classes = boxes.cls  # Классы объектов
        scores = boxes.conf  # Вероятности классов

        for cls, score in zip(classes, scores):
            cls = cls.item()
            predictions.append(f"{_classes[cls]} есть с вероятностью {score}!")

    return predictions

print(yolo_predict('/Users/7on/Dev/TGaktBot/downloads_jpg/Колокола_page_2.jpg'))