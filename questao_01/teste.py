import os
f = open(f'./dataset/pib_municipio_2010_a_2018.txt','r', encoding='utf-8')

arquivo = []
f.readline()
for linha in f:
    arquivo.append(linha.split(';'))
f.close()

qtd_anos = 0 # armazena a quantidade de registros presentes na base para a cidade e estado escolhidos
ocorrencias = [] # armazenas os registros de cada ano da respectiva cidade
pib_cidade = 0 # armazena a soma de pib per capita de todos os anos para cidade escolhida
for linha in arquivo:
    if ((linha[3].lower() == 'manaus') and (linha[2].lower() == 'amazonas')):
        pib_cidade += float(linha[13])
        ocorrencias.append(f'{linha[0]:} - {linha[2]} - {linha[3]} - R${linha[13]}')
        qtd_anos+=1

# Funcao para mostrar prints no terminal e escrever a saida dos dados em arquivo txt
def mostrar_pib_medio():
    s = open('questao_01/saida_q1.1.txt','a', encoding="utf-8")
    s.write('Ano  -  Estado -  Cidade - Pib per capita\n')
    for n in ocorrencias:
        s.write(f'{n}')
    s.write(f'Pib per capita médio de Manaus: {round(pib_cidade/qtd_anos):.2f}')
    s.close()
    print(f'Pib per capita médio de Manaus: R${(pib_cidade/qtd_anos):.2f}')


if os.path.exists('questao_01/saida_q1.1.txt'): #verificando se existe o caminho
    os.remove('questao_01/saida_q1.1.txt')
    mostrar_pib_medio() 
# caso ainda não exista, ele apenas cria o arquivo e escreve os dados
else:
    mostrar_pib_medio()