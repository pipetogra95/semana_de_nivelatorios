tarifa=2000
horas=int(input("¿Cuántas horas lleva en el parqueadero?\n"))
if horas<0:
    print("Valor inválido")
elif horas<=5:
    total=horas*tarifa
    print(f"El valor a pagar es ${total:,.0f}")
elif horas>5:
    total=horas*tarifa+5000
    print(f"El valor a pagar es ${total:,.0f}")