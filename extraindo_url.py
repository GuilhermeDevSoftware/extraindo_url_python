import re

def procura_email(texto):
    padrao_email = r'https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    urls = re.findall(padrao_email, texto)
    return urls

texto_exemplo = """
    Visite nosso site em https://www.exemplo.com e
    https://www.contato.org para mais informações
    Entre em contato conosco através do site
    https://www.maisinfo.com.br
"""

urls_encontradas = procura_email(texto_exemplo)
print(urls_encontradas)