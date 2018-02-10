import os

def extract_name(name):
    return name.split(".")[0]


def read_lines(filename):
    _file = open(os.path.join("data/meta-data",filename), "rt")
    data = _file.read().split("\n")
    _file.close()
    return data

def read_metadata(filename):
    metadata = []
    for column in read_lines(filename):
        if column:
            values = column.split("\t")
            nome = values[0]
            tipo = values[1]
            desc = values[2]
            metadata.append((nome, tipo, desc))
    return metadata

def main():
    meta = {}
    for meta_data_file in os.listdir("data/meta-data"):
        table_name = extract_name(meta_data_file)
        meta[table_name] = read_metadata(meta_data_file)

    for key, val in meta.items():
        print("Entidade {}".format(key))
        print("Atributos: ")
        for col in val:
            print("    {}: {}".format(col[1], col[0]))

    if 'Licitacao' in meta.keys():
        for indice, values in enumerate(meta['Licitacao']):
                if 'IdAno' in values:
                    print(indice)

    print(meta['Licitacao'][2][0])

    meta['Licitacao'][2] = 'mestre'

    print(meta.get('Licitacao')[2])


if __name__ == "__main__":
    main()