class Building:

    def __init__(self, name, floors):
        self.numberOfFloors = floors
        self.buildingType = name

    def __eq__(self, other):
        return self.numberOfFloors == other.numberOfFloors and self.buildingType == other.buildingType


house = Building('Korston', 14)
house1 = Building('Imperial', 5)
house2 = Building('Korston', 14)

print(house == house2, house1 == house2)
