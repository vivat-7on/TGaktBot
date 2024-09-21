from collections import Counter
from ultralytics import YOLO

from lexicon.lexicon_ru import LEXICON_YOLO

_classes = {
    0.0: 'Печати',
    1.0: 'Подписи',
    2.0: 'Номера',
    3.0: 'Даты'
}

_model = YOLO('./services/best.pt', task='detect')


def yolo_predict(image):
    result_key = 'all_right'
    results = _model(image, save=False, conf=0.7, verbose=False)
    for numb, result in enumerate(results, start=1):
        boxes = result.boxes
        coordinates = boxes.xyxy  # Координаты прямоугольников
        classes = boxes.cls  # Классы объектов
        scores = boxes.conf  # Вероятности классов
        c = Counter(classes.tolist())
        print(f"Страница{numb}, {classes}, {scores}")
        if c[0] != 2 or c[1] != 2:
            result_key = 'not_all_right'
            yield f"Страница {numb}, печатей {c[0]}, подписей {c[1]}"

    yield f"{LEXICON_YOLO[result_key]}"
