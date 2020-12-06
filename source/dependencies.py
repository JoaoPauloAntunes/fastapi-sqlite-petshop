database_path = "database/shop.db"


class LastId:
    def __init__(self):
        self.id = None

    def set_id(self, id):
        self.id = id

    def get_id(self):
        return self.id


id_checker = LastId()