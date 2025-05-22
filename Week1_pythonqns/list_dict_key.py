list= ['a', 'b', 'c', 'd']
dict= {'a':1, 'b':2, 'e':5}
K=input("Enter the key to check: ")
if K in list and K in dict:
    print("Value from dictionary:",dict[K])
