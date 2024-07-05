class Figure:
    # sides_count = 0

    def __init__(self, color, sides, filled=True):
        self.__color = color
        self.filled = filled
        self.sides = [sides]


f1 = Figure('r', 1)
print(f1.sides)
