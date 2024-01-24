import re

def validar_cpf(cpf: str):
    # Remove caracteres não numéricos do CPF
    cpf = ''.join(filter(str.isdigit, cpf))

    # Verifica se o CPF tem 11 dígitos
    if len(cpf) != 11:
        return False

    # Verifica se todos os dígitos são iguais (caso contrário, não seria um CPF válido)
    if cpf == cpf[0] * 11:
        return False

    # Calcula o primeiro dígito verificador
    soma = 0
    for i in range(9):
        soma += int(cpf[i]) * (10 - i)
    resto = soma % 11
    if resto < 2:
        digito1 = 0
    else:
        digito1 = 11 - resto

    # Verifica o primeiro dígito verificador
    if digito1 != int(cpf[9]):
        return False

    # Calcula o segundo dígito verificador
    soma = 0
    for i in range(10):
        soma += int(cpf[i]) * (11 - i)
    resto = soma % 11
    if resto < 2:
        digito2 = 0
    else:
        digito2 = 11 - resto

    # Verifica o segundo dígito verificador
    if digito2 != int(cpf[10]):
        return False

    # Se todas as verificações passarem, o CPF é válido
    return True

def validar_celular(numero: str):
    # Defina o padrão regex para números de telefone fixo e celular no Brasil
    padrao_celular = re.compile(r'^\(\d{2}\) 9\s?\d{4}-\d{4}$')

    # Use o método match para verificar se o número corresponde a um dos padrões
    correspondencia_celular = re.match(padrao_celular, numero)

    # Se houver correspondência com qualquer um dos padrões, o número é válido
    if correspondencia_celular:
        return True
    else:
        return False