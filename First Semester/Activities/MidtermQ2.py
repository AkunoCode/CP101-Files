pay_mode = int(input("Enter the mode of payment: "))
pay_amount = float(input("Enter the amount: "))

# Discount is deduction in price while interest is increase in price
# Discounted amount = total - (total * discount_percent)
# Amount w/ Interest = total + (total * discount_percent)

if pay_mode == 1:
    pay = pay_amount - (pay_amount * 0.10)
elif pay_mode == 2:
    pay = pay_amount + (pay_amount * 0.05)
elif pay_mode == 3:
    pay = pay_amount + (pay_amount * 0.10)

print(f"Total amount to be paid = {pay:.2f}")