print('')

print("Hello! I am your taxi service")

# Tatanungin kung gaano kalayo yung pupuntahan in kilometers (km)
distance = float(input("Please indicate the distance (km) of your destination: "))
print("Understood. Please wait while we travel to your destination...")

# Cocomputin kung magkano yung babayadan
pamasahe = distance * 5

# Sasabihin kung magkano yung pamasahe
print(f"We have arrived at your destination. The total fare amount is: {pamasahe} Pesos.")

# Hingin yung bayad ng pasahero
bayad = float(input("Please indicate the amount you want to pay: "))

# Computin kung magkano yung sukli
sukli = bayad - pamasahe

# Sabihin kung magkano yung sukli
print(f"I have received {bayad} Pesos. Your change is {sukli} Pesos.")