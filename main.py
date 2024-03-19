from typing import List, Dict


def add_contact(contacts: List[Dict], new_contact: Dict) -> None:
    contacts.append({
        **new_contact,
        "favorite": False
        })
    print("Novo contato adicionado!\n")

    return


def view_contacts() -> None:
    print("\nLista de contatos:")
    print(40*"-")
    for index, contact in enumerate(contacts, start=1):
        favorite = "★" if contact["favorite"] else " "
        name = contact["name"]
        number = contact["number"]
        email = f" - {contact["email"]}" if contact["email"] else ""
        print(f"{index}| [{favorite}] - {name} - {number}{email}")
    print(40*"-")

    return


def update_contact(contacts: List[Dict], index: int, data: Dict) -> None:
    contact_index = index - 1

    if contact_index < 0 or index > len(contacts):
        return print(f"Contato {index} não encontrado!")

    contacts[contact_index]["name"] = data["name"]
    contacts[contact_index]["number"] = data["number"]
    contacts[contact_index]["email"] = data["email"]

    print(37*"-", f"\n| Contato {index} atualizado com sucesso! |")
    print(37*"-")

    return


def favorite_contact(contacts: List[Dict], index: int) -> None:
    contact_index = index - 1

    if contact_index < 0 or index > len(contacts):
        return print(f"Contato {index} não encontrado!")

    contacts[contact_index]["favorite"] = (
        not contacts[contact_index]["favorite"]
        )

    return


def view_favorite_contacts() -> None:
    print("\nLista de favoritos:")
    print(40*"-")
    for index, contact in enumerate(contacts, start=1):
        if contact["favorite"]:
            name = contact["name"]
            number = contact["number"]
            email = f" - {contact["email"]}" if contact["email"] else ""
            print(f"{index}| [★] - {name} - {number}{email}")
    print(40*"-")

    return


def delete_contact(contacts: List[Dict], index: int) -> None:
    contact_index = index - 1

    if contact_index < 0 or index > len(contacts):
        return print(f"Contato {index} não encontrado!")

    contacts.pop(contact_index)
    print(f"Contato {index} deletado com sucesso!")

    return


contacts = []

while True:
    print("==================================")
    print("PhoneBook:")
    print("1. Adicionar novo contato")
    print("2. Ver lista de contatos")
    print("3. Editar contato")
    print("4. Marcar/desmarcar como favorito")
    print("5. Ver lista de favoritos")
    print("6. Apagar contato")
    print("7. Sair")
    print("==================================")

    try:
        option = input("Escolha uma opção: ")

        if option == "1":
            name = input("Digite o nome: ")
            number = input("Digite o número: ")
            email = input("Digite o email(opcional): ")

            new_contact = {
                "name": name,
                "number": number,
                "email": email,
            }

            add_contact(contacts, new_contact)

        elif option == "2":
            view_contacts()

        elif option == "3":
            view_contacts()
            index = int(input("Digite o índice do contato: "))
            name = input("Digite o nome: ")
            number = input("Digite o número: ")
            email = input("Digite o email: ")

            payload = {
                "name": name,
                "number": number,
                "email": email,
            }

            update_contact(contacts, index, payload)

        elif option == "4":
            view_contacts()
            index = int(input("Digite o index do contato: "))
            favorite_contact(contacts, index)

        elif option == "5":
            view_favorite_contacts()

        elif option == "6":
            view_contacts()
            index = int(input("Digite o índice do contato: "))
            delete_contact(contacts, index)

        elif option == "7":
            break

    except Exception as e:
        print(f"Erro: {e}")
