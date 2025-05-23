def deepest_nesting(lst):
    depth=0
    while isinstance(lst, list) and lst:
        lst= next((item for item in lst if isinstance(item, list)), [])
        depth+= 1
    return depth
lst= [1, [2, [3, [4, []]], 5]]
print(deepest_nesting(lst)) 
