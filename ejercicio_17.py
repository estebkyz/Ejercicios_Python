salario = float(input("Digite el salario del empleado: "))

ahorro = float(input("Digite el ahorro mensual: "))

salud = salario * 0.125      
pension = salario * 0.16    

total_deducciones = salud + pension + ahorro

total_a_recibir = salario - total_deducciones

print("Salario:", salario)
print("Ahorro:", ahorro)
print("Salud (12.5%):", salud)
print("Pensión (16%):", pension)
print("Total deducciones:", total_deducciones)
print("Total a recibir:", total_a_recibir)
