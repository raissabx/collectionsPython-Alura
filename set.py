usuarios_ds = [15, 23, 43, 56]
usuario_ml = [13, 23, 56, 42]

assistiram = usuarios_ds.copy()
assistiram.extend(usuario_ml)
#print(assistiram)
#print(len(assistiram))
set(assistiram)
#print(type(assistiram))

teste = set([1,2,3,1])
#print(teste)
#print(type(teste))

usuarios_data_science = {15, 23, 43, 56}
usuarios_machine_learning = {13, 23, 56, 42}

for usuario in set(assistiram):
    print(usuario)


print(usuarios_data_science | usuarios_machine_learning)

print(usuarios_data_science & usuarios_machine_learning)

print(usuarios_data_science - usuarios_machine_learning)

fez_ds_mas_nao_fez_ml = usuarios_data_science - usuarios_machine_learning
print(15 in fez_ds_mas_nao_fez_ml)

print(23 in fez_ds_mas_nao_fez_ml)
print(usuarios_data_science ^ usuarios_machine_learning)

usuarios = {1, 5, 76, 34, 52, 13, 17}
usuarios.add(13)
usuarios.add(765)
print(len(usuarios))
usuarios = frozenset(usuarios)
usuarios.add(134)
print(usuarios)


meu_texto = 'Bem vindo meu nome é Raissa eu gosto muito de nomes e tenho o meus gatos e gosto muito de gatos'
print(set(meu_texto.split()))







