from service.df_manipulator import DfManipulator
from utils.terminal_utils import TerminalUtils
from view.components.exibir_filtros_view import ExibirFiltrosView


class CriarFiltroView:
    def __init__(self, manipulator:DfManipulator):
        self.df_manipulator = manipulator
        self.colunas = []
        self.filtros = []
        self.terminal = TerminalUtils()
        self.exibir_filtros = ExibirFiltrosView()
        pass

    def exibir_colunas(self, colunas:list):
        print("=========================== Selecione a Coluna que Deseja Filtrar =========================")
        for coluna in colunas:
            print(f"{colunas.index(coluna)} - {coluna}")
        print("===========================================================================================")
        print("Digite sair para sair")

    def selecionar_coluna(self, index:int):
        try:
            return self.colunas[index]
        except IndexError:
            return None

    def exibir_opcoes(self):
        print("1 - Adicionar Filtro")
        print("2 - Remover Filtro")
        print("3 - Sair")





    def montar_filtro(self):
        self.colunas = self.df_manipulator.obter_colunas()
        while True:
            try:
                self.terminal.limpar_console()
                self.exibir_colunas(self.colunas)
                opcao = self.terminal.ler_opcao()
                if opcao.upper() == "SAIR":
                    break

                coluna = self.selecionar_coluna(int(opcao))
                if coluna:
                    dados = self.obter_dados_filtro(coluna)
                    self.filtros.append({coluna: dados})
                    break
            except Exception:
                pass


    def executar(self):
        while True:
            self.terminal.limpar_console()
            self.exibir_filtros.exibir(self.filtros)
            self.exibir_opcoes()
            sair = self.navegaca(self.terminal.ler_opcao())
            if sair:
                break
        return self.filtros

    def navegaca(self, opcao:str):
        match opcao.upper():
            case "1":
                self.montar_filtro()

            case "2":
                self.remover_filtro()

            case "3":
                return True

            case "SAIR":
                return True

        return False

    def remover_filtro(self):
        while True:
            self.terminal.limpar_console()
            try:
                self.exibir_filtros.exibir(self.filtros)
                escolha = input(f"Digite o index do filtro que deseja remover (ou digite sair): ")
                if escolha.upper() == 'SAIR':
                    break
                if escolha:
                    self.filtros.pop(int(escolha))
                    break
            except Exception:
                pass

        return

    def obter_dados_filtro(self, coluna):
        lista_de_dados_a_serem_filtados = []
        while True:
            self.terminal.limpar_console()
            print("=========================== Criar Filtro =========================")
            print(f"Coluna: {coluna}")
            print(f"Dados a serem filtrados: {lista_de_dados_a_serem_filtados}")
            print("==================================================================")
            dado = input(f"Digite o dado que deseja filtrar (ou digite sair): ")

            if dado.upper() == "SAIR":
                break
            if dado:
                lista_de_dados_a_serem_filtados.append(dado)
        return lista_de_dados_a_serem_filtados