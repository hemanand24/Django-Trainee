# This is a sample Python script.

# Press Ctrl+F5 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width

    def __iter__(self):
        yield {'length': self.length}
        yield {'width': self.width}


# Press the green button in the gutter to run the script.
rect = Rectangle(int(input()),int(input()))

for item in rect:
    print(item)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
