# Images to PDF Convertor
## O que faz?
O Images to PDF Convertor recebe como entrada uma pasta com imagens e as salva, oredenadas por seus respectivos nomes, em um único PDF.

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
