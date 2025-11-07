cantidad=int(input("Cuántos panes comprará?\n"))
if cantidad<0:
    print(f"Cantidad inválida")
elif cantidad<21:
    precio=cantidad*300
    print(f"El total a pagar es de: ${precio:,.0f}")
elif cantidad<51:
    precio=cantidad*300
    descuento=precio-((10/100)*precio)
    ahorro=precio-descuento
    print(f"El total a pagar es: ${descuento:,.0f}")
    print(f"El ahorro total fue de: ${ahorro:,.0f}")
else:
    precio=cantidad*300
    descuento=precio-((20/100)*precio)
    ahorro=precio-descuento
    print(f"El total a pagar es: ${descuento:,.0f}")
    print(f"El ahorro total fue de: ${ahorro:,.0f}")