from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
import os
from handle import *

def default_case():
    print('Opção inválida')

def main():
    menu_completer = WordCompleter(['reta', 'circulo', 'sair', 'triangulo', 'quadrado', 'trapezio', 'retangulo','lista', 'ponto', 'help'], ignore_case=True)
    menu_actions = {
        'ponto': handle_ponto,
        'reta': handle_reta,
        'circulo': handle_circulo,
        'triangulo': handle_triangulo,
        'quadrado': handle_quadrado,
        'retangulo': handle_retangulo,
        'trapezio': handle_trapezio,
        'help': handle_help,
        'lista': handle_lista,
        'sair': handle_sair
    }
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Bem-vindo ao sistema de criação de formas geométricas!')
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Criar formas geométricas:')
        print('Digite: "help" para ver as opções')
        print('Ver formas geométricas criadas: (digite: "lista")')
        print('Obs: As unidades de medida desse programa estão em unidades quadráticas')
        user_choice = prompt('Sair: (digite: "sair")\n', completer=menu_completer)
        action = menu_actions.get(user_choice, default_case)
        action()

if __name__ == '__main__':
    main()