width = int(input("Enter width of skyscraper: "))
height = int(input("Enter height of skyscraper: "))

for i in range(1,height+1):
    if i == 1: # This is for the top of the skyscraper
        if width % 2 == 0: # if width is even
            gap = int((width- 2) / 2) # to center it
            print(" "*gap,"**"," "*gap,end="")
        else: # if width is odd
            gap = int((width - 1) / 2) # to center it
            print(" "*gap,"*"," "*gap,end="")
            
    elif i != height: # This is for the body
        for j in range(1,width+2): 
            if j == 1 or j == width+2: # if left or right side
                print(" ",end="") # leave it blank
            else:
                print("*",end="") # else print the body
                
    else: # This is for the base
        print("*"*(width+2),end="") 
    print()