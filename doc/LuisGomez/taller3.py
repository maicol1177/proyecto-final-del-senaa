
altura = int(input("Introduce la altura del triángulo (entero positivo): "))

for i in range(1, altura + 1):
    for j in range(i, 0, -1):
        print(2 * j - 1, end=" ")
    print()
