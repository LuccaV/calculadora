def mostrar_menu():
    print("\n=== CALCULADORA ===")
    print("1 - adição")
    print("2 - subtração")
    print("3 - multiplicação")
    print("4 - divisão")
    print("0 - sair")


def main():
    while True:
        mostrar_menu()
        opcao = input("escolha uma opção: ")

        if opcao == "0":
            print("saindo...")
            break
        else:
            print("opção inválida!")


if __name__ == "__main__":
    main()
