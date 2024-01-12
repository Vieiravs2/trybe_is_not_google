from ting_file_management.file_management import txt_importer
import sys


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
    removed_item = instance.dequeue()

    if removed_item:
        path_file = removed_item["nome_do_arquivo"]
        sys.stdout.write(f"Arquivo {path_file} removido com sucesso\n")
    else:
        sys.stdout.write("Não há elementos\n")


def file_metadata(instance, position):
    try:
        sys.stdout.write(f'{instance.search(position)}')
    except IndexError:
        sys.stderr.write("Posição inválida\n")
    except Exception as e:
        sys.stderr.write(f"Erro inesperado: {str(e)}\n")
