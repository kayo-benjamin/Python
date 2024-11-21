
while True:
    num1 = float(input("Digite um numero: "))
    num2 = float(input("Digite outro numero: "))
    print("Escolha uma operação abaixo: ")
    print("1 - Soma (+)")
    print("2 - Subtração (-)")
    print("3 - Multiplicação (*)")
    print("4 - Divisão (/)")
    resp = input(" ")
    
    if resp not in "+-*/":
        print("Operador invalido!")
        continue
    
    else:
        if resp == "+":
            soma = num1 + num2
            print(soma)
        elif resp == "-":
            subtracao = num1 - num2
            print(subtracao)
        elif resp == "*":
            multiplicacao = num1 * num2
            print(multiplicacao)
        else:
            if resp == "/":
                if num1 == 0:
                    print("Não é possível dividir por zero")
                    continue
                else:
                    divisao = num1 / num2
                    print(divisao)
        sair = input("Quer sair: [s]im: ").startswith("s")
    if sair is True:
        break
    