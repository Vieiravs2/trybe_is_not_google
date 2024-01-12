def exists_word(word, instance):
    response = []

    for process in instance.items:
        occurrences = []

        for line, content in enumerate(process['linhas_do_arquivo']):
            if word.lower() in content.lower():
                occurrences.append({"linha": line + 1})

        if occurrences:
            response.append({
                "palavra": word,
                "arquivo": process['nome_do_arquivo'],
                "ocorrencias": occurrences
            })

    return response


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
