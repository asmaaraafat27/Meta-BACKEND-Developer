my_list = [1,2,3]

def add_to_list(lst, item):
    nl = lst.copy()
    nl.append(item)
    return nl

new_list = add_to_list(my_list, 4)

print(new_list) # output: [1,2,3,4]
print(my_list) # output: [1,2,3] 