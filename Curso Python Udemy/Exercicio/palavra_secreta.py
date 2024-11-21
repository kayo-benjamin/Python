import os

palavra = 'amor'
acertadas = ''
tentativas = 0
while True:
    user = input("Digite uma letra: ")
    tentativas += 1
    
    if len(user) > 1:
        print("Apenas uma letra, por favor!")
        continue
    
    if user in palavra:
        acertadas += user
        
    formada = ''
    for letra in palavra:
        if letra in acertadas:
            formada += letra
        else:
            formada += '_'
            
    print("Palavra formada: ", formada)
    
    if formada == palavra:
        os.system('cls')
        print("Parabéns, você acertou a palavra!")
        print(f"A palavra era {formada}")
        print(f"Você usou {tentativas} tentativas")
        acertadas = ''
        tentativas = 0