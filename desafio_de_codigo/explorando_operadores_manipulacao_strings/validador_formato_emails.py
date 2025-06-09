# definindo a função que valida o e-mail
def validar_email(email):
    # verifica se contém exatamente um "@"
    if email.count("@") != 1:
        return "E-mail inválido"

    # verifica se começa ou termina com "@"
    if email.startswith("@") or email.endswith("@"):
        return "E-mail inválido"

    # verifica se contém espaços em branco
    if email.count(" ") != 0:
        return "E-mail inválido"

    # verifica se o domínio é válido
    usuario, dominio = email.split("@")

    if "." not in dominio:
        return "E-mail inválido"

    return "E-mail válido"

# entrada do usuário
email = input().strip()
print(validar_email(email))
