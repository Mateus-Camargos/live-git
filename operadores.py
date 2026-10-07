
def sinais():
    print("Digite o número que representa a sua operação: ")
    print("1- Adição")
    print("2- Subtração")
    print("3- Multiplicação")
    print("4- Divisão")
    escolha = int(input("Digite o número: "))

    if escolha == 1:
        print("Você escolheu adição")
    elif escolha == 2:
        print("Você escolheu subtração")
    elif escolha == 3:
        print("Você escolheu multiplicação")
    elif escolha == 4:
        print("Você escoheu divisão")
    else:
        print("Valor inválido")

