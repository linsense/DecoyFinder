# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/ssorgatem/uni/PEI/decoys/MainWindow.ui'
#
# Created: Sat Jul 23 01:22:53 2011
#      by: pyside-uic 0.2.11 running on PySide 1.0.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 535)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setObjectName("tabWidget")
        self.tabWidgetPage1 = QtGui.QWidget()
        self.tabWidgetPage1.setObjectName("tabWidgetPage1")
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.tabWidgetPage1)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.kdecoysCheckBox = QtGui.QCheckBox(self.tabWidgetPage1)
        self.kdecoysCheckBox.setObjectName("kdecoysCheckBox")
        self.verticalLayout_5.addWidget(self.kdecoysCheckBox)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.label = QtGui.QLabel(self.tabWidgetPage1)
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.verticalLayout_8 = QtGui.QVBoxLayout()
        self.verticalLayout_8.setContentsMargins(-1, 14, -1, 14)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.verticalLayout.addLayout(self.verticalLayout_8)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.addQueryButton = QtGui.QPushButton(self.tabWidgetPage1)
        self.addQueryButton.setObjectName("addQueryButton")
        self.horizontalLayout_6.addWidget(self.addQueryButton)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem2)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem3)
        self.clearActives = QtGui.QPushButton(self.tabWidgetPage1)
        self.clearActives.setObjectName("clearActives")
        self.horizontalLayout_6.addWidget(self.clearActives)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.queryList = QtGui.QListWidget(self.tabWidgetPage1)
        self.queryList.setObjectName("queryList")
        self.verticalLayout.addWidget(self.queryList)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.kdecoysFrame = QtGui.QFrame(self.tabWidgetPage1)
        self.kdecoysFrame.setFrameShape(QtGui.QFrame.NoFrame)
        self.kdecoysFrame.setLineWidth(0)
        self.kdecoysFrame.setObjectName("kdecoysFrame")
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.kdecoysFrame)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.label_3 = QtGui.QLabel(self.kdecoysFrame)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.verticalLayout_6.addLayout(self.horizontalLayout_2)
        self.verticalLayout_7 = QtGui.QVBoxLayout()
        self.verticalLayout_7.setContentsMargins(-1, 14, -1, 14)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        spacerItem6 = QtGui.QSpacerItem(0, 0, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        self.verticalLayout_7.addItem(spacerItem6)
        self.verticalLayout_6.addLayout(self.verticalLayout_7)
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.addDecoysButton = QtGui.QPushButton(self.kdecoysFrame)
        self.addDecoysButton.setObjectName("addDecoysButton")
        self.horizontalLayout_9.addWidget(self.addDecoysButton)
        spacerItem7 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem7)
        spacerItem8 = QtGui.QSpacerItem(52, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem8)
        self.clearDecoys = QtGui.QPushButton(self.kdecoysFrame)
        self.clearDecoys.setObjectName("clearDecoys")
        self.horizontalLayout_9.addWidget(self.clearDecoys)
        self.verticalLayout_6.addLayout(self.horizontalLayout_9)
        self.decoyList = QtGui.QListWidget(self.kdecoysFrame)
        self.decoyList.setObjectName("decoyList")
        self.verticalLayout_6.addWidget(self.decoyList)
        self.horizontalLayout.addWidget(self.kdecoysFrame)
        self.line = QtGui.QFrame(self.tabWidgetPage1)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout.addWidget(self.line)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem9 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem9)
        self.label_2 = QtGui.QLabel(self.tabWidgetPage1)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_5.addWidget(self.label_2)
        spacerItem10 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem10)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.zinclabel = QtGui.QLabel(self.tabWidgetPage1)
        self.zinclabel.setEnabled(False)
        self.zinclabel.setObjectName("zinclabel")
        self.horizontalLayout_3.addWidget(self.zinclabel)
        self.zsubComboBox = QtGui.QComboBox(self.tabWidgetPage1)
        self.zsubComboBox.setEnabled(False)
        self.zsubComboBox.setObjectName("zsubComboBox")
        self.horizontalLayout_3.addWidget(self.zsubComboBox)
        spacerItem11 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem11)
        self.cacheCheckBox = QtGui.QCheckBox(self.tabWidgetPage1)
        self.cacheCheckBox.setEnabled(False)
        self.cacheCheckBox.setChecked(True)
        self.cacheCheckBox.setObjectName("cacheCheckBox")
        self.horizontalLayout_3.addWidget(self.cacheCheckBox)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.dbComboBox = QtGui.QComboBox(self.tabWidgetPage1)
        self.dbComboBox.setObjectName("dbComboBox")
        self.dbComboBox.addItem("")
        self.dbComboBox.addItem("")
        self.dbComboBox.addItem("")
        self.dbComboBox.addItem("")
        self.dbComboBox.addItem("")
        self.horizontalLayout_8.addWidget(self.dbComboBox)
        self.addDButton = QtGui.QPushButton(self.tabWidgetPage1)
        self.addDButton.setObjectName("addDButton")
        self.horizontalLayout_8.addWidget(self.addDButton)
        spacerItem12 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem12)
        self.clearDB = QtGui.QPushButton(self.tabWidgetPage1)
        self.clearDB.setObjectName("clearDB")
        self.horizontalLayout_8.addWidget(self.clearDB)
        self.verticalLayout_2.addLayout(self.horizontalLayout_8)
        self.dbListWidget = QtGui.QListWidget(self.tabWidgetPage1)
        self.dbListWidget.setObjectName("dbListWidget")
        self.verticalLayout_2.addWidget(self.dbListWidget)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_5.addLayout(self.horizontalLayout)
        self.formLayout_2 = QtGui.QFormLayout()
        self.formLayout_2.setFieldGrowthPolicy(QtGui.QFormLayout.ExpandingFieldsGrow)
        self.formLayout_2.setObjectName("formLayout_2")
        self.outDirButton = QtGui.QPushButton(self.tabWidgetPage1)
        self.outDirButton.setObjectName("outDirButton")
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.outDirButton)
        self.outputDirectoryLineEdit = QtGui.QLineEdit(self.tabWidgetPage1)
        self.outputDirectoryLineEdit.setObjectName("outputDirectoryLineEdit")
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.FieldRole, self.outputDirectoryLineEdit)
        self.verticalLayout_5.addLayout(self.formLayout_2)
        self.tabWidget.addTab(self.tabWidgetPage1, "")
        self.tab = QtGui.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout = QtGui.QGridLayout(self.tab)
        self.gridLayout.setObjectName("gridLayout")
        self.resultsTable = QtGui.QTableWidget(self.tab)
        self.resultsTable.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.resultsTable.setAlternatingRowColors(True)
        self.resultsTable.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.resultsTable.setObjectName("resultsTable")
        self.resultsTable.setColumnCount(7)
        self.resultsTable.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.resultsTable.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.resultsTable.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.resultsTable.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.resultsTable.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.resultsTable.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.resultsTable.setHorizontalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.resultsTable.setHorizontalHeaderItem(6, item)
        self.resultsTable.verticalHeader().setSortIndicatorShown(True)
        self.resultsTable.verticalHeader().setStretchLastSection(True)
        self.gridLayout.addWidget(self.resultsTable, 1, 0, 1, 1)
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.informationSavedToLabel = QtGui.QLabel(self.tab)
        self.informationSavedToLabel.setObjectName("informationSavedToLabel")
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.informationSavedToLabel)
        self.informationSavedToLineEdit = QtGui.QLineEdit(self.tab)
        self.informationSavedToLineEdit.setReadOnly(True)
        self.informationSavedToLineEdit.setObjectName("informationSavedToLineEdit")
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.informationSavedToLineEdit)
        self.gridLayout.addLayout(self.formLayout, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tabWidgetPage2 = QtGui.QWidget()
        self.tabWidgetPage2.setObjectName("tabWidgetPage2")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.tabWidgetPage2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self._3 = QtGui.QFormLayout()
        self._3.setFieldGrowthPolicy(QtGui.QFormLayout.ExpandingFieldsGrow)
        self._3.setLabelAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self._3.setFormAlignment(QtCore.Qt.AlignCenter)
        self._3.setObjectName("_3")
        self.tanimotoCutoffLabel = QtGui.QLabel(self.tabWidgetPage2)
        self.tanimotoCutoffLabel.setObjectName("tanimotoCutoffLabel")
        self._3.setWidget(0, QtGui.QFormLayout.LabelRole, self.tanimotoCutoffLabel)
        self.tanimotoBox = QtGui.QDoubleSpinBox(self.tabWidgetPage2)
        self.tanimotoBox.setMaximum(1.0)
        self.tanimotoBox.setSingleStep(0.1)
        self.tanimotoBox.setObjectName("tanimotoBox")
        self._3.setWidget(0, QtGui.QFormLayout.FieldRole, self.tanimotoBox)
        self.hBALabel_2 = QtGui.QLabel(self.tabWidgetPage2)
        self.hBALabel_2.setObjectName("hBALabel_2")
        self._3.setWidget(1, QtGui.QFormLayout.LabelRole, self.hBALabel_2)
        self.hbaBox = QtGui.QSpinBox(self.tabWidgetPage2)
        self.hbaBox.setObjectName("hbaBox")
        self._3.setWidget(1, QtGui.QFormLayout.FieldRole, self.hbaBox)
        self.hBDLabel = QtGui.QLabel(self.tabWidgetPage2)
        self.hBDLabel.setObjectName("hBDLabel")
        self._3.setWidget(2, QtGui.QFormLayout.LabelRole, self.hBDLabel)
        self.hbdBox = QtGui.QSpinBox(self.tabWidgetPage2)
        self.hbdBox.setObjectName("hbdBox")
        self._3.setWidget(2, QtGui.QFormLayout.FieldRole, self.hbdBox)
        self.clogPLabel = QtGui.QLabel(self.tabWidgetPage2)
        self.clogPLabel.setObjectName("clogPLabel")
        self._3.setWidget(3, QtGui.QFormLayout.LabelRole, self.clogPLabel)
        self.clogpBox = QtGui.QDoubleSpinBox(self.tabWidgetPage2)
        self.clogpBox.setSingleStep(0.1)
        self.clogpBox.setObjectName("clogpBox")
        self._3.setWidget(3, QtGui.QFormLayout.FieldRole, self.clogpBox)
        self.molecularWeightLabel = QtGui.QLabel(self.tabWidgetPage2)
        self.molecularWeightLabel.setObjectName("molecularWeightLabel")
        self._3.setWidget(4, QtGui.QFormLayout.LabelRole, self.molecularWeightLabel)
        self.molwtBox = QtGui.QSpinBox(self.tabWidgetPage2)
        self.molwtBox.setMaximum(999)
        self.molwtBox.setObjectName("molwtBox")
        self._3.setWidget(4, QtGui.QFormLayout.FieldRole, self.molwtBox)
        self.rtotationalBondsLabel = QtGui.QLabel(self.tabWidgetPage2)
        self.rtotationalBondsLabel.setObjectName("rtotationalBondsLabel")
        self._3.setWidget(5, QtGui.QFormLayout.LabelRole, self.rtotationalBondsLabel)
        self.rotbBox = QtGui.QSpinBox(self.tabWidgetPage2)
        self.rotbBox.setObjectName("rotbBox")
        self._3.setWidget(5, QtGui.QFormLayout.FieldRole, self.rotbBox)
        self.decoyLimitLabel = QtGui.QLabel(self.tabWidgetPage2)
        self.decoyLimitLabel.setObjectName("decoyLimitLabel")
        self._3.setWidget(6, QtGui.QFormLayout.LabelRole, self.decoyLimitLabel)
        self.decoyMinSpinBox = QtGui.QSpinBox(self.tabWidgetPage2)
        self.decoyMinSpinBox.setMaximum(99999)
        self.decoyMinSpinBox.setObjectName("decoyMinSpinBox")
        self._3.setWidget(6, QtGui.QFormLayout.FieldRole, self.decoyMinSpinBox)
        self.maximumDecoysPerActiveLigandLabel = QtGui.QLabel(self.tabWidgetPage2)
        self.maximumDecoysPerActiveLigandLabel.setObjectName("maximumDecoysPerActiveLigandLabel")
        self._3.setWidget(7, QtGui.QFormLayout.LabelRole, self.maximumDecoysPerActiveLigandLabel)
        self.decoyMaxSpinBox = QtGui.QSpinBox(self.tabWidgetPage2)
        self.decoyMaxSpinBox.setMaximum(99999)
        self.decoyMaxSpinBox.setObjectName("decoyMaxSpinBox")
        self._3.setWidget(7, QtGui.QFormLayout.FieldRole, self.decoyMaxSpinBox)
        self.cacheButton = QtGui.QPushButton(self.tabWidgetPage2)
        self.cacheButton.setObjectName("cacheButton")
        self._3.setWidget(9, QtGui.QFormLayout.LabelRole, self.cacheButton)
        self.cachDirectoryLineEdit = QtGui.QLineEdit(self.tabWidgetPage2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cachDirectoryLineEdit.sizePolicy().hasHeightForWidth())
        self.cachDirectoryLineEdit.setSizePolicy(sizePolicy)
        self.cachDirectoryLineEdit.setObjectName("cachDirectoryLineEdit")
        self._3.setWidget(9, QtGui.QFormLayout.FieldRole, self.cachDirectoryLineEdit)
        self.decoyDecoyTanimotoLabel = QtGui.QLabel(self.tabWidgetPage2)
        self.decoyDecoyTanimotoLabel.setObjectName("decoyDecoyTanimotoLabel")
        self._3.setWidget(8, QtGui.QFormLayout.LabelRole, self.decoyDecoyTanimotoLabel)
        self.dTanimotoBox = QtGui.QDoubleSpinBox(self.tabWidgetPage2)
        self.dTanimotoBox.setMaximum(1.0)
        self.dTanimotoBox.setSingleStep(0.1)
        self.dTanimotoBox.setObjectName("dTanimotoBox")
        self._3.setWidget(8, QtGui.QFormLayout.FieldRole, self.dTanimotoBox)
        self.verticalLayout_3.addLayout(self._3)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem13 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem13)
        self.defaultsButton = QtGui.QPushButton(self.tabWidgetPage2)
        self.defaultsButton.setObjectName("defaultsButton")
        self.horizontalLayout_7.addWidget(self.defaultsButton)
        spacerItem14 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem14)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        self.tabWidget.addTab(self.tabWidgetPage2, "")
        self.verticalLayout_4.addWidget(self.tabWidget)
        self._2 = QtGui.QHBoxLayout()
        self._2.setObjectName("_2")
        self.clearButton = QtGui.QPushButton(self.centralwidget)
        self.clearButton.setObjectName("clearButton")
        self._2.addWidget(self.clearButton)
        spacerItem15 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self._2.addItem(spacerItem15)
        self.stopButton = QtGui.QPushButton(self.centralwidget)
        self.stopButton.setEnabled(False)
        self.stopButton.setObjectName("stopButton")
        self._2.addWidget(self.stopButton)
        spacerItem16 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self._2.addItem(spacerItem16)
        self.findDecoysButton = QtGui.QPushButton(self.centralwidget)
        self.findDecoysButton.setObjectName("findDecoysButton")
        self._2.addWidget(self.findDecoysButton)
        self.verticalLayout_4.addLayout(self._2)
        self.progressBar = QtGui.QProgressBar(self.centralwidget)
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout_4.addWidget(self.progressBar)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 700, 23))
        self.menubar.setObjectName("menubar")
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionHelp = QtGui.QAction(MainWindow)
        self.actionHelp.setObjectName("actionHelp")
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addAction(self.actionHelp)
        self.menubar.addAction(self.menuHelp.menuAction())
        self.tanimotoCutoffLabel.setBuddy(self.kdecoysFrame)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.clearButton, QtCore.SIGNAL("clicked()"), self.progressBar.reset)
        QtCore.QObject.connect(self.clearButton, QtCore.SIGNAL("clicked()"), self.statusbar.clearMessage)
        QtCore.QObject.connect(self.clearDecoys, QtCore.SIGNAL("clicked()"), self.decoyList.clear)
        QtCore.QObject.connect(self.clearButton, QtCore.SIGNAL("clicked()"), self.decoyList.clear)
        QtCore.QObject.connect(self.clearButton, QtCore.SIGNAL("clicked()"), self.dbListWidget.clear)
        QtCore.QObject.connect(self.clearDB, QtCore.SIGNAL("clicked()"), self.dbListWidget.clear)
        QtCore.QObject.connect(self.clearButton, QtCore.SIGNAL("clicked()"), self.queryList.clear)
        QtCore.QObject.connect(self.clearActives, QtCore.SIGNAL("clicked()"), self.queryList.clear)
        QtCore.QObject.connect(self.kdecoysCheckBox, QtCore.SIGNAL("toggled(bool)"), self.kdecoysFrame.setVisible)
        QtCore.QObject.connect(self.clearButton, QtCore.SIGNAL("clicked()"), self.informationSavedToLineEdit.clear)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "DecoyFinder", None, QtGui.QApplication.UnicodeUTF8))
        self.kdecoysCheckBox.setToolTip(QtGui.QApplication.translate("MainWindow", "Add new decoys to an existing decoy set", None, QtGui.QApplication.UnicodeUTF8))
        self.kdecoysCheckBox.setText(QtGui.QApplication.translate("MainWindow", "  Add new decoys", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Known Active Ligands", None, QtGui.QApplication.UnicodeUTF8))
        self.addQueryButton.setText(QtGui.QApplication.translate("MainWindow", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.clearActives.setText(QtGui.QApplication.translate("MainWindow", "Clear", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "Existing Decoy files", None, QtGui.QApplication.UnicodeUTF8))
        self.addDecoysButton.setText(QtGui.QApplication.translate("MainWindow", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.clearDecoys.setText(QtGui.QApplication.translate("MainWindow", "Clear", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Sources of new Decoys", None, QtGui.QApplication.UnicodeUTF8))
        self.zinclabel.setText(QtGui.QApplication.translate("MainWindow", "ZINC subset:", None, QtGui.QApplication.UnicodeUTF8))
        self.cacheCheckBox.setText(QtGui.QApplication.translate("MainWindow", "Use caché", None, QtGui.QApplication.UnicodeUTF8))
        self.dbComboBox.setItemText(0, QtGui.QApplication.translate("MainWindow", "Select local files...", None, QtGui.QApplication.UnicodeUTF8))
        self.dbComboBox.setItemText(1, QtGui.QApplication.translate("MainWindow", "ZINC single", None, QtGui.QApplication.UnicodeUTF8))
        self.dbComboBox.setItemText(2, QtGui.QApplication.translate("MainWindow", "ZINC metals", None, QtGui.QApplication.UnicodeUTF8))
        self.dbComboBox.setItemText(3, QtGui.QApplication.translate("MainWindow", "ZINC usual", None, QtGui.QApplication.UnicodeUTF8))
        self.dbComboBox.setItemText(4, QtGui.QApplication.translate("MainWindow", "ZINC all", None, QtGui.QApplication.UnicodeUTF8))
        self.addDButton.setText(QtGui.QApplication.translate("MainWindow", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.clearDB.setText(QtGui.QApplication.translate("MainWindow", "Clear", None, QtGui.QApplication.UnicodeUTF8))
        self.outDirButton.setText(QtGui.QApplication.translate("MainWindow", "Output file", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidgetPage1), QtGui.QApplication.translate("MainWindow", "Query", None, QtGui.QApplication.UnicodeUTF8))
        self.resultsTable.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("MainWindow", "Active", None, QtGui.QApplication.UnicodeUTF8))
        self.resultsTable.horizontalHeaderItem(1).setText(QtGui.QApplication.translate("MainWindow", "Decoys found", None, QtGui.QApplication.UnicodeUTF8))
        self.resultsTable.horizontalHeaderItem(2).setText(QtGui.QApplication.translate("MainWindow", "HBA", None, QtGui.QApplication.UnicodeUTF8))
        self.resultsTable.horizontalHeaderItem(3).setText(QtGui.QApplication.translate("MainWindow", "HBD", None, QtGui.QApplication.UnicodeUTF8))
        self.resultsTable.horizontalHeaderItem(4).setText(QtGui.QApplication.translate("MainWindow", "logP", None, QtGui.QApplication.UnicodeUTF8))
        self.resultsTable.horizontalHeaderItem(5).setText(QtGui.QApplication.translate("MainWindow", "M. weight", None, QtGui.QApplication.UnicodeUTF8))
        self.resultsTable.horizontalHeaderItem(6).setText(QtGui.QApplication.translate("MainWindow", "Rot. bonds", None, QtGui.QApplication.UnicodeUTF8))
        self.informationSavedToLabel.setText(QtGui.QApplication.translate("MainWindow", "This information can be found at", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtGui.QApplication.translate("MainWindow", "Run Statistics", None, QtGui.QApplication.UnicodeUTF8))
        self.tanimotoCutoffLabel.setText(QtGui.QApplication.translate("MainWindow", "Active ligand vs Decoy Tanimoto threshold", None, QtGui.QApplication.UnicodeUTF8))
        self.hBALabel_2.setText(QtGui.QApplication.translate("MainWindow", "Hydrogen Bond Acceptors ±", None, QtGui.QApplication.UnicodeUTF8))
        self.hBDLabel.setText(QtGui.QApplication.translate("MainWindow", "Hydrogen Bond Donors ±", None, QtGui.QApplication.UnicodeUTF8))
        self.clogPLabel.setText(QtGui.QApplication.translate("MainWindow", "Octanol-water partition coefficient (logP) ±", None, QtGui.QApplication.UnicodeUTF8))
        self.molecularWeightLabel.setText(QtGui.QApplication.translate("MainWindow", "Molecular weight ±", None, QtGui.QApplication.UnicodeUTF8))
        self.molwtBox.setSuffix(QtGui.QApplication.translate("MainWindow", " Da", None, QtGui.QApplication.UnicodeUTF8))
        self.rtotationalBondsLabel.setText(QtGui.QApplication.translate("MainWindow", "Rotational bonds ±", None, QtGui.QApplication.UnicodeUTF8))
        self.decoyLimitLabel.setText(QtGui.QApplication.translate("MainWindow", "Minimum decoys per active ligand:", None, QtGui.QApplication.UnicodeUTF8))
        self.decoyMinSpinBox.setToolTip(QtGui.QApplication.translate("MainWindow", "Limit how many decoys to find for each ligand. If the limit is 0, there is no limit.", None, QtGui.QApplication.UnicodeUTF8))
        self.maximumDecoysPerActiveLigandLabel.setText(QtGui.QApplication.translate("MainWindow", "Maximum decoys per active ligand", None, QtGui.QApplication.UnicodeUTF8))
        self.cacheButton.setText(QtGui.QApplication.translate("MainWindow", "Caché directory", None, QtGui.QApplication.UnicodeUTF8))
        self.decoyDecoyTanimotoLabel.setText(QtGui.QApplication.translate("MainWindow", "Decoy vs Decoy Tanimoto threshold", None, QtGui.QApplication.UnicodeUTF8))
        self.defaultsButton.setText(QtGui.QApplication.translate("MainWindow", "Load Defaults", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidgetPage2), QtGui.QApplication.translate("MainWindow", "Options", None, QtGui.QApplication.UnicodeUTF8))
        self.clearButton.setText(QtGui.QApplication.translate("MainWindow", "Clear all", None, QtGui.QApplication.UnicodeUTF8))
        self.stopButton.setText(QtGui.QApplication.translate("MainWindow", "Stop", None, QtGui.QApplication.UnicodeUTF8))
        self.findDecoysButton.setText(QtGui.QApplication.translate("MainWindow", "Find decoys", None, QtGui.QApplication.UnicodeUTF8))
        self.progressBar.setFormat(QtGui.QApplication.translate("MainWindow", "%v decoys found", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHelp.setTitle(QtGui.QApplication.translate("MainWindow", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout.setText(QtGui.QApplication.translate("MainWindow", "About", None, QtGui.QApplication.UnicodeUTF8))
        self.actionHelp.setText(QtGui.QApplication.translate("MainWindow", "Homepage", None, QtGui.QApplication.UnicodeUTF8))

import resources_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

