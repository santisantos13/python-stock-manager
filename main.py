stock = [["Arroz", 20]]


def add_item():
    print("--------------------------")
    print("Adicionando item ao estoque")
    print("--------------------------")

    item = input("Item: ").capitalize()

    if not item:
        print("Item inválido.")
        return
    if item_exists(item):
        print("Produto já cadastrado.")
        return

    else:
        try:
            amount = int(input("Quantidade: "))

        except ValueError:
            invalid_quantity()
            return

        if amount <= 0:
            invalid_quantity()
            return

        else:
            print(f"{item} adicionado com sucesso.")
            stock.append([item, amount])


def item_exists(nome):
    for produto in stock:
        if produto[0] == nome:
            return True
    return False


def end_program():
    print("Encerrando programa...")
    print("Programa encerrado.")


def invalid_quantity():
    print("Digite uma quantidade válida")


def see_stock():
    if not stock:
        print("Estoque vazio.\nAdicione itens ao estoque.")
    else:
        for i in stock:
            print(f"{i[0]} - Quantidade: {i[1]}")


def remove_item():
    if not stock:
        print("Estoque vazio.\nNão é possível remover itens.")
    else:
        print("--------------------------")
        print("Removendo item do estoque")
        print("--------------------------")

        for i, item in enumerate(stock, start=1):
            print(f"{i} - {item[0]} - Quantidade: {item[1]}")

        try:
            print("\nQual item deseja remover?: ")
            print(f"Escolha o índice, ex: 1 = {stock[0]}")
            item_remove = int(input("\n: "))

            if 1 <= item_remove <= len(stock):
                stock.pop(item_remove - 1)
                for i, item in enumerate(stock, start=1):
                    print(f"{i} - {item[0]} - Quantidade: {item[1]}")
            else:
                print("Índice inválido!")

        except ValueError:
            print("Digite um indice válido.")


def search_item():
    if not stock:
        print("Estoque vazio.")
    else:
        print("--------------------------")
        print(" Buscando item do estoque ")
        print("--------------------------")

        requested_item = input("Item: ").capitalize()

        for produto in stock:

            if requested_item == produto[0]:
                print(f"{produto[0]} tem {produto[1]} unidades armazenadas.")
                return

        print(f"{requested_item} não está cadastrado.")
        return


def update_quantity():
    if not stock:
        print("Estoque vazio.")
    else:
        item = input("Produto: ").capitalize()

        for produto in stock:

            if item == produto[0]:
                print(f"{produto[0]} encontrado.")
                print(f"quantidade atual: {produto[1]}")
                try:
                    quantity = int(input("Nova quantidade: "))
                    if quantity < 0:
                        invalid_quantity()
                        return

                except ValueError:

                    invalid_quantity()
                    return
                produto[1] = quantity
                print(f"Quantidade de {item} atualizado para {quantity}.")
                return

        print(f"{item} não está cadastrado.")


while True:

    print("\n          Estoque         ")
    print("--------------------------")
    print(
        "1 - Ver estoque\n2 - Adicionar item \n3 - Remover item \n4 - Buscar item\n5 - Atualizar item\n0 - Sair"
    )
    print("--------------------------")
    try:
        option = int(input("Escolha uma opção: "))

    except ValueError:

        print("Digite uma opção válida.")
        try:
            continuing = input("Deseja continuar? [s] ou [n]: ").lower()
            if continuing.startswith("s"):
                continue
            else:
                end_program()
                break

        except ValueError:
            end_program()
            break

    if option == 0:
        end_program()
        break

    elif option == 1:
        see_stock()

    elif option == 2:
        add_item()

    elif option == 3:
        remove_item()

    elif option == 4:
        search_item()

    elif option == 5:
        update_quantity()

    else:
        print("\nEscolha um opção válida \n0, 1, 2, 3, 4 ou 5.")
