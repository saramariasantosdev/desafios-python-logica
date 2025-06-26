quantidade_1 = 0
quantidade_2 = 0
menu = print('Produtos:\n1 - Caderno\n2 - Livro\n3 - Total')

while True:
    opcao = int(input('Qual produto você deseja comprar? '))
    match opcao:
        case 1:
            preco_unitario_1 = 12.99
            if opcao == 1:
                quantidade_1 += 1 
            total_1 = preco_unitario_1 * quantidade_1
        case 2:
            preco_unitario_2 = 24.90
            if opcao == 2:
               quantidade_2 += 1
            total_2 = preco_unitario_2 * quantidade_2
        case 3:
            total = total_1 + total_2
            print(f'Total: {total:.2f}')
            break
