nombre=input("ingrese su nombre: ")
dias=int(input("ingrese los dias trabajados: "))
salario=int(input("ingrese su salario: "))

prima=(salario*dias)/360
cesantias=(salario*dias)/360
InteresesCesantias=(cesantias*0.12)/dias
vacaciones=(salario*dias)/720
liquidacion=(prima+cesantias+InteresesCesantias+vacaciones)

print(f"señor {nombre} para los {dias} dias trabajados y salario ${salario},"
      f"su liquidacion se compone asi prima ${prima:.2f},cesantias ${cesantias:.2f},"
      f"interesesCesantias ${InteresesCesantias:.2f},vacaciones ${vacaciones:.2f},"
      f"liquidacion ${liquidacion:.2f}.")