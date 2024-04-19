#!/usr/bin/python3
import requests,argparse,time

################################################################################
# Titulo    : Directory Finder.                                                #
# Versao    : 2.0                                                              #
# Data      : 18/04/2024                                                       #
# Tested on : Linux/Windows10                                                  #
# created by: Charli Castelli.                                                 #
# -----------------------------------------------------------------------------#
# Descrição:                                                                   #
#   Esse programa busca por caminhos, arquivos e subdominios.                  #
#   User-Agent personalizado.                                                  #
# -----------------------------------------------------------------------------#
# Nota da Versão:                                                              #
# Adicionado busca por subdominos.                                             #
################################################################################

#Constantes cores
RED   = "\033[1;31m"  
RESET = "\033[0;0m"
BOLD    = "\033[;1m"
BLUE = "\033[34m"
GREEN = "\033[32m"
YELLOW = "\033[33m"

#Icones
iconSuccess = BOLD + BLUE + "[+]" + RESET
iconSuccessGreen = GREEN + "[+]" + RESET
iconSuccessYellow = YELLOW + "[+]" + RESET
iconError = BOLD + RED + "[-]" + RESET
iconHelp = BLUE + "[?]" + RESET

#Menssagens
close = "\n\n🛑 Execução interrompida pelo usuário!"
stop = f"{iconHelp} Para interromper a execução, pressione Ctrl + C"
head = "-"*53

#User-Agent personalizado
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
}

banner = YELLOW + """
 ____  _               _                   
|  _ \(_)_ __ ___  ___| |_ ___  _ __ _   _ 
| | | | | '__/ _ \/ __| __/ _ \| '__| | | |
| |_| | | | |  __/ (__| || (_) | |  | |_| |
|____/|_|_|  \___|\___|\__\___/|_|   \__, |
                                     |___/ 
 _____ _           _
|  ___(_)_ __   __| | ___ _ __ 
| |_  | | '_ \ / _` |/ _ \ '__|
|  _| | | | | | (_| |  __/ |   
|_|   |_|_| |_|\__,_|\___|_|   V.2.0
""" + RESET

print(banner)

