# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindowvdCZPC.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Vertical)
        self.splitter.setChildrenCollapsible(False)
        self.viewFrame = QGroupBox(self.splitter)
        self.viewFrame.setObjectName(u"viewFrame")
        self.verticalLayout_2 = QVBoxLayout(self.viewFrame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.splitter.addWidget(self.viewFrame)
        self.settingsFrame = QGroupBox(self.splitter)
        self.settingsFrame.setObjectName(u"settingsFrame")
        self.settingsFrame.setMinimumSize(QSize(0, 0))
        self.settingsFrame.setMaximumSize(QSize(16777215, 16777215))
        self.settingsFrame.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.settingsFrame.setFlat(False)
        self.settingsFrame.setCheckable(False)
        self.settingsFrame.setChecked(False)
        self.gridLayout = QGridLayout(self.settingsFrame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.freqLabel = QLabel(self.settingsFrame)
        self.freqLabel.setObjectName(u"freqLabel")

        self.gridLayout.addWidget(self.freqLabel, 6, 0, 1, 1)

        self.upperCutFreqLabel = QLabel(self.settingsFrame)
        self.upperCutFreqLabel.setObjectName(u"upperCutFreqLabel")

        self.gridLayout.addWidget(self.upperCutFreqLabel, 2, 0, 1, 1)

        self.typeLabel = QLabel(self.settingsFrame)
        self.typeLabel.setObjectName(u"typeLabel")
        self.typeLabel.setMaximumSize(QSize(150, 16777215))

        self.gridLayout.addWidget(self.typeLabel, 0, 0, 1, 1)

        self.tapsLabel = QLabel(self.settingsFrame)
        self.tapsLabel.setObjectName(u"tapsLabel")

        self.gridLayout.addWidget(self.tapsLabel, 5, 0, 1, 1)

        self.lowerCutFreq = QSpinBox(self.settingsFrame)
        self.lowerCutFreq.setObjectName(u"lowerCutFreq")
        self.lowerCutFreq.setMinimumSize(QSize(0, 20))
        self.lowerCutFreq.setMinimum(1)
        self.lowerCutFreq.setMaximum(100000)
        self.lowerCutFreq.setSingleStep(2)
        self.lowerCutFreq.setValue(1)

        self.gridLayout.addWidget(self.lowerCutFreq, 1, 1, 1, 1)

        self.taps = QSpinBox(self.settingsFrame)
        self.taps.setObjectName(u"taps")
        self.taps.setMinimumSize(QSize(0, 20))
        self.taps.setMinimum(2)
        self.taps.setMaximum(10000)
        self.taps.setSingleStep(2)
        self.taps.setValue(100)

        self.gridLayout.addWidget(self.taps, 5, 1, 1, 1)

        self.lowerCutFreqLabel = QLabel(self.settingsFrame)
        self.lowerCutFreqLabel.setObjectName(u"lowerCutFreqLabel")
        self.lowerCutFreqLabel.setMaximumSize(QSize(150, 16777215))

        self.gridLayout.addWidget(self.lowerCutFreqLabel, 1, 0, 1, 1)

        self.types = QFrame(self.settingsFrame)
        self.types.setObjectName(u"types")
        self.types.setMinimumSize(QSize(0, 20))
        self.types.setFrameShape(QFrame.StyledPanel)
        self.types.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.types)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.typeLowPass = QRadioButton(self.types)
        self.typeLowPass.setObjectName(u"typeLowPass")
        self.typeLowPass.setChecked(True)

        self.horizontalLayout_3.addWidget(self.typeLowPass)

        self.typeBandPass = QRadioButton(self.types)
        self.typeBandPass.setObjectName(u"typeBandPass")

        self.horizontalLayout_3.addWidget(self.typeBandPass)

        self.typeHighPass = QRadioButton(self.types)
        self.typeHighPass.setObjectName(u"typeHighPass")
        self.typeHighPass.setEnabled(False)

        self.horizontalLayout_3.addWidget(self.typeHighPass)


        self.gridLayout.addWidget(self.types, 0, 1, 1, 1)

        self.upperCutFreq = QSpinBox(self.settingsFrame)
        self.upperCutFreq.setObjectName(u"upperCutFreq")
        self.upperCutFreq.setMinimumSize(QSize(0, 20))
        self.upperCutFreq.setMinimum(1)
        self.upperCutFreq.setMaximum(100000)
        self.upperCutFreq.setSingleStep(2)
        self.upperCutFreq.setValue(10)

        self.gridLayout.addWidget(self.upperCutFreq, 2, 1, 1, 1)

        self.numTypesLabel = QLabel(self.settingsFrame)
        self.numTypesLabel.setObjectName(u"numTypesLabel")
        self.numTypesLabel.setMaximumSize(QSize(150, 16777215))

        self.gridLayout.addWidget(self.numTypesLabel, 7, 0, 1, 1)

        self.numTypes = QFrame(self.settingsFrame)
        self.numTypes.setObjectName(u"numTypes")
        self.numTypes.setMinimumSize(QSize(0, 20))
        self.numTypes.setFrameShape(QFrame.StyledPanel)
        self.numTypes.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.numTypes)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.numTypeFloat = QRadioButton(self.numTypes)
        self.numTypeFloat.setObjectName(u"numTypeFloat")
        self.numTypeFloat.setChecked(True)

        self.horizontalLayout_2.addWidget(self.numTypeFloat)

        self.numTypeInt16 = QRadioButton(self.numTypes)
        self.numTypeInt16.setObjectName(u"numTypeInt16")

        self.horizontalLayout_2.addWidget(self.numTypeInt16)

        self.numTypeInt32 = QRadioButton(self.numTypes)
        self.numTypeInt32.setObjectName(u"numTypeInt32")

        self.horizontalLayout_2.addWidget(self.numTypeInt32)


        self.gridLayout.addWidget(self.numTypes, 7, 1, 1, 1)

        self.freq = QSpinBox(self.settingsFrame)
        self.freq.setObjectName(u"freq")
        self.freq.setMinimum(10)
        self.freq.setMaximum(100000)
        self.freq.setSingleStep(10)
        self.freq.setValue(2000)

        self.gridLayout.addWidget(self.freq, 6, 1, 1, 1)

        self.splitter.addWidget(self.settingsFrame)

        self.verticalLayout.addWidget(self.splitter)

        self.saveButton = QPushButton(self.centralwidget)
        self.saveButton.setObjectName(u"saveButton")

        self.verticalLayout.addWidget(self.saveButton)

        MainWindow.setCentralWidget(self.centralwidget)
        self.saveButton.raise_()
        self.viewFrame.raise_()
        self.settingsFrame.raise_()
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.viewFrame.setTitle(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435", None))
        self.settingsFrame.setTitle(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b", None))
        self.freqLabel.setText(QCoreApplication.translate("MainWindow", u"\u0427\u0430\u0441\u0442\u043e\u0442\u0430 \u0434\u0438\u0441\u043a\u0440\u0435\u0442\u0438\u0437\u0430\u0446\u0438\u0438 (\u0413\u0446)", None))
        self.upperCutFreqLabel.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0435\u0440\u0445\u043d\u044f\u044f \u0447\u0430\u0441\u0442\u043e\u0442\u0430  \u0441\u0440\u0435\u0437\u0430", None))
        self.typeLabel.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0438\u043f \u0444\u0438\u043b\u044c\u0442\u0440\u0430", None))
        self.tapsLabel.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0440\u044f\u0434\u043e\u043a \u0444\u0438\u043b\u044c\u0442\u0440\u0430", None))
        self.lowerCutFreqLabel.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0438\u0436\u043d\u044f\u044f \u0447\u0430\u0441\u0442\u043e\u0442\u0430  \u0441\u0440\u0435\u0437\u0430", None))
        self.typeLowPass.setText(QCoreApplication.translate("MainWindow", u"Low-pass", None))
        self.typeBandPass.setText(QCoreApplication.translate("MainWindow", u"Band-pass", None))
        self.typeHighPass.setText(QCoreApplication.translate("MainWindow", u"High-pass", None))
        self.numTypesLabel.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0438\u043f \u0432\u044b\u0445\u043e\u0434\u043d\u044b\u0445 \u0434\u0430\u043d\u043d\u044b\u0445", None))
        self.numTypeFloat.setText(QCoreApplication.translate("MainWindow", u"float", None))
        self.numTypeInt16.setText(QCoreApplication.translate("MainWindow", u"int16_t", None))
        self.numTypeInt32.setText(QCoreApplication.translate("MainWindow", u"int32_t", None))
        self.saveButton.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0433\u0435\u043d\u0435\u0440\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u0444\u0430\u0439\u043b", None))
    # retranslateUi

