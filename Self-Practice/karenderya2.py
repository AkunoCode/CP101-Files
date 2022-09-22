menu = {"hotdog":20,"pancit":15,"gulaman":10}
pay = 0
number_order = 0
order_list = []
type_count = {}
while True:
    print("""
    Hello! What would you like to order?: 

    Type "Menu" to print the menu.
    Type "Done" if you're finished ordering.
    """)
    order = input("\t")
    if order.lower() in menu.keys():
        order_list.append(order.lower())
        pay += menu[order.lower()]
        number_order += 1
    elif order.lower() == "menu":
        print("\nToday we have the following available: ")
        for item in menu.keys():
            print("-",item)
    elif order.lower() == "done":
        print("\nOk, Thank you! I'll serve your order now.")
        break

for i in order_list:
    type_count[i] = order_list.count(i)

for order, count in type_count.items():
    print(f"\tHere's your {count} {order}")

if number_order >= 2:
    pay = pay - (pay * 0.20)
else:
    pass

print(f"\nThanks for eating here, the amount of your bill is P{pay}")

payment = float(input("\nPlace your payment here: "))

print(f"\nThank you! Here is your change P{payment - pay} Come again!\n")