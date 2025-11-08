tecnica=float(input("Nota de la prueba técnica: "))
if 0>tecnica or tecnica>5:
    print("Nota inválida")
else:
    logica=float(input("Nota de la prueba lógica: "))
    if 0>logica or logica>5:
        print("Nota inválida")
    else:
        nota_final=(tecnica*0.7)+(logica*0.3)
        if nota_final<2:
            print("Reprobado")
        elif 2<=nota_final<3:
            print("Revisión")
        elif nota_final>=3:
            print("Aprobado")