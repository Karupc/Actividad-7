def pedir_entero(mensaje):
    numero = int(input(mensaje))
    return numero
def ingresar_lista():
    n = pedir_entero("¿Cuántos números desea ingresar?: ")
    lista = []
    for i in range(n):
        num = int(input(f"Ingrese el número {i+1}: "))
        lista.append(num)
    return lista
def suma_total(lista):
    return sum(lista)
def promedio(lista):
    return sum(lista) / len(lista)
def contar_pos_neg_ceros(lista):
    positivos = 0
    negativos = 0
    ceros = 0
    for x in lista:
        if x > 0:
            positivos += 1
        elif x < 0:
            negativos += 1
        else:
            ceros += 1
    return positivos, negativos, ceros
def multiplos_de_3(lista):
    return sum(1 for x in lista if x % 3 == 0)
def area_rectangulo(base, altura):
    return base * altura
def perimetro_rectangulo(base, altura):
    return 2 * (base + altura)
def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True
def promedio_calificaciones(lista):
    prom = promedio(lista)
    altas = sum(1 for x in lista if x >= 85)
    riesgo = sum(1 for x in lista if x < 60)
    return prom, altas, riesgo
def mayor(lista):
    return max(lista)
def menor(lista):
    return min(lista)
def frecuencia(lista):
    repes = {}
    for num in lista:
        repes[num] = repes.get(num, 0) + 1
    return {k: v for k, v in repes.items() if v > 1}
def calculadora(a, b, operacion):
    if operacion == "+":
        return a + b
    elif operacion == "-":
        return a - b
    elif operacion == "*":
        return a * b
    elif operacion == "/":
        if b == 0:
            return "No se puede dividir entre cero."
        return a / b
    else:
        return "Operación no válida."
    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Operaciones sobre una lista de números")
        print("2. Área y perímetro de un rectángulo")
        print("3. Verificar si un número es primo")
        print("4. Promedio de calificaciones y evaluación")
        print("5. Operaciones con una lista de enteros")
        print("6. Calculadora básica")
        print("7. Salir")
        opcion = input("Seleccione una opción: ")

        match opcion:
            case "1":
                lista = ingresar_lista()
                print("Suma total:", suma_total(lista))
                print("Promedio:", promedio(lista))
                pos, neg, ceros = contar_pos_neg_ceros(lista)
                print(f"Positivos: {pos}, Negativos: {neg}, Ceros: {ceros}")
                print("Cantidad de múltiplos de 3:", multiplos_de_3(lista))
            case "2":
                base = pedir_entero("Ingrese la base: ")
                altura = pedir_entero("Ingrese la altura: ")
                print("Área:", area_rectangulo(base, altura))
                print("Perímetro:", perimetro_rectangulo(base, altura))
            case "3":
                num = pedir_entero("Ingrese un número: ")
                if es_primo(num):
                    print(f"{num} es primo.")