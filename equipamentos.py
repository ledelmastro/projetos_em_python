# TODO: Crie uma Lista 'itens' para armazenar os equipamentos:
equipamentos = list()

# TODO: Crie um loop para solicita os itens ao usuário:
for i in range (3):
    itens = str(input())
# TODO: Adicione o item à lista "itens":
    equipamentos.append(itens)
# Exibe a lista de itens

for itens in equipamentos:
    print(f"- {(itens)}")


