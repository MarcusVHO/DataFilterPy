import global_context.global_context as global_context
from utils.terminal_utils import TerminalUtils
from view.filtrar_dados_view import FiltrarDadosView
from view.selecionar_arquivo_view import SelecionarArquivoView

class MenuPrincipal:
    def __init__(self):
        self.terminal = TerminalUtils()
        self.selecionar_arquivo_view = SelecionarArquivoView()
        self.filtrar_dados_view = FiltrarDadosView()
        pass

    def mostrar_menu(self):
        print(
f"""
========================== Sistema de Filtragem de Dados ==========================
Arquivo Selecionado: {global_context.current_archive.name if global_context.current_archive else "None"}
===================================================================================
1 - Selecionar arquivo 
2 - Filtrar Dados 
"""
        )

    def navegarcao(self, opcao):
        match(opcao):
            case("1"):
                self.selecionar_arquivo_view.executar()
            case("2"):
                self.filtrar_dados_view.executar()


    def executar(self):
        while True:
            self.terminal.limpar_console()
            self.mostrar_menu()
            self.navegarcao(self.terminal.ler_opcao())
            