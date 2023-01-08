data_set = [[6,7,8],[7,5,8],[9,4,6],[5,4,3],[7,6,7],[8,7,7],[6,5,8],[5,6,4]]

def problem1(x,y,z):
    return x + y + 2*z

def problem2(x,y,z):
    return (x*y) - (2*z)

def problem3(x,y,z):
    return 3*x*y*z

def problem4(x,y,z):
    return x**2 + 3*y - 2*z

sum1 = 0
sum2 = 0
sum3 = 0
sum4 = 0
for n in data_set:
    sum1 += problem1(n[0],n[1],n[2])
    sum2 += problem2(n[0],n[1],n[2])
    sum3 += problem3(n[0],n[1],n[2])
    sum4 += problem4(n[0],n[1],n[2])

print(f"""
Problem 1: {sum1}
Problem 2: {sum2}
Problem 3: {sum3}
Problem 4: {sum4}
""")
