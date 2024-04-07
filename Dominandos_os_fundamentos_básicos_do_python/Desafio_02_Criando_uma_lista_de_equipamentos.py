# TODO: Crie uma Lista 'itens' para armazenar os equipamentos:
# TODO: Crie um loop para solicita os itens ao usuário:
# TODO: Solicite o item e armazena na variável "item":
# TODO: Adicione o item à lista "itens":


# Exibe a lista de itens
itens = []
cont = 0
while cont < 3:
    #Solicita a entrada do item
    item = input("Digite o nome do item:" )
    #Adiciona o item na lista 'itens'
    itens.append(item)
    cont += 1

print("Lista de Equipamentos:")  
for item in itens:
    # Loop que percorre cada item na lista "itens"
    print(f"- {item}")