numeros = [1,2,3,4,6,8,9,10,11,12,13,15,17,20,25,28]


def numeros_binarios(num,novonum):
    baixo = 0
    alto = len(num) -1

    while baixo <= alto:
        meio = (baixo + alto) // 2
        chute = num[meio]

        if chute == novonum:
            return True
        elif chute > novonum:
            alto = meio - 1
        else:
            baixo = meio +1

    return False

digitaNum = int(input("Digite um numero"))

if numeros_binarios(numeros, digitaNum):
    print("Número já existe")
else:
    print("Número disponível")