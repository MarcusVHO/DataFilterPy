import os
import subprocess

class TerminalUtils:
    def __init__(self):
        pass


    def ler_opcao(self):
        return input("Digite a opção desejada: ")

    def limpar_console(self):
        if os.name == "nt":
            subprocess.run(["cls"], shell=True)
        else:
            subprocess.run(["clear"])