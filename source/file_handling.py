import shutil
from source.dependencies import SAMPLE_AVATAR


def avatar_creation(files, id):
    try:
        for file in files:
            file_name = "avatar_" + str(id) + ".png"
            file_path = "source/data_avatar/" + file_name
            with open(file_path, "wb") as buffer:
                shutil.copyfileobj(file.file, buffer)
        state = True
    except:
        state = False
        file_name = SAMPLE_AVATAR
    return file_name, state