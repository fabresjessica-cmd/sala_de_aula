def formatar_saudacao(nome:str, cidade:srt):
    return f"Olá {nome},seja bem-vindo(a) a {cidade}!"

if __name__ =='__main__': 
    saudacao = formatar_saudacao('Alice, Porto Alegre')
    
    print(saudacao)
    
