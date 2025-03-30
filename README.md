# Extração de URLs com Regex

Este exercício utiliza expressões regulares em Python para identificar e extrair URLs a partir de um texto.

## Funcionalidade

- Define uma função `procura_email` que recebe um texto como entrada.
- Utiliza regex para localizar URLs que comecem com `http://` ou `https://`.
- Retorna uma lista contendo as URLs encontradas no texto.

## Exemplo de uso

texto_exemplo = """
    Visite nosso site em https://www.exemplo.com e
    https://www.contato.org para mais informações
    Entre em contato conosco através do site
    https://www.maisinfo.com.br
"""

urls_encontradas = procura_email(texto_exemplo)
print(urls_encontradas)

## Saída esperada

- ['https://www.exemplo.com', 'https://www.contato.org', 'https://www.maisinfo.com.br']
