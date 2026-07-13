import pandas as pd


class DfManipulator:
    def __init__(self):
        self.df = pd.DataFrame()
        self.df_filtrado = pd.DataFrame()
        pass

    def carregar_df(self, arquivo):
        self.df = pd.read_excel(arquivo)


    def obter_colunas(self):
        return self.df.columns.to_list()

    def obter_colunas_filtrado(self):
        return self.df_filtrado.columns.to_list()

    def filtrar_dados(self, lista_de_filtros):
        self.df_filtrado = self.df.copy()

        for filtro in lista_de_filtros:
            coluna, dados = next(iter(filtro.items()))
            self.df_filtrado = self.df_filtrado[self.df_filtrado[coluna].isin(dados)]

        return self.df_filtrado.size

    def obter_dataframe_copy(self):
        return self.df_filtrado.copy()

    def remover_colunas_df_filtrado(self, coluna):
        self.df_filtrado = self.df_filtrado.drop(
            columns=[coluna]
        )