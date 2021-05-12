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

q2 = input("Deseja passar um ano para saber o Ranking de Pib per capita por estado(caso não queira mandaremos o ano default)[S/N]? ").upper().strip()
while q2 not in ['S','N','SIM','NÃO','NAO']:
    q2 = input("Digite apenas ['S' para sim ou 'N' para não). Deseja passar um ano para saber o Ranking de Pib per capita por estado?  ").upper().strip()
if q2 in ['S','SIM']:
    ano = None
    try:
        ano = int(input("Qual ano você deseja obter o Ranking? "))
    except ValueError as err:
        print("O ano precisa ser um número do tipo inteiro - erro: ", err)

    while ((ano not in range(2010,2019)) and (ano not in [-1])):
        try:
            ano = int(input("O ano precisa ser um número inteiro entre 2010 e 2018. Qual ano você deseja obter o Ranking? Ou digite -1 para usar valor default: "))
        except ValueError as err:
            print("O ano precisa ser um número do tipo inteiro", err)
    if ano == -1:
        ano = 2010
        
else:
    ano = 2010


dict_estados ={}
for linha in arquivo:
    dict_estados[linha[2]] = None


i = 0
qtd_cidades = 0 # armazena a quantidade de registros presentes na base para a cidade e estado escolhidos
pib_estado = 0 # armazena a soma de pib per capita de todos os anos para cidade escolhida
for  key in dict_estados:
    for linha in arquivo:
        if ((int(linha[0]) == ano) and (linha[2] == key)):
            pib_estado += float(linha[13])
            qtd_cidades+=1
    media = pib_estado/qtd_cidades
    qtd_cidades = 0
    pib_estado = 0
    dict_estados[key]= round(media,2)
        
    
ocorrencias = []
for idx,item in enumerate(sorted(dict_estados, key = dict_estados.get,reverse=True)):
    print (f'{idx+1} - {item} - R${dict_estados[item]}')
    ocorrencias.append(f'{idx+1:4}{" "*4} - {item:19} - R${dict_estados[item]:>10.2f}')


def mostrar_ranking():
    s = open('questao_02/saida_q2.txt','a', encoding="utf-8")
    s.write(f"RANKING {ano} - PIB PER CAPTA MÉDIO TODOS OS ESTADOS\n")
    s.write('Posição  -      Estado         - Pib per capta médio\n')
    for n in ocorrencias:
        s.write(f'{n}\n')
    s.close()

# condicional para verificar se o arquivo ja existe, caso exista o programa apaga o arquivo e o recria, chamando a funcao anteriormente criada
if os.path.exists('questao_02/saida_q2.txt'): #verificando se existe o caminho
    os.remove('questao_02/saida_q2.txt')
    mostrar_ranking() 
# caso ainda não exista, ele apenas cria o arquivo e escreve os dados
else:
    mostrar_ranking()