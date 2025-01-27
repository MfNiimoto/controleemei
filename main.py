from PyQt6 import QtWidgets
import sqlite3
import sys

# Importa os módulos gerados a partir dos arquivos .ui
from login import Ui_MainWindow as UiLogin
from paineladministrador import Ui_MainWindow as UiAdminPanel
from mainwindow import Ui_MainWindow as UiMainWindow

class LoginScreen(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = UiLogin()
        self.ui.setupUi(self)

        # Conecta o botão de login à função de verificação
        self.ui.loginButton.clicked.connect(self.handle_login)

    def handle_login(self):
        username = self.ui.usernameField.text()
        password = self.ui.passwordField.text()

        # Verificação no banco de dados
        with sqlite3.connect('dados.db') as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT role FROM user WHERE username = ? AND password = ?", (username, password))
            result = cursor.fetchone()

            if result:
                role = result[0]
                if role == 'admin':
                    main_app.show_admin_panel()
                else:
                    main_app.show_user_panel()
            else:
                self.ui.errorLabel.setText("Usuário ou senha inválidos!")

class AdminPanel(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = UiAdminPanel()
        self.ui.setupUi(self)

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = UiMainWindow()
        self.ui.setupUi(self)

class MainApp(QtWidgets.QStackedWidget):
    def __init__(self):
        super().__init__()

        # Instancia as telas
        self.login_screen = LoginScreen()
        self.admin_panel = AdminPanel()
        self.main_window = MainWindow()

        # Adiciona as telas ao QStackedWidget
        self.addWidget(self.login_screen)
        self.addWidget(self.admin_panel)
        self.addWidget(self.main_window)

        # Define a tela inicial como login
        self.setCurrentWidget(self.login_screen)

    def show_admin_panel(self):
        self.setCurrentWidget(self.admin_panel)

    def show_user_panel(self):
        self.setCurrentWidget(self.main_window)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_app = MainApp()
    main_app.show()
    sys.exit(app.exec())
