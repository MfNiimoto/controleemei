# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt6 UI code generator 6.8.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(661, 425)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.tabWidget = QtWidgets.QTabWidget(parent=self.centralwidget)
        self.tabWidget.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.tabWidget.setAutoFillBackground(True)
        self.tabWidget.setObjectName("tabWidget")
        self.movimentosTab = QtWidgets.QWidget()
        self.movimentosTab.setObjectName("movimentosTab")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.movimentosTab)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame = QtWidgets.QFrame(parent=self.movimentosTab)
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.entradaSaidaEmeiTxt = QtWidgets.QLineEdit(parent=self.frame)
        self.entradaSaidaEmeiTxt.setObjectName("entradaSaidaEmeiTxt")
        self.gridLayout.addWidget(self.entradaSaidaEmeiTxt, 1, 1, 1, 1)
        self.label = QtWidgets.QLabel(parent=self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 0, 1, 1)
        self.confirmarButton = QtWidgets.QPushButton(parent=self.frame)
        self.confirmarButton.setObjectName("confirmarButton")
        self.gridLayout.addWidget(self.confirmarButton, 2, 1, 1, 1)
        self.frame_3 = QtWidgets.QFrame(parent=self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_7 = QtWidgets.QLabel(parent=self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 0, 0, 1, 1)
        self.recentesTwidget = QtWidgets.QTreeWidget(parent=self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.recentesTwidget.sizePolicy().hasHeightForWidth())
        self.recentesTwidget.setSizePolicy(sizePolicy)
        self.recentesTwidget.setMaximumSize(QtCore.QSize(16777215, 167))
        self.recentesTwidget.setObjectName("recentesTwidget")
        self.recentesTwidget.header().setCascadingSectionResizes(True)
        self.recentesTwidget.header().setHighlightSections(True)
        self.recentesTwidget.header().setMinimumSectionSize(50)
        self.recentesTwidget.header().setStretchLastSection(True)
        self.gridLayout_2.addWidget(self.recentesTwidget, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.frame_3, 3, 0, 1, 3)
        self.label_2 = QtWidgets.QLabel(parent=self.frame)
        font = QtGui.QFont()
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.previaTwidget = QtWidgets.QTreeWidget(parent=self.frame)
        self.previaTwidget.setObjectName("previaTwidget")
        self.gridLayout.addWidget(self.previaTwidget, 1, 2, 2, 1)
        self.verticalLayout_2.addWidget(self.frame)
        self.tabWidget.addTab(self.movimentosTab, "")
        self.relatoriosTab = QtWidgets.QWidget()
        self.relatoriosTab.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.relatoriosTab.setObjectName("relatoriosTab")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.relatoriosTab)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_2 = QtWidgets.QFrame(parent=self.relatoriosTab)
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.frame_4 = QtWidgets.QFrame(parent=self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_3 = QtWidgets.QLabel(parent=self.frame_4)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.gridLayout_4.addWidget(self.frame_4, 0, 0, 1, 2)
        self.frame_7 = QtWidgets.QFrame(parent=self.frame_2)
        self.frame_7.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_7.setObjectName("frame_7")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.frame_7)
        self.gridLayout_6.setObjectName("gridLayout_6")
        spacerItem2 = QtWidgets.QSpacerItem(456, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_6.addItem(spacerItem2, 0, 0, 1, 1)
        self.relatorioButton = QtWidgets.QPushButton(parent=self.frame_7)
        self.relatorioButton.setObjectName("relatorioButton")
        self.gridLayout_6.addWidget(self.relatorioButton, 0, 2, 1, 1)
        self.pastaTButton = QtWidgets.QToolButton(parent=self.frame_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pastaTButton.sizePolicy().hasHeightForWidth())
        self.pastaTButton.setSizePolicy(sizePolicy)
        self.pastaTButton.setMaximumSize(QtCore.QSize(30, 16777215))
        self.pastaTButton.setObjectName("pastaTButton")
        self.gridLayout_6.addWidget(self.pastaTButton, 0, 1, 1, 1)
        self.gridLayout_4.addWidget(self.frame_7, 2, 0, 1, 2)
        self.frame_5 = QtWidgets.QFrame(parent=self.frame_2)
        self.frame_5.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_5.setObjectName("frame_5")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.frame_5)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.inicioDate = QtWidgets.QDateEdit(parent=self.frame_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.inicioDate.sizePolicy().hasHeightForWidth())
        self.inicioDate.setSizePolicy(sizePolicy)
        self.inicioDate.setMaximumSize(QtCore.QSize(120, 16777215))
        self.inicioDate.setObjectName("inicioDate")
        self.gridLayout_5.addWidget(self.inicioDate, 1, 2, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_5.addItem(spacerItem3, 0, 3, 1, 1)
        self.agentesRelatorioCbb = QtWidgets.QComboBox(parent=self.frame_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.agentesRelatorioCbb.sizePolicy().hasHeightForWidth())
        self.agentesRelatorioCbb.setSizePolicy(sizePolicy)
        self.agentesRelatorioCbb.setMaximumSize(QtCore.QSize(167, 16777215))
        self.agentesRelatorioCbb.setObjectName("agentesRelatorioCbb")
        self.gridLayout_5.addWidget(self.agentesRelatorioCbb, 0, 2, 1, 1)
        self.finalCbox = QtWidgets.QCheckBox(parent=self.frame_5)
        self.finalCbox.setMaximumSize(QtCore.QSize(120, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        self.finalCbox.setFont(font)
        self.finalCbox.setLayoutDirection(QtCore.Qt.LayoutDirection.RightToLeft)
        self.finalCbox.setObjectName("finalCbox")
        self.gridLayout_5.addWidget(self.finalCbox, 2, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(parent=self.frame_5)
        self.label_5.setMaximumSize(QtCore.QSize(120, 16777215))
        self.label_5.setObjectName("label_5")
        self.gridLayout_5.addWidget(self.label_5, 1, 1, 1, 1)
        self.finalDate = QtWidgets.QDateEdit(parent=self.frame_5)
        self.finalDate.setMaximumSize(QtCore.QSize(120, 16777215))
        self.finalDate.setObjectName("finalDate")
        self.gridLayout_5.addWidget(self.finalDate, 2, 2, 1, 1)
        self.relatorioEmeiTxt = QtWidgets.QLineEdit(parent=self.frame_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.relatorioEmeiTxt.sizePolicy().hasHeightForWidth())
        self.relatorioEmeiTxt.setSizePolicy(sizePolicy)
        self.relatorioEmeiTxt.setMaximumSize(QtCore.QSize(167, 16777215))
        self.relatorioEmeiTxt.setObjectName("relatorioEmeiTxt")
        self.gridLayout_5.addWidget(self.relatorioEmeiTxt, 3, 2, 1, 1)
        self.label_6 = QtWidgets.QLabel(parent=self.frame_5)
        self.label_6.setMaximumSize(QtCore.QSize(120, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout_5.addWidget(self.label_6, 3, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(parent=self.frame_5)
        self.label_4.setMaximumSize(QtCore.QSize(120, 16777215))
        self.label_4.setObjectName("label_4")
        self.gridLayout_5.addWidget(self.label_4, 0, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_5.addItem(spacerItem4, 0, 0, 1, 1)
        self.gridLayout_4.addWidget(self.frame_5, 1, 0, 1, 2)
        self.verticalLayout_3.addWidget(self.frame_2)
        self.tabWidget.addTab(self.relatoriosTab, "")
        self.gridLayout_3.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 661, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Lançar entrada/saída</span></p></body></html>"))
        self.confirmarButton.setText(_translate("MainWindow", "Confirmar"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Movimentações recentes</span></p></body></html>"))
        self.recentesTwidget.headerItem().setText(0, _translate("MainWindow", "Agente"))
        self.recentesTwidget.headerItem().setText(1, _translate("MainWindow", "Entrada/Saída"))
        self.recentesTwidget.headerItem().setText(2, _translate("MainWindow", "Horário"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\"><span style=\" font-weight:700;\">EMEI</span></p></body></html>"))
        self.previaTwidget.headerItem().setText(0, _translate("MainWindow", "Agente"))
        self.previaTwidget.headerItem().setText(1, _translate("MainWindow", "Aparelho"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.movimentosTab), _translate("MainWindow", "Entrada/Saída"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700;\">Gerar Relatórios</span></p></body></html>"))
        self.relatorioButton.setText(_translate("MainWindow", "Gerar Relatório"))
        self.pastaTButton.setText(_translate("MainWindow", "..."))
        self.finalCbox.setText(_translate("MainWindow", "Data Final"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:700;\">Data Inicial</span></p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "EMEI"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:700;\">Agente</span></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.relatoriosTab), _translate("MainWindow", "Relatórios"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
