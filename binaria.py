ids_cadastrados = [
    1, 2, 3,4, 9, 14, 25, 30, 40
]

def cadastro_binaria(ids, id_usuario):
    baixo = 0
    alto = len(ids) -1

    while baixo <= alto:
        meio = (baixo + alto) //2
        chute = ids[meio]

        if chute == id_usuario:
            return True
        elif chute > id_usuario:
            alto = meio -1
        else:
            baixo = meio +1

    return False

novo_id = int(input("Digite seu ID "))

if cadastro_binaria(ids_cadastrados,novo_id):
    print("Já possui cadastro")
else:
    print("ID disponível")