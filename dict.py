from collections import defaultdict, Counter

aparicoes = {
    'Raissa': 1,
    'gato': 2,
    'nome': 2,
    'vindo': 1
}
#print(type(aparicoes))
#print(aparicoes['Raissa'])
#print(aparicoes['gato'])
#print(aparicoes['xpto'])
#print(aparicoes.get('xpto', 0))
#print(aparicoes.get('gato', 0))

aparicoes2 = dict(Raissa=33, Rafael=30)
#print(type(aparicoes2))
#print(aparicoes2)

aparicoes2['Gael'] = 1
#print(aparicoes2)
aparicoes2['Gael'] = 0
#print(aparicoes2)

#print('Gael' in aparicoes2)

#for elemento in aparicoes2:
#    print(elemento)

#for elemento in aparicoes2.keys():
#    print(elemento)

#for elemento in aparicoes2.values():
#    print(elemento)

#for elemento in aparicoes2.items():
#    print(elemento)

#print([f'palavra {chave}' for chave in aparicoes2.keys()])

meu_texto = 'Bem vindo meu nome é Raissa eu gosto muito de nomes e tenho o meus gatos e gosto muito de gatos'
meu_texto = meu_texto.lower()

#aparicoes3 = {}

#for palavra in meu_texto.split():
#    ate_agora = aparicoes3.get(palavra, 0)
#    aparicoes3[palavra] = ate_agora + 1
#print(aparicoes3)

aparicoes3 = defaultdict(int)

#for palavra in meu_texto.split():
#    ate_agora = aparicoes3[palavra]
#    aparicoes3[palavra] = ate_agora + 1
#print(aparicoes3)

#dicionario = defaultdict(int)
#dicionario['Raissa']
#print(dicionario)
#dicionario['Raissa'] = 33
#print(dicionario)

for palavra in meu_texto.split():
    aparicoes3[palavra] += 1

print(aparicoes3)

aparicoes4 = Counter() #achei o melhor jeito de fazer contagem de palavras de um dict.

for palavra in meu_texto.split():
    aparicoes4[palavra] += 1
print(aparicoes4)