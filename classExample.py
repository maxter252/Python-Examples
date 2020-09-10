class example():
    def __init__(self):
        self.data = 10

    def prepare_data(self):
        return 5

    def fetch_data(self):
        return prepare_data()



eg = example()

print(eg.fetch_data())