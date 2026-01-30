def mostrar_menu():
    print("\n=== CALCULADORA ===")
    print("1 - adição")
    print("2 - subtração")
    print("3 - multiplicação")
    print("4 - divisão")
    print("0 - sair")


def adicao(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        return "erro"
    return a / b


def main():
    while True:
        mostrar_menu()
        opcao = input("escolha uma opção: ")

        if opcao == "0":
            print("saindo...")
            break

        a = float(input("Digite o primeiro número: "))
        b = float(input("Digite o segundo número: "))

        if opcao == "1":
            print("Resultado:", adicao(a, b))
        elif opcao == "2":
            print("Resultado:", subtracao(a, b))
        elif opcao == "3":
            print("Resultado:", multiplicacao(a, b))
        elif opcao == "4":
            print("Resultado:", divisao(a, b))
            
        else:
            print("opção inválida!")


if __name__ == "__main__":
    main()
