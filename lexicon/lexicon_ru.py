LEXICON: dict[str: str] = {
    'start': 'Привет! Я полезный телеграм бот!\nПришли мне акты в pdf-файле\n'
             'и я проверю каждую страницу\nна корректность заполнения.\n'
             '\n'
             '*Обращаю твоё внимание на то,\nчто я могу помочь только с актами\n'
             'определённого формата.\n\nПрикрепляю образец проверяемых мною актов.',
    'help': 'Пришли мне pdf файл и посмотри что будет',
    'other': 'Лучше покажи мне твой акт...',
    'send_files': 'Приступил к проверке документов.\n'
                  'Это может занять некоторое время.\n'

}
LEXICON_YOLO = {
    'all_right': 'Все акты заполнены корректно ✅',
    'not_all_right': 'Остальные акты заполнены корректно ✅\n'
}

LEXICON_COMMANDS: dict[str, str] = {
    '/start': 'старт бота',
    '/help': 'список команд бота',
    '/support': 'написать в поддержку',
    '/contacts': 'контакты для связи'
}

LEXICON_YOLO_LOGGING = {
    'yolo_start_load': 'Загрузка модели YOLO...',
    'yolo_loaded': 'Модель YOLO успешно загружена.',
    'yolo_start_predicts': 'Получение предсказаний от модели YOLO...',
    'yolo_none_predict': 'Модель не вернула предсказаний.',
    'yolo_get_predict': 'Предсказания успешно получены.',
    'yolo_predict_empty': 'Пустой список предсказаний. Завершаем обработку.',
}

LEXICON_YOLO_ERROR = {
    'yolo_load_err': 'Ошибка при загрузке модели: ',
    'yolo_predict_err': 'Ошибка при получении предсказаний: ',
    'yolo_predict_empty_err': 'Ошибка: предсказания отсутствуют.'
}

LEXICON_HANDLERS_LOGGING = {
    'get_doc': 'Получен документ от пользователя',
    'loading_file': 'Загрузка файла',
    'convert_file': 'Конвертация файла {} в изображения...',
    'failed_load_yolo': 'Не удалось загрузить модель YOLO.',
    'getting_predictions': 'Получение предсказаний от модели YOLO...',
    'failed_predictions': 'Модель не вернула предсказаний.',
}

LEXICON_HANDLERS_ERROR = {
    'default_answer': 'Не фартонуло( Попробуйте загрузить файл ещё раз.',
    'doc_processing_err': 'Произошла ошибка при обработке вашего документа. Пожалуйста, попробуйте снова.'
}