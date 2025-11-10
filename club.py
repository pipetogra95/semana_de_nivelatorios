try:
    edad=int(input("Ingrese su edad: "))
    if edad<0:
        print("Edad inválida")
    elif 0<=edad<18:
        print("Entrada denegada")
    else:
        documento=input("Tiene documento?s/n\n").lower()
        if documento=="s":
            print("Bienvenido!")
        else:
            print("Debe presentar documento")
except ValueError:
    print("Ingrese edad válida")