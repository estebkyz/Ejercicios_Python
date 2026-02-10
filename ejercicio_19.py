nombre = input("Digite el nombre: ")
programa = input("Digite el programa de formación: ")
ficha = input("Digite la ficha: ")

print("Digite las 5 notas:")
nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))
nota3 = float(input("Nota 3: "))
nota4 = float(input("Nota 4: "))
nota5 = float(input("Nota 5: "))

promedio = (nota1 + nota2 + nota3 + nota4 + nota5) / 5

print("Nombre:", nombre)
print("Programa:", programa)
print("Ficha:", ficha)
print("Promedio final:", promedio)
