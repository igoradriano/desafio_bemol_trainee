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
    arquivo.append(linha.replace('\n', '').split(';'))
f.close()

'''estado = input("Digite o nome do estado: ")
ano = input("Digite o ano: ")'''
estadoo = 'Amazonas'
ano = 2018

dict_estados = {}
for linha in arquivo:
    if linha[2] not in dict_estados:
        dict_estados[linha[2]] = None


reg =[]
for estado in dict_estados:
    for linha in arquivo:
        if estado == linha[2]:
            reg.append(linha)
    dict_estados[estado] = reg.copy()
    reg.clear()


ocorrencias = []
soma_servico = 0
soma_v_total = 0
for linha in dict_estados[estadoo]:
    if int(linha[0]) == ano:
        soma_servico += int(linha[8])
        soma_v_total += int(linha[10])
        ocorrencias.append(f'{linha[0]} - {linha[2]} - {linha[3]} - R${int(linha[8])*1000} - R${int(linha[10])*1000}')


# Funcao para mostrar prints no terminal e escrever a saida dos dados em arquivo txt
def mostrar_relacao():
    s = open('questao_03/saida_q3.txt','a', encoding="utf-8")
    s.write('Ano  -  Estado -  Cidade - Valor adicionado Serviços - Valor adicionado bruto total  \n')
    for n in ocorrencias:
        s.write(f'{n}\n')
    s.write(f'\nTotal valor bruto médio do setor de serviço: R${soma_servico}\n')
    s.write(f'Total valor bruto total médio adicionado: R${soma_v_total}\n')
    s.write(f'Relação valor bruto médio do setor de serviço e valor bruto total médio adicionado no estado do {estadoo.upper()} no ano de {ano}: {(soma_servico/soma_v_total)*100:.2f}%')
    s.close()
    print(f'Relação valor bruto médio do setor de serviço e valor bruto total médio adicionado no estado do {estadoo.upper()} no ano de {ano}: {(soma_servico/soma_v_total)*100:.2f}%')


# condicional para verificar se o arquivo ja existe, caso exista o programa apaga o arquivo e o recria, chamando a funcao anteriormente criada
if os.path.exists('questao_03/saida_q3.txt'): #verificando se existe o caminho
    os.remove('questao_03/saida_q3.txt')
    mostrar_relacao() 
# caso ainda não exista, ele apenas cria o arquivo e escreve os dados
else:
    mostrar_relacao()
    
