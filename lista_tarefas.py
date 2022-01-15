import json
import time
lista = []

while True:
    print('Digite 0 para sair e salvar suas tarefas em um arquivo.json.\n')
    print('Digite 1 para adicionar tarefa.\n')
    print('Digite 2 para listar tarefas.\n')
    print('Digite 3 para desfazer ultima tarefa adicionada.\n')
    op = int(input('Digite um numero de 0 a 3'))
    if op == 1:
        adiciona = input('Adicione uma tarrefa a lista')
        lista.append(adiciona)
        print(f'A tarefa {adiciona} foi adicionada ')
        time.sleep(1)
    elif op == 2:
        print(f'Tarefas listadas até o momento: {lista}')
        time.sleep(1)
    elif op == 3:
        ctz = input('Tem certeza que deseja remover a tarefa?.S/N')
        if ctz == 's' or 'S':
            lista.pop()
            print('Tarefa removida')
            time.sleep(1)
    elif op == 0:
        print('Obrigado por usar nosso programa')
        lista_json = json.dumps(lista, indent=True)

        with open('tarefas.json', 'w+') as file:
            file.write(lista_json)

        time.sleep(1)
        break
    else:
        print('Digite um numero inteiro de 0 a 3.')
        break
