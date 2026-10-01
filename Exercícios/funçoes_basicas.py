#Exercício 1

def formatar_saudacao(nome:str, cidade:str):
    return f"Olá {nome},seja bem-vindo(a) a {cidade}!"

#Exercício 2
def calcular_perimetro(largura:float,altura:float):
    perimetro = 2*(largura+altura)
    return perimetro

#Exercicio 3
def fahrenheit_para_celcius(temp_f: float):
    temp_celcius = (temp_f -32)
    return gorjeta

#Exercicio 4
def alcular_gorjeta_por_pessoa(conta:float, porcentagem_gorjeta:float, pessoas:int): 
    gorjeta = conta* (porcentagem_gorjeta/100) / pessoas
    return gorjeta

#Exercicio 5

def resumo_circulo(raio):
    pi = 3.14159
    area = pi * (raio ** 2)
    return f"Um circulo com raio {raio} tem uma area de {area: .2f}."

#Exercicio 6

def resumo_juros_compostos(capital:float,taxa:float):
    montante_final = capital * ((1 + (taxa / 100)) ** anos)
    return f"Apos {anos} anos, R$ {capital:.2f} cresce para R$ {montante_final:.2f}."

#exercicio 7

def metricas_cilindro(raio, altura):
    pi = 3.14159
    


if __name__ =='__main__': 

    print("EXERCICIOS=============================== \n\n")
    saudacao = formatar_saudacao('Alice', 'Porto Alegre')
    print(f"1 - {saudacao}")
    perimetro = calcular_perimetro(altura=10, largura=5)
    print(f"2 - {perimetro}")
    print("==================================================================")

