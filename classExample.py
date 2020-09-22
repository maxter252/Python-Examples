import main
class Example():
    def __init__(self):
        self.data = 10

    def prepare_data(self):
        return main.main()

    def fetch_data(self):
        return self.prepare_data()

    def get_data(self):
        return self.data

# eg = Example()

# print(eg.fetch_data())