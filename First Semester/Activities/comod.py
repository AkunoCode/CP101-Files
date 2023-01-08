toothpaste_list = [tuple(commodity.split("-")) for commodity in "toothpaste1-100, toothpaste2-150, toothpaste3-135".split(", ")]
soap_list = [tuple(commodity.split("-")) for commodity in "soap1-80, soap2-50, soap3-135".split(", ")]
detergent_list = [tuple(commodity.split("-")) for commodity in "detergent1-280, detergent2-350, detergent3-635".split(", ")]
chips_list = [tuple(commodity.split("-")) for commodity in "chips1-60, chips2-20, chips3-35".split(", ")]
candies_list = [tuple(commodity.split("-")) for commodity in "candies1-60, candies2-20, candies3-35".split(", ")]

cheapest_toothpaste = min(toothpaste_list, key=lambda x: x[1])
cheapest_soap = min(soap_list, key=lambda x: int(x[1]))
cheapest_detergent = min(detergent_list, key=lambda x: x[1])
cheapest_chips = min(chips_list, key=lambda x: x[1])
cheapest_candies = min(candies_list, key=lambda x: x[1])

print(f"Cheapest: {cheapest_toothpaste[0]}, {cheapest_soap[0]}, {cheapest_detergent[0]}, {cheapest_chips[0]}, {cheapest_candies[0]}")

total_price = int(cheapest_toothpaste[1]) + int(cheapest_soap[1]) + int(cheapest_detergent[1]) + int(cheapest_chips[1]) + int(cheapest_candies[1])
print(f"Total: {total_price}")