from service.df_manipulator import DfManipulator
from utils.terminal_utils import TerminalUtils
from view.components.exibir_filtros_view import ExibirFiltrosView


class ExecutarOpercaoesView:
    def __init__(self, manipulator:DfManipulator):
        self.manipulator = manipulator
        self.terminal = TerminalUtils()
        self.exibir_filtros = ExibirFiltrosView()
        pass

    def mostrar_informacoes_resultado(self, tamanho, success):
        print("========================= Resultado =========================")
        print("Quantidade de linhas: ", tamanho)
        print("Sucesso: ", success)
        print("=============================================================")

    def executar(self, lista_filtros):
        try:
            self.terminal.limpar_console()
            self.exibir_filtros.exibir(lista_filtros)
            print("Executando opercaoes ........")
            tamanho = self.manipulator.filtrar_dados(lista_filtros)
            self.terminal.limpar_console()
            success = True
        except Exception:
            tamanho = 0
            success = False
        self.mostrar_informacoes_resultado(tamanho, success)
        input("Digite qualquer pra sair...")