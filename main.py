from PyQt6 import QtWidgets
import sqlite3
import sys

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

                # Conectar o botão de salvar ao método de salvar dados
                self.ui.salvarCadastroButton.clicked.connect(self.save_device)

                # Conectar o botão de salvar login ao método de salvar login
                self.ui.salvarLoginButton.clicked.connect(self.save_login)

                # Carregar os dispositivos cadastrados
                self.load_devices()

            def save_device(self):
                nome = self.ui.nomeTxt.text()
                matricula = self.ui.matriculaTxt.text()
                modelo = self.ui.modeloTxt.text()
                emei = self.ui.emeiTxt.text()
                emei2 = self.ui.emei2Txt.text()

                # Salvar os dados no banco de dados
                with sqlite3.connect('dados.db') as conn:
                    cursor = conn.cursor()
                    # Criar a tabela se não existir
                    cursor.execute('''
                        CREATE TABLE IF NOT EXISTS aparelhos (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            nome TEXT NOT NULL,
                            matricula INTEGER NOT NULL,
                            modelo TEXT NOT NULL,
                            emei TEXT NOT NULL,
                            emei2 TEXT NOT NULL
                        )
                    ''')
                    # Inserir os dados na tabela
                    cursor.execute('''
                        INSERT INTO aparelhos (nome, matricula, modelo, emei, emei2)
                        VALUES (?, ?, ?, ?, ?)
                    ''', (nome, matricula, modelo, emei, emei2))
                    conn.commit()

                QtWidgets.QMessageBox.information(self, "Sucesso", "Dados salvos com sucesso!")
                self.ui.nomeTxt.clear()
                self.ui.matriculaTxt.clear()
                self.ui.modeloTxt.clear()
                self.ui.emeiTxt.clear()
                self.ui.emei2Txt.clear()

                # Atualizar a lista de dispositivos
                self.load_devices()

            def save_login(self):
                login = self.ui.loginCadastroTxt.text()
                senha = self.ui.senhaCadastroTxt.text()

                if not login or not senha:
                    QtWidgets.QMessageBox.warning(self, "Erro", "Os campos de login e senha não podem estar vazios!")
                    return

                # Perguntar se o usuário é administrador
                resposta = QtWidgets.QMessageBox.question(
                    self,
                    "Confirmação de Permissão",
                    "O usuário é administrador?",
                    QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No
                )

                role = "admin" if resposta == QtWidgets.QMessageBox.StandardButton.Yes else "user"

                # Salvar o login no banco de dados
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
                    # Inserir o novo usuário
                    try:
                        cursor.execute('''
                            INSERT INTO user (username, password, role)
                            VALUES (?, ?, ?)
                        ''', (login, senha, role))
                        conn.commit()
                        QtWidgets.QMessageBox.information(self, "Sucesso", "Usuário salvo com sucesso!")
                        self.ui.loginCadastroTxt.clear()
                        self.ui.senhaCadastroTxt.clear()
                    except sqlite3.IntegrityError:
                        QtWidgets.QMessageBox.warning(self, "Erro", "O nome de usuário já existe!")

            def load_devices(self):
                # Limpar o widget antes de carregar os dados
                self.ui.cadastroAparelhosTwidget.clear()

                # Conectar ao banco de dados e buscar os dados
                with sqlite3.connect('dados.db') as conn:
                    cursor = conn.cursor()
                    cursor.execute("SELECT nome, modelo FROM aparelhos")
                    devices = cursor.fetchall()

                # Preencher o TreeWidget com os dados
                self.ui.cadastroAparelhosTwidget.setHeaderLabels(["Nome", "Modelo"])
                for nome, modelo in devices:
                    item = QtWidgets.QTreeWidgetItem([nome, modelo])
                    self.ui.cadastroAparelhosTwidget.addTopLevelItem(item)

        self.admin_panel = AdminPanel()
        self.admin_panel.show()
        self.close()

    def open_user_panel(self):
        QtWidgets.QMessageBox.information(self, "Info", "Painel de usuário ainda não implementado.")
        self.close()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    login_screen = LoginScreen()
    login_screen.show()
    sys.exit(app.exec())
