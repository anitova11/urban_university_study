grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

# решение на основе пройденного материала
students_sorted = sorted(students)
dict_avg = {students_sorted[0]: sum(grades[0]) / (len(grades[0])), students_sorted[1]: sum(grades[1]) / (len(grades[1])),
            students_sorted[2]: sum(grades[2]) / (len(grades[2])), students_sorted[3]: sum(grades[3]) / (len(grades[3])),
            students_sorted[4]: sum(grades[4]) / (len(grades[4]))}
print(dict_avg)
# второй способ с применением цикла for
dict_avg = {}
for i in range(len(grades)):
    dict_avg.update({min(students): sum(grades[i]) / len(grades[i])})
    students.remove(min(students))
print(dict_avg)
