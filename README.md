## Directory Finder.
- Mensionei no exemplo a página http://businesscorp.com.br que usei no curso Pentest profissional da Desec Security.
- Esse programa busca por caminhos, arquivos e subdominios. Todos em uma unica execução ou apenas a opção que desejar.
  
### Exemplo de uso:
- `python3 dfinder.py -h` ou `python3 dfinder.py --help`
- `python3 dfinder.py -w lista.txt -u businesscorp.com.br -f .txt -s` (Busca por arquivos .txt e subdominios).
- `python3 dfinder.py -u businesscorp.com.br -w wordlist.txt -f .html -s -t 4` (Busca por arquivos .html e subdominios, com tempo de 4 segundos entre as requisições).


### `python3 dfinder.py --help`

![1](https://github.com/charlicastelli/dfinder/assets/80997263/30c90708-a687-47d7-9e89-7617507eeb9d)

### `python3 dfinder.py -u businesscorp.com.br -w lista.txt -s -d -f .txt,.php`

![2](https://github.com/charlicastelli/dfinder/assets/80997263/4fe1582b-4374-4ca6-bfcf-ea8c52cd155c)

### `python3 dfinder.py -u businesscorp.com.br -w lista.txt -d`

![3](https://github.com/charlicastelli/dfinder/assets/80997263/ee460910-8c70-4bdb-9d39-e76ea5bd2dfa)
