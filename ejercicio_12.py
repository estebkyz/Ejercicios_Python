hombres = int(input("Digite el número de hombres: "))
mujeres = int(input("Digite el número de mujeres: "))

total = hombres + mujeres

porcentaje_hombres = (hombres / total) * 100
porcentaje_mujeres = (mujeres / total) * 100

print("Total de estudiantes:", total)
print("Porcentaje de hombres:", porcentaje_hombres, "%")
print("Porcentaje de mujeres:", porcentaje_mujeres, "%")
