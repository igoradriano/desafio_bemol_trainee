#-*- coding:utf-8 -*-

# Importando Bibliotecas
import os
import funcoes
arquivo = funcoes.open_file_mod()

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
    dict_estados['manus'] = None



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