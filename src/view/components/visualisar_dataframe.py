from service.df_manipulator import DfManipulator
from service.visualization_service import VisualizarService
from utils.terminal_utils import TerminalUtils
from tabulate import tabulate

class VisauliarDataframe:
    def __init__(self, manipulator:DfManipulator):
        self.manipulator = manipulator
        self.terminal = TerminalUtils()
        self.service = VisualizarService()

    def exibir_opcoes(self):
        print("======================= Visualizar ======================")
        print("1 - Visualizar no Terminal")
        print("2 - Visualizar no Excel")
        print("3 - Visulizar em HTML")
        print("4 - Salvar XLSX")
        print("5 - Sair")
        print("========================================================")

    def executar(self):
        while True:
            self.terminal.limpar_console()
            self.exibir_opcoes()
            sair = self.navegar(self.terminal.ler_opcao())
            if not sair:
                break


    def navegar(self, opcao:str):
        match opcao.upper():
            case "1":
                self.visulizar_terminal(self.manipulator.obter_dataframe_copy())

            case "2":
                self.visualizar_excel(self.manipulator.obter_dataframe_copy())

            case "3":
                self.visualizar_html(self.manipulator.obter_dataframe_copy())

            case "4":
                self.salvar_dataframe_xlsx(self.manipulator.obter_dataframe_copy())

            case "5":
                return False

            case "SAIR":
                return False

        return True


    def visulizar_terminal(self, dataframe):
        self.terminal.limpar_console()
        print("Carregando.....")
        print(tabulate(dataframe, headers="keys", tablefmt="grid", showindex=False))
        input("Pressione qualquer tecla para sair...")

    def visualizar_excel(self, dataframe):
        self.terminal.limpar_console()
        print("Carregando.....")
        self.service.abrir_df_excel(dataframe)
        input("Pressione qualquer tecla para sair...")

    def salvar_dataframe_xlsx(self, dataframe):
        self.terminal.limpar_console()
        print("Carregando.....")
        self.service.salvar_dtaframe_xlsx(dataframe)
        input("Pressione qualquer tecla para sair...")

    def visualizar_html(self, dataframe):
        self.terminal.limpar_console()
        print("Carregando.....")
        self.service.abrir_df_html(dataframe)
        input("Pressione qualquer tecla para sair...")
