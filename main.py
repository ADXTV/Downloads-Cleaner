import pathlib, shutil, os
from pathlib import Path

path = Path.home() / "Downloads"

FILE_CATEGORIES = {
    "images": {".jpeg", ".jpg", ".png", ".svg", ".avif", ".ico", ".webp", ".gif"},
    "executables": {".exe", ".msi", ".bat", ".cmd"},
    "videos": {".mp4", ".avi", ".mov", ".webm", ".mpeg", ".mpg", ".wmv"},
    "musics": {".mp3", ".wav", ".m4a"},
    "documents": {".pdf", ".docx", ".doc", ".txt", ".odt", ".rtf", ".xls", ".xlsx", ".ppt", ".md"},
    "archives": {".zip", ".rar", ".7z", ".tar", ".gz"},
    "torrents": {".torrent"},
    "iso": {".iso"}
}


def get_cotegory(suffix: str) -> str:
    for cat, ext in FILE_CATEGORIES.items():
        if suffix in ext:
            return cat
    return "others"


try:
    for filepath in path.iterdir():
        if not filepath.is_file():
            continue
        suffix = filepath.suffix.lower()
        category = get_cotegory(suffix)

        target_folder = path / category
        target_folder.mkdir(exist_ok=True)

        target_path = target_folder / filepath.name

        if target_path.exists():
            stem = filepath.stem()
            print(f"STEM: {stem}")
            counter = 1
            while target_path.exists():
                target_path = target_folder / f"{stem}_{counter}{suffix}"
                counter += 1
    
        shutil.move(str(filepath), str(target_path))
        print(f"{filepath.name} -> {category}")
except Exception as e:
    print(f"Произошла ошибка: {e}")



print("Сортировка завершена ✅")
