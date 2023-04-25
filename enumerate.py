idades = [15, 87, 32, 65, 56, 32, 49, 37]
nomes = ['Raissa', 'Rafael','Gael', 'Aurora']

# mostrar a posição de cada idade na lista idades.

#for i in range(len(idades)): # lazy
    #print(i, idades[i])

#assim gera apenas as posições.
#print(list(range(len(idades))))

# assim gera as posições com as respectivas idades em um lista de tuplas.
# print(list(enumerate(idades))) #melhor opção

#unpacking da lista de tuplas
#for indice, idade, in enumerate(idades): #melhor opção
#    print(indice, '->', idade)

# ========================================================

usuarios = [
    ('Raissa', 33, 1990),
    ('Rafael', 30, 1993),
    ('Gael/Aurora', 0, 2024)
]

#for nome, idade, ano in usuarios:
#    print(nome, idade, ano)


print(sorted(idades))
print(sorted(idades, reverse=True))

print(list(reversed(idades)))
print(list(reversed(sorted(idades))))
idades.sort()
print(idades)

print(sorted(nomes))