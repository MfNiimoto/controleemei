import sys
import sqlite3
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QTreeWidgetItem, QMessageBox
from datetime import datetime
from relatorios import Ui_Form


class RelatorioApp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.configurar_filtros()
        self.conectar_sinais()
        self.carregar_nomes()
        self.carregar_movimentacoes(inicial=True)  # Exibe todos os dados ao iniciar

    def configurar_filtros(self):
        # Configura os filtros iniciais
        data_atual = datetime.now().date()
        self.ui.finalDate.setDate(data_atual)
        data_inicial = data_atual.replace(day=1)
        self.ui.inicioDate.setDate(data_inicial)

    def conectar_sinais(self):
        # Conecta os botões da interface às funções apropriadas
        self.ui.aplicarButton.clicked.connect(self.carregar_movimentacoes)
        self.ui.exportarButton.clicked.connect(self.exportar_dados)

    def carregar_nomes(self):
        # Carrega os nomes dos usuários no ComboBox nomeCbox
        try:
            self.ui.nomeCbox.clear()
            self.ui.nomeCbox.addItem("Todos")
            
            with sqlite3.connect("dados.db") as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT DISTINCT nome FROM aparelhos ORDER BY nome")
                nomes = cursor.fetchall()

            for nome in nomes:
                self.ui.nomeCbox.addItem(nome[0])

        except sqlite3.Error as e:
            QMessageBox.critical(self, "Erro", f"Erro ao carregar nomes: {str(e)}")

    def carregar_movimentacoes(self, inicial=False):
        # Busca e exibe os dados de movimentação aplicando os filtros selecionados
        try:
            nome_filtro = self.ui.nomeCbox.currentText()
            emei_filtro = self.ui.emeiTxt.text().strip()
            inicio_data = self.ui.inicioDate.date().toString("yyyy-MM-dd")
            final_data = self.ui.finalDate.date().toString("yyyy-MM-dd")

            query = """
                SELECT m.emei, m.estado, m.data_hora, 
                       COALESCE(a.nome, 'Desconhecido') AS nome, 
                       COALESCE(a.modelo, 'Desconhecido') AS modelo
                FROM movimentacao m
                LEFT JOIN aparelhos a ON m.emei = a.emei OR m.emei = a.emei2
            """

            params = []
            if not inicial:
                query += " WHERE m.data_hora BETWEEN ? AND ?"
                params.extend([inicio_data + " 00:00:00", final_data + " 23:59:59"])

                if nome_filtro and nome_filtro.lower() != "todos":
                    query += " AND a.nome = ?"
                    params.append(nome_filtro)

                if emei_filtro:
                    query += " AND m.emei = ?"
                    params.append(emei_filtro)

            query += " ORDER BY a.nome, m.emei, m.data_hora"

            with sqlite3.connect("dados.db") as conn:
                cursor = conn.cursor()
                cursor.execute(query, params)
                resultados = cursor.fetchall()

            self.ui.exibicaoTwidget.clear()
            movimentos = {}

            for emei, estado, data_hora, nome, modelo in resultados:
                data_hora_formatada = datetime.strptime(data_hora, "%Y-%m-%d %H:%M:%S").strftime("%d-%m-%Y %H:%M:%S")
                chave = (nome, modelo, emei)
                if chave not in movimentos:
                    movimentos[chave] = []
                
                if estado.lower() == "entrada":
                    movimentos[chave].append({"entrada": data_hora_formatada, "saida": None})
                elif estado.lower() == "saida" and movimentos[chave]:
                    for mov in movimentos[chave]:
                        if mov["saida"] is None:
                            mov["saida"] = data_hora_formatada
                            break

            for (nome, modelo, emei), lista_movimentos in movimentos.items():
                for mov in lista_movimentos:
                    entrada = mov["entrada"] if mov["entrada"] else "—"
                    saida = mov["saida"] if mov["saida"] else "—"
                    item = QTreeWidgetItem([str(nome), str(modelo), str(entrada), str(saida)])
                    self.ui.exibicaoTwidget.addTopLevelItem(item)

            for i in range(4):
                self.ui.exibicaoTwidget.resizeColumnToContents(i)

            if not resultados:
                QMessageBox.information(self, "Informação", "Nenhum resultado encontrado.")

        except sqlite3.Error as e:
            QMessageBox.critical(self, "Erro", f"Erro ao buscar dados: {str(e)}")
        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Erro inesperado: {str(e)}")

    def exportar_dados(self):
        # Função para exportar os dados para CSV
        pass


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = RelatorioApp()
    window.show()
    sys.exit(app.exec())
