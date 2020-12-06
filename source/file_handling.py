import shutil


def file_uploader(file, id):
    file_path = "data/avatar_" + str(id) + ".png"
    file_name = "/avatar_" + str(id) + ".png"
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return file_name