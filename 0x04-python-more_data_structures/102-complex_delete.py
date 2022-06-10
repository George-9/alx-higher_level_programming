
def complex_delete(a_dictionary, value):
    if value not in list(a_dictionary.values()):
        return a_dictionary
    new_dict = {}
    for item in a_dictionary:
        if a_dictionary[item] is not value:
            new_dict[item] = a_dictionary[item]
    a_dictionary.clear()
    for item in new_dict:
            a_dictionary[item] = new_dict[item]
    return new_dict
