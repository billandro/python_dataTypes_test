def create_squares_of_evens():
    first_list = []
    second_list = [] 
    for i in range(1, 20 + 1):
        if i % 2 == 0:
            first_list.append(i)
    
    print(first_list)
    for i in range(0, len(first_list) - 5):
        second_list.append(first_list[i] ** 2)

    return second_list


def convert_to_dict(students):
    dict_of_students = {}
    for i in range(len(students)):
        dict_of_students[students[i][0]] = students[i][1]

    return dict_of_students


def access_value_x(nested):
    return nested['c']["x"]


def append_to_list_in_dict(nested):
    nested["a"].append(6)
    return nested
    

def convert_tuple_to_list_and_append(nested):
    nested["b"] = list(nested["b"])
    nested["b"].append(6)

    return nested