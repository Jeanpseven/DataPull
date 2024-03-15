#Snuking/Somos uma legião. 2021 ©

import requests, time
import os
import platform
try:
   import requests
   import bs4
   import html5lib
   import phonenumbers
   import argparse
   import urllib3
   import colorama
except:
   os.system("python3 -m pip install --upgrade pip")
   os.system("pip install -r requirements.txt")
   clear()
   print(code_result + "Instalado com sucesso.\n")
   main()

version = "2.0"

# Definindo constantes de cores
R = '\033[1;31m'  # Vermelho
B = '\033[1;34m'  # Azul
C = '\033[1;37m'  # Cinza
Y = '\033[1;33m'  # Amarelo
G = '\033[1;32m'  # Verde
RT = '\033[;0m'   # Reset

def clear():
   print("-------DEDSEC Wrench-------")

def listar_scripts():
    scripts = [file for file in os.listdir() if file.endswith('.py')]
    return scripts

def main():
    clear()
    v = "1.0.3"
    print(f'''{G}
\n
.----.______
|           |
|    ___________
|   /          /
|  /          /
| /          /
|/__________/ {v}
{C}
 ''')
    print(f"{Y}Atual: {version}{C}")

    print("\n" + code_info + "Menu.")

    print(f"{C}[{G}i{C}] Scripts disponíveis:")
    scripts = listar_scripts()
    for i, script in enumerate(scripts, 1):
        print(f"[{G}{i}{C}] {script}")

    print(f'''
[{G}44{C}] Atualizar.
[{G}55{C}] Novidades.
[{G}66{C}] Ajuda.
[{G}00{C}] {R}Sair.{C}
''')
    tool=input(f'{C}[{G}+{C}] Selecione o script pelo número correspondente:{B} ')
    if tool.isdigit():
        tool = int(tool)
        if 1 <= tool <= len(scripts):
            clear()
            script_name = scripts[tool - 1]
            exec(f"import {script_name[:-3]}")
            eval(f"{script_name[:-3]}.main()")
        else:
            clear()
            print(f'{C}[{R}-{C}] Seleção inválida.')
            time.sleep(0.2)
            main()
    elif tool == "44":
       print(code_result + "Abrindo o tutorial de como atualizar no YouTube...")
       time.sleep(2)
       youtube()
       main()
    elif tool == "55":
       import novidades
       novidades.main()
    elif tool == "66":
       import ajuda
       ajuda.main()
    elif tool == "00":
       clear()
       print(f'\n{G}Somos uma legião.{C}\n')
       exit()
    else:
       clear()
       print(f'{C}[{R}-{C}] Seleção inválida.')
       time.sleep(0.2)
       main()

if __name__ == "__main__":
    main()