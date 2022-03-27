
def count_integer(numbers, integer):
    count = 0
    for item in numbers:
        if item == integer:
            count += 1
    if count > 0:
        return count
    else:
        return 42


def list_func(numbers, integer):
    empty_list = []
    if integer not in numbers:
        return empty_list
    else:
        numbers[5] = integer
        print(numbers[::-1])
        return numbers


def compare_lists(list1, list2):
    newlist = []
    for item in list1:
        if item in list2:
            newlist.append(item)
    return newlist


def remove_duplicates(lst):
    new_list = []
    for item in lst:
        if item not in new_list:
            new_list.append(item)
    return new_list


def dict_func(dictionary):
    typ = dictionary['Type']
    brand = dictionary['Brand']
    price = dictionary['Price']
    print(f'You have a {typ} from {brand} that costs {price}.')
    dictionary['OS'] = 'Linux'
    return dictionary



