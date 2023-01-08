from math import sqrt

def Mean(set):
    global mean
    mean = round((sum(set)/len(set)),2)
    return mean

def Median(set):
    global median
    if len(set) % 2 == 0:
        n1 = int(len(set)/2) - 1
        n2 = n1 + 1
        median = (set[n1] + set[n2])/2
    else:
        median = set[int((len(set)+1)/2)-1]
    return median

def Mode(set):
    global mode
    list = []
    for i in set:
        if i not in list:
            list.append(i)

    freq = [(set.count(x),x) for x in list]
    freq.sort(key= lambda x: x[0], reverse= True)

    if freq[0][0] == 1:
        mode = "None"
    else:
        highest = []
        for i in freq:
            if i[0] == freq[0][0]:
                highest.append(i[1])
        mode = highest
    return mode

def Midrange(set):
    global midrange
    midrange = (max(set) + min(set)) / 2
    return midrange

def Range(set):
    global ranges
    ranges = max(set) - min(set) 
    return ranges

def Variance(set, mode):
    global variance
    if mode.lower() == "population":
        variance = (sum([((i-mean)**2) for i in set]))/len(set)
    
    elif mode.lower() == "sample":
        variance = (sum([((i-mean)**2) for i in set]))/(len(set)-1)
    return variance

def SD(variance):
    global sd
    sd = sqrt(variance)
    return sd

def CV():
    global cv
    cv = (sd/mean) * 100
    return cv

def Interpret():
    print("Data Interpretation: ",end="")
    if sd > -2 and sd < 2:
        print("""
        The data is closely spread around the mean and has a small variance. 
        Therefore the data is considered to be precise and reliable.\n""")
    else:
        print("""
        The data is widely spread and has a huge variance. 
        Therefore the data is considered to be less precise and less reliable.\n""")

def Execute():
    type = input("\nPopulation set or Sample set? (Type \"Population\" or \"Sample\"): " )
    set = input("Input the data set with each data seperated by spaces:\n").split()
    set = [int(i) for i in set]
    set.sort()

    print(f"\n\nData Set: {set}")
    print("\nMeasures of Central Tendency:")
    print(f"\tThe Mean of the set is: {Mean(set)}")
    print(f"\tThe Median of the set is: {Median(set)}")
    print(f"\tThe Mode of the set is: {Mode(set)}")
    print(f"\tThe Midrange of the set is: {Midrange(set)}\n")

    print("Measures of Variability:")
    print(f"\tThe Range of the set is: {Range(set)}")
    print(f"\tThe Variance of the set is: {round(Variance(set,type),2)}")
    print(f"\tThe Standard Deviation of the set is: {round(SD(variance),2)}")
    print(f"\tThe Coefficient of Variation of the set is: {round(CV(),1)}\n")
    Interpret()

Execute()