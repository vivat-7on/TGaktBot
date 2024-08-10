from collections import Counter
from ultralytics import YOLO

from lexicon.lexicon_ru import LEXICON_YOLO

_classes = {
    0.0: 'Печати',
    1.0: 'Подписи',
    2.0: 'Номера',
    3.0: 'Даты'
}

counter = Counter()

_model = YOLO('./services/best (1).pt', task='detect')


def yolo_predict(image):
    results = _model(image, save=False, conf=0.2, verbose=False)
    for numb, result in enumerate(results, start=1):
        boxes = result.boxes  # Получаем объект Boxes
        # Извлекаем координаты прямоугольников, классы и вероятности
        coordinates = boxes.xyxy  # Координаты прямоугольников
        classes = boxes.cls  # Классы объектов
        scores = boxes.conf  # Вероятности классов
        answers = []
        c = Counter(classes.tolist())

        if c[0] != 2 or c[1] != 2:
            yield f"Страница {numb}, печатей {c[0]}, подписей {c[1]}"
        # for cls, score in zip(c, scores):
        #     cls = cls.item()
        #     answers.append(f"{_classes[cls]} есть с вероятностью {score}!")
    yield f"{LEXICON_YOLO['end']}"