import requests
import time
import re
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
    [{G}1{C}] Consultar CPF.
    [{G}2{C}] Voltar.
    [{G}3{C}] {R}Sair.{C}
    ''')
    tool = input(f'{C}[{G}+{C}] Selecione a forma de operação:{B} ')
    if tool == '1':
        cpf = input(f'{C}[{G}*{C}] Informe o CPF a ser consultado (sem espaço, sem ponto e sem traço):')
        cpf = cpf.replace(' ', '').replace('.', '').replace('-', '')  # Remover espaços, pontos e traços
        nome_filtro = input(f'{C}[{G}*{C}] Informe o nome a ser filtrado:')
        filtrar_por_nome(cpf, nome_filtro)
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
        time.sleep(0.2)
        main()

def filtrar_por_nome(cpf, nome_filtro):
    nomes = requests.get(f"https://tudosobretodos.info/{cpf}").text
    viz = re.findall(r"[A-Z][a-z]+ [A-Z][a-z]+", nomes)
    filtered_viz = [v for v in viz if nome_filtro.lower() in v.lower()]
    if filtered_viz:
        print(f'\n{code_result} Vizinhos encontrados:')
        for vizinho in filtered_viz:
            print(f'{code_result} - {vizinho}')
    else:
        print(f'{code_error} Nenhum vizinho encontrado com o nome "{nome_filtro}".')

main()
