year=int(input("Escriba el año a evaluar\n"))
if year%4==0 and year%100==0:
	if year%400==0:
		print("Es un año bisiesto\n")
	elif year%400!=0:
		print("No es año bisiesto\n")
elif year%4==0 and year%100!=0:
	print("Es un año bisiesto\n")
else:
	print("No es año bisiesto\n")
