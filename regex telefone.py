# Conheça mais sobre o Regex: https://docs.python.org/pt-br/3.8/howto/regex.html
# Conheça mais sobre o 're' do python: https://docs.python.org/pt-br/3/library/re.html

# Módulo 're' que fornece operações com expressões regulares.
import re

 # TODO: Crie uma função chamada 'validate_numero_telefone' que aceite um argumento 'phone_number':
def validate_numero_telefone(entrada):
     # TODO: Defina um padrão de expressão regular (regex) para validar números de telefone no formato (XX) 9XXXX-XXXX:    
    padrao = r'\(\d{2}\) 9\d{4}-\d{4}'
    if re.match(padrao, entrada):  
        return print("Número de telefone válido.")
    else:
        return print ("Número de telefone inválido.")

        # TODO: Agora crie um return, para retornar que o número de telefone é válido:
        
        # TODO: Crie um else e return, caso não o número de telefone seja inválido:


    # Solicita ao usuário que insira um número de telefone e armazena o valor fornecido na variável 'phone_number'.
print ("entre com um numero de telefone com DDD: ")
entrada = str(input())
    # TODO: Chame a função 'validate_numero_telefone()' com o número de telefone fornecido como argumento e armazene o resultado retornado na variável 'result'.
resultado = validate_numero_telefone(entrada)
    # Imprime o resultado:
#print(resultado)