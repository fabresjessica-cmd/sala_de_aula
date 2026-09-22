def fizz_buzz (numero:int):
    if numero % 3 == 0:
        return "fizz"
    elif numero % 5 == 0:
        return "buzz"
    elif numero % 3 == 0 and numero % 5 == 0:
        return "fizzbuzz"
    else: 
        return numero 

def verificar_maioridade(idade:int):
    if idade > 18:
        return "maior_de_idade"
    else:
        return "menor_de_idade"
    
def verificar_paridade(numero:int):
    if numero > 0: 
        return "positivo"
    elif numero < 0:
        return "negativo"
    else:
        return "zero"
    

def classificar_numero(numero):
    if numero > 0:
        return "Positivo"
    elif numero < 0:
        return "Negativo"
    else:
        return "Zero"
 
def calcular_resultado(nota_1:float,nota_2:float ):
    if (nota_1 + nota_2)/ 2>7:
        return "aprovado" 
    else:
        return "reprovado"
    
     
def maior_de_dois(a, b):
    if a > b:
        return "O primeiro é maior"
    elif b > a:
        return "O segundo é maior"
    else:
        return "São iguais"

def calcular_desconto(valor_compra:float, e_cliente_vip):
    if e_cliente_vip or valor_compra > 200:
        desconto = 0.85 # 15%
        return f"Valor final: R$ {valor_compra*desconto}"
    else:
        desconto = 0.05 # 5%
        valor_final  

    


if __name__ =="__main__":
 teste = fizz_buzz(15)
print (teste)


    