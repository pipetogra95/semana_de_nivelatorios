tarifa_estandar=50.0
tarifa_premium=80.0
penalizacion_fija=5000
continuar = True
while continuar:
    print("===== MENÚ PRINCIPAL - ECORIDE =====")
    print("1. Alquilar bicicleta")
    print("2. Consultar tarifas")
    print("3. Salir")
    opcion=input("Seleccione una opción: ")
    if opcion == "1":
        print("\nTipos de bicicleta disponibles:")
        print("1. Estándar")
        print("2. Premium")
        tipo_opcion = input("Seleccione el tipo de bicicleta (1 o 2): ")
        if tipo_opcion == "1":
            tipo_bicicleta = "Estándar"
            tarifa = tarifa_estandar
        elif tipo_opcion == "2":
            tipo_bicicleta = "Premium"
            tarifa = tarifa_premium
        else:
            print("Opción no válida. Volviendo al menú principal.")
            continue
        while True:
            try:
                minutos = int(input("Ingrese el tiempo de uso en minutos: "))
                if minutos <= 0:
                    print("El tiempo debe ser mayor a 0")
                else:
                    break
            except ValueError:
                print("Ingrese un número entero válido")
        costo_base=minutos*tarifa
        metodo_pago=input("Método de pago (efectivo / tarjeta / puntos): ").lower()
        dia=input("¿Es fin de semana? (s/n): ").lower()
        retraso=input("¿Devolvió la bicicleta fuera de tiempo? (s/n): ").lower()
        descuento=0
        recargo=0
        penalizacion=0
        if metodo_pago=="tarjeta":
            if minutos>60:
                descuento=costo_base*0.10
        elif metodo_pago=="puntos" and minutos<10:
            descuento=0
        if dia=="s":
            recargo=costo_base*0.05
        if retraso=="s":
            penalizacion=penalizacion_fija
        total=costo_base-descuento+recargo+penalizacion
        print("\n===== RESUMEN DEL SERVICIO =====")
        print(f"Tipo de bicicleta: {tipo_bicicleta}")
        print(f"Tiempo de uso: {minutos} minutos")
        print(f"Precio base: ${costo_base:,.2f}")
        print(f"Descuento aplicado: ${descuento:,.2f}")
        print(f"Recargo aplicado: ${recargo:,.2f}")
        print(f"Penalización: ${penalizacion:,.2f}")
        print(f"TOTAL A PAGAR: ${total:,.2f}")
        print("===============================")
        respuesta=input("¿Desea realizar otro alquiler? (s/n): ").lower()
        continuar=(respuesta=="s")
    elif opcion=="2":
        print("\n===== TARIFAS =====")
        print(f"Bicicleta Estándar: ${tarifa_estandar:.2f} por minuto")
        print(f"Bicicleta Premium:  ${tarifa_premium:.2f} por minuto")
    elif opcion=="3":
        print("Gracias por usar el sistema EcoRide. ¡Hasta pronto!")
        continuar=False
    else:
        print("Opción no válida. Intente de nuevo.")