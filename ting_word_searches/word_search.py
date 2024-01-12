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
    result_set = []

    for file_data in instance.items:
        word_occurrences = [
            {"linha": index + 1, "conteudo": line_content}
            for index, line_content in enumerate(
                file_data["linhas_do_arquivo"]
            )
            if word.lower() in line_content.lower()
        ]

        if word_occurrences:
            result_set.append({
                "palavra": word,
                "arquivo": file_data["nome_do_arquivo"],
                "ocorrencias": word_occurrences,
            })

    return result_set
