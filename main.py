def binary_search(my_list, num):
    mid_list = (0 + len(my_list)-1)//2
    pos = mid_list
    found = False
    while num != my_list[pos] and not found:
        if num < my_list[pos]:
            pos -= 1
        elif num > my_list[pos]:
            pos += 1
        else:
            found = True
    return pos
my_list = [23,453,567,8776,454,23,54,23,12]
_sorted = sorted(my_list)
print(_sorted)
print(binary_search(_sorted,453))
            
        