num1 = int(input("nota 1: "))
num2 = int(input("nota 2: "))
num3 = int(input("nota 3: "))

sumatoria = num1 + num2 + num3
promedio = sumatoria/3
if promedio >=71:
    print ("Aprobado", promedio)
else:
    print ("Reprobado", promedio)

