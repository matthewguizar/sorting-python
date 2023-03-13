# first index in compared to rest of items using for loop
# aligns all bigger items together and smaller items together
# moves first index after smaller items and returns index

def swap(my_list, index1, index2):
    temp = my_list[index1]
    my_list[index1] = my_list[index2]
    my_list[index2] = temp

# rearranges items in list so first index is placed in correct spot
# while smaller items are in front and bigger items are at the end
def pivot(my_list, pivot_index, end_index):
    swap_index = pivot_index

    # starts at second item in list
    for i in range(pivot_index + 1, end_index + 1):
        if my_list[i] < my_list[pivot_index]:  # comparison
            swap_index += 1
            swap_index(my_list, swap_index, i)
    swap_index(my_list, pivot_index, swap_index)
    return swap_index  # returns index
