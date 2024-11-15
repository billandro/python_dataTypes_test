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
    the_intersection = set1.intersection(set2)
    return the_intersection


def find_union(set1, set2):
    the_union = set1.union(set2)
    return the_union


def find_difference(set1, set2):
    the_difference = set1.difference(set2)
    return the_difference


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
