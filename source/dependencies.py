database_path = "source/database/shop.db"
DATABASE_PATH = "source/database/shop.db"
SAMPLE_AVATAR = "sample.png"


class LastId:
    def __init__(self):
        self.id = None

    def set_id(self, id):
        self.id = id

    def get_id(self):
        return self.id


id_checker = LastId()