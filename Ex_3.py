"""
n количество дней для анализа (всего дней) = number_of_days
k желаемое ежедневное количество ядер
m количество тарифных планов

тарифный план доступен только в дни с l по r
c – количество ядер в сутки
p – стоимость аренды одного ядра в сутки

"""


def cost_calculation(number_of_days, k, first_day, last_day, c, cost):

    total_cost = 0
    work_time = number_of_days - (first_day + last_day)

    for day in range(work_time):

        if c >= k:
            cores = k
        else:
            cores = c

        total_cost += cores * work_time * cost

    return total_cost
