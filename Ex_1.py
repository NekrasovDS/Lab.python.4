# Вариант 8. Задание 1.

def get_min_cost(count, full_distance, tank, spot):
    total_cost = 0
    for i in range(count):
        n = 0
        distance, fuel = spot[i]

        if (full_distance - distance) < distance:
            distance = full_distance - distance

        if tank >= fuel:
            n = 1
        else:
            n = (-1 * distance//tank * -1)
        total_cost += distance * n
        n = 0
    return total_cost


with open("C:/Python/27-123a.txt", "r") as f1:
    N, K, V = map(int, f1.readline().split())
    stations1 = []
    for line in f1:
        code, value = map(int, line.split())
        stations1.append((code, value))
print(get_min_cost(N, K, V, stations1))

with open("C:/Python/27-123b.txt", "r") as f2:
    N, K, V = map(int, f2.readline().split())
    stations2 = []
    for line in f2:
        code, value = map(int, line.split())
        stations2.append((code, value))
print(get_min_cost(N, K, V, stations2))
