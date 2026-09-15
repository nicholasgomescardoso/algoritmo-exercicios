# Atividade 03 - Entrada de dados do usuario
print()
nome_cliente = input('Digite o nome do cliente: ')
produto = input('Digite o nome do produto: ')
preco = float(input('Digite o preço unitario do produto (R$): '))
quantidade = int(input('Digite a quantidade do(s) produto: '))
desconto = float(input('Digite o valor do desconto em percentual (%): '))
print()

subtotal = preco * quantidade
valor_desconto = subtotal * (desconto / 100)
total = subtotal - valor_desconto
media = total / quantidade

print(f'Nome do cliente: {nome_cliente}')
print(f'Produto: {produto}')
print(f'Preço unitario: R$ {preco:.2f}')
print(f'Quantidade: {quantidade}')
print(f'Subtotal: R$ {subtotal:.2f}')
print(f'Desconto: R$ {valor_desconto:.2f}')
print(f'Total: R$ {total:.2f}')
print(f'Média do valor final por produto: R$ {media:.2f}')