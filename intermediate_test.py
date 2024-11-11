def add_to_list(numbers):
    numbers.append(6)
    return numbers


def remove_from_list(numbers):
    numbers.remove(3)
    return numbers


def insert_at_beginning(numbers):
    new_list = [0]
    for number in numbers:
        new_list.append(number)

    return new_list


def reverse_list(numbers):
    numbers.reverse()
    return numbers


def create_new_tuple(t):
    return (t[0],t[1])


def check_if_value_exists(t, value):
    for number in t:
        if number == value:
            return True
        
    return False


def find_intersection(set1, set2):
    """
    Task:
    - Find the intersection of sets `set1` and `set2`.
    
    Return:
    - The intersection of the two sets.
    """
    return 

# print(find_intersection({1, 2, 3, 4}, {3, 4, 5, 6}))


def find_union(set1, set2):
    """
    Task:
    - Find the union of sets `set1` and `set2`.
    
    Return:
    - The union of the two sets.
    """
    new_set = {}
    for i in range(len(set1)):
        print(set1[i])
        print(set2[i])

    # return new_set


def find_difference(set1, set2):
    """
    Task:
    - Find the difference between set1 and set2 (i.e., set1 - set2).
    
    Return:
    - The difference between the two sets.
    """
    pass


def add_student(student_grades):
    student_grades['David'] = 92
    return student_grades


def change_bob_grade(student_grades):
    student_grades["Bob"] = 95
    return student_grades


def delete_charlie(student_grades):
    del student_grades["Charlie"]
    return student_grades


def retrieve_alice_grade(student_grades):
    return student_grades["Alice"]
