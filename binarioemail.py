emails_cadastrados = [
    "ana@email.com",
    "bruno@email.com",
    "carla@email.com",
    "daniel@email.com",
    "felipe@email.com",
    "joao@email.com",
    "maria@email.com"
]

def cadastro_binario(email, emailnovo):
    baixo = 0
    alto = len(emails_cadastrados) -1

    while baixo <= alto:
        meio = (baixo + alto) //2
        chute = email[meio]

        if chute == emailnovo:
            return True
        elif chute > emailnovo:
            alto = meio -1
        else:
            baixo = meio +1
    return False

novo_email = str(input("Digite seu email"))

if cadastro_binario(emails_cadastrados,novo_email):
    print("email já cadastrado")
else:
    print("email disponivel")