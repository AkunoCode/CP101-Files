def bigBoi(*numbers):
    biggest = numbers[0]
    for i in numbers:
        if i > biggest:
            biggest = i
    return biggest


def addMeUp(*numbers):
    total = 0
    for i in numbers:
        total += i
    return total


def multiplyMe(*numbers):
    product = 0
    for i in numbers:
        product *= i
    return product


def reverseMeme(word):
    return word[::-1]


def factoringMe(number):
    product = 1
    for i in range(1, number + 1):
        product *= i
    return product


def rangeMeUp(number, min_range, max_range):
    if number in range(min_range, max_range+1):
        return "Number is in range"
    else:
        return "Number is not in range"


def UpperLower(sentence=""):
    upper = 0
    lower = 0
    space = 0
    number = 0
    for i in sentence:
        if i.isupper():
            upper += 1
        elif i.islower():
            lower += 1
        elif i == " ":
            space += 1
        elif i.isnumeric():
            number += 1

    return f"""
    Uppercase Letters: {upper}
    Lowercase Letters: {lower}
    Space Character: {space}
    Numbers: {number}
    """


def PickMe(*list):
    unique = []
    for i in list:
        if i not in unique:
            unique.append(i)
    return unique


def sumRecur(list):
    if len(list) == 1:
        return list[0]
    else:
        return list[0] + sumRecur(list[1:])
