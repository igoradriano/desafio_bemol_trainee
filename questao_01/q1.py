#-*- coding:utf-8 -*-
import os
# 1) MODOS DE PASSAR O CAMINHO DO ARQUIVO
# Podemos inserir um caminho relativo ou absoluto para um arquivo com mesma estrutura, porém com nome e diretório diferentes. Ou simplesmente executar o este código com o arquivo no mesmo diretório deste código, porém este arquivo tem o nome igual ao fornecido pelo desafio.

q1 = input("Deseja adicionar o caminho do arquivo[S/N]?  ").upper().strip()
while q1 not in ['S','N','SIM','NÃO','NAO']:
    q1 = input("Digite apenas ['S' para sim ou 'N' para não). Deseja adicionar o caminho do arquivo ?  ").upper().strip()

# Pede o nome, caminho e extensão, caso o usuário queira inserir um arquivo com outro nome e arquivado em outro diretório
if q1 in ['S','SIM']:
    extensao = input("Qual a extensão do arquivo(sem o ponto)? ").lower()
    nome = input("Digite o nome do arquivo: ")
    caminho = input('Digite o Caminho do arquivo: ')
# Abre o arquivo guardado na mesma pasta deste código (caso o usuário não queira inserir o caminho do arquivo)
else:
    extensao = 'txt'
    nome = 'pib_municipio_2010_a_2018'
    caminho = './dataset'


#-------------------------------------------------------------------------------------------------------
# 2) ABRINDO O ARQUIVO PARA LEITURA
# precisamos adicionar um parâmetro a mais no 'open'. O encoding='utf-8'para especificar a codificação dos caractéres.
# A codificação baseada em Unicode, tal como UTF-8, oferece suporte para vários idiomas e assim sendo admite páginas e formulários em qualquer combinação de idiomas.

f = open(f'{caminho}/{nome}.{extensao}','r', encoding="utf-8")
arquivo = []
f.readline()
for linha in f:
    arquivo.append(linha.split(';'))
f.close()

#-------------------------------------------------------------------------------------------------------

q2 = input("Deseja passar o nome de outra cidade(caso não queira mandaremos a cidade default)[S/N]? ").upper().strip()
while q2 not in ['S','N','SIM','NÃO','NAO']:
    q2 = input("Digite apenas ['S' para sim ou 'N' para não). Deseja passar o nome de outra cidade?  ").upper().strip()
if q2 in ['S','SIM']:
    cidade = input("Qual cidade você quer saber o pib médio per capita? ").lower()
    estado = input("Esta cidade pertence a qual estado? ").lower()
else:
    cidade = 'manaus'
    estado = 'amazonas'

qtd_anos = 0 # armazena a quantidade de registros presentes na base para a cidade e estado escolhidos
ocorrencias = [] # armazenas os registros de cada ano da respectiva cidade
pib_cidade = 0 # armazena a soma de pib per capita de todos os anos para cidade escolhida
for linha in arquivo:
    if ((linha[3].lower() == cidade) and (linha[2].lower() == estado)):
        pib_cidade += float(linha[13])
        ocorrencias.append(f'{linha[0]:} - {linha[2]} - {linha[3]} - R${linha[13]}')
        qtd_anos+=1

# Funcao para mostrar prints no terminal e escrever a saida dos dados em arquivo txt
def mostrar_pib_medio():
    s = open('questao_01/saida_q1.txt','a', encoding="utf-8")
    s.write('Ano  -  Estado -  Cidade - Pib per capita\n')
    for n in ocorrencias:
        s.write(f'{n}')
    s.write(f'Pib per capita médio de {cidade.upper()}: {round(pib_cidade/qtd_anos):.2f}')
    s.close()
    print(f'Pib per capita médio de {cidade.upper()}: R${(pib_cidade/qtd_anos):.2f}')


# condicional para verificar se o arquivo ja existe, caso exista o programa apaga o arquivo e o recria, chamando a funcao anteriormente criada
if os.path.exists('questao_01/saida_q1.txt'): #verificando se existe o caminho
    os.remove('questao_01/saida_q1.txt')
    mostrar_pib_medio() 
# caso ainda não exista, ele apenas cria o arquivo e escreve os dados
else:
    mostrar_pib_medio()
    




