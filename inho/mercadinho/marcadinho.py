#dicionário de produtos
produtos = {
    "Cartela de Ovos": 10.49,
    "Leite": 6.99,
    "Macarrão": 4.99,
    "Café": 65.99,
    "Arroz": 16.99,
    "Sobrecoxa": 22.49
}

#carrinho = lista de tuplas -> nome, preco, quantidade e subtotal
carrinho: list[tuple[str, float, int, float]] = []

#adicionar itens
def add_item(nome: str, quant: int):
    preco = produtos.get(nome)
    if preco is None:
        raise ValueError(f"Produto não encontrado: {nome}")
    subtotal = preco * quant
    return (nome, preco, quant, subtotal)

def listar_produtos():
    print("\n=== Produtos Disponíveis ===")
    for nome, preco in produtos.items():
        print(f"- {nome}: R${preco:.2f}")

def ver_carrinho():
    if not carrinho:
        print("\nCarrinho vazio.")
        return
    print("\n=== Carrinho ===")
    for item in carrinho:
        print(item)
    total = calcular_total()
    print(f"\nTOTAL: {total:.2f}")

def calcular_total():
    return round(sum(sub for (_, _, _, sub) in carrinho), 2)

def remover_do_carrinho(nome: str):
    for i, (n, _, _, _) in enumerate(carrinho):
        if n == nome:
            carrinho.pop(i)
            return True
    return False

while True:
    print("\n=== MENU ===")
    print("1) Listar produtos disponíveis")
    print("2) Adicionar produto ao carrinho")
    print("3) Remover produto do carrinho")
    print("4) Ver carrinho")
    print("5) Finalizar compra")

    opn = input("Escolha uma opção: ")

    if opn == "1":
        listar_produtos()

    elif opn == "2":
        nome = input("Digite o nome do produto: ")
        if nome not in produtos:
            print("Produto não encontrado. Veja as opções no item 1 do menu.")
            continue
        try:
            quant = int(input("Quantidade: "))
            if quant <= 0:
                print("Quantiddade deve ser > 0.")
                continue
        except ValueError:
            print("Quantidade inválida (use número inteiro).")
            continue

        item = add_item(nome, quant)
        carrinho.append(item)
        print("Item adicionado!")

    elif opn == "3":
        if not carrinho:
            print("Carrinho já está vazio.")
            continue
        nome = input("Digite o nome do produto: ")
        if remover_do_carrinho(nome):
            print("Produto removido do carrinho.")
        else:
            print("Esse produto não está no carrinho.")

    elif opn == "4":
        ver_carrinho()

    elif opn == "5":
        ver_carrinho()
        print("Compra finalizada. Volte sempre!")
        break

    else:
        print("Opção inválida. Tente novamente.")