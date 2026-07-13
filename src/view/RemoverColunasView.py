from service.df_manipulator import DfManipulator
from utils.terminal_utils import TerminalUtils


class RemoverColunasView:
    def __init__(self, manipulador:DfManipulator):
        self.service = manipulador
        self.terminal = TerminalUtils()
        self.lista_de_colunas = []
        pass

    def exibir_colunas(self):
        self.lista_de_colunas = self.service.obter_colunas_filtrado()
        print("============================= Remover Colunas ===============================")
        for coluna in self.lista_de_colunas:
            print(f"{self.lista_de_colunas.index(coluna)} - {coluna}")

    def executar(self):
        while True:
            opcao = None
            self.terminal.limpar_console()
            self.exibir_colunas()
            opcao = self.terminal.ler_opcao()
            if opcao.upper() == "SAIR":
                break
            self.remover(opcao)

    def remover(self, opcao):
        try:
            self.terminal.limpar_console()
            coluna = self.lista_de_colunas[int(opcao)]
            self.service.remover_colunas_df_filtrado(coluna)
            print(f"{coluna} removido com sucesso!")
            input("Pressione qualquer tecla para continuar...")
            return
        except Exception as e:
            print(e)
            input("Pressione qualquer tecla para continuar...")
            return
