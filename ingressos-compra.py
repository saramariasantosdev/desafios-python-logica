pista = 100
cadeira_superior = 200
cadeira_inferior = 300

menu = print(f'Ingressos:\n1 - Pista: {pista}\n2 - Cadeira Superior: {cadeira_superior}\n3 - Cadeira Inferior: {cadeira_inferior}\n4 - Sair')

while True:
    opcao = int(input('Informe qual ingresso deseja comprar ou digite 4 para sair: '))
    match opcao:
        case 1:
            if pista > 0:
                quantidade = int(input('Informe quantos ingressos deseja comprar: '))
                print('Ingresso para pista comprado com sucesso!')
                pista = pista - quantidade
            else:
                print('Ingresso indisponível')
        case 2:
            if cadeira_superior > 0:
                quantidade = int(input('Informe quantos ingressos deseja comprar: '))
                print('Ingresso para cadeira superior comprado com sucesso!')
                cadeira_superior = cadeira_superior - quantidade
            else:
                print('Ingresso indisponível')
        case 3:
            if cadeira_inferior > 0:
                quantidade = int(input('Informe quantos ingressos deseja comprar: '))
                print('Ingresso para cadeira inferior comprado com sucesso!')
                cadeira_inferior = cadeira_inferior - quantidade
            else:
                print('Ingresso indisponível!')
        case 4:
            print('Encerrando compra')
            break

menu = print(f'Ingressos:\n1 - Pista: {pista}\n2 - Cadeira Superior: {cadeira_superior}\n3 - Cadeira Inferior: {cadeira_inferior}')