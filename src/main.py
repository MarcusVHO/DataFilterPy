from service.archive_service import ArchiveService
from view.menu_principal import MenuPrincipal
class Main1:
    def __init__(self):
        self.menu_principal = MenuPrincipal()

    def executar(self):
        print("Iniciando...")
        self.menu_principal.executar()



if __name__ == "__main__":
    app = Main1()
    app.executar()



