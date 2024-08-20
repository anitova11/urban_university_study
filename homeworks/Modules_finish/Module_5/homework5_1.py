class House:
    def __init__(self, name, floors):
        self.name = name
        self.floors = floors

    def go_to(self, new_floor):
        if new_floor < 1 or new_floor > self.floors:
            print('There is no such floor')
        else:
            for i in range(1, new_floor + 1):
                print(i)


h1 = House('Clover_House', 18)
h2 = House('Imperial Turkiz Resort Hotel', 5)
h1.go_to(5)
h2.go_to(10)
