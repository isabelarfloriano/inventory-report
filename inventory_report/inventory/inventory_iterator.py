from collections.abc import Iterator


class InventoryIterator(Iterator):
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __next__(self):
        result = self.data[self.index]

        if not result:
            raise StopIteration()

        self.index += 1
        return result
