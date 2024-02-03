# Lista de valores
import os

lista = []
while True:
    print('Selecionar uma opção')
    opcao = input('[i]nserir [a]pagar [l]istar [s]sair: ')
    
    if opcao == 'i':
        os.system('cls')
        valor = input('Valor: ')
        lista.append(valor)
    elif opcao == 'a':
        indice_str = input('Escolha o índice para apagar: ')
        
        try:
            indice = int[indice]
            del lista[indice]
        except ValueError:
            print('Por favor digite número inteiro')
        except IndexError:
            print('índice não existe na lista')
        except Exception:
            print('Erro desconhecido')
    elif opcao == 'l':
        os.system('cls')

        if len(lista) == 0:
            print('Nada a listar')

        for i, valor in enumerate(lista):
            print(i, valor)
    elif opcao == 's':
        break
    else:
        print('Por favor, escolha i, a ou l.')
