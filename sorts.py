def bubble_sort(my_list):
    # starts with first item and compare to second and
    # switches smaller item to first position
    # continues this way through the list comparing adjacent items
    for i in range(len(my_list) - 1, 0, -1):
        for j in range(i):
            if my_list[j] > my_list[j + 1]:
                temp = my_list[j]
                my_list[j] = my_list[j + 1]
                my_list[j + 1] = temp
    return my_list


def selection_sort(my_list):
    # sorting using index.
    # minimum index starts at first value
    # loops through comparing first with each item until finding a smaller value
    # changing minimum index every time a smaller value is found
    # moving smallest value in list to front
    # then moving on to next item in list
    for i in range(len(my_list) - 1):
        min_index = i
        for j in range(i + 1, len(my_list)):
            if my_list[j] < my_list[min_index]:
                min_index = j
        if i != min_index:
            temp = my_list[i]
            my_list[i] = my_list[min_index]
            my_list[min_index] = temp
    return my_list


def insertion_sort(my_list):
    # starts at second item and compares to item before
    # if less, then it is switched and moved on to next item
    # continuing comparing with previous item
    for i in range(1, len(my_list)):
        temp = my_list[i]
        j = i - 1
        while temp < my_list[j] and j > -1:
            my_list[j + 1] = my_list[j]
            my_list[j] = temp
            j -= 1
    return my_list


print(bubble_sort([4, 2, 6, 5, 1, 3]))
print(selection_sort([4, 2, 6, 5, 1, 3]))
print(insertion_sort([4, 2, 6, 5, 1, 3]))
