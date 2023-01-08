def checker(series = list):
    arithmetic = False
    if series[1] - series[0] == series[2] - series [1]:
        arithmetic = True
    
    return (arithmetic)


def nth_term(a1=float,nth=float,d=float):
    nth_series = a1 + (nth-1)*d

    return(nth_series)

def difference(series = list):
    a = series[1] - series[0]
    b = series[2] - series [1]
    if a == b:
        return(a)
    else:
        return("series is not arithmetic")

def main():
    series = []
    while True:
        arithmetic = input("Enter a number in the series (Type \"None\" if done): ")
        if arithmetic.lower() == "none":
            prompt = "What function would you like to do?"
            prompt += "\n\tType A if you want to check if the list is an arithmetic sequence"
            prompt += "\n\tType B if you want to find the common difference"
            prompt += "\n\tType C if you want to find the nth term."
            choose = input(prompt)
            if choose.lower() == "a":
                print(checker(series))
            elif choose.lower() == "b":
                print(difference(series))
            elif choose.lower() == "c":
                a1 = series[0]
                nth = int(input("Which nth term are you looking for?: "))
                d = difference(series)
                print(nth_term(a1,nth,d))
        else:
            series.append(float(arithmetic))

main()