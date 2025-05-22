string = input("Enter a string: ")
dict= {}
for char in string:
    if char in dict:
        dict[char]+= 1
    else:
        dict[char]= 1
print("Frequency of Character:")
for key in dict:
    print(key,":", dict[key])
