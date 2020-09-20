# Images to PDF Convertor
## O que faz?
O Images to PDF Convertor recebe como entrada uma pasta com imagens e as salva, oredenadas por seus respectivos nomes, em um único PDF.

## Download:
Se você quer baixar o projeto completo, inclusive os arquivos python, <a href="https://github.com/gustadsg/to_pdf_convertor/archive/master.zip">clique aqui</a>.

Caso prefira baixar apenas o executável para Windows, <a href="https://doc-44-00-drive-data-export.googleusercontent.com/download/2mlsj89mviua2646s2r7ai02sc83n7cq/k2i7jmn862vjmcjvt09o7tl4lddqn0lp/1600623000000/cdcce071-a854-4316-a8db-8bcc4fae4c4a/108444827400362615109/ADt3v-MgWb6DCC_RY0UzzJeTxXpS0n1hKTGfZjKQg8V-4fz3pbwVQZUGnn94R6tepqCq9HWed22RW-G9JQ85n5Kdi2y3MA7nBm6BzscD9EbjtPrIUuZ92ALbQYBTrVWoEliVDX2gE4_XTqy2D7TSPEqEII54t9cIVWrrRTvbshvRidsh4Eezo01CN76d8xiCIZEXFKVzLEuCsdXKR6QTmy-lb-sWko5SoEKoBbBIkCT26djpqGNwfHwgca1W2mu6bxpBeTvtz82GZT4DzSmE7bLDY3K90Im4CBCNSkvG5vHMNpac4270W2caqSApFfgQG_9TdZH3FCh9?authuser=0&nonce=17rbq2hqat3ie&user=108444827400362615109&hash=935ns77aa3pf4813mv9t3bo0rg3mr7g0">clique aqui</a>.

Ou, se preferir apenas o executável para Linux, <a href="https://doc-54-90-drive-data-export.googleusercontent.com/download/2mlsj89mviua2646s2r7ai02sc83n7cq/lh7f7l9slofcv3e8nj0drh52mtpk1slc/1600623000000/e5c74f0c-86f5-41fa-b0f9-7141f6aea615/108444827400362615109/ADt3v-Oh7WJxKSrrpe_v9K4SHx5COc8qh6YAIpplYiDhkBKalmAZHbUoJuzK5X9yis8Ubq_C8fU-HDpTioJukqtpE6dBJK0nYa9qg2ShRDYV6sNGW9UInFU9eI-AYeZp-ivxOm9Fk3x6CJ8ov7ihP-w44mSSYEI55otMqPmy4_LHNDcJNZ-HOouQFlSrD4PT436VucuQBpKBDNpXnaWLAXLfWETnmIueV04JYfk08nCCPO12KQspL636G7XmQgTWnmrZYG5fOrAIMIazcAO8Oi8jWXYRzgPdIDwjAxr1cQX2qqrDxqWNrAaYnuR02dDg_TJfBS049i9C?authuser=0&nonce=tbie35pm843ls&user=108444827400362615109&hash=8t6fhtddg2ksta61urmmk08iu1mspnaj">clique aqui</a>.

Depois de fazer o download, basta descomprimir o arquivo e começar a usar.

## Como usar:
###  -  Via linha de comando:
1. Instale as dependências usando o arquivo indicado através do comando:
```python
pip install -r requirements.txt
```
1. Agora, para executar:
```python
python main.py  [--directory] [--output]
```
#### Opções:
    `[-d ]` ou ` [--directory]`: Caminho para a pasta onde estão as imagens
	
	`[-o ]` ou ` [--output]`: Nome do arquivo PDF que será salvo

Obs:  se o caminho para a pasta onde estão as imagens não for passado como argumento, será perguntado durante a execução do programa.

###  -  Via interface gráfica:

<img src="/images/screenshot.png" />

1. Abra a pasta win ou linux de acordo com o seu sistema operacional
1. Agora execute o arquivo executável
1. Preencha o campo "Digite o nome da saída" para definir o nome do arquivo PDF  que será salvo (opcional)
1. Selecione a pasta onde estão salvas as imagens que quer converter
1. Clique em converter para PDF


O arquivo PDF será salvo no diretório que foi fornecido anteriormente. Caso o nome do arquivo de saída não seja fornecido, o PDF será salvo como "output.pdf"
###  -  Atenção: 
Como critério de ordenação, o Images to PDF Convertor desconsidera espaços e parênteses nos nomes dos seus arquivos de imagem
