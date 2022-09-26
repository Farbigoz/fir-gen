import os
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QApplication


from ui.ui_MainWindow import Ui_MainWindow
from ui.FirPlotter import SignalPlotter

from src.firGen import *


class FirGeneratorApp(QMainWindow):
    taps = []

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.resize(1000, 800)
        self.setWindowTitle("Генератор FIR фильтров")

        # Добавление графика
        self.plotter = SignalPlotter()
        self.ui.viewFrame.layout().addWidget(self.plotter)

        # Реакция на кнопку сохранения
        self.ui.saveButton.clicked.connect(self.saveFilter)

        # Реакция на изменения парметров
        self.ui.lowerCutFreq.valueChanged.connect(self.settingsChanged)
        self.ui.upperCutFreq.valueChanged.connect(self.settingsChanged)
        self.ui.taps.valueChanged.connect(self.settingsChanged)
        self.ui.freq.valueChanged.connect(self.settingsChanged)

        self.ui.typeLowPass.toggled.connect(self.settingsChanged)
        self.ui.typeBandPass.toggled.connect(self.settingsChanged)
        self.ui.typeHighPass.toggled.connect(self.settingsChanged)

        self.settingsChanged()

    # Параметры были изменены
    def settingsChanged(self):
        if self.ui.typeLowPass.isChecked():
            self.ui.lowerCutFreq.setDisabled(True)
            self.ui.lowerCutFreqLabel.setDisabled(True)
            self.ui.upperCutFreq.setDisabled(False)
            self.ui.upperCutFreqLabel.setDisabled(False)

        elif self.ui.typeBandPass.isChecked():
            self.ui.lowerCutFreq.setDisabled(False)
            self.ui.lowerCutFreqLabel.setDisabled(False)
            self.ui.upperCutFreq.setDisabled(False)
            self.ui.upperCutFreqLabel.setDisabled(False)

        elif self.ui.typeHighPass.isChecked():
            self.ui.lowerCutFreq.setDisabled(False)
            self.ui.lowerCutFreqLabel.setDisabled(False)
            self.ui.upperCutFreq.setDisabled(True)
            self.ui.upperCutFreqLabel.setDisabled(True)

        loCut = self.ui.lowerCutFreq.value()
        hiCut = self.ui.upperCutFreq.value()
        tapNum = self.ui.taps.value()
        samplerate = self.ui.freq.value()

        # Фильтр низких частот
        if self.ui.typeLowPass.isChecked():
            if (samplerate / 2) <= hiCut:
                self.ui.statusbar.showMessage("Ошибка: Частота сэмплирования должна быть в 2 раза выше частоты среза!")
                return

            # Генерируем фильтр
            try:
                self.taps = lpf_fir(tapNum, hiCut, samplerate)
            except Exception as e:
                self.ui.statusbar.showMessage("Ошибка: " + str(e))
                return

            # Отображаем параметры фильтра
            self.plotter.plotLowPass(hiCut, samplerate, self.taps)

        # Полосовой фильтр
        elif self.ui.typeBandPass.isChecked():
            if loCut >= hiCut:
                self.ui.statusbar.showMessage("Ошибка: Верхняя частота среза должна быть больше нижней частоты среза!")
                return

            if (samplerate / 2) <= loCut or (samplerate / 2) <= hiCut:
                self.ui.statusbar.showMessage("Ошибка: Частота сэмплирования должна быть в 2 раза выше частоты среза!")
                return

            # Генерируем фильтр
            try:
                self.taps = bpf_fir(tapNum, loCut, hiCut, samplerate)
            except Exception as e:
                self.ui.statusbar.showMessage("Ошибка: " + str(e))
                return

            # Отображаем параметры фильтра
            self.plotter.plotBandPass(loCut, hiCut, samplerate, self.taps)

        # Фильтр верхних частот
        elif self.ui.typeHighPass.isChecked():
            if (samplerate / 2) <= loCut:
                self.ui.statusbar.showMessage("Ошибка: Частота сэмплирования должна быть в 2 раза выше частоты среза!")
                return

            # Генерируем фильтр
            try:
                self.taps = hpf_fir(tapNum, loCut, samplerate)
            except Exception as e:
                self.ui.statusbar.showMessage("Ошибка: " + str(e))
                return

        else:
            return

        self.ui.statusbar.showMessage("Фильтр успешно сгенерирован!")

    # Сохранение фильтра
    def saveFilter(self):
        loCut = self.ui.lowerCutFreq.value()
        hiCut = self.ui.upperCutFreq.value()
        tapNum = self.ui.taps.value()
        samplerate = self.ui.freq.value()

        # Определение типа фильтра
        if self.ui.typeLowPass.isChecked():
            type = "LPF"
            freq = hiCut

        elif self.ui.typeBandPass.isChecked():
            type = "BPF"
            freq = loCut + (hiCut - loCut) // 2

        elif self.ui.typeHighPass.isChecked():
            type = "HPF"
            freq = loCut
        else:
            return

        # Определение типа значений
        if self.ui.numTypeFloat.isChecked():
            numType = "float"
            taps = self.taps

        elif self.ui.numTypeInt16.isChecked():
            numType = "int16_t"
            taps = list(map(lambda x: int(x*0x7fff), self.taps))

        elif self.ui.numTypeInt32.isChecked():
            numType = "int32_t"
            taps = list(map(lambda x: int(x*0x7fffffff), self.taps))

        else:
            return

        fileName = f"FIR_{type}_{freq}_{samplerate}"

        # Генерация таблицы
        tapsTable = ""
        for k in range(0, tapNum, 8):
            tapsTable += "\t"

            for i in range(0, 8):
                if k + i >= tapNum:
                    break

                if numType == "float":
                    tapsTable += f"{taps[k + i]:>24}"
                if numType == "int16_t":
                    tapsTable += f"{taps[k+i]:>6}"
                else:
                    tapsTable += f"{taps[k + i]:>12}"

                tapsTable += ", "

            tapsTable += "\n"

        tapsTable = tapsTable[:-3]  # Отрезаем последние 3 символа - запятая, пробел и перенос строки

        # Шаблон файла фильтра для языка СИ
        with open("src/template.h", "r", encoding="UTF-8") as templateCFile:
            templateC = templateCFile.read()

        # Заполнение шаблона и сохранение файла
        with open(f"out/c/{fileName}.h", "w", encoding="UTF-8") as cFile:
            cFile.write(
                templateC.format(
                    fileName=f"{fileName}.h",
                    type=type,
                    freq=freq,
                    samplerate=samplerate,
                    tapNum=tapNum,
                    numType=numType,
                    tapsTable=tapsTable
                )
            )

        # Шаблон файла фильтра для языка Python
        with open("src/template.py", "r", encoding="UTF-8") as templatePyFile:
            templatePy = templatePyFile.read()

        # Заполнение шаблона и сохранение файла
        with open(f"out/py/{fileName}.py", "w", encoding="UTF-8") as pyFile:
            pyFile.write(
                templatePy.format(
                    fileName=f"{fileName}.py",
                    type=type,
                    freq=freq,
                    samplerate=samplerate,
                    tapNum=tapNum,
                    numType=numType,
                    tapsTable=tapsTable
                )
            )

        # Вывод сообщения об успешном сохранении файлов
        self.ui.statusbar.showMessage(f"Фильтр сохранён в \"{os.path.abspath('out')}\". Название файлов: {fileName}")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = FirGeneratorApp()
    window.show()

    exitId = app.exec()
    sys.exit(exitId)
