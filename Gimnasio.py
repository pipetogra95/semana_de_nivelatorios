dias=int(input("¿Cuántos días has entrenado esta semana?\n"))
if 0>dias or dias>7:
    print("Dato inválido")
elif 4<=dias<=7:
    print("¡Excelente disciplina!")
    print("1 punto de energía ganado")
elif dias==2 or dias==3:
    print("Bien, pero puedes dar más")
elif dias==0 or dias==1:
    print("No aflojes, tú puedes mejorar")