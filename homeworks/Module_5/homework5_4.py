class Building:
    total = 0

    def __init__(self):
        Building.total += 1


print(Building.total)
for _ in range(40):
    Building()
    print(f'Количество домов - {Building.total}')

print(Building.total)
