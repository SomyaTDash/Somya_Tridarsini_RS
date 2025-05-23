import random
def shuffle_restricted(lst):
    while True:
        shuffled=random.sample(lst, len(lst))
        if all(shuffled[i] !=lst[i] for i in range(len(lst))):
            return shuffled
original= [4,9,8,2,1]
shuf= shuffle_restricted(original)
print("Original:",original)
print("Deranged:",shuf)
