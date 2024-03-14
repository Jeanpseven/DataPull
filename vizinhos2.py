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
    print("----------=----------")

R='\033[1;31m'
B='\033[1;34m'
C='\033[1;37m'
Y='\033[1;33m'
G='\033[1;32m'
RT='\033[;0m'

code_info = C + '[' + Y + 'i' + C + '] '
code_details = C + '[' + G + '*' + C + '] '
code_result = C + '[' + G + '+' + C + '] '
code_error = C + '[' + R + '!' + C + '] '

clear()

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
        time.sleep(0.2)
        main()

def iniciar_busca():
    nomes_vizinhos = []
    cpf = input(f'{C}[{G}*{C}] Informe o CPF a ser consultado (sem pontos ou traços): {B}')
    nomes = requests.get(f"https://tudosobretodos.info/{cpf}", headers=header).text
    viz = re.findall(r"[A-Z]+ [A-Z ]+", nomes)
    clear()
    print("\n" + code_info + f"Vizinhos encontrados:{B}\n")
    print(viz)
    salvar_nomes_log(viz)

def salvar_nomes_log(nomes):
    with open('vizinhos.log', 'a+') as f:
        f.seek(0)  # Mover o cursor para o início do arquivo
        nomes_salvos = f.read().splitlines()

        for nome in nomes:
            if nome not in nomes_salvos:
                f.write(nome + '\n')
                print(f'{code_result} Nome "{nome}" salvo com sucesso!')

main()
