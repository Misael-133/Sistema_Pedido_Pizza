print("🍕Bem vindo a Pizzaria Misael Gonçalves de Lima🍕")
#Criação do cardápio que aparecera para o usuário
print(("-" *10),  "Cardápio", ("-" * 10))
print("Tamanho P: Pizza Salgada (PS) custa R$ - 30.00  e a Pizza Doce (PD) custa R$ - 34.00;")
print("Tamanho M: Pizza Salgada (PS) custa R$ - 45.00  e a Pizza Doce (PD) custa R$ - 48.00;")
print("Tamanho G: Pizza Salgada (PS) custa R$ - 60.00  e a Pizza Doce (PD) custa R$ - 66.00;")

#Criando acumulador
total_pedido = 0
while True:
    #Input do sabor
    sabor = input("\nEscolha o sabor (PS para Salgada, PD para Doce): ").upper()
    while sabor not in ['PS', 'PD']:
        print("\nSabor inválido. Tente novamente.")
        sabor = input("Escolha o sabor (PS para Salgada, PD para Doce): ").upper()
        continue

    # Input do tamanho
    tamanho = input("Escolha o tamanho (P, M, G): ").upper()
    while tamanho not in ['P', 'M', 'G']:
        print("\nTamanho inválido. Tente novamente.")
        tamanho = input("Escolha o tamanho (P, M, G): ").upper()
        continue


    #  Cálculo do valor com base no sabor e tamanho
    valor_item = 0
    if tamanho == 'P':
        if sabor == 'PS':
            valor_item = 30.00
        elif sabor == 'PD':
            valor_item = 34.00
    elif tamanho == 'M':
        if sabor == 'PS':
            valor_item = 45.00
        elif sabor == 'PD':
            valor_item = 48.00
    elif tamanho == 'G':
        if sabor == 'PS':
            valor_item = 60.00
        elif sabor == 'PD':
            valor_item = 66.00
    #Cálculo do valor do acumulativo
    total_pedido += valor_item
    # Print do item acicionado e valor]
    print(f"Você adicionou uma pizza {sabor} tamanho {tamanho} no valor de R$ {valor_item:.2f} ao seu pedido.")

    #  Perguntar se quer pedir mais alguma pizza
    mais_pedidos = input("\nDeseja pedir mais alguma coisa? (sim/não): ").lower()
    if mais_pedidos != 'sim':
        break

# Exibição do valor total do pedido
print(f"\nValor total do pedido: 💸R$ {total_pedido:.2f}")