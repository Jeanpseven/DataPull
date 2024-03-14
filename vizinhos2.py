import os
import platform

def clear():
    if platform.system() == "Windows":
        os.system("cls")
    elif platform.system() == "Linux":
        os.system("clear")
    else:
        os.system("clear")
    print("--------=DEDSEC=Wrench=--------")

R='\033[1;31m'
B='\033[1;34m'
C='\033[1;37m'
Y='\033[1;33m'
G='\033[1;32m'

code_info = C + '[' + Y + 'i' + C + '] '
code_details = C + '[' + G + '*' + C + '] '
code_result = C + '[' + G + '+' + C + '] '
code_error = C + '[' + R + '!' + C + '] '

def main():
    clear()
    print("\n" + code_info + "Vizinhos.")
    print(f'''
    {C}[{G}i{C}] Formas de operação:
    [{G}1{C}] Iniciar busca.
    [{G}2{C}] Voltar.
    [{G}3{C}] {R}Sair.{C}
    ''')
    tool = input(f'{C}[{G}+{C}] Selecione a forma de operação:{B} ')
    if tool == '1':
        iniciar_busca()
    elif tool == '2':
        clear()
        import consulta
        consulta.main()
    elif tool == '3':
        clear()
        print(f'\n{G}Somos uma legião.{C}\n')
        exit()
    else:
        clear()
        print(f'{C}[{R}-{C}] Seleção inválida.')
        main()

def iniciar_busca():
    nomes_vizinhos = []
    while True:
        nome_filtro = input(f'{C}[{G}*{C}] Informe um nome de vizinho (ou digite "sair" para encerrar):')
        if nome_filtro.lower() == 'sair':
            break
        
        if nome_filtro in nomes_vizinhos:
            print(f'{code_result} Nomes repetidos encontrados! Removendo duplicatas...')
            nomes_vizinhos = list(set(nomes_vizinhos))
            print(f'{code_result} Nomes únicos restantes:')
            for nome in nomes_vizinhos:
                print(f'{code_result} - {nome}')
            break
        
        nomes_vizinhos.append(nome_filtro)

main()
