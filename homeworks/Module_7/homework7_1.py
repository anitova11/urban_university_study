class Product:

    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    def __init__(self):
        self.__file_name = 'product.txt'

    def get_products(self):
        file = open(self.__file_name, 'r')
        st = file.read()
        file.close()
        return st

    def add(self, *products):
        for i in products:
            file = open(self.__file_name, 'a+')
            s = self.get_products()
            if i.name in s:
                print(f'Продукт {i.name} уже есть')
            else:
                file.write(str(i) + '\n')
            file.close()


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)
s1.add(p1, p2, p3)
print(s1.get_products())
