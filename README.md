# Resumo do Software
Esse software foi criado com a intenção de ser um framework para processar rotas de entrega e de recebimento de mercadorias.  Entretanto, houve contratempos no entendimento dos dados, fazendo com que eu não consiga entrelaçar os dados disponibilizados no teste. 

## Construção do código
O código foi todo feito em Python (3.11.0) usando as bibliotecas citadas abaixo para ter acesso aos arquivos disponibilizados e dar os comandos necessários, também usa algumas bibliotecas pré-instaladas

- Pandas
- Loguru

## Estrutura do projeto
Dentro da pasta principal encontramos os seguintes arquivos/pastas:
- modules (pasta onde contém os códigos)
- .gitignore (configuração para não fazer commit dos arquivos que julgo ser desnecessários)
- README.MD (este MarkDown)
- Main.py (arquivo onde é chamado as classes e outros arquivos Python dentro da pasta modules)
- requirements.txt (bibliotecas necessárias para rodar o projeto)

Dentro da pasta modules temos:
- folders.py (arquivo de configuração onde podemos substituir com facilidade os arquivos de alimentação para o software)
- framework.py (onde seria desenvolvido a junção dos arquivos e consequentemente a formação do relatório final)
- get_demands.py (trata o tipo de dados e configura os arquivos de "pedidos.csv")
- get_distances.py (trata o tipo de dados e configura o arquivo de "distancia.csv")
- get_hubs.py (trata o tipo de dados e configura o arquivo de "hubs.csv")
- get_provinces.py (trata o tipo de dados e configura o arquivo de "municipios.csv")
- logs.py (configura de forma genérica os arquivos de logs para consulta posterior caso haja algum erro)
- organizer.py (serve como um extrator de arquivos .zip para não ter nenhum tipo de configuração manual)
- time_meter.py (este é um calculador de quanto tempo a função demorou para ser executada, calculando assim todo o tempo de processamento)

## Funcionalidades
- Com esse código na versão atual conseguimos apenas tratar os dados e extrair os arquivos de pedidos, nenhum relatório será gerado

## Instruções para executar o software
- Clone o repositório
```{.py3 linenums='0'}
git clone https://github.com/KernelGM/solution
```
- Crie um ambiente virtual
```{.py3 linenums='0'}
python -m venv .venv
```
- Ative o ambiente virtual (Windows)
```{.py3 linenums='0'}
.venv\Scripts\activate.bat
```
- Instale os requisitos do software
```{.py3 linenums='0'}
pip install -r requirements.txt
```
- Abra o arquivo main.py com o Python
```{.py3 linenums='0'}
python -m ./main.py
```
