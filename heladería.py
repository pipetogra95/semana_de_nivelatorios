print("¿Qué sabor de helado desea?")
sabor=input("¿chocolate o vainilla?\n").lower()
if sabor=="chocolate":
    topping=input("¿Desea agregar topping? si/no\n").lower()
    if topping=="si":
        print("El valor total a pagar es $5.000")
    elif topping=="no":
        print("El valor total a pagar es $4.000")
elif sabor=="vainilla":
    topping=input("¿Desea agregar topping? si/no\n").lower()
    if topping=="si":
        print("El valor a total a pagar es $4.500")
    elif topping=="no":
        print("El valor total a pagar es $3.500")
else:
    print("Sabor no disponible")