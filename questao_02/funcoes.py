def open_file_mod():
    # 1) MODOS DE PASSAR O CAMINHO DO ARQUIVO

    # Pergunta se quer passar um caminho diferente
    q1 = input("Deseja adicionar o caminho do arquivo[S/N]?  ").upper().strip()
    while q1 not in ['S','N','SIM','NÃO','NAO']:
        q1 = input("Digite apenas ['S' para sim ou 'N' para não). Deseja adicionar o caminho do arquivo ?  ").upper().strip()

    # Caso queira pede o nome, caminho e extensão do arquivo
    if q1 in ['S','SIM']:
        extensao = input("Qual a extensão do arquivo(sem o ponto)? ").lower()
        nome = input("Digite o nome do arquivo: ")
        caminho = input('Digite o Caminho do arquivo: ')

    # Caso não queira passar outro arqivo, abre o default
    else:
        extensao = 'txt'
        nome = 'pib_municipio_2010_a_2018'
        caminho = './dataset'
    
    # Depois de escolhido o caminho, de fato abre o arquivo no modo leitura e copia tudo para uma lista
    # precisamos do 'utf-8' para leitura de caracteres acentuados
    f = open(f'{caminho}/{nome}.{extensao}','r', encoding="utf-8") 
    arquivo = []
    f.readline()
    for linha in f:
        arquivo.append(linha.split(';'))  # Quando passar para lista, divide a linha onde tem ';' e coloca tudo dentro de uma lista
    f.close()

    return arquivo
