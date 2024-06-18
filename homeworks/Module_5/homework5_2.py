# class House:
#     def __init__(self):
#         self.number_of_floors = 0
#
#     def set_number_of_floors(self, floors):
#         if floors > 0 and isinstance(floors, int):
#             self.number_of_floors = floors
#         else:
#             print('error')
#
#     def get_number_of_floors(self):
#         return self.number_of_floors
#
#
# first_house = House()
# print(first_house.get_number_of_floors())
# first_house.set_number_of_floors(1)
# print(first_house.get_number_of_floors())


class House:
    def __init__(self):
        self.number_of_floors = 0

    def set_number_of_floors(self, floors):
        self.number_of_floors = floors
        print('Количество этажей -', self.number_of_floors)


first_house = House()
first_house.set_number_of_floors(19)