try:
    def scan_directories(domain, wordlist_file, file_extension=None, delay=None):
        text = f"{iconSuccessGreen} Iniciando varredura no Host: http://{domain}"
        print(f"{stop}")
        time.sleep(2)
        print(f"{text}\n\n")
        time.sleep(2)

        print(head)
        print(BOLD + f"Buscando diretórios..." + RESET)
        print(head)
        directory_found = False
        if wordlist_file is not None:
            with open(wordlist_file, "r") as file:
                for line in file:
                    directory = line.strip()
                    url = f"{domain}/{directory}"
                    response = requests.head(f"http://{url}", headers=headers, timeout=5)
                    if response.status_code == 200:
                        print(f"{iconSuccessGreen} http://{url: <35}",end="")
                        print(BOLD + GREEN + f" [{response.status_code}]" + RESET)
                        directory_found = True
                    elif response.status_code > 399 and response.status_code < 500 and response.status_code != 404:
                        print(f"{iconSuccessYellow} http://{url: <35}",end="")
                        print(BOLD + YELLOW + f" [{response.status_code}]" + RESET)
                        directory_found = True
                    elif response.status_code != 404:
                        print(f"{iconSuccess} http://{url: <35}",end="")
                        print(BOLD + BLUE + f" [{response.status_code}]" + RESET)
                        directory_found = True
                    if delay:
                        time.sleep(delay)
        if not directory_found:
            print(f"{iconError} Nenhum caminho foi encontrado.")
        if file_extension:
            scan_files(domain, wordlist_file, file_extension, delay)

    def scan_files(domain, wordlist_file, file_extension, delay):
        print()
        print(head)
        print(BOLD + f"Buscando por arquivos [{file_extension}]..." + RESET)
        print(head)
        directory_found = False
        if wordlist_file is not None:
            with open(wordlist_file, "r") as file:
                for line in file:
                    directory = line.strip()
                    url = f"{domain}/{directory}{file_extension}"
                    response = requests.head(f"http://{url}", headers=headers, timeout=5)
                    if response.status_code == 200:
                        print(f"{iconSuccessGreen} http://{url: <35}",end="")
                        print(BOLD + GREEN + f" [{response.status_code}]" + RESET)
                        directory_found = True
                    elif response.status_code > 399 and response.status_code < 500 and response.status_code != 404:
                        print(f"{iconSuccessYellow} http://{url: <35}",end="")
                        print(BOLD + YELLOW + f" [{response.status_code}]" + RESET)
                        directory_found = True
                    elif response.status_code != 404:
                        print(f"{iconSuccess} http://{url: <35}",end="")
                        print(BOLD + BLUE + f" [{response.status_code}]" + RESET)
                        directory_found = True
                    if delay:
                        time.sleep(delay)
        if not directory_found:
            print(f"{iconError} Nenhum arquivo <{file_extension}> encontrado.")

    def scan_subdomains(domain, wordlist_file, delay=None):
        print()
        print(head)
        print(BOLD + f"Buscando por subdominios..." + RESET)
        print(head)
        directory_found = False
        if wordlist_file is not None:
            with open(wordlist_file, "r") as file:
                for line in file:
                    directory = line.strip()
                    url = f"{directory}.{domain}"
                    try:
                        response = requests.get(f"http://{url}", headers=headers, timeout=5)
                        if response.status_code == 200:
                            print(f"{iconSuccessGreen} http://{url: <35}",end="")
                            print(BOLD + GREEN + f" [{response.status_code}]" + RESET)
                            directory_found = True
                        elif response.status_code > 399 and response.status_code < 500 and response.status_code != 404:
                            print(f"{iconSuccessYellow} http://{url: <35}",end="")
                            print(BOLD + YELLOW + f" [{response.status_code}]" + RESET)
                            directory_found = True
                        elif response.status_code != 404:
                            print(f"{iconSuccess} http://{url: <35}",end="")
                            print(BOLD + BLUE + f" [{response.status_code}]" + RESET)
                            directory_found = True
                        if delay:
                            time.sleep(delay)
                    except requests.exceptions.RequestException:
                        pass
         
        if not directory_found:
            print(f"{iconError} Nenhum subdominio foi encontrado.")

    def validate_file_extension(value):
        if not value.startswith('.'):
            raise argparse.ArgumentTypeError("A extensão do arquivo deve começar com um ponto '.'")
        return value
            
    class CustomHelpParser(argparse.ArgumentParser):
        def print_help(self):
            space1 = " "*7
            space2 = " "*7
            space3 = " "*6
            space4 = " "*5
            space5 = " "*3
            space6 = " "*7
            space7 = " "*2
            text1 = f"-h,--help {space1} No {space2} Help"
            text2 = f"-d,--domain {space4} Yes {space3} Include domain"
            text3 = f"-w,--wordlist {space5} Yes {space3} Include wordlist.txt"
            text4 = f"-f,--file {space6} No {space2} Search for files, enter extension <.txt> or <.php>"
            text5 = f"-t,--delay {space3} No {space2} Time between requests"
            text6 = f"-s,--subdomain {space7} No {space2} Search for subdomain"

            print(BOLD + f'{"Option":<17} {"Required":<10} {"Meaning":<10}' + RESET)
            custom_help_message = f"{text1}\n{text2}\n{text3}\n{text4}\n{text5}\n{text6}\n"

            print(custom_help_message)

        def error(self, message):
            #self.print_help()
            msg1 = "python3 dfinder.py -d <domain> -w <wordlist.txt> -f <.php> -t <time> --subdomain"
            msg2 = "python3 dfinder.py -h"
            self.exit(2, f"\n{iconError} Exemplo de uso da ferramenta:\n{msg1}\n{msg2}\n\n")

    if __name__ == "__main__":
        parser = CustomHelpParser(description="Descubra diretórios em páginas web usando uma wordlist.")
        parser.add_argument("-d", "--domain", help="O domínio da página web para escanear.")
        parser.add_argument("-w", "--wordlist", help="O arquivo com a lista de diretórios potenciais.")
        parser.add_argument("-f", "--file", type=validate_file_extension, help="A extensão do arquivo para procurar após a busca por diretórios.")
        parser.add_argument("-t", "--delay", type=float, help="Adiciona tempo entre as requisições.")
        parser.add_argument("-s", "--subdomain", action='store_true', help="Realizar uma busca por subdomínios.")
        args = parser.parse_args()

        if args.domain is None or args.wordlist is None:
            parser.error("Os argumentos domain e wordlist são obrigatórios")
        else:
            scan_directories(args.domain, args.wordlist, args.file, args.delay)
            if args.subdomain:
                scan_subdomains(args.domain, args.wordlist, args.delay)

except KeyboardInterrupt:
    print(close) # Se o usuário precionar Ctrl + c vai interromper a execução do script.

print()
print()