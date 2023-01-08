from cmath import sqrt


fibonacci = []
real = []
length = int(input("How many fibonacci numbers do you want?: "))

for i in range(1,(length+1)):
    fibonumber = 1/sqrt(5)*((((1+sqrt(5))/2)**i)-(((1-sqrt(5))/2)**i))
    fibonacci.append(fibonumber)

for i in range(0,(len(fibonacci))):
    real.append(int(fibonacci[i].real))

print(real)