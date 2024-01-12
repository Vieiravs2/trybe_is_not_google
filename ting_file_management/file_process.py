from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    file_content = txt_importer(path_file)
    file_metadata = {'nome_do_arquivo': path_file,
                     'qtd_linhas': len(file_content),
                     'linhas_do_arquivo': file_content}

    if any(file['nome_do_arquivo'] == path_file for file in instance.items):
        return None

    instance.enqueue(file_metadata)
    print(instance.items)
    return None


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
