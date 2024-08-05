import requests
from pdf2image import convert_from_bytes, convert_from_path

from yolo.yolo import yolo_predict

# Вставьте ваш токен бота
TOKEN = '7489469462:AAGCJ3zmSAH9fy0ctSCHEskpBy9MAT4wpWE'

# Вставьте file_id, полученный из апдейта
file_id = 'BQACAgIAAxkBAAObZq9v1BTPFrTjceSTpanHdgABKhv4AAJdTgACvZd4SWZQ_mfIwqJBNQQ'

# Шаг 1: Получаем file_path, вызывая getFile метод
response = requests.get(f'https://api.telegram.org/bot{TOKEN}/getFile', params={'file_id': file_id})
file_info = response.json()

if not file_info['ok']:
    raise Exception('Error getting file info')

file_path = file_info['result']['file_path']

# Шаг 2: Формируем URL для скачивания файла
file_url = f'https://api.telegram.org/file/bot{TOKEN}/{file_path}'

# Шаг 3: Скачиваем файл и получаем байты
file_response = requests.get(file_url)
file_bytes = file_response.content
images = convert_from_bytes(file_bytes)
for image in images:
    result = yolo_predict(convert_from_bytes(file_bytes))
    print(result)