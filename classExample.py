import main
from constants import Config
class Example():
    def __init__(self):
        self.data = 10
        self.URL = ''

    def prepare_data(self):
        return main.main()

    def fetch_data(self):
        return self.prepare_data()

    def get_data(self):
        return self.data

    def get_url(self):
        cfg = Config()
        return cfg.get_url()

# eg = Example()

# print(eg.fetch_data())