menu=12000
bebida=input("¿Desea incluir bebida?si/no\n").lower()
if bebida=="si":
    total=menu+3000
    iva=total+(total*(8/100))
    print(f"Total a pagar:{iva:,.0f}")
elif bebida=="no":
    iva=menu+(menu*(8/100))
    print(f"Total a pagar:{iva:,.0f}")
