while True:
    print("\nMenu:")
    print("[1] Olá")
    print("[2] Ajuda")
    print("[3] Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        print("Olá! Seja bem-vindo.")
    elif opcao == "2":
        print("Esta é a seção de ajuda. Escolha uma opção do menu.")
    elif opcao == "3":
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida, tente novamente.")