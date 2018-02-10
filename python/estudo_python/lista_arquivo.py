import os

def ler_arquivo(path):
    dados = open(path, "rt")
    meta_dados = []

    for linha in dados:
        linha_array = linha.split('\t')
        meta_dados.append((linha_array[0],
                           linha_array[1],
                           linha_array[2]))
    dados.close()
    return meta_dados

caminho = 'data/meta-data/'

for arquivo in os.listdir(caminho):
    print(ler_arquivo(caminho+arquivo))