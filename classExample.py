import main
class example():
    def __init__(self):
        self.data = 10

    def prepare_data(self):
        return main.main()

    def fetch_data(self):
        return self.prepare_data()

eg = example()

print(eg.fetch_data())