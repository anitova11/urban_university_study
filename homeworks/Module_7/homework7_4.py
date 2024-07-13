team1_num = 5
print('В команде Мастера кода участников: %s! ' % team1_num)

team2_num = 6
print('Итого сегодня в командах участников: %s и %s!' % (team1_num, team2_num))

score1 = 40
score2 = 42
print('Команда Волшебники данных решила задач: {}!'.format(score2))

team1_time = 1552.55
print('Волшебники данных решили задачи за {} с!'.format(team1_time))

team2_time = 2153.31
print(f'Команды решили {score1} и {score2} задач.')

tasks_total = score1 + score2
time_avg = format((team1_time + team2_time) / tasks_total, ".2f")
print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!.')


def challenge(score_1, score_2, team1, team2):
    if score_1 > score_2 or score_1 == score_2 and team2 > team1:
        return 'Победа команды Мастера кода!'
    elif score_1 < score_2 or score_1 == score_2 and team2 < team1:
        return 'Победа команды Волшебники Данных!'
    else:
        return 'Ничья!'


print(f'Поздравляем! {challenge(score1, score2, team1_time, team2_time)}')

