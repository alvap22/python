
lista_de_compras = []

while True:
    print("\nOpções:")
    print("1 - Adicionar Item")
    print("2 - Remover Item")
    print("3 - Editar Item")
    print("4 - Listar Itens")
    print("5 - Sair")

    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        item = input("Digite o item que deseja adicionar: ")
        lista_de_compras.append(item)
        print("{} foi adicionado à lista de compras.".format(item))
    elif escolha == "2":
        item = input("Digite o item que deseja remover: ")
        if item in lista_de_compras:
            lista_de_compras.remove(item)
            print("{} foi removido da lista de compras.".format(item))
        else:
            print("{} não foi encontrado na lista de compras.".format(item))
    elif escolha == "3":
        item_antigo = input("Digite o item que deseja editar: ")
        item_novo = input("Digite o novo valor para o item: ")
        if item_antigo in lista_de_compras:
            index = lista_de_compras.index(item_antigo)
            lista_de_compras[index] = item_novo
            print("{} foi alterado para {} na lista de compras.".format(item_antigo, item_novo))
        else:
            print("{} não foi encontrado na lista de compras.".format(item_antigo))
    elif escolha == "4":
        if lista_de_compras:
            print("Lista de Compras:")
            for item in lista_de_compras:
                print(item)
        else:
            print("A lista de compras está vazia.")
    elif escolha == "5":
        break
    else:
        print("Opção inválida. Tente novamente.")
