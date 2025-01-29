from PyQt6 import QtWidgets
import sqlite3
import sys
from datetime import datetime
from login import Ui_LoginForm

# Importação da classe gerada pelo pyuic6 a partir do arquivo login.ui
from login import Ui_LoginForm  # Nome correto da classe gerada pelo pyuic6

class LoginScreen(QtWidgets.QWidget):  # Alterado para QWidget em vez de QMainWindow
    def __init__(self):
        super().__init__()
        self.ui = Ui_LoginForm()
        self.ui.setupUi(self)

        # Conecta o botão de login ao método de verificação de login
        self.ui.loginButton.clicked.connect(self.handle_login)

    def handle_login(self):
        username = self.ui.usernameTxt.text()
        password = self.ui.senhaTxt.text()

        # Verificação no banco de dados
        with sqlite3.connect('dados.db') as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT role FROM user WHERE username = ? AND password = ?", (username, password))
            result = cursor.fetchone()

            if result:
                role = result[0]
                if role == 'admin':
                    self.open_admin_panel()
                else:
                    self.open_user_panel()
            else:
                QtWidgets.QMessageBox.warning(self, "Erro", "Usuário ou senha inválidos!")

    def open_admin_panel(self):
        from paineladministrador import Ui_PainelAdministrador

        class AdminPanel(QtWidgets.QWidget):
            def __init__(self):
                super().__init__()
                self.ui = Ui_PainelAdministrador()
                self.ui.setupUi(self)
                self.ui.salvarCadastroButton.clicked.connect(self.save_device)
                self.ui.salvarLoginButton.clicked.connect(self.save_login)
                self.ui.deletarLoginButton.clicked.connect(self.delete_login)
                self.ui.cadastroTwidget.itemSelectionChanged.connect(self.populate_login_fields)
                self.load_devices()
                self.load_logins()

            def validar_emei(self, emei):
                if len(emei) != 15 or not emei.isdigit():
                    return False
                soma = 0
                for i, digito in enumerate(map(int, emei)):
                    if i % 2 == 0:
                        soma += digito
                    else:
                        soma += sum(map(int, str(digito * 2)))
                return soma % 10 == 0

            def save_device(self):
                nome = self.ui.nomeTxt.text().strip()
                matricula = self.ui.matriculaTxt.text().strip()
                modelo = self.ui.modeloTxt.text().strip()
                emei = self.ui.emeiTxt.text().strip()
                emei2 = self.ui.emei2Txt.text().strip()

                erros = []

                # Validação do EMEI1 (obrigatório)
                if not emei:
                    erros.append("EMEI 1 é obrigatório")
                else:
                    if not self.validar_emei(emei):
                        erros.append("EMEI 1 inválido (deve ter 15 dígitos e ser válido)")

                # Validação do EMEI2 (opcional)
                if emei2:
                    if not self.validar_emei(emei2):
                        erros.append("EMEI 2 inválido (deve ter 15 dígitos e ser válido)")

                # Verificar duplicatas
                with sqlite3.connect('dados.db') as conn:
                    cursor = conn.cursor()
    
                    query = '''SELECT * FROM aparelhos 
                                WHERE ? IN (emei, emei2)'''
                    params = [emei]
    
                if emei2:
                    query += ''' OR ? IN (emei, emei2)'''
                    params.append(emei2)
    
                cursor.execute(query, params)
    
                if cursor.fetchone():
                    erros.append("EMEI já cadastrado no sistema")

                if erros:
                    QtWidgets.QMessageBox.warning(self, "Erro de Validação", "\n".join(erros))
                    return

                try:
                    with sqlite3.connect('dados.db') as conn:
                        cursor = conn.cursor()
                        cursor.execute('''
                            CREATE TABLE IF NOT EXISTS aparelhos (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                nome TEXT NOT NULL,
                                matricula INTEGER NOT NULL,
                                modelo TEXT NOT NULL,
                                emei TEXT NOT NULL UNIQUE,
                                emei2 TEXT
                            )
                        ''')
                        cursor.execute('''
                            INSERT INTO aparelhos (nome, matricula, modelo, emei, emei2)
                            VALUES (?, ?, ?, ?, ?)
                        ''', (nome, matricula, modelo, emei, emei2 or None))
                        conn.commit()

                    QtWidgets.QMessageBox.information(self, "Sucesso", "Dados salvos com sucesso!")
                    self.ui.nomeTxt.clear()
                    self.ui.matriculaTxt.clear()
                    self.ui.modeloTxt.clear()
                    self.ui.emeiTxt.clear()
                    self.ui.emei2Txt.clear()
                    self.load_devices()

                except sqlite3.IntegrityError as e:
                    QtWidgets.QMessageBox.warning(self, "Erro", f"Erro ao salvar: {str(e)}")

            def save_login(self):
                login = self.ui.loginCadastroTxt.text()
                senha = self.ui.senhaCadastroTxt.text()

                if not login or not senha:
                    QtWidgets.QMessageBox.warning(self, "Erro", "Os campos de login e senha não podem estar vazios!")
                    return

                # Verificar se o login já está selecionado para atualização
                selected_item = self.ui.cadastroTwidget.currentItem()

                with sqlite3.connect('dados.db') as conn:
                    cursor = conn.cursor()
                    # Criar a tabela se não existir
                    cursor.execute('''
                        CREATE TABLE IF NOT EXISTS user (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            username TEXT NOT NULL UNIQUE,
                            password TEXT NOT NULL,
                            role TEXT NOT NULL
                        )
                    ''')

                    if selected_item:  # Atualizar o login existente
                        current_login = selected_item.text(0)
                        cursor.execute('''
                            UPDATE user SET password = ? WHERE username = ?
                        ''', (senha, current_login))
                        QtWidgets.QMessageBox.information(self, "Sucesso", "Senha atualizada com sucesso!")
                    else:  # Inserir um novo login
                        # Perguntar se o usuário é administrador
                        resposta = QtWidgets.QMessageBox.question(
                            self,
                            "Confirmação de Permissão",
                            "O usuário é administrador?",
                            QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No
                        )

                        role = "admin" if resposta == QtWidgets.QMessageBox.StandardButton.Yes else "user"

                        try:
                            cursor.execute('''
                                INSERT INTO user (username, password, role)
                                VALUES (?, ?, ?)
                            ''', (login, senha, role))
                            QtWidgets.QMessageBox.information(self, "Sucesso", "Usuário salvo com sucesso!")
                        except sqlite3.IntegrityError:
                            QtWidgets.QMessageBox.warning(self, "Erro", "O nome de usuário já existe!")

                    conn.commit()

                self.ui.loginCadastroTxt.clear()
                self.ui.senhaCadastroTxt.clear()
                self.load_logins()

            def delete_login(self):
                selected_item = self.ui.cadastroTwidget.currentItem()
                if not selected_item:
                    QtWidgets.QMessageBox.warning(self, "Erro", "Nenhum login selecionado para exclusão!")
                    return

                login = selected_item.text(0)
                with sqlite3.connect('dados.db') as conn:
                    cursor = conn.cursor()
                    cursor.execute("DELETE FROM user WHERE username = ?", (login,))
                    conn.commit()

                QtWidgets.QMessageBox.information(self, "Sucesso", "Login excluído com sucesso!")
                self.load_logins()

            def populate_login_fields(self):
                selected_item = self.ui.cadastroTwidget.currentItem()
                if selected_item:
                    login = selected_item.text(0)
                    with sqlite3.connect('dados.db') as conn:
                        cursor = conn.cursor()
                        cursor.execute("SELECT password FROM user WHERE username = ?", (login,))
                        result = cursor.fetchone()
                        if result:
                            self.ui.loginCadastroTxt.setText(login)
                            self.ui.senhaCadastroTxt.setText(result[0])

            def load_devices(self):
                self.ui.cadastroAparelhosTwidget.clear()
                with sqlite3.connect('dados.db') as conn:
                    cursor = conn.cursor()
                    cursor.execute("SELECT nome, modelo FROM aparelhos")
                    devices = cursor.fetchall()
                self.ui.cadastroAparelhosTwidget.setHeaderLabels(["Nome", "Modelo"])
                for nome, modelo in devices:
                    item = QtWidgets.QTreeWidgetItem([nome, modelo])
                    self.ui.cadastroAparelhosTwidget.addTopLevelItem(item)

            def load_logins(self):
                # Limpar o widget antes de carregar os dados
                self.ui.cadastroTwidget.clear()

                # Conectar ao banco de dados e buscar os dados
                with sqlite3.connect('dados.db') as conn:
                    cursor = conn.cursor()
                    cursor.execute("SELECT username, role FROM user")
                    logins = cursor.fetchall()

                # Preencher o TreeWidget com os dados
                self.ui.cadastroTwidget.setHeaderLabels(["Login", "Permissão"])
                for username, role in logins:
                    item = QtWidgets.QTreeWidgetItem([username, role])
                    self.ui.cadastroTwidget.addTopLevelItem(item)

        self.admin_panel = AdminPanel()
        self.admin_panel.show()
        self.close()

    def open_user_panel(self):
        from mainwindow import Ui_MainWindow

        class UserPanel(QtWidgets.QMainWindow):  # Alterado para QMainWindow
            def __init__(self):
                super().__init__()
                self.ui = Ui_MainWindow()
                self.ui.setupUi(self)

                # Criar a tabela movimentacao caso não exista
                self.create_movimentacao_table()

                # Conectar o botão confirmar ao método de registrar movimentação
                self.ui.confirmarButton.clicked.connect(self.registrar_movimentacao)

                # Carregar as movimentações iniciais
                self.load_movimentacoes()

            def create_movimentacao_table(self):
                with sqlite3.connect('dados.db') as conn:
                    cursor = conn.cursor()
                    cursor.execute('''
                        CREATE TABLE IF NOT EXISTS movimentacao (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            emei TEXT NOT NULL,
                            estado TEXT NOT NULL,
                            data_hora TEXT NOT NULL
                        )
                    ''')
                    conn.commit()

            def registrar_movimentacao(self):
                emei = self.ui.entradaSaidaEmeiTxt.text().strip()
                if not emei:
                    QtWidgets.QMessageBox.warning(self, "Erro", "O campo EMEI não pode estar vazio!")
                    return

                with sqlite3.connect('dados.db') as conn:
                    cursor = conn.cursor()
                    cursor.execute("SELECT emei, emei2 FROM aparelhos WHERE emei = ? OR emei2 = ?", (emei, emei))
                    aparelho = cursor.fetchone()

                    if aparelho:
                        emei = aparelho[0]  # Sempre usar o EMEI principal registrado

                    cursor.execute("SELECT estado FROM movimentacao WHERE emei = ? ORDER BY data_hora DESC LIMIT 1", (emei,))
                    ultimo_registro = cursor.fetchone()

                    if not ultimo_registro:
                        novo_estado = "entrada"
                    else:
                        novo_estado = "saida" if ultimo_registro[0] == "entrada" else "entrada"

                    data_hora_atual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    cursor.execute("INSERT INTO movimentacao (emei, estado, data_hora) VALUES (?, ?, ?)", (emei, novo_estado, data_hora_atual))
                    conn.commit()

                QtWidgets.QMessageBox.information(self, "Sucesso", f"Movimentação registrada: {emei} - {novo_estado}")
                self.ui.entradaSaidaEmeiTxt.clear()
                self.load_movimentacoes()

            def load_movimentacoes(self):
                with sqlite3.connect('dados.db') as conn:
                    cursor = conn.cursor()

                    # Carregar últimas 10 movimentações
                    cursor.execute('''
                        SELECT a.nome, m.estado, m.data_hora 
                        FROM movimentacao m
                        JOIN aparelhos a ON m.emei = a.emei
                        ORDER BY m.data_hora DESC LIMIT 10
                    ''')
                    registros = cursor.fetchall()
                    self.ui.recentesTwidget.clear()
                    self.ui.recentesTwidget.setHeaderLabels(["Agente", "Entrada/Saída", "Horário"])
                    for nome, estado, data_hora in registros:
                        item = QtWidgets.QTreeWidgetItem([nome, estado, data_hora])
                        self.ui.recentesTwidget.addTopLevelItem(item)
                    
                    # Carregar aparelhos com entrada sem saída
                    cursor.execute('''
                        SELECT a.nome, a.modelo FROM aparelhos a
                        WHERE a.emei IN (
                            SELECT m.emei FROM movimentacao m
                            GROUP BY m.emei
                            HAVING MAX(m.data_hora) = (SELECT MAX(data_hora) FROM movimentacao WHERE emei = m.emei AND estado = 'entrada')
                        )
                    ''')
                    registros = cursor.fetchall()
                    self.ui.previaTwidget.clear()
                    self.ui.previaTwidget.setHeaderLabels(["Agente", "Aparelho"])
                    for nome, modelo in registros:
                        item = QtWidgets.QTreeWidgetItem([nome, modelo])
                        self.ui.previaTwidget.addTopLevelItem(item)
                    
        self.user_panel = UserPanel()
        self.user_panel.show()
        self.close()
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    login_screen = LoginScreen()
    login_screen.show()
    sys.exit(app.exec())
