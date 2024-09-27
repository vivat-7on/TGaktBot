from collections import Counter

from ultralytics import YOLO

from lexicon.lexicon_ru import LEXICON_YOLO

_model = YOLO('./services/best.pt', task='detect')


def yolo_predicts(list_bytes):
    predicts = _model(list_bytes, save=False, conf=0.7, verbose=False)
    return predicts


def _answer_for_yolo(page_number, predict):
    classes = predict.boxes.cls
    c = Counter(classes.tolist())
    if c[0] != 2 or c[1] != 2 or c[2] < 1:
        return f"Страница {page_number}, печатей {c[0]}, подписей {c[1]}, дат {c[2]}"


def predict_processing(predicts):
    _result_key = 'all_right'
    for page_number, predict in enumerate(predicts, start=1):
        answer = _answer_for_yolo(page_number, predict)
        if answer:
            _result_key = 'not_all_right'
            yield answer
    yield f"{LEXICON_YOLO[_result_key]}"
