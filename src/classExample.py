import src.main
from src.constants import Config


class Example:
    def __init__(self):
        self.data = 10
        self.URL = ""
        self.object = MiniObject()

    def prepare_data(self):
        return main.main()

    def fetch_data(self):
        return self.prepare_data()

    def get_data(self):
        return self.data

    def get_url(self):
        cfg = Config()
        return cfg.get_url()

    def get_object(self):
        return self.object


class MiniObject:
    def __init__(self):
        self.param1 = 1
        self.param2 = 2


# eg = Example()

# print(eg.fetch_data())
