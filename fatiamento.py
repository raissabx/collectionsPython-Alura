url = 'bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar'

indice_interrogacao = url.find('?')

url_base = url[:indice_interrogacao]
print(url_base)

url_parametro = url[indice_interrogacao+1:]
print(url_parametro)

parametro_busca = 'moedaOrigem'

indice_parametro = url_parametro.find(parametro_busca)

indice_valor = indice_parametro + len(parametro_busca) + 1

indice_e_comercial = url_parametro.find('&', indice_valor)

if indice_e_comercial == -1:
    valor = url_parametro[indice_valor]
else:
    valor = url_parametro[indice_valor:indice_e_comercial]
print(valor)
