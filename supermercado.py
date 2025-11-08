cantidad=int(input("¿Cuántas unidades llevará?\n"))
total=cantidad*2000
if 0<cantidad<10:
    envio=total+5000
    print(f"El total es: {envio:,.0f}")
elif 10<=cantidad<30:
    descuento=total-(total*(5/100))
    if descuento<50000:
        envio=descuento+5000
        print(f"El total es: {envio:,.0f}")
    else:
        print(f"El total es: {descuento:,.0f}")
elif cantidad>=30:
    descuento=total-(total*(15/100))
    print(f"El total es: {descuento:,.0f}")
else:
    print("Debe ser un número positivo y mayor que cero")