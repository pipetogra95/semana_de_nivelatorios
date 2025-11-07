suma=0
numero=float(input("Ingrese un número, si es cero terminará y sumará los ingresados\n"))
while numero!=0:
    suma=suma+numero
    numero=float(input("Ingrese número\n"))
else:
    print(f"la suma total es: {suma}")