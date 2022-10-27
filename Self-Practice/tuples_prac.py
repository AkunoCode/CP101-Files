input_tuple = (('abc', 121),('abc', 231),('abc', 148), ('abc',221))

def second_item(tuple_element):
    return tuple_element[1]

print(sorted(input_tuple, key=second_item))