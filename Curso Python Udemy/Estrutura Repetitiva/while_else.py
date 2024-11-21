"""While/Else"""

str = "Valor"

i = 0

while i < len(str):
    letra = str[i]
    
    if letra == "":
        break
    
    print(letra)
    
    i += 1
    