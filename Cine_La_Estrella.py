edad=int(input("¿Cuál es su edad?\n"))
if edad<0:
    print("Edad inválida")
elif edad<5:
    print("Entrada gratis!")
elif 5<=edad<=11:
    print("El valor de su entrada es $5.000")
elif 12<=edad<=59:
    print("El valor de su entrada es $8.000")
else:
    print("El valor de su entrada es $4.000")
