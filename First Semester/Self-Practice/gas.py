"""
Problem: Gas Station Promo
Suppose that the gas price is P55.0/Liters but the gas station has a promo 
that FOR EVERY P250.0 SPENT, 2 LITERS OF GAS WILL BE FREE of charge.

Make a program that will:
1. Ask the user how many liters of gas do they want to load.
2. Compute the price per liters and apply the promo.
3. Display how much the user will need to pay.
4. Take the users money and display their change.

Examples:

How many liters of gas would you like to load?: 1
That will be P55        
How much will you pay?: 60
I received P60. Your change is P5

How many liters of gas would you like to load?: 4
That will be P220       
How much will you pay?: 300
I received P300. Your change is P80

How many liters of gas would you like to load?: 5
That will be P165       
How much will you pay?: 200
I received P200. Your change is P35

"""


"""
Basically, Kailangan mo munang icheck yung base price (price without the promo) which is liters * 55
at pagkatapos ay gagamitan mo ng floor division (base_price // 250) para makuha kung ilang 250 yung nagastos nya.
Pagkatapos ay kung ilang 250 ang nagastos niya, imumultiply mo sa 2 dahil 2 liters nga yung malilibre nya per every 250.
After that, imumultiply mo ulet sa 55 at ibabawas mo na sa base_price at ayun na yung magiging promo_price. 

"""
liters = int(input("How many liters of gas would you like to load?: "))

# To get the base price without the promo.
base_price = liters * 55

# To get how many P250.0 were spent.
promo = base_price // 250

# To get the amount that will be free. 2 * 55 to get the price of 2 liters of gas then multiply sa promo amount
promo_price = (2 * 55) * promo

# Now calculate the deducted promo price that the user will have to pay.
deducted_price = base_price - promo_price

print(f"That will be P{deducted_price}")

payment = int(input("How much will you pay?: "))

change = payment - deducted_price

print(f"I received P{payment}. Your change is P{change}")