# criar verificador e gerador de senhas com quantidade de caracteres predefinidos
# o verificador analisa a senha e verifica se esta com todas as diretrizes, e armazena esssa senha
# o gerador gera uma senha de acordo o pedido do usuario, com quantidade de caracteres, letras, numero e entre outros.
# ramdom para o gerador de senha
# e re para o verificador

import random
import re
import string

def criar_senha():
    orient = (f'A senha deve ter letra MAIÚSCULA, minuscula, número e caractere')
    print(orient)

    senha = input( "Digite a senha que deseja inserir: ")
    return senha

    verificar = verificador(senha, senha_gerar)

def verificador(senha, senha_gerer):

    problema = []

    if len(senha, senha_gerer) < 8:
        problema.append('A senha deve ter no mínimo 8 caracteres')

    if not re.search(r'\d+', senha, senha_gerer):
        problema.append('A senha deve conter pelo menos um número')

    if not re.search(r'[A-Z]',senha, senha_gerer):
        problema.append('A senha deve conter pelo menos uma letra maiúscula')

    if not re.search(r'[a-z]', senha, senha_gerer):
        problema.append('A senha deve conter pelo menos uma letra minúscula')

    if not re.search(r'\W', senha, senha_gerer):
        problema.append('A senha deve conter pelo menos um caractere especial')

    if re.search(r'\s', senha, senha_gerer):
        problema.append('A senha não pode conter espaços em branco')

    return problema


    # else:
    #     print(f'Senha aprovada')

def gerador_senha():
    letras_min = string.ascii_lowercase
    letras_mai = string.ascii_uppercase
    numeros = string.digits
    caracteres = string.punctuation

    lt_min = random.choices(letras_min, k=3)
    lt_max = random.choices(letras_mai, k=3)
    num = random.choices(numeros, k=3)
    carac = random.choices(caracteres, k=3)

    senha_regex = lt_min + lt_max + num + carac

    embra = random.shuffle(senha_regex)
    senha_gerar = ''.join(embra)

    return senha_gerar