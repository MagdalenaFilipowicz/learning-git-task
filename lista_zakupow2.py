print("Zadanie 1.1")
shop = {'Zoologiczny':['Piesek','Kotek','Rybki'] , 'Warzywniak':['Marchew','Seler','Rukola']}
for k in shop:
    print(f"Idę do {k.capitalize()}, Kupuję tu następujące rzeczy: {str(shop[k]).title()}")
print(f"W sumie kupuję {sum(len(v)for v in shop.values())} produktów.")
