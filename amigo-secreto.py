import random
amigos = []

for i in range(5):
    amigos_secretos = input('Digite um amigo: ')
    amigos.append(amigos_secretos)

embaralhados = amigos[:]
random.shuffle(embaralhados)

for n in range(len(amigos)):
    pares = f'{amigos[n]}' + ' -> ' + f'{embaralhados[n-1]}'
    print(pares)
    