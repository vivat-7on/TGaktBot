import logging
from collections import Counter
from ultralytics import YOLO
from lexicon.lexicon_ru import LEXICON_YOLO
from typing import List, Generator, Optional

SEAL_CLASS = 0.0
SIGNATURE_CLASS = 1.0
DATE_CLASS = 2.0

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


def load_model(weights_path: str = './services/best.pt',
               task: str = 'detect') -> Optional[YOLO]:
    """Загружает и возвращает модель YOLO"""
    try:
        logging.info("Загрузка модели YOLO...")
        model = YOLO(weights_path, task='detect')
        logging.info("Модель YOLO успешно загружена.")
        return model

    except Exception as e:
        logging.error(f"Ошибка при загрузке модели: {e}")
        return None


def yolo_predicts(model: YOLO, list_bytes: List[bytes],
                  conf_threshold: float = 0.7) -> Optional[List]:
    """Получает предсказания от модели YOLO. Логирует ошибки."""
    try:
        logging.info("Получение предсказаний от модели YOLO...")
        predicts = model(list_bytes, save=False, conf=conf_threshold,
                         verbose=False)
        if not predicts:
            logging.warning("Модель не вернула предсказаний.")
            return None
        logging.info("Предсказания успешно получены.")
        return predicts
    except Exception as e:
        logging.error(f"Ошибка при получении предсказаний: {e}")
        return None


def _answer_for_yolo(page_number: int, predict) -> Optional[str]:
    """Генерирует строку с информацией о количестве классов на странице."""
    try:
        classes = predict.boxes.cls
        counts = Counter(classes.tolist())

        seals = counts.get(SEAL_CLASS, 0)
        signatures = counts.get(SIGNATURE_CLASS, 0)
        dates = counts.get(DATE_CLASS, 0)

        if seals != 2 or signatures != 2 or dates < 1:
            return f"Страница {page_number}, печатей {seals}, подписей {signatures}, дат {dates}"
    except Exception as e:
        logging.error(f"Ошибка при обработке страницы {page_number}: {e}")
        return None

    return None


def predict_processing(predicts: Optional[List]) -> Generator[str, None, None]:
    """Обрабатывает предсказания и генерирует результаты. Логирует ошибки."""
    if predicts is None:
        logging.warning("Пустой список предсказаний. Завершаем обработку.")
        yield "Ошибка: предсказания отсутствуют."
        return

    result_key = 'all_right'

    for page_number, predict in enumerate(predicts, start=1):
        answer = _answer_for_yolo(page_number, predict)
        if answer:
            result_key = 'not_all_right'
            yield answer  # Отправляем ответ по мере его обработки

    yield LEXICON_YOLO.get(result_key, "Ошибка: ключ результата не найден")
