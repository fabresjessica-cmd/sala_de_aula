def dobrar(numeros:[]):
    for numero in numeros:
        numero = numero*2
        print (numero)

#exercício 1

def filtrar_pares(numeros):
    lista_pares = []
    for num in numeros:
    if num % 2 == 0:
        lista_pares.append(num)
    return lista_pares

#Exercicio 2

def contar_negativos(numeros):
    contador = 0
    for num in numeros:
    if num < 0:
       contador += 1
       return contador
    
#exercicio 3

def zerar_negativos(numeros):
    


if __name__=='__main__':
    dobrar ([1,2,3,4,5])
    