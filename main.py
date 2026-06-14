import pathlib, shutil, os

home_path = os.path.expanduser('~')
path = home_path + r"\Downloads"



try: 
    for filename in os.listdir(path):
        p = pathlib.Path(filename)
        filepath = os.path.join(path, filename)
        if os.path.isfile(filepath):
            if p.suffix == ".jpeg" or p.suffix == ".jpg" or p.suffix == ".png" or p.suffix == ".svg" or p.suffix == ".avif" or p.suffix == ".ico" or p.suffix == ".webp" or p.suffix == ".gif":
                print("КАРТИНКА 📷: ", filename)
                if not os.path.exists(path + r"\images"):
                    print("СОЗДАЕМ ПАПКУ 📁")
                    os.mkdir(path + r"\images")
                shutil.move(filepath, os.path.join(path, "images"))
            elif p.suffix == ".exe" or p.suffix == ".msi" or p.suffix == ".bat" or p.suffix == ".cmd":
                if not os.path.exists(path + r"\executables"):
                    print("СОЗДАЕМ ПАПКУ 📁")
                    os.mkdir(path + r"\executables")
                shutil.move(filepath, os.path.join(path, "executables"))
            elif p.suffix == ".mp4" or p.suffix == ".avi" or p.suffix == ".mov" or p.suffix == ".webm" or p.suffix == ".mpeg" or p.suffix == ".mpg" or p.suffix == ".wmv":
                if not os.path.exists(path + r"\videos"):
                    print("СОЗДАЕМ ПАПКУ 📁")
                    os.mkdir(path + r"\videos")
                shutil.move(filepath, os.path.join(path, "videos"))
            elif p.suffix == ".mp3" or p.suffix == ".wav" or p.suffix == ".m4a":
                if not os.path.exists(path + r"\musics"):
                    print("СОЗДАЕМ ПАПКУ 📁")
                    os.mkdir(path + r"\musics")
                shutil.move(filepath, os.path.join(path, "musics"))
            elif p.suffix == ".pdf" or p.suffix == ".docx" or p.suffix == ".doc" or p.suffix == ".txt" or p.suffix == ".odt" or p.suffix == ".rtf" or p.suffix == ".xls" or p.suffix == ".xlsx" or p.suffix == ".ppt" or p.suffix == ".md":
                if not os.path.exists(path + r"\documents"):
                    print("СОЗДАЕМ ПАПКУ 📁")
                    os.mkdir(path + r"\documents")
                shutil.move(filepath, os.path.join(path, "documents"))
            elif p.suffix == ".zip" or p.suffix == ".7z" or p.suffix == ".rar" or p.suffix == ".tar" or p.suffix == ".gz":
                if not os.path.exists(path + r"\archives"):
                    print("СОЗДАЕМ ПАПКУ 📁")
                    os.mkdir(path + r"\archives")
                shutil.move(filepath, os.path.join(path, "archives"))
            elif p.suffix == ".torrent":
                if not os.path.exists(path + r"\torrents"):
                    print("СОЗДАЕМ ПАПКУ 📁")
                    os.mkdir(path + r"\torrents")
                shutil.move(filepath, os.path.join(path, "torrents"))
            else:
                if not os.path.exists(path + r"\others"):
                    print("СОЗДАЕМ ПАПКУ 📁")
                    os.mkdir(path + r"\others")
                shutil.move(filepath, os.path.join(path, "others"))
except Exception as e:
    print(f"Что то пошло не так...: {e}")


print("Сортировка завершена ✅")
