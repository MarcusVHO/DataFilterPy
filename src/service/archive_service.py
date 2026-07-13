import os
from config.configurations import caminho_arquivos
import global_context.global_context as global_context


class ArchiveService:
    def __init__(self):
        self._pasta = caminho_arquivos

    def listar_arquivos(self)->list:
        lista_de_arquivos = [] 
        for arquivo in self._pasta.glob("*.xlsx"):
                lista_de_arquivos.append(arquivo)

        return lista_de_arquivos

    def adicionar_arquivo_no_contexto(arquivo):
         global_context.current_archive = arquivo
        
