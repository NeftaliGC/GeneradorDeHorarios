import os

class Reader:
    def __init__(self, path):
        self.path = os.path.join(os.getcwd(), path)
        self.data = None

    def read(self):
        # leer a partir de la segunda linea
        with open(self.path, 'r') as file:
            self.data = file.readlines()[1:]

    def getData(self):
        return self.data

    def __str__(self):
        return