import global_context.global_context as global_context


class ExibirFiltrosView:
    def __init__(self):
        pass

    def exibir(self, filtros):
        print("========================== Filtros ===========================")
        print(f"Arquivo: {global_context.current_archive.name if global_context.current_archive else "None"}")
        print(f"Filtros:")
        if filtros:
            for filtro in filtros:
                chave, valor = next(iter(filtro.items()))
                print(f"{filtros.index(filtro)} - {chave} - {valor}".center(5))
        print("===============================================================")