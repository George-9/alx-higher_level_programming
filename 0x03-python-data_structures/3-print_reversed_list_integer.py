def p(my_list=[]):
    count = len(my_list) - 1
    for num in my_list:
        print('{:d}'.format(my_list[count]))
        count -= 1
