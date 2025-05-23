numbers=[4, 5, 6, 7, 8, 9]
k= 3
grp= []
for i in range(k):
    grp.append([])
numbers.sort(reverse=True)
for num in numbers:
    min_sum = sum(grp[0])
    min_index = 0
    for i in range(1, k):
        if sum(grp[i]) < min_sum:
            min_sum= sum(grp[i])
            min_index= i
    grp[min_index].append(num)
for i in range(k):
    print("Group",i+1,":",grp[i],"Sum =",sum(grp[i]))
