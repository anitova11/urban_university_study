name = 'Ksu'
age = 24
print('my name is %s' % 'Kseniya')
print('my name is %s, i`m %s' % (name, age))
print('my name is %(name)s and i`m %(age)s ' % {'name': 'Ksusha', 'age': 24})

# format
print('i`m learning {} {}'.format('python', 'lang'))
print('i live in {1} {0}'.format('city', 'Moscow'))
print('i was born in {city} in {year}'.format(year=2000, city='Zelenodolsk'))
