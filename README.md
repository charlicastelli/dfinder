## Directory Finder.
- Mensionei no exemplo a página http://businesscorp.com.br que usei no curso Pentest profissional da Desec Security.
- Esse programa busca por caminhos, arquivos e subdominios.
  
### Exemplo de uso:
- `python3 dfinder.py -h` ou `python3 dfinder.py --help`
- `python3 dfinder.py -w lista.txt --domain businesscorp.com.br -f .txt -s` (Busca por diretórios, arquivos .txt e subdominios)
- `python3 dfinder.py -d businesscorp.com.br -w wordlist.txt -f .html -s -t 4` (Busca por diretórios, arquivos .html e subdominios, com tempo de 4 segundos entre as requisições)


### Imagem
![2](https://github.com/charlicastelli/dfinder/assets/80997263/b356c6fc-3c43-4085-a3fe-cfd45eb9c948)
![1](https://github.com/charlicastelli/dfinder/assets/80997263/b98b215b-34be-4db7-9ec5-bdf734d0836a)
