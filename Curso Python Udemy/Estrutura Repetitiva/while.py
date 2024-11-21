"""
Estrutura de repetição
while (enquanto)
Executa uma ação enquanto uma condição fo verdadeira
Loop infinito -> Quando um codigo não tem fim
"""
# condicao = True

# while condicao:
#    nome =  input("Qual seu nome? ")
#    print(f"Seu nome é {nome}")
#    break


# 0 ao 9
#contador = 0

# while contador < 10:
#     print(contador)
#     contador += 1

# 1 ao 10
# while contador < 10:
#     contador += 1
#     print(contador)
    
""" Qual letra apareceu mais vezes na frase """

#Fazendo iteração
frase = "Estudar programação é a melhor coisa do mundo!"

i = 0
aparareceu_mais_vezes = 0
letra_apareceu_mais_vezes = ''

while i < len(frase):
    atual = frase[i]
    qtd_letras = frase.count(atual)
    
    if aparareceu_mais_vezes < qtd_letras:
        aparareceu_mais_vezes = qtd_letras
        letra_apareceu_mais_vezes = atual
        
    i += 1
    
print(f"A letra que mais apareceu foi '{letra_apareceu_mais_vezes}' que apareceu {qtd_letras}x")
