estudiante=input("¿Eres estudiante?si/no\n").lower()
if estudiante=="si":
    descuento1=25000-(25000*(15/100))
    cupon=input("Ingrese cupón\n")
    if cupon=="LIBRO10":
        descuento2=descuento1-(descuento1*(10/100))
        print(f"Cupon correcto.\nEl precio total es de: {descuento2:,.0f}")
    else:
        print(f"Cupon incorrecto.\nEl precio total es de: {descuento1:,.0f}")
elif estudiante=="no":
    print("El precio total es de: $25.000")