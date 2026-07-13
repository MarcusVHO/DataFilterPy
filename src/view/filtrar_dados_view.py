from service.df_manipulator import DfManipulator
from utils.terminal_utils import TerminalUtils
import global_context.global_context as global_context
from view.RemoverColunasView import RemoverColunasView
from view.components.criar_filtro_view import CriarFiltroView
from view.components.executar_opercaoes_view import ExecutarOpercaoesView
from view.components.exibir_filtros_view import ExibirFiltrosView
from view.components.visualisar_dataframe import VisauliarDataframe


class FiltrarDadosView:
    def __init__(self):
        self.filtros = []
        self.terminal = TerminalUtils()
        self.service = DfManipulator()
        self.criar_filtro_view = CriarFiltroView(self.service)
        self.exibir_filtros = ExibirFiltrosView()
        self.executar_opercaoes = ExecutarOpercaoesView(self.service)
        self.visulisar_dataframe = VisauliarDataframe(self.service)
        self.remover_colunas_view = RemoverColunasView(self.service)
        pass

    def mostrar_menu(self):
        print("============================== Filtragem de Dados =================================")
        self.exibir_filtros.exibir(self.filtros)
        print("1. Modificar Filtros")
        print("2. Executar Filtros")
        print("3. Visulizar")
        print("4. Remover Colunas")
        print("5. Sair")
        print("===================================================================================")

    def executar(self):
        self.terminal.limpar_console()
        print(f"Carregando DF do arquivo {global_context.current_archive.name if global_context.current_archive else "None"}...................")
        self.service.carregar_df(global_context.current_archive)
        self.terminal.limpar_console()

        while True:
            self.terminal.limpar_console()
            self.mostrar_menu()
            sair = self.navegacao(self.terminal.ler_opcao())
            if not sair:
                break


    def navegacao(self, opcao:str):
        match opcao.upper():
            case "1":
                self.filtros = self.criar_filtro_view.executar()

            case "2":
                self.executar_opercaoes.executar(self.filtros)

            case "3":
                self.visulisar_dataframe.executar()

            case"4":
                self.remover_colunas_view.executar()

            case "5":
                return False

            case "SAIR":
                return False

        return True

