def exists_word(word, instance, search_by_word=False):
    result = []

    for item in instance._queue:
        ocorrencias = []

        for count, row in enumerate(item["linhas_do_arquivo"], start=1):
            if word.lower() in row.lower():
                ocorrencias.append(
                    {"linha": count, "conteudo": row}
                    if search_by_word
                    else {"linha": count}
                )

        if ocorrencias:
            result.append({
                "palavra": word,
                "arquivo": item["nome_do_arquivo"],
                "ocorrencias": ocorrencias
                })

    return result


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
    return exists_word(word, instance, search_by_word=True)
