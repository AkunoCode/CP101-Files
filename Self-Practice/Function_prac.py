# Warmup Problems
def lesser_of_two_evens(n1,n2):
    if n1 % 2 == 0 and n2 % 2 == 0:
        return min(n1,n2)
    else:
        return max(n1,n2)

def animal_crackers(text):
    text = text.split()
    if text[0][0] == text[1][0]:
        return True
    else:
        return False

def makes_twenty(n1,n2):
    if n1 + n2 == 20 or 20 in [n1,n2]:
        return True
    else:
        return False



# Level 1 Problems
def old_mcdonald(text):
    new_text = ""
    for x,y in enumerate(text):
        if x == 0 or x == 3:
            new_text += y.upper()
        else:
            new_text += y
    return new_text

def master_yoda(text):
    text = text.split()
    text = text[::-1]

    return " ".join(text)

def almost_there(n):
    if abs(n-100) <= 10 or abs(n-200) <= 10:
        return True
    else:
        return False



# Level 2 Problems:
def find_33(list):
    pos = list.index(3)
    if pos != len(list):
        if list[pos + 1] == 3:
            return True
        else:
            return False

def blackjack(n1,n2,n3):
    list = [n1,n2,n3]
    sum1 = sum(list)
    if sum1 <= 21:
        return sum1
    elif 11 in list:
        sum1 -= 10
        if sum1 <= 21:
            return sum1
        else:
            return "BUST"
    else:
        return "BUST"

def summer_69(list):
    counting = True
    test = []
    for i in list:
        if i != 6 and counting:
            test.append(i)
        elif i == 6:
            counting = False
        elif i == 9:
            counting = True
    return sum(test)



# Challenging Problems
def spy_game(list):
    recording = False
    spy = []
    for i in list:
        if i == 0 or i == 7:
            recording = True
        else:
            recording = False
        if recording:
            spy.append(i)
    spy = [str(i) for i in spy]
    if "".join(spy) == "007":
        return True
    else:
        return False          

def count_primes(num):
    factors = []
    for i in range(1,num+1):
        divs = []
        for divisor in range(1,i+1):
            if i % divisor == 0:
                divs.append(divisor)
        if len(divs) == 2:
            factors.append(i)
    return len(factors)

def print_big(letter):
    letters = {
        "A" : ["***","* *","***","* *","* *"],
        "B" : ["** ","* *","** ","* *","** "],
        "C" : ["***","*  ","*  ","*  ","***"],
        "D" : ["** ","* *","* *","* *","** "],
        "E" : ["***","*  ","***","*  ","***"]
    }

    if letter.upper() in letters.keys():
        for i in letters[letter.upper()]:
            print(i)
