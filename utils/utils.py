# sudo apt-get install poppler-utils
# import os

from settings import DOWNLOAD_PDF_DIR, DPI, DOWNLOAD_JPG_DIR
from pdf2image import convert_from_bytes, convert_from_path

# from pathlib import Path

_download_file_dir = DOWNLOAD_PDF_DIR
_dpi = DPI

# current_directory = os.getcwd()
# file_path = os.path.join(current_directory, _download_file_dir)
# file_name = os.listdir(file_path)
# file_path_name = os.path.join(file_path, *file_name)


def user_convert_from_path(pdf_path, name):
    return convert_from_path(
        pdf_path, dpi=_dpi, output_folder=DOWNLOAD_JPG_DIR, fmt='jpg',
        output_file=name
    )

