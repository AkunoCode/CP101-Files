def sequence(num=int):
    n_1 = 0  
    n_2 = 1  
    count = 0  
    while count < num:  
        print(n_1)  
        nth = n_1 + n_2  
        n_1 = n_2  
        n_2 = nth  
        count += 1  

print(sequence(5))