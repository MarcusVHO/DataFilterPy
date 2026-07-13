import os
import pandas as pd
import tempfile
from pathlib import Path
import webbrowser
from tkinter import Tk
from tkinter.filedialog import asksaveasfilename

class VisualizarService:
    def __init__(self):
        pass

    def abrir_df_excel(self, dataframe:pd.DataFrame):
        arquivo = Path(tempfile.gettempdir()) / "visualizacao.xlsx"
        dataframe.to_excel(arquivo, index=False)
        os.startfile(arquivo)


    def abrir_df_html(self, dataframe:pd.DataFrame):
        arquivo = "src/temp/visualizacao.html"
        dataframe.to_html(arquivo, index=False)
        webbrowser.open(arquivo)


    def salvar_dtaframe_xlsx(self, dataframe):
        root = Tk()
        root.withdraw()

        caminho = asksaveasfilename(
            title="Salvar relatório",
            initialfile="RelatorioFiltrado.xlsx",
            defaultextension=".xlsx",
            filetypes=[
                ("Arquivos Excel", "*.xlsx"),
                ("Todos os arquivos", "*.*")
            ]
        )

        root.destroy()

        if caminho:
            dataframe.to_excel(caminho, index=False)
            print(f"Arquivo salvo em:\n{caminho}")
        else:
            print("Operação cancelada.")