data = ((10, 10, 10, 12),
        (30, 45, 56, 45),
        (81, 80, 39, 32),
        (1, 2, 3, 4))
average= []
for i in range(4):
    total = 0
    for row in data:
        total += row[i]
    average.append(total / 4)
print(average)
