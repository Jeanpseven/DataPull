#Snuking/Somos uma legião. 2021 ©

import os, requests, time
import platform
import ipadress

def clear():
   if platform.system() == "Windows":
      os.system("cls")
   elif platform.system() == "Linux":
      os.system("clear")
   else:
       os.system("clear")

R='\033[1;31m'; B='\033[1;34m'; C='\033[1;37m'; Y='\033[1;33m'; G='\033[1;32m'; RT='\033[;0m'

code_info = C + '[' + Y + 'i' + C + '] '
code_details = C + '[' + Y + '*' + C + '] '
code_result = C + '[' + G + '+' + C + '] '
code_error = C + '[' + R + '!' + C + '] '

def main():
  clear()
  api = requests.get("https://ipapi.co/json")
  resultado = api.json()
  ip = resultado['ip']
  print("\n" + code_info + "IP.")
  print(code_details + f"Seu IP: {ip}")
  print(f'''
{C}[{G}i{C}] Formas de operação: 

[{G}1{C}] Consultar meu IP.
[{G}2{C}] Consultar IP.
[{G}3{C}] Localizar.
[{G}4{C}] Voltar.
[{G}5{C}] {R}Sair.{C}
''')
  tool = input(f'{C}[{G}+{C}] Selecione a forma de operação:{B} ')
  if tool == "1":
     consultar(ip)
  elif tool == "2":
     ip=input(f'{C}[{G}*{C}] Informe o IP a ser consultado (COM pontos): {B}')
     consultar(ip)
  elif tool == "3":
     ip=input(f'{C}[{G}*{C}] Informe o IP a ser consultado (COM pontos): {B}')
     clear()
     localizar(ip)
  elif tool == "4":
     import consulta
     consulta.main()
  elif tool == "5":
      clear()
      print(f"\n{G}Somos uma legião.{C}\n")
      exit()
  else:
     clear()
     print(f'{C}[{R}-{C}] Seleção inválida.')
     time.sleep(0.2)
     main()


def again():
  opt = input("\n" + f'{C}[{G}+{C}] Deseja realizar uma nova consulta?[{G}s{C}/{R}n{C}]: ')
  if opt == "s":
      clear()
      main()
  elif opt == "n":
      print(f"\n{G}Somos uma legião.{C}\n")
      exit()
  else:
      clear()
      print(f'{C}[{R}-{C}] Seleção inválida.')
      time.sleep(0.2)
      exit()

#Snuking/Somos uma legião. 2021 ©

def maps(ip):
  opt = input("\n" + f'{C}[{G}+{C}] Deseja localizar no {Y}Google Maps{C}?[{G}s{C}/{R}n{C}]: ')
  if opt == "s":
      localizar(ip)
  elif opt == "n":
      again()
  else:
      print(f'{C}[{R}-{C}] Seleção inválida.')
      time.sleep(0.2)
      exit()

#Snuking/Somos uma legião. 2021 ©

def consultar(ip):
  try:
    ip_address = ipaddress.ip_address(ip)
  except ipaddress.AddressValueError:
    print(f"{code_error} Invalid IP address.")
    return

  clear()
  api = requests.get(f"https://ipapi.co/{ip}/json")
  if api.status_code != 200:
    print(f"{code_error} Error fetching information for IP address {ip}.")
    return

  resultado = api.json()
  print(f"{code_info} IP address {ip} information:")
  print(f"{code_details} IP address: {resultado['ip']}")
  print(f"{code_details} City: {resultado['city']}")
  print(f"{code_details} Region: {resultado['region']}")
  print(f"{code_details} Country: {resultado['country_name']}")
  print(f"{code_details} Country code: {resultado['country_code']}")
  print(f"{code_details} Country code ISO3: {resultado['country_code_iso3']}")
  print(f"{code_details} Country population: {resultado['country_population']}")
  print(f"{code_details} Country currency: {resultado['currency']}")
  print(f"{code_details} Country currency name: {resultado['currency_name']}")
  print(f"{code_details} Country area: {resultado['country_area']}")
  print(f"{code_details} Country TLD: {resultado['country_tld']}")
  print(f"{code_details} Country calling code: {resultado['country_calling_code']}")
  print(f"{code_details} Region code: {resultado['region_code']}")
  print(f"{code_details} Postal code: {resultado['postal']}")
  print(f"{code_details} Continent code: {resultado['continent_code']}")
  print(f"{code_details} In EU: {resultado['in_eu']}")
  print(f"{code_details} Timezone: {resultado['timezone']}")
  print(f"{code_details} Latitude: {resultado['latitude']}")
  print(f"{code_details} Longitude: {resultado['longitude']}")
  print(f"{code_details} UTC offset: {resultado['utc_offset']}")
  print(f"{code_details} Languages: {resultado['languages']}")
  print(f"{code_details} ASN: {resultado['asn']}")
  print(f"{code_details} ORG: {resultado['org']}")
  print(f"{code_details} Version: {resultado['version']}")
  maps(ip)


def localizar(ip):
  api = requests.get("https://ipapi.co/json")
  resultado = api.json()
  print(code_info + "Google Maps")
  print(code_info + "Gerando URL...")
  time.sleep(0.5)
  print ('\n' + code_result + f'Google Maps: {Y}' + 'https://www.google.com/maps/place/' + f"{resultado['latitude']}" + '+' + f"{resultado['longitude']}")
  again()


main()

#Snuking/Somos uma legião. 2021 ©
