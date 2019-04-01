# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from pandasParser import PandasModel
import pandas as pd
import numpy as np

# importing mplotlib necessary functions to render regression in QGridLayout
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar

# importing sklearn necessary modules
from sklearn import datasets, linear_model
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, MinMaxScaler


class Ui_MainWindow(object):
        def setupUi(self, MainWindow):
                MainWindow.setObjectName("MainWindow")
                MainWindow.resize(1100, 780)
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap(":/img/icons/drop.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                MainWindow.setWindowIcon(icon)
                MainWindow.setStyleSheet("QPushButton {\n"
                                        "    border-radius: 3px;\n"
                                        "    background-color: rgb(223, 220, 220);\n"
                                        "    border: 1px solid black;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover {\n"
                                        "    border-radius: 3px;\n"
                                        "    background-color: rgb(206, 251, 255);\n"
                                        "    border: 1px solid black;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:pressed {\n"
                                        "  background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
                                        "                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
                                        " }")
                MainWindow.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
                self.centralwidget = QtWidgets.QWidget(MainWindow)
                self.centralwidget.setObjectName("centralwidget")
                self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
                self.verticalLayout_2.setObjectName("verticalLayout_2")
                self.gridLayout = QtWidgets.QGridLayout()
                self.gridLayout.setContentsMargins(5, 5, 5, 5)
                self.gridLayout.setObjectName("gridLayout")
                self.line = QtWidgets.QFrame(self.centralwidget)
                self.line.setFrameShape(QtWidgets.QFrame.HLine)
                self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
                self.line.setObjectName("line")
                self.gridLayout.addWidget(self.line, 3, 0, 1, 2)
                self.browseCsvPushButton = QtWidgets.QPushButton(self.centralwidget)
                self.browseCsvPushButton.setMinimumSize(QtCore.QSize(100, 30))
                self.browseCsvPushButton.setMaximumSize(QtCore.QSize(100, 16777215))
                icon1 = QtGui.QIcon()
                icon1.addPixmap(QtGui.QPixmap(":/img/icons/file.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.browseCsvPushButton.setIcon(icon1)
                self.browseCsvPushButton.setObjectName("browseCsvPushButton")
                self.gridLayout.addWidget(self.browseCsvPushButton, 2, 0, 1, 1)
                self.browseFileName = QtWidgets.QTextBrowser(self.centralwidget)
                self.browseFileName.setMinimumSize(QtCore.QSize(0, 30))
                self.browseFileName.setMaximumSize(QtCore.QSize(16777215, 30))
                self.browseFileName.setOverwriteMode(True)
                self.browseFileName.setObjectName("browseFileName")
                self.gridLayout.addWidget(self.browseFileName, 2, 1, 1, 1)
                self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
                self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
                self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
                self.tabWidget.setDocumentMode(False)
                self.tabWidget.setObjectName("tabWidget")
                self.tab_2 = QtWidgets.QWidget()
                self.tab_2.setObjectName("tab_2")
                self.gridLayout_6 = QtWidgets.QGridLayout(self.tab_2)
                self.gridLayout_6.setObjectName("gridLayout_6")
                self.gridLayout_3 = QtWidgets.QGridLayout()
                self.gridLayout_3.setObjectName("gridLayout_3")
                self.csvDataTable = QtWidgets.QTableView(self.tab_2)
                self.csvDataTable.setObjectName("csvDataTable")
                self.gridLayout_3.addWidget(self.csvDataTable, 1, 0, 1, 1)
                self.label = QtWidgets.QLabel(self.tab_2)
                font = QtGui.QFont()
                font.setPointSize(12)
                font.setBold(True)
                font.setItalic(False)
                font.setWeight(75)
                font.setStyleStrategy(QtGui.QFont.PreferAntialias)
                self.label.setFont(font)
                self.label.setTextFormat(QtCore.Qt.AutoText)
                self.label.setAlignment(QtCore.Qt.AlignCenter)
                self.label.setObjectName("label")
                self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)
                self.gridLayout_6.addLayout(self.gridLayout_3, 0, 0, 1, 1)
                self.tabWidget.addTab(self.tab_2, "")
                self.tab = QtWidgets.QWidget()
                self.tab.setObjectName("tab")
                self.gridLayout_5 = QtWidgets.QGridLayout(self.tab)
                self.gridLayout_5.setObjectName("gridLayout_5")
                self.gridLayout_4 = QtWidgets.QGridLayout()
                self.gridLayout_4.setObjectName("gridLayout_4")
                self.buildLinearModel = QtWidgets.QPushButton(self.tab)
                self.buildLinearModel.setMinimumSize(QtCore.QSize(0, 30))
                self.buildLinearModel.setMaximumSize(QtCore.QSize(150, 16777215))
                icon2 = QtGui.QIcon()
                icon2.addPixmap(QtGui.QPixmap(":/img/icons/regression-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.buildLinearModel.setIcon(icon2)
                self.buildLinearModel.setIconSize(QtCore.QSize(25, 25))
                self.buildLinearModel.setAutoDefault(False)
                self.buildLinearModel.setDefault(False)
                self.buildLinearModel.setObjectName("buildLinearModel")
                self.gridLayout_4.addWidget(self.buildLinearModel, 0, 0, 1, 1)
                self.clearPlotButton = QtWidgets.QPushButton(self.tab)
                self.clearPlotButton.setMinimumSize(QtCore.QSize(0, 30))
                self.clearPlotButton.setMaximumSize(QtCore.QSize(100, 16777215))
                icon3 = QtGui.QIcon()
                icon3.addPixmap(QtGui.QPixmap(":/img/icons/red_cross.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.clearPlotButton.setIcon(icon3)
                self.clearPlotButton.setIconSize(QtCore.QSize(20, 20))
                self.clearPlotButton.setCheckable(False)
                self.clearPlotButton.setChecked(False)
                self.clearPlotButton.setAutoRepeat(False)
                self.clearPlotButton.setObjectName("clearPlotButton")
                self.gridLayout_4.addWidget(self.clearPlotButton, 0, 4, 1, 1)
                self.plotLayout = QtWidgets.QGridLayout()
                self.plotLayout.setObjectName("plotLayout")
                self.gridLayout_4.addLayout(self.plotLayout, 1, 0, 1, 5)
                self.checkBox = QtWidgets.QCheckBox(self.tab)
                self.checkBox.setMaximumSize(QtCore.QSize(100, 16777215))
                self.checkBox.setChecked(True)
                self.checkBox.setObjectName("checkBox")
                self.gridLayout_4.addWidget(self.checkBox, 0, 1, 1, 1)
                self.scatterShow = QtWidgets.QCheckBox(self.tab)
                self.scatterShow.setMaximumSize(QtCore.QSize(100, 16777215))
                self.scatterShow.setChecked(True)
                self.scatterShow.setObjectName("scatterShow")
                self.gridLayout_4.addWidget(self.scatterShow, 0, 2, 1, 1)
                self.gridLayout_5.addLayout(self.gridLayout_4, 1, 0, 1, 1)
                self.tabWidget.addTab(self.tab, "")
                self.tab_3 = QtWidgets.QWidget()
                self.tab_3.setObjectName("tab_3")
                self.gridLayout_7 = QtWidgets.QGridLayout(self.tab_3)
                self.gridLayout_7.setObjectName("gridLayout_7")
                self.gridLayout_2 = QtWidgets.QGridLayout()
                self.gridLayout_2.setObjectName("gridLayout_2")
                self.groupBox = QtWidgets.QGroupBox(self.tab_3)
                font = QtGui.QFont()
                font.setPointSize(9)
                font.setBold(True)
                font.setWeight(75)
                self.groupBox.setFont(font)
                self.groupBox.setObjectName("groupBox")
                self.gridLayout_9 = QtWidgets.QGridLayout(self.groupBox)
                self.gridLayout_9.setObjectName("gridLayout_9")
                self.gridLayout_8 = QtWidgets.QGridLayout()
                self.gridLayout_8.setContentsMargins(6, -1, -1, -1)
                self.gridLayout_8.setObjectName("gridLayout_8")
                self.label_2 = QtWidgets.QLabel(self.groupBox)
                self.label_2.setMinimumSize(QtCore.QSize(0, 20))
                self.label_2.setMaximumSize(QtCore.QSize(150, 30))
                font = QtGui.QFont()
                font.setPointSize(9)
                font.setBold(False)
                font.setWeight(50)
                self.label_2.setFont(font)
                self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
                self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
                self.label_2.setObjectName("label_2")
                self.gridLayout_8.addWidget(self.label_2, 0, 0, 1, 1)
                self.line_2 = QtWidgets.QFrame(self.groupBox)
                self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
                self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
                self.line_2.setObjectName("line_2")
                self.gridLayout_8.addWidget(self.line_2, 0, 1, 6, 1)
                self.methodLabel = QtWidgets.QLabel(self.groupBox)
                font = QtGui.QFont()
                font.setPointSize(9)
                font.setBold(True)
                font.setWeight(75)
                self.methodLabel.setFont(font)
                self.methodLabel.setObjectName("methodLabel")
                self.gridLayout_8.addWidget(self.methodLabel, 0, 2, 1, 1)
                self.label_3 = QtWidgets.QLabel(self.groupBox)
                self.label_3.setMinimumSize(QtCore.QSize(0, 20))
                self.label_3.setMaximumSize(QtCore.QSize(150, 30))
                font = QtGui.QFont()
                font.setPointSize(9)
                font.setBold(False)
                font.setWeight(50)
                self.label_3.setFont(font)
                self.label_3.setObjectName("label_3")
                self.gridLayout_8.addWidget(self.label_3, 1, 0, 1, 1)
                self.label_5 = QtWidgets.QLabel(self.groupBox)
                self.label_5.setMinimumSize(QtCore.QSize(150, 20))
                self.label_5.setMaximumSize(QtCore.QSize(150, 30))
                font = QtGui.QFont()
                font.setPointSize(9)
                font.setBold(False)
                font.setWeight(50)
                self.label_5.setFont(font)
                self.label_5.setObjectName("label_5")
                self.gridLayout_8.addWidget(self.label_5, 4, 0, 1, 1)
                self.cardLabel = QtWidgets.QLabel(self.groupBox)
                self.cardLabel.setMinimumSize(QtCore.QSize(150, 0))
                self.cardLabel.setMaximumSize(QtCore.QSize(16777215, 30))
                font = QtGui.QFont()
                font.setPointSize(9)
                font.setBold(True)
                font.setWeight(75)
                self.cardLabel.setFont(font)
                self.cardLabel.setText("")
                self.cardLabel.setObjectName("cardLabel")
                self.gridLayout_8.addWidget(self.cardLabel, 2, 2, 1, 1)
                self.stationLabel = QtWidgets.QLabel(self.groupBox)
                self.stationLabel.setMinimumSize(QtCore.QSize(150, 0))
                self.stationLabel.setMaximumSize(QtCore.QSize(16777215, 30))
                font = QtGui.QFont()
                font.setPointSize(9)
                font.setBold(True)
                font.setWeight(75)
                self.stationLabel.setFont(font)
                self.stationLabel.setText("")
                self.stationLabel.setObjectName("stationLabel")
                self.gridLayout_8.addWidget(self.stationLabel, 3, 2, 1, 1)
                self.latLabel = QtWidgets.QLabel(self.groupBox)
                self.latLabel.setMinimumSize(QtCore.QSize(150, 0))
                self.latLabel.setMaximumSize(QtCore.QSize(16777215, 30))
                font = QtGui.QFont()
                font.setPointSize(9)
                font.setBold(True)
                font.setWeight(75)
                self.latLabel.setFont(font)
                self.latLabel.setText("")
                self.latLabel.setObjectName("latLabel")
                self.gridLayout_8.addWidget(self.latLabel, 4, 2, 1, 1)
                self.label_12 = QtWidgets.QLabel(self.groupBox)
                self.label_12.setMinimumSize(QtCore.QSize(150, 0))
                self.label_12.setMaximumSize(QtCore.QSize(16777215, 30))
                font = QtGui.QFont()
                font.setPointSize(9)
                font.setBold(False)
                font.setWeight(50)
                self.label_12.setFont(font)
                self.label_12.setObjectName("label_12")
                self.gridLayout_8.addWidget(self.label_12, 3, 0, 1, 1)
                self.label_6 = QtWidgets.QLabel(self.groupBox)
                self.label_6.setMinimumSize(QtCore.QSize(150, 0))
                self.label_6.setMaximumSize(QtCore.QSize(150, 30))
                font = QtGui.QFont()
                font.setPointSize(9)
                font.setBold(False)
                font.setWeight(50)
                self.label_6.setFont(font)
                self.label_6.setObjectName("label_6")
                self.gridLayout_8.addWidget(self.label_6, 5, 0, 1, 1)
                self.label_4 = QtWidgets.QLabel(self.groupBox)
                self.label_4.setMinimumSize(QtCore.QSize(0, 20))
                self.label_4.setMaximumSize(QtCore.QSize(150, 30))
                font = QtGui.QFont()
                font.setPointSize(9)
                font.setBold(False)
                font.setWeight(50)
                self.label_4.setFont(font)
                self.label_4.setObjectName("label_4")
                self.gridLayout_8.addWidget(self.label_4, 2, 0, 1, 1)
                self.equationLabel = QtWidgets.QLabel(self.groupBox)
                font = QtGui.QFont()
                font.setPointSize(9)
                font.setBold(True)
                font.setWeight(75)
                self.equationLabel.setFont(font)
                self.equationLabel.setText("")
                self.equationLabel.setObjectName("equationLabel")
                self.gridLayout_8.addWidget(self.equationLabel, 1, 2, 1, 1)
                self.longLabel = QtWidgets.QLabel(self.groupBox)
                self.longLabel.setMinimumSize(QtCore.QSize(150, 0))
                self.longLabel.setMaximumSize(QtCore.QSize(16777215, 30))
                font = QtGui.QFont()
                font.setPointSize(9)
                font.setBold(True)
                font.setWeight(75)
                self.longLabel.setFont(font)
                self.longLabel.setText("")
                self.longLabel.setObjectName("longLabel")
                self.gridLayout_8.addWidget(self.longLabel, 5, 2, 1, 1)
                spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
                self.gridLayout_8.addItem(spacerItem, 7, 0, 1, 4)
                self.gridLayout_9.addLayout(self.gridLayout_8, 0, 0, 1, 1)
                self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 1)
                self.gridLayout_7.addLayout(self.gridLayout_2, 0, 0, 1, 1)
                self.tabWidget.addTab(self.tab_3, "")
                self.gridLayout.addWidget(self.tabWidget, 4, 0, 1, 2)
                self.verticalLayout_2.addLayout(self.gridLayout)
                MainWindow.setCentralWidget(self.centralwidget)
                self.statusbar = QtWidgets.QStatusBar(MainWindow)
                self.statusbar.setObjectName("statusbar")
                MainWindow.setStatusBar(self.statusbar)
                self.menubar = QtWidgets.QMenuBar(MainWindow)
                self.menubar.setGeometry(QtCore.QRect(0, 0, 1100, 26))
                self.menubar.setObjectName("menubar")
                MainWindow.setMenuBar(self.menubar)

                self.retranslateUi(MainWindow)
                self.tabWidget.setCurrentIndex(1)
                QtCore.QMetaObject.connectSlotsByName(MainWindow)
                MainWindow.setTabOrder(self.browseCsvPushButton, self.tabWidget)
                MainWindow.setTabOrder(self.tabWidget, self.browseFileName)

                # define vars
                self.fileLoaded = False
                self.checkBox.setChecked(False)
                self.checkBox.setEnabled(False)
                # connecting slots to objects
                self.browseCsvPushButton.clicked.connect(self.on_browseCsvPushButton_clicked)
                self.clearPlotButton.clicked.connect(self.on_clearPlotButton_clicked)
                self.buildLinearModel.clicked.connect(self.on_buildLinearModel_clicked)

                self.init_plot_and_axes()
                self.update_plot()

                # checkbox slots
                self.checkBox.toggled.connect(self.update_plot)
                self.scatterShow.toggled.connect(self.update_plot)

        def init_plot_and_axes(self):
                self.figure = Figure()
                self.canvas = FigureCanvas(self.figure)
                self.toolbar = NavigationToolbar(self.canvas, None)
                self.plotLayout.addWidget(self.canvas)
                self.plotLayout.addWidget(self.toolbar)

                self.axes = self.figure.add_subplot(111)

                self.axes.set(xlabel='River_flow / River_flow_max',
                              ylabel='WSA / WSA_max',
                              title='Dependency figure for WSA and river flow')


        def on_browseCsvPushButton_clicked(self):
                self.fileName = QtWidgets.QFileDialog.getOpenFileName(None, 'Choose CSV file', './', '*.csv')[0]
                if self.fileName.__len__() == 0:
                        return
                self.fileLoaded = True

                self.browseFileName.clear()
                self.browseFileName.setText(self.fileName)

                # filling data table
                self.dataFrame = pd.read_csv(self.fileName, delimiter=';', encoding='utf8')
                self.update_plot()
                # print(self.dataFrame)
                self.dataModel = PandasModel(self.dataFrame)
                self.csvDataTable.setModel(self.dataModel)

                # plotting data got from csv on plotLayout (matplotlib implementation)


        def update_plot(self):
                self.axes.cla()
                self.axes.set(xlabel='River_flow / River_flow_max',
                              ylabel='WSA / WSA_max',
                              title='Dependency figure for WSA and river flow')
                self.axes.grid(color='gray', which='major', linestyle='-', linewidth=0.4, alpha=0.5)
                if self.fileLoaded:
                        self.x = self.dataFrame[['X']].values.astype(float)
                        self.y = self.dataFrame[['Y']].values.astype(float)

                        if self.scatterShow.isChecked():
                                self.axes.scatter(MinMaxScaler().fit_transform(self.x).ravel(),
                                                  MinMaxScaler().fit_transform(self.y).ravel(),
                                                  s=12, color='blue', label="WSA/Flow")
                        if self.checkBox.isChecked():
                                # plotting model result
                                self.axes.plot(self.testX.ravel(), self.pred, color='green', linewidth=2)
                self.canvas.draw()


        def on_buildLinearModel_clicked(self):
                if not self.fileLoaded:
                        msgBox = QtWidgets.QMessageBox()
                        msgBox.setIcon(QtWidgets.QMessageBox.Warning)
                        msgBox.setWindowTitle("Warning")
                        msgBox.setWindowIcon(QtGui.QIcon(":/img/icons/drop.png"))
                        msgBox.setText("No data")
                        msgBox.setInformativeText("Import CSV to build a model!")
                        msgBox.setDefaultButton(QtWidgets.QMessageBox.Ok)
                        msgBox.exec_()
                        self.on_browseCsvPushButton_clicked()
                        return
                # normalizing values
                x_reshaped = MinMaxScaler().fit_transform(self.x)
                y_reshaped = MinMaxScaler().fit_transform(self.y)

                self.trainX, self.testX = train_test_split(x_reshaped, shuffle=False)
                self.trainY, self.testY = train_test_split(y_reshaped, shuffle=False)

                self.model = linear_model.LinearRegression(n_jobs=-1)
                self.model.fit(self.trainX, self.trainY)
                print(round(self.model.score(self.trainX, self.trainY), 3))
                self.pred = self.model.predict(self.testX)
                # print("y = {}*x + {}".format(round(self.model.coef_[0][0], 2),
                #                              round(self.model.intercept_[0], 2)))
                self.checkBox.setChecked(True)
                self.checkBox.setEnabled(True)
                # plotting model result
                self.update_plot()
                self.fill_regression_parameters()


        def fill_regression_parameters(self):
                symb_plus = '+'
                if self.model.intercept_[0] < 0.0:
                        symb_plus = '-'
                self.equationLabel.setText(str('Y = {a}*X ' + symb_plus + ' {b}').
                                           format(a=round(self.model.coef_[0][0], 2),
                                                  b=round(abs(self.model.intercept_[0]), 2)))

                self.cardLabel.setText('{tr_card}/{test_card}'.format(tr_card=self.trainX.shape[0],
                                                                      test_card=self.testX.shape[0]))
                self.stationLabel.setText('unknown')
                self.latLabel.setText('-')
                self.longLabel.setText('-')


        def on_clearPlotButton_clicked(self):
                self.csvDataTable.setModel(PandasModel())
                self.browseFileName.clear()
                self.axes.cla()
                self.fileLoaded = False

                # drop the flags
                self.scatterShow.setChecked(True)
                self.checkBox.setChecked(False)
                self.checkBox.setEnabled(False)
                self.clear_regression_parameters()


        def clear_regression_parameters(self):
                self.equationLabel.clear()
                self.cardLabel.clear()
                self.stationLabel.clear()
                self.latLabel.clear()
                self.longLabel.clear()


        def retranslateUi(self, MainWindow):
                _translate = QtCore.QCoreApplication.translate
                MainWindow.setWindowTitle(_translate("MainWindow", "River Parameters Regression"))
                self.browseCsvPushButton.setText(_translate("MainWindow", "Browse"))
                self.label.setText(_translate("MainWindow", "Data table"))
                self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "CSV Data"))
                self.buildLinearModel.setText(_translate("MainWindow", "Build Linear Model"))
                self.clearPlotButton.setText(_translate("MainWindow", "Clear all"))
                self.checkBox.setText(_translate("MainWindow", "Line"))
                self.scatterShow.setText(_translate("MainWindow", "Scatter"))
                self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Results"))
                self.groupBox.setTitle(_translate("MainWindow", "Model details"))
                self.label_2.setText(_translate("MainWindow", "Method"))
                self.methodLabel.setText(_translate("MainWindow", "Linear Regression"))
                self.label_3.setText(_translate("MainWindow", "Equation"))
                self.label_5.setText(_translate("MainWindow", "Latitude"))
                self.label_12.setText(_translate("MainWindow", "Station"))
                self.label_6.setText(_translate("MainWindow", "Longitude"))
                self.label_4.setText(_translate("MainWindow", "Train/Test set card."))
                self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Output"))


import resource_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
