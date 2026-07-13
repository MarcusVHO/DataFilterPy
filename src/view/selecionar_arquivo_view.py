from time import sleep

from service.archive_service import ArchiveService
from utils.terminal_utils import TerminalUtils
import global_context.global_context as global_context

class SelecionarArquivoView:
    
    def __init__(self):
        self.archive_service = ArchiveService()
        self.terminal = TerminalUtils()
        self.lista_arquivos = self.archive_service.listar_arquivos()
        pass

    def mostar_cabecalho(self):
        print(
            """
========================== Selecionar Um Arquivo ==========================
                          Digite (Sair) para sair!"""
        )
        for arquivo in self.lista_arquivos:
            print(f"{self.lista_arquivos.index(arquivo) } - {arquivo.name}".center(0))

    def executar(self):
        while True:
            self.mostar_cabecalho()
            opcao = self.terminal.ler_opcao()
            if opcao.upper() == "SAIR":
                break
            selecionado = self.selecionar_arquivo(opcao)
            if selecionado:
                break

    def selecionar_arquivo(self, opcao):
        try:
            arquivo = self.lista_arquivos[int(opcao)]
            resposta = input(f"Deseja selecionar o arquivo {arquivo.name} (S/N): ").upper()
            if resposta == "S":
                global_context.current_archive = arquivo
                print("Arquivo selecionado com sucesso!")
                sleep(2)
                return True
            else:
                return False

        except Exception:
            return False
