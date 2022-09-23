money = float(input("Enter the amount: "))

if money >= 1000:
    thousand = money // 1000
    money -= thousand * 1000
    money = round(money,2)
else:
    thousand = 0

if money >= 500:
    five_hun = money // 500
    money -= five_hun * 500
    money = round(money,2)
else:
    five_hun = 0


if money >= 200:
    two_hun = money // 200
    money -= two_hun * 200
    money = round(money,2)
else:
    two_hun = 0

if money >= 100:
    one_hun = money // 100
    money -= one_hun * 100
    money = round(money,2)
else:
    one_hun = 0

if money >= 50:
    fifty = money // 50
    money -= fifty * 50
    money = round(money,2)
else:
    fifty = 0

if money >= 20:
    twenty = money // 20
    money -= twenty * 20
    money = round(money,2)
else:
    twenty = 0

if money >= 10:
    ten= money // 10
    money -= ten * 10
    money = round(money,2)
else:
    ten = 0

if money >= 5:
    five = money // 5
    money -= five * 5
    money = round(money,2)
else:
    five = 0

if money >= 1:
    one = money // 1
    money -= one * 1
    money = round(money,2)
else:
    one = 0

if money >= 0.25:
    twentyfive = money // 0.25
    money -= twentyfive * 0.25
    money = round(money,2)
else:
    twentyfive = 0
    

if money >= 0.01:
    cent = money // 0.01
    money -= cent * 0.01
    money = round(money,2)
else:
    cent = 0


print(f"P1000 bills: {int(thousand)}")
print(f"P500 bills: {int(five_hun)}")
print(f"P200 bills: {int(two_hun)}")
print(f"P100 bills: {int(one_hun)}")
print(f"P50 bills: {int(fifty)}")
print(f"P20 bills: {int(twenty)}")
print(f"P10 coins: {int(ten)}")
print(f"P5 coins: {int(five)}")
print(f"P1 coins: {int(one)}")
print(f"P25 cents: {int(twentyfive)}")
print(f"P1 cents: {int(cent)}")