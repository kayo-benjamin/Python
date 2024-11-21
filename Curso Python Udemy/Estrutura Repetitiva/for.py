# texto = "Python"

# for letra in texto:
#     print(letra)

'''
for + range
range -> range(start, stop, step)
'''

# num = range(10, 0, -1)

# for valor in num:
#     print(valor)

"""
Iterável -> str, range, etc (__iter__)
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue seu iterador
"""
# for letra in texto
texto = 'Luiz'  # iterável

# iteratador = iter(texto)  # iterator

# while True:
#     try:
#         letra = next(iteratador)
#         print(letra)
#     except StopIteration:
#         break

for letra in texto:
    print(letra)