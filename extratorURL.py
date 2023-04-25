import re


class ExtratorURL:
    def __init__(self, url):
        self.url = self.sanitiza_url(url)
        self.valida_url()

    def sanitiza_url(self, url):
        if type(url) == str:
            return url.strip()
        else:
            return ''

    def valida_url(self):
        if not self.url:
            raise ValueError('A URL está vazia')
        padrao_url = re.compile('(http(s)://)?(www.)?bytebank.com(.br)?/cambio')
        match = padrao_url.match(self.url)
        if not match:
            raise ValueError('A URL não é valida!')

    def get_url_base(self):
        indice_interrogacao = self.url.find('?')
        url_base = self.url[:indice_interrogacao]
        return url_base

    def get_url_parametros(self):
        indice_interrogacao = self.url.find('?')
        url_parametros = self.url[indice_interrogacao + 1:]
        return url_parametros

    def get_valor_parametro(self, parametro_busca):
        indice_parametro = self.get_url_parametros().find(parametro_busca)
        indice_valor = indice_parametro + len(parametro_busca) + 1
        indice_e_comercial = self.get_url_parametros().find('&', indice_valor)
        if indice_e_comercial == -1:
            valor = self.get_url_parametros()[indice_valor:]
        else:
            valor = self.get_url_parametros()[indice_valor:indice_e_comercial]
        return valor

    def __len__(self):
        return len(url)

    def __str__(self):
        return f'URL Completa: {self.url} \nParâmetros: {self.get_url_parametros()} \nBase: {self.get_url_base()}' \

    def __eq__(self, other):
        return self.url == other.url




url = 'bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar'
url2 = 'bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar'
extrator_url = ExtratorURL(url)
extrator_url2 = ExtratorURL(url2)

valor_quantidade = extrator_url.get_valor_parametro('quantidade')
#print(valor_quantidade)
print(len(extrator_url))
print(str(extrator_url))
print(extrator_url == extrator_url2)

#--------------------------------------------------------------

valor_dolar = 5.50  # 1 dólar = 5.50 reais
moeda_origem = extrator_url.get_valor_parametro("moedaOrigem")
moeda_destino = extrator_url.get_valor_parametro('moedaDestino')
quantidade = extrator_url.get_valor_parametro('quantidade')

if moeda_origem == 'real':
    real_para_dolar = float(valor_quantidade) * valor_dolar
    print(f'O valor de R$ {valor_quantidade} convertido em dolar é de $ {real_para_dolar:.2f}')

if moeda_origem == 'dolar':
    dolar_para_real = float(valor_quantidade) / valor_dolar
    print(f'O valor de $ {valor_quantidade} convertido em real é de R$ {dolar_para_real:.3r76y555555555555555552f}')


