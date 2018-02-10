entidades = {
    'Instituicao' : [
        ('IdInstituicao', 'bigint', 'Identificador da instituição-PK'),
        ('IdTipoInstituicao', 'bigint', 'Id do tipo de instituição'),
        ('NomInstituicao', 'varchar', 'Nome da instituição'),
        ('NumCnpj', 'vachar', 'Número do CNPJ')
    ]
}

print(entidades)