import os
import platform

def clear():
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
        salvar_nomes_vizinhos(cpf, nome_filtro)
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

def salvar_nomes_vizinhos(cpf, nome_filtro):
    nomes_arquivo = f"{cpf}_vizinhos.log"
    with open(nomes_arquivo, 'a+') as f:
        f.seek(0)  # Mover o cursor para o início do arquivo
        nomes_salvos = f.read().splitlines()
        
        if nome_filtro not in nomes_salvos:
            f.write(nome_filtro + '\n')
            print(f'{code_result} Nome salvo com sucesso!')
        else:
            print(f'{code_error} O nome "{nome_filtro}" já foi salvo anteriormente.')

main()
