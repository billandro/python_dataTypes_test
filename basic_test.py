def int_division():
    result = 7 / 2
    return int(result)


def float_multiplication():
    result = 3.0 * 2
    return result


def combine_operations():
    result = float_multiplication()
    return result

print(f"comb: {combine_operations()}")

def extract_word():
    sentence = 'Python is awesome!'
    the_list = sentence.split(" ")
    the_word = ""

    for i in range(len(the_list)):
        if the_list[i] == "awesome!":
            for j in range(0, len(the_list[i]) - 1):
                the_word += the_list[i][j]

    return the_word


def to_lowercase():
    sentence = 'Python is awesome!'
    return sentence.lower()


def count_o():
    count = 0
    sentence = 'Python is awesome!'
    for letter in sentence:
        if letter == "o":
            count += 1

    return count


def evaluate_boolean():
    if (5 > 3) and (10 == 5 * 2):
        return False
    else:
        return True