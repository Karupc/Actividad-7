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