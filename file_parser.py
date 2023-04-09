import sys
from pathlib import Path

JPEG_IMAGES = []
JPG_IMAGES = []
PNG_IMAGES = []
SVG_IMAGES = []

MP3_AUDIO = []
OGG_AUDIO = []
WAV_AUDIO = []
AMR_AUDIO = []

AVI_VIDEO = []
MP4_VIDEO = []
MOV_VIDEO = []
MKV_VIDEO = []

ZIP_ARCHIVES = []
GZ_ARCHIVES = []
TAR_ARCHIVES = []

MY_OTHER = []

DOCX_DOCUMENT = []
DOC_DOCUMENT = []
TXT_DOCUMENT = []
PDF_DOCUMENT = []
XLSX_DOCUMENT = []
PPTX_DOCUMENT = []


REGISTER_EXTENSION = {
    'JPEG': JPEG_IMAGES,
    'JPG': JPG_IMAGES,
    'PNG': PNG_IMAGES,
    'SVG': SVG_IMAGES,
    'MP3': MP3_AUDIO,
    'OGG': OGG_AUDIO,
    'WAV': WAV_AUDIO,
    'AMR': AMR_AUDIO,
    'AVI': AVI_VIDEO,
    'MP4': MP4_VIDEO,
    'MOV': MOV_VIDEO,
    'MKV': MKV_VIDEO,
    'ZIP': ZIP_ARCHIVES,
    'GZ': GZ_ARCHIVES,
    'TAR': TAR_ARCHIVES,
    'DOCX': DOCX_DOCUMENT,
    'DOC': DOC_DOCUMENT,
    'TXT': TXT_DOCUMENT,
    'PDF': PDF_DOCUMENT,
    'XLSX': XLSX_DOCUMENT,
    'PPTX': PPTX_DOCUMENT,
}

FOLDERS = []
EXTENSIONS = set()
UNKNOWN = set()


def get_extension(filename: str) -> str:
    return Path(filename).suffix[1:].upper()


def scan(folder: Path):
    for item in folder.iterdir():
        # Робота з папкою
        if item.is_dir():
            # Перевіряємо, щоб папка не була тією в яку ми вже складаємо файли.
            if item.name not in ('archives', 'video', 'audio', 'documents', 'images', 'other'):
                FOLDERS.append(item)
                scan(item)  # скануємо цю вкладену папку - рекурсія
            continue  # переходимо до наступного елемента в сканованій папці
        # else:
        # Робота з файлом
        ext = get_extension(item.name)  # беремо розширення файлу
        full_name = folder / item.name  # беремо повний шлях до файлу
        if not ext:
            MY_OTHER.append(full_name)
        else:
            try:
                container = REGISTER_EXTENSION[ext]
                EXTENSIONS.add(ext)
                container.append(full_name)
            except KeyError:
                UNKNOWN.add(ext)
                MY_OTHER.append(full_name)


if __name__ == '__main__':
    folder_for_scan = sys.argv[1]
    print(f'Start in folder: {folder_for_scan}')

    scan(Path(folder_for_scan))
    print(f"JPEG_IMAGES: {JPEG_IMAGES}")
    print(f"JPG_IMAGES: {JPG_IMAGES}")
    print(f"PNG_IMAGES: {PNG_IMAGES}")
    print(f"SVG_IMAGES: {SVG_IMAGES}")

    print(f"MP3_AUDIO: {MP3_AUDIO}")
    print(f"OGG_AUDIO: {OGG_AUDIO}")
    print(f"WAV_AUDIO: {WAV_AUDIO}")
    print(f"AMR_AUDIO: {AMR_AUDIO}")

    print(f"AVI_VIDEO: {AVI_VIDEO}")
    print(f"MP4_VIDEO: {MP4_VIDEO}")
    print(f"MOV_VIDEO: {MOV_VIDEO}")
    print(f"MKV_VIDEO: {MKV_VIDEO}")

    print(f"ZIP_ARCHIVES: {ZIP_ARCHIVES}")
    print(f"GZ_ARCHIVES: {GZ_ARCHIVES}")
    print(f"TAR_ARCHIVES: {TAR_ARCHIVES}")

    print(f'DOCX: {DOCX_DOCUMENT}')
    print(f'DOC: {DOC_DOCUMENT}')
    print(f'TXT: {TXT_DOCUMENT}')
    print(f'PDF: {PDF_DOCUMENT}')
    print(f'XLSX: {XLSX_DOCUMENT}')
    print(f'PPTX: {PPTX_DOCUMENT}')

    print('*' * 50)
    print(f'Types of file in folder: {EXTENSIONS}')
    print(f'UNKNOWN: {UNKNOWN}')
